https://realpython.com/python-profiling/#how-to-find-performance-bottlenecks-in-your-python-code-through-profiling

Prima di entrare nel dettaglio del tuning delle performance di un programma scritto in Python, è bene prendere familiarità con la tecnica della profilazione software. Ci può aiutare a rispondere alla domanda relativa al fatto che l'ottimizzazione sia o meno necessaria e, se sì, su quali parti del codice dovremmo focalizzarci.

A volte, il RoI nelle ottimizzazioni delle performance semplicemente non vale la pena. Se eseguiamo il nostro codice soltanto una volta o due, o se richiede più tempo migliorare il codice che eseguirlo, qual è il punto nel farlo?

Quando dobbiamo migliorare la qualità del codice, probabilmente dobbiamo ottimizzarlo per le performance come step finale. Spesso il codice diventerà più veloce ed efficiente grazie ad altri cambi che facciamo. Quando siamo nel dubbio, possiamo vedere la seguente checklist per capire se lavorare o meno sulle perfomrnace.

1. Testing: abbiamo testato il codice per provare che funziona come atteso e senza erorri?
2. refactoring: il docie ha bisognodi cleanup per diventare più manutenibile?
3. profiling: abbiamo identificato le parti meno efficienti del nsotro codice?

Una volta che abbiamo fatto tutte queste cose, possiamo pensare ad ottimizzare le performance del nostro cdoice.

E' di solito più importante che il codice venga eseguito correttamente, rispettando i requisiti di business, e che gli altri membri possano capirlo, piuttosto che sia la soluzione più efficiente.

E, in realtà, la soluzione può risiedere altrove. Ad esempio, avere l'abilità di estendere rapidamente il codice con nuove feature prima dei nostri competitor avrà un impatto reale. Questo è vero specialmente quanod il collo di bottiglia nelle perfomance non è nel codice ma in parti esterne, come ad esempio la banda di comunicazione. Rendere Python più veloce non ci darà nessun vantaggio, ma renderà probabilmente il codice più complesso.

Infine, il codice diventerà spesso più rapido come risultato del fix di bug e del refactoring.

Come regola aurea, ogni volta che stiamo considerando l'ottimizzazione, dobbiamo per prima cosa effettuare la profilazione del codice per identificare quali colli di bottiglia risolvere. Altrimenti, potremmo trovarci ad inseguire il coniglio sbagliato. Seguendo il principio di pareto della regola 80/20, che si applica ad un sorprendente ampio range di aree, ottimizzare solo il 20% del nostro codice porterà spesso l'80% dei benefici.

Ma senza avere dati da un tool di profiling, non sapremo che parti del codice devono esere migliorate. E' motlo facile fare degli assunti sbagliati.

## Come trovare le perofmrance bottlenekc nel codice python mediante il profiling

Il software profiling è il processo legato al collezionamento ed analisi di varie metriche di un programma in esecuzione per identificare dei colli di bottiglia in termini di performance conosciuti come *hot spots*. Gli hot spot possono accadere per diverse ragioni, incluso un eccessivo uso della memoria, un uso inefficiente della CPU, o un layout dei dati non ottimale, che risulta in frequenti cache miss che aumentano la latenza complessiva.

!!!note "Nota"
    Un profiler è uno strumento la cui valenza sta nell'identificare gli hot spot  nel codice, ma che non ci dice come scrivere codice efficiente. E' spesso la scelta dell'algoritmo o struttura dati sottostante che fa la differenza. Anche se usiamo l'hardware più performante, un algorithmo con elevate complessità spaziali o temporali non convergerà in un tempo accettabile.

Quando facciamo la profilazione, è importante fare un'analisi dinamica, eseguendo il codice e collezionando dati reali piuttosto che contare su una review statica del codice. Dato che l'analisi dinamica spesso prevede l'esecuzione di un pezzo di software lento più volte, dovremmo iniziare con un quantiativo limitato di dati di input al nostro algoritmo, se possibile. Questo limiterà ilquantitativo di tempo che spendiamo attendendo i risultati di ciascuna iterazione.

Una volta che abbiamo il codice in esecuzione, possiamo usare uno dei molti profiler Python disponibili. Ci sono molti tipi di profiler, il che potrebbe confonderci. Tuttavia, dobbiamo sapere come scegleire il tool giusto per il lavoro da fare. Vediamo un rapido tour dei tool più popolari:

