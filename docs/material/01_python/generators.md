# Generator

Alle volte può essere capitato di lavorare con una funzione così compolessa che deve mantenere uno stato interno in memoria ogni volta che viene chiamata, ma che non è abbastanza grande da giustificare la creazione di una calsse. In altri casi, potrebbe esserci capitato di lavorare con un insieme di dati così grande da aver saturato la memoria della nostra macchina. In questi casi, i generator e l'istruzione yield possono aiutare.

In questa lezione, vedremo:

* cosa sono i generatori, e come usarli
* come creare delle funzioni ed espressioni generatrici
* come funziona l'istruzione yield in Python
* come usare più istruzioni yield in una funzione generatrice
* come usare metodi generatori avanzati
* come costruire pipeline di dati con più generatori

## Utilizzare i generatori

Introdotti con PEP 255, i generatori sono un tipo particolare di funzione che restituisce un cosiddetto *lazy iterator*. Questo oggetto altro non è un iteratore su cui è possibile cciclare, un po come le liste. Tuttavia, a differenza di queste, i lazy iterator non salvano il loro contenuto in memoria. 

Ora, potremmo chiederci come funzionano. Vediamo due esempi. Nel primo, vedremo come funzionano i generatori da una prospettiva "alta", nel secondo andremo a vedere nel dettaglio ogni esempio.

##### Esempio 1: lettura di file di grandi dimensioni

Un caso d'uso comune per i generatori è quello di lavorare con dei flussi di dati o con dei file di grandi dimensioni, come ad esempio dei grossi CSV. Ad esempio, come potremmo contare il numero di righe in un file di questo tipo? Potremmo usare una ciclo for:

```py
csv_content = csv_reader('file_csv.csv')

rows = 0
for row in csv_content:
    rows += 1

print(f'Numero di righe: {rows}')
```

Se guardiamo questo esempio possiamo pensare che `csv_content` sia una lista. Per crearla, `csv_reader()` apre `file_csv.csv` e carica i suoi contenuti in `csv_content`. Quindi, il programma itera sulal lsita, ed aumenta il valore di `rows` ad ogni riga.

Quessta spiegazione appare ragionevole, ma funzionerebbe se il file è di grandi dimensioni? Cosa succede se il file è più grande della memoria disponibile nel sistema? Per rispondere a questa domanda, supponiamo che `csv_reader()` apra il file e ne salvi i contenuti in un array:

```py
def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result
```

Questa funzione apre un file ed utilizza `file.read()` con `.split()` per aggiungere ogni riga come elemento separato di una lista. Se usassimo questa versione di csv_reader(), avremmo un output di quesot tipo:

```sh
Traceback (most recent call last):
  File "ex1_naive.py", line 22, in <module>
    main()
  File "ex1_naive.py", line 13, in main
    csv_gen = csv_reader("file.txt")
  File "ex1_naive.py", line 6, in csv_reader
    result = file.read().split("\n")
MemoryError
```

In questo caso, infatti, `open()` restituisce un generatore su cui possiamo iterare riga per riga. Tuttavia, file.read().split() carica tutto in memoria, causando il MemoryError.

Prima che questo accada, noteremo che il nostro computer probabilmente rallenterà; potrebbe essere addiorittura necessario forzare l'uscita del programma premendo Ctrl+C. Come possiamo gestire queste situazioni? Vediamo la nuova versione di csv_reader():

```
def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row
```

In questa versione, apriamo il file, lo iteriamo, e restituiamo una riga. Usare questa funzione dovrebbe produrre il seguente output senza errori di memoria:

Row count is 64186394

Cosa sta succedendo quindi? In poche parole, abbiamo modificato csv_reader() in un generatore. Quyesta versione apre un file, e "renderizza" ogni riga, invece di restituirla in memoria.

Possiamo anche definire un'*espressione generatrice* (generator comprehension), che ha una sintassi molto simile a quella delle listh comprehension. In questo modo, possiamo usare il generator senza chiamare una funzione:

```py
csv_gen = (row for row in open(file_name))
```

Questo è un modo più conciso di creare la lista csv_gen. Vedremo a breve maggior informazioni sull'istruzione yield; per adesso, ricordiamo questa differenza chiave:

* usare ytield restituirà un generator
* usare return restituirà la prima riga del file soltanto

