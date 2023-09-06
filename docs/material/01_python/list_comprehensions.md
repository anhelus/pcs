# List comprehension

Python è noto per permetterci di scrivere codice elegante, semplice da scrivere, e praticamente semplice da leggere come se fosse normale inglese. Una delle feature più distintyinge del linguaggio è la *list comprehension*, che psosiamo usare per creare potenti funzionalità con una singola riga di codice. Tuttavia, molti ancor anon riescono a sfurttare le feature più avanzate delle list comprehensioni in Python. Altri invece le usano troppo, il che può condurre a difficoltà di lettura e inefficiente.

In questa lezione, illustreremo le potenzialità delle list comprehensioni in Python, e come usarle in modo ottimale. Vedremo anche i compromessi che derivano dal loro uso, in modo da capire quanod possono essere preferibili altri approcci. IN particolare,v edremo:

* riscrivere cicli e chiamate alla funzione map() come delle list comprehension
* scegleire tra list comprehension, cicli, e chyiamate a map()
* miglirare le list comprehension usando la logica condizionale
*é usar ele list comprehension per sostituire filter()
* effettuare il profiling del codice per risolvere problemi di performance

## Come creare liste in Python

Esistono diversi modi in cui possiamo creare delle liste in Python. per comprendere al meglio i compromessi legati all'uso delle list comprehension, vediamo come usare questi approcci.

##### Usare un ciclo for

Il più comune tipo di ciclo è il ciclo for. Possiamo usarlo per crear una lista di elementi in tre passi:

* inizializzare una lsita vuota;
* effettuare un ciclo su una sequenza di elementi;
* aggiungere ogni elemento al termine della lista.

Se vogliamo creare una lista contenente i primi dieci numeri quadrati, possiamo ad esempio usare le seguenti tre righe di codice:

>>> squares = []
>>> for i in range(10):
...     squares.append(i * i)
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

Qui, stiamo inizializzando la lista vuota quadrati. Quindi, usiamo un ciclo for per iterare la sequenza definita da range(10). Infine, moltiplichiamo ogni numero per ste sesso, aggiungendo il risultaot alla fine della lsita.

##### Utilizzo di map()

La funzione map() fornisce un approccio alternativo basato sulla programmazione funzionale. Passiamo una funzione ed un iterabile, e map() crea un oggetto. Questo contiene l'output che avremmo passando ogni elemento dell'iterabile attraverso la funzione.

Come esempio, consideriamo una situazione nella quale dobbiamo calcolare il prezzo netto per una serie di transwzioni:

>>> txns = [1.09, 23.56, 57.84, 4.56, 6.78]
>>> TAX_RATE = .08
>>> def get_price_with_tax(txn):
...     return txn * (1 + TAX_RATE)
>>> final_prices = map(get_price_with_tax, txns)
>>> list(final_prices)
[1.1772000000000002, 25.4448, 62.467200000000005, 4.9248, 7.322400000000001]

Nel codice precedente abbiamo un iterabile txns ed una funzione get_price_with_tax(). Passiamo questi argomenti a map(), e memorizziamo l'oggetto risultante in final_prices. Possiamo facilmente convertire questo oggetto in una lsita usando list().

##### Utilizzo delle list comprehension

Le list comprehension sono il terzo modo per creare delle liste. COn questo approccio, possiamo riscirvere il ciclo for del primo esempio in una singola riga di codice:

>>> squares = [i * i for i in range(10)]
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

Piuttosto che creare una lista vuota ed aggiungere ogni elemento al termien della stessa, ci limitiamo a definire la lista ed i suoi contenuti nello stesso momento seguendo questo formato:

new_list = [expression for member in iterable]

Ogni list comprehensioni in Python include tre elementi:

* l'espressione è il membro stesso, una chiamata ad un metodo, o una qualsiasi altra espressione valida che restitusice un valore. Nell'esmepio precedente, l'espressione i * i è il quadrato del valore del membro.
* il membro è lk'oggetto o valore nella lista o nell'ioterabile. Nell'esempio precedente, è pari ad i;
* l'iterabile è una lista, insieme, o ion geenerale una qualsiasi sequenza che può restituire i suoi elementi uno alla volta. Nell'esempio precedemte, l'iterabile è range(10).