* timer, come le librerie standard time e timeit, o il package codetiming
* profiler deterministici, come profile, cProfile, e line_profiler
* profiler statistici, come Pyinstrument o perf

### time: misurare il tempo di esecuzione

La forma più semplice di profilazione del nostro codice prevede la misura del tempo di esecuzione del codice chiamando una delle funzioni del modulo time. Ad esempio:



>>> import time

>>> def sleeper():
...     time.sleep(1.75)
...

>>> def spinlock():
...     for _ in range(100_000_000):
...         pass
...

>>> for function in sleeper, spinlock:
...     t1 = time.perf_counter(), time.process_time()
...     function()
...     t2 = time.perf_counter(), time.process_time()
...     print(f"{function.__name__}()")
...     print(f" Real time: {t2[0] - t1[0]:.2f} seconds")
...     print(f" CPU time: {t2[1] - t1[1]:.2f} seconds")
...     print()
...
sleeper()
 Real time: 1.75 seconds
 CPU time: 0.00 seconds

spinlock()
 Real time: 1.77 seconds
 CPU time: 1.77 seconds



Per prima cosa, definiamo due funzioni, sleeper() e spinlock(). La prima funzione chiede al task scheduler del nostro sistema operativo di sospendere l'attuale thread di esecuzione per circa 1.75 secondi. Durante questo periodo, la funzioen rimane inattiva senza occupare la CPU del nostro computer, pemrettendo ad altri thread o programmi di essere eseguiti. Di contro, la seconda funzione effettua una forma di *busy waiting*, sprecando cicli della CPU senza fare alcun lavoro utile.

Successivamente, chiamiamo entrambe le nostre funzioni di test. Prima e dopo ogni invocazione, controlliamo il tempo attuale con time.perf_coutner() per ottenere il tempo trascorso, e time.process_time() per ottenere il CPU time. Questi ci diranno quanto è stato necessario alle nostre funzioni per essere eseguite e quanto di questo tempo hanno speso sul processore. Se una funzione attende un altro thread o un'operazione I/O per temrninare, allora non userà il tempo della CPU.

!!!note "Nota"
    Le performance di un programma per computer sono tipicamente limitate dalla potenza computazionale disponibile, dalla quanittà di memoria, operazioni di I ed O, e la latenza del programma. Se un certo task fa molti calcoli, allora sarà la velocità del processore a detemrinare di quanto tempo avrà bisogno per finire. Un task di questo tipo è vincolato alla CPU (CPU-bound). possiamo alle volte ese guire task in parallelo su più core della CPU per ridurre il tempo complessivo di elaborazione. D'altro canto, un task I/O bound spende la maggior parte del suo tempo attendendo che i dati arrivino dal disco, da un database, o da una rete. Questi task possono beneficiare dell'uso di canali di I/O più rapidi, o eseguirli in maniera concorrente o asincrona.

Chiamare la funzione timer direttamente per profilare il nostro codice Python può essere impegnativo, specialmente quando dobbiamo effettuare il profiling di molti snippet di codice. Per rendere più semplice il lavoro, possiamo usare dei package come codetiming, che utilizza classi, context managers e decorator.

Il modulo time è versatile e semplice da setuppare, il che lo rende adatto a check rapidi e temporanei. Ci darà un'impressione fedele del runtime richiesto nelle condizioni reali, prendenndo in considerazioni fattori come il carico attuale del sistema. Tuttavia, se siamo più interessati nell'avere delle condizioni di laboratorio per i nostri snippet, con meno influenze esterne, allora time potrebbe non essere la scelta migliore.

In questic asi, dovremmo disabilitare idealmente il garbage collector di Pythno e ripertere l'esercizio più volte provando a minimizzare l'influenza di fattori esterni, come il tempo di startup dell'interprete o il rumore del sistema. Per farlo, potremmo usare il modulo timeit.

### timeit: benchmark short code snippets

Per fare in modo che non si vada nei problemi comuni, Python ha un utile modulo chiamato timeit, che si occupa della maggior parte delle complesistà della profilazione. Questo significa tenere in conto di fattori come carico del sitema, garbage collection, o altri processi concorrenti che possono influenzare i risultati ottenuti. Il modulo timeit aiuta a mitigare questi fattori, fornendo una misura più accurata del tempo di esecuzione del codice.

Ecco un esempio di una funzione ricorsiva che calcola l'n-mo elemento della sequenza di Fibonacci.


