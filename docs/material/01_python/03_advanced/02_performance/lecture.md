# 1.3.2 - Profiling del software

Man mano che avanziamo nella nostra carriera di programmatori, potremmo voler migliorare la qualità del nostro codice, ottimizzandone contestualmente le performance. Tuttavia, questa fase non può prescindere dalla valutazione delle tre ulteriori questioni descritte di seguito.

1. *Abbiamo testato il software per provare che funzioni come ci si aspetta?*
2. *Abbiamo effettuato un'adeguata operazione di refactoring del nostro codice?*
3. *Abbiamo identificato le parti meno efficienti del nostro programma?*

Infatti, è solitamente più importante che il nostro codice venga eseguito correttamente, rispetti i requisiti definiti in fase di progetto, e sia comprensibile ai nostri collaboratori, piuttosto che sia in grado di risparmiare 0.01 secondi in termini di velocità di esecuzione modificando dei cicli con list comprehension annidate.

Inoltre, la problematica potrebbe *non* risiedere nel nostro codice: ad esempio, se il nostro programma prevede un interscambio di dati attraverso la rete, il collo di bottiglia potrebbe risiedere nell'ampiezza di banda richiesta; in questi casi, rendere più performante il nostro software ci darà pochi vantaggi, rendendo tuttavia il codice più complesso del necessario.

!!!tip "Suggerimento"
    Opportuno notare come alle volte il nostro programma diventerà più performante semplicemente a seguito dell'individuazione e della risoluzione dei bug. Inoltre, il [principio di Pareto](https://it.wikipedia.org/wiki/Principio_di_Pareto) si applica anche al profiling: infatti, accade spesso che ottimizzare anche solo il $20\%$ del nostro codice ci porterà ad ottenere un $80\%$ in termini di miglioramento delle performance.

Tuttavia, per far questo, dovremo necessariamente utilizzare degli appositi strumenti. Vediamo insieme quali sono.




DA QUI
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

Possiamo usare cProfile sul nostro itnero programma mediante la riga di comando, o effettuare in alternativa il profiling di un codice più piccolo, come nel seguente esempio:


>>> from cProfile import Profile
>>> from pstats import SortKey, Stats

>>> def fib(n):
...     return n if n < 2 else fib(n - 2) + fib(n - 1)
...

>>> with Profile() as profile:
...     print(f"{fib(35) = }")
...     (
...         Stats(profile)
...         .strip_dirs()
...         .sort_stats(SortKey.CALLS)
...         .print_stats()
...     )
...
fib(35) = 9227465
         29860712 function calls (10 primitive calls) in 9.624 seconds

   Ordered by: call count

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
29860703/1    9.624    0.000    9.624    9.624 <stdin>:1(fib)
        1    0.000    0.000    0.000    0.000 pstats.py:118(init)
        1    0.000    0.000    0.000    0.000 pstats.py:137(load_stats)
        1    0.000    0.000    0.000    0.000 pstats.py:108(__init__)
        1    0.000    0.000    0.000    0.000 cProfile.py:50(create_stats)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}


<pstats.Stats object at 0x7fbbd6d47610>


L'output è decisamente verboso, ma ci dice che il programma ha richiesto più di nove secondi e mezzo per finrie, facendo esattamente 29860712 chiamata a funzione. Solo dieci di queste erano chiamate primitive o non ricorsive, inclusa una sola chiamata non ricorsiva a fib(). Le altre erano chiamate all'interno di fib() stessa.

!!!note
    Possiamo suare un modulo sepratao chiamato pstats per formattare, ordinare e stampare a schermo le statistiche collezionate a runtime. Il modulo diventa ancora più utile se mettiamo le statistiche in un file binario. In questo caso, possiamoe seguire pstats come un programma interattivo per esplorare i contenuti del file nel terminale.

Chiamare fib() con un input relativament epiccolo di 35 fa in modo che ci siano quasi trenta milioni di chiamate ricorsive. Il profiler ci restituisce che questo alto numero di chiamate conincide con un'area del codice dove il rpogramma spende la maggior parte del suo tempo. Quando approfondiamo, notiamo che la maggior parte di queste chiamate ricorsive sono ridondanti perché continuano a calcoalare lo stesso valore più e più volte.

Come rapida ottimizzazione, potremmo usare la memoization per mettere in cache i risutlati intermedi. In questo modo, calcoleremo ogni numero di fibonacci ua volta sola, ritulizzando irisultati in cache per chiamate successive a fib().

Non sapremmo questo senza aver fatto la profilazione del codice. Tuttavia, questa operazione comprota un notevole overhead a runtime a causa del codice di instrumentation che deve resgistrare etemere traccia di certi eventi. In alcuni casi, questo può far sì che non si riesca ad usare un tool di profilazione, specialmente in un ambiente di produzione con performance già compromesse.