Siccome il requisito dell'espressione è molto flessibile, una list comprehension in Python funziona bene in tutti i posti dove useremmo map(). Possiamo anche riscrivere il secondo esempio con la sua list comprehension:

>>> txns = [1.09, 23.56, 57.84, 4.56, 6.78]
>>> TAX_RATE = .08
>>> def get_price_with_tax(txn):
...     return txn * (1 + TAX_RATE)
>>> final_prices = [get_price_with_tax(i) for i in txns]
>>> final_prices
[1.1772000000000002, 25.4448, 62.467200000000005, 4.9248, 7.322400000000001]

L'unica distinzione tra questa implementaizone e map() è che la list comprehension in Python restituisce una lista, e non un oggetto map.

## Benefici dell'uso delle list comprehension

Le list comprehension sono spesso descritte come più *Pythonic* dei cicli o di map(). Ma piuttosto che accettare ciecamente questa affermazione, vale la pena comprendere i benefici dell'uso di una list comprehension in Python quando comparati alle alternative. Più avanti, vedremo alcuni degli scenari dove le alternative sono una scelta migliroe.

Uno dei benefici legati all'uso di una list comprehension in Python è che è un singolo strumento che possiamo usare in molte situazioni differenti. Oltre alla classica creazione di una lista, le list comprehension possonoe ssere usate anche per il *mapping* ed il filtraggio. Non dobbiamo usare un diverso approccio per ogni scenario.

Questa è la ragione principale per cui le list comprehension sono considerate Pythonic, in quanto Python prevede l'uso di semplici, potenti strumenti che è possibile usare in un'ampia varietà di situazioni. Come ulteriore beneficio, quando usiamo una list comprehension in Python, non dobbiamo ricordare l'ordine esatto degli argomenti come dovremmo farfe quando chiamiamo ad esempio map().

Le list comprehension sono inoltre più dichiarative dei cicli, il che significa che sono più semplici da capire e comprendere. I cicli ci chiedono di focalizzarci su come viene creata la lista. Dobbiamo creare manulamente una lista vuota, ciclare sugli elementi, ed aggiungere ciascuno di essi al termine della lista. Con una list comprehension, possiamo invece focalizzarci su quello che vogliamo vada nella lista, e lasciare a Python il compito di gestire la costruzione della stessa.

## Comprendere le list comprehension

Per comprendere il valore aggiunto che possono darci le list comprehension, è utile illustrare lo spettro di possibili funzionlità. 

##### Uso della logica condizionale

Prima, abbiamo visto questa formula per come creare le list comprehension:

new_list = [expression for member in iterable]

Anche se questa formula è accurata, è anche incompleta. Una descrizione più completa della formula per la list comprehension aggiunge il supporto ai condizionali opzionali. Il modo più comune di usare la logica condizionale in una list comprehension è aggiungere una condizione al termine dell'espressione:

new_list = [expression for member in iterable (if conditional)]

Qui, l'istruzione condizionale viene prima la parentesi quadra di chiusura.

L'istruzioen condizionale è importante perché permette alla list comprehension di filtrare valori non voluti, che richiederebbero normalmente una chiamata a filter():

>>> sentence = 'the rocket came back from mars'
>>> vowels = [i for i in sentence if i in 'aeiou']
>>> vowels
['e', 'o', 'e', 'a', 'e', 'a', 'o', 'a']

In questo codice, l'istruzione condizionale filtra tutti i caratteri nella frase che non sono una vocale.ù

L'istruzione condizionale può testare una qualsiasi espressione valida. Se abbiamo bisogno di un filtro più complesso, possiamo spostare la logica condizionale in una funzione separata.

L'istruzione condizionale può testare una qualunque espressione valida. Se abbiamo bisogno di un filtro più compless, possiamo spostare la logica condizionale in una funzione separata:

>>> sentence = 'The rocket, who was named Ted, came back \
... from Mars because he missed his friends.'
>>> def is_consonant(letter):
...     vowels = 'aeiou'
...     return letter.isalpha() and letter.lower() not in vowels
>>> consonants = [i for i in sentence if is_consonant(i)]
['T', 'h', 'r', 'c', 'k', 't', 'w', 'h', 'w', 's', 'n', 'm', 'd', \
'T', 'd', 'c', 'm', 'b', 'c', 'k', 'f', 'r', 'm', 'M', 'r', 's', 'b', \
'c', 's', 'h', 'm', 's', 's', 'd', 'h', 's', 'f', 'r', 'n', 'd', 's']