##### Esempio 2: genmerare una sequenza infinita

Proviamo adesso a generare una sequenza infinita. In Python, per ottenere una sequenza finita, possiamo chiamare la funzione range() e valutarla come una lista:

>>> a = range(5)
>>> list(a)
[0, 1, 2, 3, 4]

Per generare una sequenza infinita, tuttavia, dovremo usare un genratore, vistoe  considerato che la memoria del nostro comptuer è finita:


def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

Questo codice è conciso. per prima cosa, inizializziamo la variabile num ed iniziamo un ciclo infinitoi. A questo punto, usiamo la funzione yield per restitruire num, in modo da catturare lo stato iniziale. Questo "mima" l'azione compiuta da range().

Dopo l'istruzione yield, incrementiamo il valore di num di 1. Se proviamo a farlo con un ciclo for, vedremo che quello che fa sembra inifinto:

>>> for i in infinite_sequence():
...     print(i, end=" ")
...
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29
30 31 32 33 34 35 36 37 38 39 40 41 42
[...]
6157818 6157819 6157820 6157821 6157822 6157823 6157824 6157825 6157826 6157827
6157828 6157829 6157830 6157831 6157832 6157833 6157834 6157835 6157836 6157837
6157838 6157839 6157840 6157841 6157842
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
KeyboardInterrupt

Il pèrogramma continuerà ad essere eseguito quindi fino a che non lo fermeremo manualmente.

Invece di usare un ciclo for, possiamo chiamare next() direttamente sul generatore. Questo è utile specialmente per testare un generatore nella console:

>>> gen = infinite_sequence()
>>> next(gen)
0
>>> next(gen)
1
>>> next(gen)
2
>>> next(gen)
3

Qui abbiamo un generatore chiamato gen, che iteriamo manualmente chiamando next(). Questo è un sanity check per assicurarci che i nostri generatori stiamo producendo l'output atteso.

!!!note 
    Quando usiamo next(), Python chiama .__next__() sulla funzione passata come parametro. Ci sono alcuni effetti che questa parametrizzazione permette, ma ciò va oltre lo scopo di questa lezione.

##### Esempio 3: individuare i palindromi

Possiamo usare delle sequenze infinite in molti modi, ma un uso pratico è nella costruzione di individuatori di palindromi. Un individuatore di palindromi trova tutte le sequenze di lettere o numeri che sono palindrome. Queste sono parole o numeri che sono lette allo stesso modo in avanti o all'indietro, come Anna o 1221. Per prima cosa, definiamo l'individuatore di palindromi numerico:



def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return num
    else:
        return False


Non focalizziamoci troppo sulla matematica nel coidce. Limitiamoci a notare che questa funzione prende un numero in input, lo inverte, e prova a vedere se il numero inverso è identico all'originale. Adesso possiamo usare il nostro genertatore di sequenze infinito per ottenere una lista di tutti i palindromi numerici:

>>> for i in infinite_sequence():
...     pal = is_palindrome(i)
...     if pal:
...         print(i)
...
11
22
33
[...]
99799
99899
99999
100001
101101
102201
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "<stdin>", line 5, in is_palindrome
KeyboardInterrupt

In questo caso, gli unici numeri che sono stampati a schermo sono quelli i cui valori sono gli stessi all'indietro o in avanti.

!!!note
    In pratica, è poco probabile che scriveremo dei generatori di sequenza infinite. Il modulo itertools infatti fornisce un generatore di questo tipo mediante itertools.count().

Ora che abbiamo visto un uso semplice per un generatore di sequenza infinita, addentriamoci nel come funzionano i generatori.

## Comprendere i generatori

Finora, abbiamo appreso le due modalità princiupali di creare un generatore: usare delle funzioni o delle espressioni. Potremmo avere anche una comprensione intuitiva di come funzionano i generatori. Prendiamoci però un momento per renderq eusta conoscenza un po' più esplicita.

Le funzioni generatrici appaiono come delle normali funzioni, ma con una caratteristica fondamentale: usano la parola chiave yield invece di return. Richiamiamo il generatore scritto in precedenza:

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