Vedremo quindi una tecnica popolare che permette di risolvere questo problema.

### Pyinstrument: snapshot del call stack

Per abbassare l'overhead del profiler, posisamo suare il profiling statistico (https://en.wikipedia.org/wiki/Profiling_(computer_programming)#Statistical_profilers) e collezionare solo le metriche una volta ogni tanto. Questo funziona prendendo uno snapshot dello stato del programma a specifici intervalli. Ogni volta, il profiler registara un campione che consiste dell'intero stack di chiamata (https://en.wikipedia.org/wiki/Call_stack) dalla funzione attualmente in esecuzione fino all'ultimo antenato nelal gerarchia di chiamate.

Mentre un profiler statistico non fornisce lo stesso livello di dettaglio di uno deterministico, ci libera da alcuni dei problemi di questo.

DAto che un profile derterministico monitra tutte le chaimate a funzione nella nostra applicazione, ha un overhead notevole e produce molto rumore nel report. Inoltre,q uesto non è uniforme perché dipende dal numero attuale di chiamate a fuznione, il che ci porta a risultati inaccurati e distorti.

Di contro, un profiler statistico filtra le chiamate non significative che non influiscono sulle performance complessive, ed il suo overhead è uniforme e modificabiel. A seconda del tasso dic ampionamento, le funzioni che terminano velocemente ptorebbero anche non mostrarsi nel report.

Per usare un profiler statistico in Python, dovremo installare un tool come Pyinstrument o py-spy. Alcuni di questi sono migliori a seocndao del caso. Ad esempio, Pyinstrument non gestisce codice che viene seguito in più thread o chiama funzioni implementati in moduli C come NumPy o Pandsa.

Per sfruttare Pyinstrumnt, è meglio usare un esempio che comprende più di una funzione. Ecco un'impleentazione diretta di un metodo Monte Carlo (https://en.wikipedia.org/wiki/Monte_Carlo_method)per stimare i valori di pi per mezzo di simulazioni (https://realpython.com/simpy-simulating-with-python/) e probabiltià geometrica (https://en.wikipedia.org/wiki/Geometric_probability):


>>> from random import uniform

>>> def estimate_pi(n):
...     return 4 * sum(hits(point()) for _ in range(n)) / n
...

>>> def hits(point):
...     return abs(point) <= 1
...

>>> def point():
...     return complex(uniform(0, 1), uniform(0, 1))
...

>>> for exponent in range(1, 8):
...     n = 10 ** exponent
...     estimates = [estimate_pi(n) for _ in range(5)]
...     print(f"{n = :<10,} {estimates}")
...
n = 10         [2.8, 2.8, 3.6, 4.0, 3.6]
n = 100        [3.04, 3.04, 3.2, 2.96, 3.28]
n = 1,000      [3.136, 3.144, 3.128, 3.14, 3.12]
n = 10,000     [3.1448, 3.1408, 3.1448, 3.1456, 3.1664]
n = 100,000    [3.14872, 3.13736, 3.14532, 3.14668, 3.13988]
n = 1,000,000  [3.140528, 3.14078, 3.14054, 3.140972, 3.141344]
n = 10,000,000 [3.1414564, 3.1427292, 3.1402788, 3.1420736, 3.1407568]



Più iterazioni ci sono nella simulazione, migliore sarà l'approssimazione di pi- Qui, usiamo numeri complessi (https://realpython.com/python-complex-numbers/) come modo conveniente per rappresentare punti bidimensionali scelti casualmente (https://realpython.com/python-random/) usando una distribuzione di probabilità uniforme. Ogni punto giace in un quadrato univerario (https://en.wikipedia.org/wiki/Unit_square). Contando i punti che giacciono su un quadrant of a circle  (https://en.wikipedia.org/wiki/Circular_sector) chiuso in questo quadrato, possiamos timare il rapporto delle loro aree (pi/4).

Come altri tool Pyiunstrument ci permette di usare la command line o di fare il profiling di specifici parti di codice.


>>> from pyinstrument import Profiler
>>> with Profiler(interval=0.1) as profiler:
...     estimate_pi(n=10_000_000)
...

3.142216
>>> profiler.print()

  _     ._   __/__   _ _  _  _ _/_   Recorded: 11:17:13  Samples:  201
 /_//_/// /_\ / //_// / //_'/ //     Duration: 20.150    CPU time: 20.149
/   _/                      v4.5.0

Program:

20.100 <module>  <stdin>:1
└─ 20.100 estimate_pi  <stdin>:1
      [12 frames hidden]  <stdin>, random, <built-in>
         19.200 <genexpr>  <stdin>:2
         ├─ 12.900 point  <stdin>:1
         │  ├─ 8.000 Random.uniform  random.py:520
         │  │  ├─ 6.400 [self]  None
         │  └─ 4.900 [self]  None
         ├─ 4.800 [self]  None

>>> profiler.open_in_browser()


In questo caso, impostando il parametro inverval, diciamo a Pyinstrument di fare uno snapshot ogni ventesimo di secondo Quindi stimiamo il valore di pi usando un metodo Monte Carlo con dieci milioni di iterazioni.

Una frequenza di 0.1 secondi è bassa, per cui avremo dell'overhead a runtime, ma avremo dei dati meno fini nel report. Rifinendo l'intervallo di campionament, possiamoc ambiare la quantità di dettagli che apapre nel report. Più frequente è il campionamento, più dati il profiler collezionerà, al costo di un overhead più alto.

A qusto punto, stiampiamo il report vedendo la gerarchia di chiamate. Questo albero è più utile del report di default di cProfile perché ci msotra il contesto di una chiamata a funzione. Dopotutto, la stessa funzioen può esere chiamata da più punti e con diversi cscopi.

Tuttavia, alcuni degli stack frame (https://en.wikipedia.org/wiki/Call_stack#STACK-FRAME) sono nascosti per endere il report più leggibile. Se vogliamo rivelarli, dobbiamo aprire un interactive report (https://calmcode.io/pyinstrument/html.html) nel browser chiamadno profiler.open_in_browser().

Il report i dice che estimate_pi() spende la maggior parte del suo tempo nella generator expression (https://realpython.com/introduction-to-python-generators/#building-generators-with-generator-expressions). Quando andiamo ad approfnodire, notiamoc he la funzioen point() è il collo di bottiglia. Sfotuantamente, non possiamo fare molto perché chiama la funzione random.uniform() che richiede tempo per essere eseuigta.


Se però andiamo a vedre la funzione random.uniform(), vedremo che è puramente Python. Questo significa che può essere molto più lenta di una funzione implementata in C. In questo caso, posisamo rimpiazzare la chiamata ad uniform(0, 1) con random() perché le funzioni sono matematicamente equivalenti per questi valori di input. Quando lo facciamo, vedremo un migliroamento notevole nel tempo di calcolo.


### Key takeaways

Vediamo alcune questioni e risposte che riassumono i conctti più importanti che abbiamo appreso in questo tutorial. Possiamo usare queste domande per comprende la comprensione o ricapitolare e solidificare quello che abbiamo appreso. Dopo ogni domanda, avremo una breve spiegazione nascosta in una sezione collassabile.

**Cosa è il software profiling?**

Il profiling del software misura e analizza le sue statistiche a runtime epr trovare i colli di bottiglia. Un alto consumo di meomria, un uso non efficiente della CPU, e delle eccessive chiamate a funzione possono essere indicatori comuni di problemi potenziali nel software che hanno bisogno di miglioramenti.

**Perché dovremmo ottimizzare le performance del nostro codice?**

Il modello giusto per ottimizzare le performance ci aiuta a vrificare la correttezza dle codice, pulirlo per migliore manutenibilità, e identificare le parti meno efficienti mediante il profiling. Il pareto princple suggerisce che normalmente ottengono la maggioranza dei guadagni modificando solo i colli di bottiglio più critici nel codice.

**Quali sono i tool di profilazione più comuni per Python?**

Python offre diversi tool per profilazione, inclusi tool interni e di terze parti.

* per il timing base, possiamo usare i moduli della standard library time e timeit o un package esterno come codetiming.
* per collezionare statsitcihe dettagliate al costo di un alto overhead, possiamo usar ei profiler detemrinistici offerti dalla standard library profile o cProfile
* se abbiamo bisogno di un profiler stratistico, che periodicamente prende un'istantanea dello stato del programma, allora usiamo Pyinstrument

**Qual è la differneza tra la profilazione statistica e deterministica?**

Il profili deterministico rgistra tutte le chiamate a funzione fatte dal nostro programma. Fornisce un dettagliato report con il numero esatto di chiamate ad una particolare funzione o il suo tempo di esecuzione. La profilazione stastitica, d'altro canto, prend un campione del call stack solo ad intervalli periodici. Come risultato, filtra chiamante isniginifcatnti che non contano, e ha meno overhead di un profiler deterministico.

https://realpython.com/introduction-to-python-generators/#building-generators-with-generator-expressions

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

https://realpython.com/fibonacci-sequence-python/#visualizing-the-memoized-fibonacci-sequence-algorithm

https://en.wikipedia.org/wiki/Instrumentation_(computer_programming)