Qui stiamo creando un filtro complesso, chiamato is_consonant(), e passiamo questa funzione come istruzione condizionale alla list comprehension. notiamo che il valore `i` viene anche passato come argomento alla nostra funzione.

Possiamo piazzare l'istruzione condizionale al termine dell'istruzione per un semplice filtraggio. Tuttavia, se vogliamo cambiare il valore di un membro invece di filtrarlo, è utile piazzare il valore condizionale vicino all'inizio dell'espressione:

new_list = [expression (if conditional) for member in iterable]

Con questa formula, possiamo usare la logica condizionale per scegliere tra più opzioni di output possibili. Ad esempio, se abbiamo una list adi prezzi, potremmo voler rimpiazzare i prezzi negativi con 0 e lasciare i valori positivi intatti:

>>> original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
>>> prices = [i if i > 0 else 0 for i in original_prices]
>>> prices
[1.25, 0, 10.22, 3.78, 0, 1.16]

Qui, l'espressione i contiene un'istruizione condizionale. Questo dice a Pyuthon di mandare in output il valroe di i se il numero è positivo, cambiandolo a 0 se il numero è negativo. Se sembra eccessivamente complesso, potrebbe essere utile vedere la logica condizionale come una funzione a se stante:

>>> def get_price(price):
...     return price if price > 0 else 0
>>> prices = [get_price(i) for i in original_prices]
>>> prices
[1.25, 0, 10.22, 3.78, 0, 1.16]

Adesso, la nostra istruzione condizionale è contenuta in get_price(), e possiamo usarla come parte dell'espressione della list comprehension.

Usare Set e Dictionary Comprehnension

La list comphrenesion è uno strumento di uso comune, ma potremmo voler usare nche set e dictionary comprehnension. UNa set comprehension è molto simile ad una list comprehension; la differenza sta nel fatto che questa si assicura che l'output non contenga alcun duplicato. Possiamo creare una set comprehension usando delle parentesi graffe invece di quadre:

>>> quote = "life, uh, finds a way"
>>> unique_vowels = {i for i in quote if i in 'aeiou'}
>>> unique_vowels
{'a', 'e', 'u', 'i'}

La nostra set comprehension manda in uscita tutte le vocali univoche trovate in quote. A differenza delle lsite, gli insiemi non garantiscono che gli oggetti saranno salvati in ordine. Questo è il motivo per cui il primo membro del set è a, anche se la prima vocale è i.

Le dictionary comprehension sono simili, con il requisito aggiuntivo di dover definrie una chiave:

>>> squares = {i: i * i for i in range(10)}
>>> squares
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

Per creare i dizionari, possiamo suare le parentesi graffe e le coppie chiave valore.

## Usare il walrus operator

A partire da Python 3.8 è disponibile l'assignment expression, o walrus operator. per comprenderne il funzionamento, consideriamo il seguente esempio.

Diciamo di dover fare dieci richieste ad una API che restituisce i dati di temperatura. Ci interessano soltanto i risultati che sono superiori a 25 gradi. Immaginiamo che ogni richiesta restituirà dati differenti. IN questo caso, non vi è un modo per usare una lsit comprehension in Python per risolvere il problema.

Il walrus operator risolve qeusto problema. Ci permette di eseguire un'espressione, assegnando simultaneamente il valore di output ad una variabile. Il seguente esempio mostra come questo sia possibile, usanod la funzione get_weather_data() per generare dati meteo falsi:

>>> import random
>>> def get_weather_data():
...     return random.randrange(90, 110)
>>> hot_temps = [temp for _ in range(20) if (temp := get_weather_data()) >= 100]
>>> hot_temps
[107, 102, 109, 104, 107, 109, 108, 101, 104]

Spesso non dovremo usare l'assignment expression in una list comprehension, ma è uno strumento utile da avere a disposizione qualora necessario.

## Quando non usare una list comprehension