Notiamo come questa appaia come una normalissima funzione, ad eccezione del fatto che viene usata l'istruzione yield. Questa indica dove un certo valore viene mandato indietro al programma chiamante; tuttavia, a differenza di return, non usciamo immediatamente dalla funzione.

Invece, lo *stato della funzione viene mantenuto*. In questo modo, quando chiamiamo next() su un generatore (sia esplicitamente sia implicitamente all'interno di un ciclo for) la variabile num viene incrementata e restituita nuovamente. Dal momento che le funzioni generatrici assomigliano alle funzioni normali e agiscono allo stesso modo, possiamo presupporere che l'espressioni generatrici siano molto simili alle altre comprehension disponibili in Python.

## Usare le espressioni generatrici

Come le list comprehension, le espressioni generatrici ci permettono di creare rapidamente un genratore. Sono anche utili nei casi in cui vengono usate le list comprehension, con un beneficio aggiuntivo: possiamoc rearle senza costruire e mantener el'intero oggetto in memoria prima dell'iterazione. In altre parole, non avremo alcuna penalità di memoria quando siamo le espressioni generatrici. Facciamo un esempio con un quadrato di alcuni numeri.

>>> nums_squared_lc = [num**2 for num in range(5)]
>>> nums_squared_gc = (num**2 for num in range(5))

Sia nums_squared_lc e nums_squared_gc sono praticamente identiche, ma c'è una differenza. Vediamo cosa succede se ispezioniamo ciascuno di questi oggetti:

>>> nums_squared_lc
[0, 1, 4, 9, 16]
>>> nums_squared_gc
<generator object <genexpr> at 0x107fbbc78>

Il primo oggetto usa delle parentesi quadre per creare una lista, mentre il secondo crea un'espressione generatrice usando delle parentesi. L'output conferma che abbiamo creato un generatore e che è diverso da una lista.

## Profilazione delle performance

Abbiamo appreso che i generatori son un ottimo modo per ottimizzare la memoria. Mentre un genratore di una sequenza inifinta è un esempio estremo di questa ottimizzazione, vediamo l'esempio dei numeri quadrati, e monitoriamo la dimensione degli oggetti risultanti usando la funzione sys.getsizeof():

>>> import sys
>>> nums_squared_lc = [i ** 2 for i in range(10000)]
>>> sys.getsizeof(nums_squared_lc)
87624
>>> nums_squared_gc = (i ** 2 for i in range(10000))
>>> print(sys.getsizeof(nums_squared_gc))
120

In questo caso, la lista che otteniamo dalla list comprehension è di XXXXX byte, mentre il generatore soltanto di XXX. Questo significa che la lista è estremamente più "PESAnte" del generatore.

Vi è tuttavia una cos da tenere in mente. Se la lista può essere contenuta nella memoria disponibile della macchina, la list comprehension può essere più rapida dell'espressione generatrice equivalente. Per capirlo, sommiamo i risultati ottenuti dalle due espressioni precedenti, usando cProfile.run():

>>> import cProfile
>>> cProfile.run('sum([i * 2 for i in range(10000)])')
         5 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.001    0.001 <string>:1(<listcomp>)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


>>> cProfile.run('sum((i * 2 for i in range(10000)))')
         10005 function calls in 0.003 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    10001    0.002    0.000    0.002    0.000 <string>:1(<genexpr>)
        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
        1    0.001    0.001    0.003    0.003 {built-in method builtins.sum}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

Possiamo vedere che la somma di tutti i valori nella list comprehension ha richiesto un terzo del tempo di quello necessario ai generatori. Se la velocità è il problema, e non la memoria, una list comprehension potrebbe essere uno strumento migliore per il lavoro.

!!!note
    Queste misure non sono valide soltanto per gli oggetti cerati con le espressioni generatrici. Valgono anche per gli oggetti fatti dall'analoga funzione, dal momento che i generatori risultanti sono equivalenti.

Ricordiamo quindi che le list comprehension restituiscono litste intere, mentre le espressioni generatrici restituiscono generatori. I generatori lavorano allo stesso modo sia che siano creati da una funzione sia che lo siano da un'espressione. Usare unì'espressione ci permette semplicemente di defeinire generaotri più semplici in una singola riga.

L'istruzione yield è ciò che rende possibile tutto questo, per cui vale la pena analizzarla nel dettaglio.

## Comprendere l'istruzione yield

yield è un'istruzione abbastanza semplice da comprendere. Il suo compito primario è quello di controllare il flusso di una funzione generatrice in un modo simile all'istruzione return. Come detto brevemente prima, tuttavia, questa istruzione ha alcuni assi nella manica.

Quando usiamo una funzione generatrice o un'espressione generatrice,. restituiamo un particolare iteratore chiamato generatore. Possiamo assegnare questo generatore ad una variabile per utilizzarlo. Quando chiamiamo alcuni metodi sul generatore, come next(), il codice all'interno della funzione è eseguito fino all'istruzione `yield`.

Quando viene lanciata l'iustruzione yield, il programma sospende l'esecuzione della funzione e restituisce il valore genrato al chiamante. Di contro, return interrompe completamente l'escuzuione. Quando una funzione viene sospesa, lo stato della funzione viene salvato; questo permette di riprendere l'esecuzione quando chiamiamo uno dei metodi del generatore. In questo modo la valutazione della funzione riprende esattamente dopo lo yiueld. Possiamo vedere questo effetto in azione usando più istruzioni yield in Python:

>>> def multi_yield():
...     yield_str = "This will print the first string"
...     yield yield_str
...     yield_str = "This will print the second string"
...     yield yield_str
...
>>> multi_obj = multi_yield()
>>> print(next(multi_obj))
This will print the first string
>>> print(next(multi_obj))
This will print the second string
>>> print(next(multi_obj))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

Diamo uno sguardo più vicino all'ultima chiamata a nex(). Possiamo vedere che l'esecuzione si è interrotta con un traceback. questo è perché i generatori, come tutti gli iteratori, possono essere terminati. A meno che il generatore non sia infinto, si può iterarvi soltanto una volta sola. Una volta che tutti i valori sono stati valutati, l'iterazione si interromperà, edd il ciclo for terminerà. Se avessimo usato enxt(), allora avremmo avuto un'eccezione StopIteration esplicita.

!!!note
    StopIteration è un'eccezione naturale che viene lanciata per segnalare la fine di un iteratore. I cicli for, ad esempio, sono costruiti attorno a StopIteration. Possiamo poerfino implementare il nostro ciclo for usando un ciclo while:

>>> letters = ["a", "b", "c", "y"]
>>> it = iter(letters)
>>> while True:
...     try:
...         letter = next(it)
...     except StopIteration:
...         break
...     print(letter)
...
a
b
c
y

Possiamo approfonodire la StopIteration nella documentazione Pythons ulle eccezioni.

yield può essere usato in molti modi per controllare il flusso di esecuzione del nostro generatore. L'uso di piùà istruzioni yield può essere sfruttato liberamente.

## Uso di metodi generatori avanzati

Abbiamo visto gli usi più comuni dei generfatori, ma vi sono alcuni altri trucchi da scoprire. Oltre a yield, i genraotri possono usare i seguenti metodi:

.send()
.throw()
.close()

##### .send()

Vediamo di costruire un programma che usa tutti e tre questi metodi. Questo programma stampa dei palindromi numerici, come in precedneza, ma con alcuni accorgimenti. Quando trova un palindromo, il nostro nuivov programma aggiungerà una cira ed inziiera a cercare ils eguente da qui. Gestiremo inoltre le eccezioni con .throw(), e fermeremo il genratore dopo und ato numero di cifre con .close(). Per prima cosa, richiamiamo il codice per il nostro idnividuatore di palindromi:

```
def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return True
    else:
        return False
```

Il codice è in pratica analogo al precedente, ad eccezione del fatto che adesso il programma restituisce strettamente vero o falso. Dovremo anche modifichare il nostro generatore di sequenze infinite originario come segue:

def infinite_palindromes():
    num = 0
    while True:
        if is_palindrome(num):
            i = (yield num)
            if i is not None:
                num = i
        num += 1

In questo caso vi sono diversi cambi. Il primo è alla riga 5, dove i = (yield num). Soffermiamoci un attimo.

Abbiamo detto in precedenza che yield è un'istruzione: ciò non è totalmente vero, più propriamente è un'espressione a partire da Python 2.5. Ciò ci pèermette di usarla in un blocco come il precedente, dove i prende il valore che viene generato. Qeusto ci permette di manipolare il valore generato. Inoltr,e ci permette di chiamare il metodo .send() per iniviare un valore al genratore. Quando l'esecuzione riprende dopo yield, i assumerà il valore che viene mandato.

Verifichiamo anche che i non sia None, il che può susccedere se next() viene chiamato sul genratore. Se i ha un valore, allora aggiorniamo num con questo nuovo valore. Indipendetnemente dal fatoto che i abbia un valroe, incrementeremo num ed inizieremo nuovamente il ciclo.

Adesso diamo un'occhiata al codice della fuznione principale, che ivnia il numero più basso con un'altra cifra al generatore. Per esempio, se il palindrmo è 121, allora invierà 1000:

pal_gen = infinite_palindromes()
for i in pal_gen:
    digits = len(str(i))
    pal_gen.send(10 ** (digits))

Con questo codice, creiamo un geratore e vi iteriamo sopra. Il programma genera un valore soltanto quando si trova un palindromo. Viene usata la funzione len(9n per determinare) il numero di cifre nel palindromo, e inviato 10 ** questo numero al genratore. Questo porta l'esecuzione nella logica del genratore e assegna 10 ** cifra a i. Dal momento che i ha adesso un valore, il programma aggiorna num, incrementandolo, e controlla di nuovo la presenza di palindromi.

Una volta che il nostro codice trova e genera un altro palindromo, si itera mediante il ciclo for. Questo è lo stesso che iterare con next(). Il generatore riprende alla riga 5 con i = (yield num). Tuttavia, ora i è None, perché non abbiamo mandato esplicitamente un valroe.

Quello che abbiamo creato qui altro non è se non una coroutine, o una funzione generatrice nella quale possiamo passare dei dati. Queste sono utili per costruire delle pipeline di dati, ma come vedremo presto, non sono necessarie.

Ora che abbiamo visto come si usa .send(), vediamo come si usa .throw().

.throw() ci permette di lanciare eccezioni nel genratore. Nell'esempio precedente, lanciamo l'eccezione alla rgia 6. Questo codice lancia un ValueError una volta che le cifre raggiungono il valore 5:

pal_gen = infinite_palindromes()
for i in pal_gen:
    print(i)
    digits = len(str(i))
    if digits == 5:
        pal_gen.throw(ValueError("We don't like large palindromes"))
    pal_gen.send(10 ** (digits))

Il codice è praticamente lo stesso, ma adesso controlliamo se digits è pari a 5. Se ciò avviene, si lancia un ValueError. PEr confermare che questo funziona come atteso, vediamo l'output del codice:

11
111
1111
10101
Traceback (most recent call last):
  File "advanced_gen.py", line 47, in <module>
    main()
  File "advanced_gen.py", line 41, in main
    pal_gen.throw(ValueError("We don't like large palindromes"))
  File "advanced_gen.py", line 26, in infinite_palindromes
    i = (yield num)
ValueError: We don't like large palindromes

.throw() è utile nei casi in cui potremmo voler catturare un'eccezione. In questo esempio, abbiamo usato .throw() pèer controllare quando abbiamo smesso di iterare nel genratore. Possiamo farlo in modo più elegante con .close().

Come implica il nome, close() ci permette di fermare un genrator. Questo può tornare utile quando si controlla un generatore di sequenza infita. Aggiorniamo il codice precedente cambiando .thorw() in .close() per fermare l'iterazione:

pal_gen = infinite_palindromes()
for i in pal_gen:
    print(i)
    digits = len(str(i))
    if digits == 5:
        pal_gen.close()
    pal_gen.send(10 ** (digits))
Instead of calling .throw(), you use .close() in line 6. The advantage of using .close() is that it raises StopIteration, an exception used to signal the end of a finite iterator:

11
111
1111
10101
Traceback (most recent call last):
  File "advanced_gen.py", line 46, in <module>
    main()
  File "advanced_gen.py", line 42, in main
    pal_gen.send(10 ** (digits))
StopIteration

Ora che abbiamo appreso di più sui metodi speciali che vengono con i generatori, parliamo dell'uso dei genratori per creare delle data pipelines.

## Esempio: creware delle data pipeline con dei generator

Le data pipeline ci permettono di creare del codice che elabori grossi dataset o flussi di dati senza saturare la memoria della nostra macchina. Imaginiamo di avree un file CSV di grandi dimensioni.

Per analizzarlo, pensiamo ad una strategia di questo tipo:

* leggere ogni riga del file
* suddividere ogni riga in una lista di valori
* estrarre i nomi delle colonne
* usare i nomi delle colonne e delle liste per creare un dizionario
* filtrare ciò che non ci interessa
* calcolare dei valori statistici

!!!note
    Nel caso reale, lo faremo con pandas. Tuttavia, dimostriamo l'uso dei generatori.

Iniziamo leggendo ogni riga dal file con un'espressione generatrice:

file_name = "techcrunch.csv"
lines = (line for line in open(file_name))

Quindi usiamo una ltra espressione con la precedente per suddividere ogni riga in una lista:

list_line = (s.rstrip().split(",") for s in lines)

Qui creiamo il generatore list_line, che itera lugngo le righe del primo generatore. Questo è un pattern comune da usare quando si progettano delle pipeline. A questo punto, estraiamo i dati che ci interessano. Dato che i nomi delle colonne sono di solito la prima riga in un file CSV; possiamo prenderla usando una breve chiamata a nex():

cols = next(list_line)

Questa chiamata a next() avanza l'iuteratore sul generatore list_line una volta. Se mettiamo tutto insieme, il codice dovrebbe assomigliare al seguente:

file_name = "techcrunch.csv"
lines = (line for line in open(file_name))
list_line = (s.rstrip().split(",") for s in lines)
cols = next(list_line)

In pratica, creiamo per prima cosa un'espressione generatrice per generare ogni riga nel file. A questo punto, iteriamo nel generatore all'interno della definizione di un'altra espressione generatrice chiamata list_line, che trasforma ogni riga in una lista di valori. Quindi, proseguiamo l'iterazione di list_line una volta con next() per ottenere una lista die nomi delle colonne per il nostro file CSV.

Per aiutare a filtrare ed effettuaire operazioni sui dati, creremo dei dizionari dove le chiavi sono i nomi delle colonne nel CSV:

company_dicts = (dict(zip(cols, data)) for data in list_line)

Quest'espèressione generatrice itera attraverso le liste prodotte da list_line. Quinid sua zip() e dict() per creare i dizionari come deto in precedenza. A questo punto, useremo un quarto generatore per filtrare ciò che vogliamo:

funding = (
    int(company_dict["raisedAmt"])
    for company_dict in company_dicts
    if company_dict["round"] == "a"
)

L'espressione generatrice itera i risultati di company_dicts e prende il valore desiderato.

Ricoridamo che non stiamo iterando su questi valori in una volta sola nella espressioen generatrice. nei fatti, non stiamo iterando su inente fino a che non usiamo un ciclo for o una funzione che opera sugli iteratori, come sum(). Infatti, chiamando sum() itereremo sul generatore:

total_series_a = sum(funding)

Lo script finale avrà una forma simile a questa:

file_name = "techcrunch.csv"
lines = (line for line in open(file_name))
list_line = (s.rstrip().split(",") for s in lines)
cols = next(list_line)
company_dicts = (dict(zip(cols, data)) for data in list_line)
funding = (
    int(company_dict["raisedAmt"])
    for company_dict in company_dicts
    if company_dict["round"] == "a"
)
total_series_a = sum(funding)
print(f"Total series A fundraising: ${total_series_a}")

In pratioca:

* alla riga 2, leggiamo ogni riga del fiel
* alla riga 3, suddividiamo le righe in valori e inseriamo i valori in una lsita
* alla riga 4 usiamo enxt() per memorizzare i nomi delle colonne in una lsita
* alla riga 5 creiamo dei dizionari ed uniamo gli stessi con una chiamata a zip(),, in cui le chjiavi sono i nomi delle colonne, mentre i vlaori sono le righe sotto forma di lista
* la riga 6 ottiene i valori necessari
* la riga 11 inizia il processo di iterazione chiamando la funzione sum().

!!!note
    I metodi per la gestione dei file CSV che abbiamo sviluppato sono utili a capire come usare i generatori e l'istruzione yuield. Tuttavia, lavorando con file CSV, è consigliabile usare il modulo CSV o la libreria Pandas, che risultano essere ottimizzati.