>>> from timeit import timeit

>>> def fib(n):
...     return n if n < 2 else fib(n - 2) + fib(n - 1)
...

>>> iterations = 100
>>> total_time = timeit("fib(30)", number=iterations, globals=globals())

>>> f"Average time is {total_time / iterations:.2f} seconds"
'Average time is 0.15 seconds'

In particolare, chiedimao A timeit di misurare il tempo totale di esecuzione di fib(30) ripetuto cento volte in un ciclo. QUindi, calcoliamo il tempo mdio divendo i risultati per il numero di iterazioni.

Questa ripetizione minimizza gli effetti del rumore di sistema sul conteggio. Ripendendo le stesse chiamate a funzione più volte, possiamo avere la media delle fluttuazioni casuali nel tempo di esecuzione che possono arrivare dai processi in esecuzione sul nostro computer. Possiamo iniziare con le cinque iterazioni di defaulut lasciamo fuori il parametor number. Se la funzione è molto veloce o lenta, possiamo modificare questo parametro come serve per ottenere una misura accurata.

Quadno eseguiamo timeit dalla command line, o usiamo il magic command %timeit in un notebook Jupyter, vedremo il miglior runtime del code snippet che abbiamo fornito.


$ SETUP_CODE="def fib(n): return n if n < 2 else fib(n - 2) + fib(n - 1)"
$ python3 -m timeit -s "$SETUP_CODE" -r 100 "fib(30)"
2 loops, best of 100: 158 msec per loop


Se il codice testato richiede un setup, possiamo opzionalemnte istruire timeit ad eseguire una volta entrato nel loop. Spesso, saremo interessati soltanto nel vedere il miglior risultato, che è il più vicino al vero, mentre le run più lunghe indicano dei disturbi causati da rumore casuale.

Mentre timeit permette di effettuare il benchmark di un certo snippet misurando il tempo di esecuzione, non riesce a collezionare metriche più dettagliate per individuare eventuali colli di bottiglia. Per fortuna, Pyton ha un profile più sofisticato che vedremo a breve.

### cProfile: Collect Detailed Runtime Statistics

La libreria standard Python include un modulo profile (puramente in Pyuton) ed un'estensione equivalente implementata in C usando la stessa interfaccia, chiamata cProfile. In generale, è meglio usare cProfile, che ha performance migliori e meno overhead.

Di converso, dovremmo usare profile quando cProfile non è disponibile sul nostro sistema. Inoltre, potremmo preferire alle volte profiel quando vogliamo estenderlo usadno Python.

Entrambi i moduli forniscono un profiler deterministico, che ci può aiutare a rispondere ad omeande come quante volte uance rta funzione è stata chiamata o qunato tempo è stato speso all'interno diq uelal funzioen. Un profiler determinsitico può darci risultati ripdorduibili nelle stesse condizioni perché traccia tutte le chiamate a funzione nel nostro programma.

!!!note
    Internamente, cPRofile sfrutta sys.setprofile() per registrare un event listener che sarà notificato ogni volta che una delle nostre funzioni viene chiaamata. Per un monitoraggio ancora più granurlare, possiamo chiamare sys.settrace(), che ci permette di tracciare alcuni tipi di eventi al livello delle singole righe di codice. In altenrativa, possiamo trovare un tool di terze parti come line_profiler.

DA DOPO LA NOTA


https://realpython.com/python-profiling/#timeit-benchmark-short-code-snippets 


## Reference

https://realpython.com/python-concurrency/#what-is-parallelism

https://en.wikipedia.org/wiki/CPU-bound

https://realpython.com/intro-to-python-threading/

https://en.wikipedia.org/wiki/Scheduling_(computing)

https://en.wikipedia.org/wiki/Busy_waiting

https://en.wikipedia.org/wiki/Instruction_cycle

https://en.wikipedia.org/wiki/Elapsed_real_time

https://en.wikipedia.org/wiki/CPU_time

https://en.wikipedia.org/wiki/Input/output

https://en.wikipedia.org/wiki/I/O_bound

https://realpython.com/python-concurrency/

https://realpython.com/async-io-python/

https://realpython.com/python-with-statement/

https://realpython.com/primer-on-python-decorators/

https://realpython.com/python-memory-management/

https://realpython.com/python-thinking-recursively/

https://realpython.com/build-python-c-extension-module/