Le list comprehension sono utili e ci possono aiutare a scrivere codice elegante facile da leggere e debuggare, ma non sono sempre la scelta giusta. Possono rendere il coidce più lento, o usare più memoria. Se il nostro codice ha performance inferiori, o è più complesso da capire, allora è probabilmente meglio scegliere un'alternativa.

##### Occhio alle nested comprehension

Le compehension possono essere annidate per creare combinazioni di liste, dizionari, ed insiemi all'internod i una singola collezione. Ad esempio, diciamo che un laboratorio climatico stia tracciando le alte temperature in cinque diverse città per la prima settimana di giugno. La struttura dati perfetta per memorizzare questi dati potrebbe essere una lista Python in un dizionario:

>>> cities = ['Austin', 'Tacoma', 'Topeka', 'Sacramento', 'Charlotte']
>>> temps = {city: [0 for _ in range(7)] for city in cities}
>>> temps
{
    'Austin': [0, 0, 0, 0, 0, 0, 0],
    'Tacoma': [0, 0, 0, 0, 0, 0, 0],
    'Topeka': [0, 0, 0, 0, 0, 0, 0],
    'Sacramento': [0, 0, 0, 0, 0, 0, 0],
    'Charlotte': [0, 0, 0, 0, 0, 0, 0]
}

Creiamo la collezione esterna con una dictionary comprehension. L'espressione è data da una coppia chiave-valore,c he contiene un'altra comprension.

Le liste annidate sono un modo comune per creare delle matrici, che sono spesso usate per scopi matematici. Ad esempio:

>>> matrix = [[i for i in range(5)] for _ in range(6)]
>>> matrix
[
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4]
]

La list comprehension esterna [... for _ in range(6)] crea sei righe, mentre quella interna [i for i in range(5)] riempie ciascuna di queste righe con dei valori.

Finora, lo scopo di ogni comprehension annidata è abbastanza intuitiva. Tuttavia, ci sono altre situazioni, come il flattening di una lista, dove la logica rende il codice più complesso. Prendiamo ad esempio il caso in cui si usi una list comprehension annidata per vettorizzare una matrice:

matrix = [
...     [0, 0, 0],
...     [1, 1, 1],
...     [2, 2, 2],
... ]
>>> flat = [num for row in matrix for num in row]
>>> flat
[0, 0, 0, 1, 1, 1, 2, 2, 2]

Il codice per vettorizzare la matrice è sì conciso, ma potrebbe non essere facilmente comprensibile. D'altro canto, se usassimo dei cicli for per vettorizzar ela stessa matrice, il codice sarebbe molto più comprensibile:

>>> matrix = [
...     [0, 0, 0],
...     [1, 1, 1],
...     [2, 2, 2],
... ]
>>> flat = []
>>> for row in matrix:
...     for num in row:
...         flat.append(num)
...
>>> flat
[0, 0, 0, 1, 1, 1, 2, 2, 2]

Ora possiamo vedere che il codice atgtraversa una riga della matrice alla volta, estraendo tutti gli elementi nella riga prima di spostarsi alla seguente.

Mentre la list comprehension annidata a singola riga può sembrare più Pythonic,. quello che è più importante è escirvere codice che i nostri collaboratori possano facilmente comprendere e modificare. Quando scegliamo l'approccio, dovremo capire se la comprehension migliora op peggiora la leggibilità.

##### Scegliamo generator per grossid ataset

Una list comprehension in Python funziona caricando l'intera lista di uscita in memoria. Per liste di piccola o media dimensione questo va in generale bene. Se vogliamo sommare i quadrati dei primi mille interi, ad esempio, possiamo usare una lista:

>>> sum([i * i for i in range(1000)])
332833500

Ma se volessimo sommare i quadrati del primo miliardo di interi? Se provassimo a farlo sulla nostra macchina, il nostro computer probabilmente si bloccherebbe. Questo è legato al fatto che Python sta provando a creare una lista con un miliardo di interi, che consuma la memoria del nostro sistema,c he potrebbe non avere le risorse richieste per generare una enorme lista e memorizzarla in memoria. 

Quando la dimensione della lista diventa problematica, è spesso utile usare un generator invece di una list comprehension. Un generatore non crea una singola, grossa struttura data in memoria, ma invece restituisce un iteratore. Il nostro codice può richiedere il valore successivo dell'iteratore tante volte quanto necessario o fino a che non abbiamo raggiunto la fine della sequenza, memorizznado soltanto un valroe alla volta.

Se dovessimo sommare il primo miliardo di numeroi con un generatore, il programma potrebbe richiedere qualche secondo, ma sicurametne il computer non si bloccherà:

>>> sum(i * i for i in range(1000000000))
333333332833333333500000000

Possiamo dire che questo è un generatore perché l'espressione non è circondatra da parentesi quadre o graffe.

L'esempio precedente richiede comunque un certo sforzo da parte del computer, ma effettua le operazioni in maniera *lazy*. Ciò significa che i valori sono calcolati soltanto quando sono richiesti esplicitamente. Dopo che il generatore genera un valore (ad esempio 567 * 567), può aggiungere quel valore alla somma in esecuzione, quindi scartare questo valore e generare quello successivo. Quando la funzione somma richiede il valore successivo, il ciclo ricomincia. Il processo mantiene l'impronta in memoria piccola.

map() opera anche in maniera lazy, il che significa che la memoria non sarà un problema se scegliamo di usarla in questo caso:

>>> sum(map(lambda i: i*i, range(1000000000)))
333333332833333333500000000

Sta al programmatore scegliere se preferiamo l'espressione generatrice o la funzione map().

##### Profilare per ottimizzare le perforamance

Quidni, quale approccio è il più veloce? Dovremmousare la liost comprehension o una delle possibili alternative? Piuttosto che aderire ad una singola regola che sia vera in ogni caso, è più utile chiederci se le performance contano nelle circostanze specifiche. Se non è vero, allora è di solito meglio scegliere l'approccio che porta al codice più leggibiel.

Se siamo in uno scenario dove le performance sono importanti, allora è tipicamente meglio provare diversi approcci ed ascoltare i dati. Per esempio, possiamo sfruttare la libreria timeit per vedere quanto richiede a dei pezzi di codice l'esecuzione, comparando il runtime di map(), cicli for, e list comprehension:

>>> import random
>>> import timeit
>>> TAX_RATE = .08
>>> txns = [random.randrange(100) for _ in range(100000)]
>>> def get_price(txn):
...     return txn * (1 + TAX_RATE)
...
>>> def get_prices_with_map():
...     return list(map(get_price, txns))
...
>>> def get_prices_with_comprehension():
...     return [get_price(txn) for txn in txns]
...
>>> def get_prices_with_loop():
...     prices = []
...     for txn in txns:
...         prices.append(get_price(txn))
...     return prices
...
>>> timeit.timeit(get_prices_with_map, number=100)
2.0554370979998566
>>> timeit.timeit(get_prices_with_comprehension, number=100)
2.3982384680002724
>>> timeit.timeit(get_prices_with_loop, number=100)
3.0531821520007725

Mel caso precedente, definiamo tre metodi che usano un diverso approccio per la creazione di una lista. Quindi, diciamo a timeit di eseguire ciascuna di queste funzioni cento volte. timeit restituisce il tempo totale richiesto per queste 100 esecuzioni.

Come il codice dimostra, la differenza principale sta tra i cicli e map(), con il ciclo che richiede il 50% di più per esesre eseguito. Se questo conta o meno dipende dalla nostra applicazione.

## Conclusioni

Abbiamo visto come usare una list comprehension in Python persvolgere task complessi senza rendere il nostro codice troppo complicato.

Ora possiamo:

* semplificare cicli e chiamate a map() con delle list comprehension
* usare la logica condizionale nelle nostre list comprehension
* creare set e dictionary comprehension
* determinare se il nostro caso richiede maggiore chiarezza o performance

Quando vogliamo scegliere un metood per la creazione di una lsita, possiamo provare tra più implementazione e considerae quella che è più semplice da leggere e comprendere nel nostro scenario specifico. Se le performance sono importani, possiamo usare dei tool di profilazione per verificare il tutto.

Ricoridamo infine che anche se le list comprehension hanno molta attenzione, è l'abilità dello sviluppatore ad aiutarlo a scrivere codice pulito che soddisfa il task in gioco. Questo è quello che rende davvero il nostro codice Pyuthonic.

