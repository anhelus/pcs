In Python, un ciclo for è normalmente scritto come un ciclo su un oggetto iterabile. Questo singifica che non abbiamo bisogno di un contatore per accedere agli oggetti nell'iterabile. Alle volte, tuttavia, vogliamo avere una variabile che cambia ad ogni iterazione del ciclo. Piuttosto che creare ed incrementare una varaibile, possiamo usare il metodo enumerate() per ottenere un contatore ed un valore dall'iterabile allo stesso tempo.

## iterare con i cicli for in Python

Un ciclo for in Python usa delle *collection-based iteration*. In altri termini, ciò singifica che Python assegna l'oggetto successivo in un iterabile alla variabile di loop ad ogni iterazione, come in questo esempio:

```py
>>> values = ["a", "b", "c"]

>>> for value in values:
...     print(value)
...
a
b
c
```

In questo esempio, `values` è una lista con tre stringhe. In Python, le liste sono un tipo di oggetto iterabile. Nel ciclo for, la variabile su cui si cicla è il valore. Ad ogni iterazione del ciclo, il valore è impostato all'oggetto successivo sui valori.

Adesso, stampiamo a schermo `value`. Il vantaggio delle iterazioni collection-based è che ci aiutano ad evitare l'errore `off-by-one` che è comune in altri lingauggi di programmazione.

Adesso immaginiamo che, oltre al valore stesso, vogliamo stampare l'indice dell'oggetto nella lista sullo schermo ad ogni iterazione. Un modo di approcciare questo task è creare una variabile per memorizzare l'indice ed aggiornarla ad ogni iterazione:

```py
>>> index = 0

>>> for value in values:
...     print(index, value)
...     index += 1
...
0 a
1 b
2 c
```

In questo esempio, `index` è un intero che tiene traccia di dove siamo nella lista. Ad ogni iterazione del loop, stampiamo `index` così come `value`. L'ultimo step nel ciclo è aggiornare il numero memorizzato nell'indice di uno. Un bug comune avviene quando dimentichiamo di aggiornare l'indice ad ogni iterazione:

```py
>>> index = 0

>>> for value in values:
...     print(index, value)
...
0 a
0 b
0 c
```

In questo esempio, l'indice rimane a 0 ad ogni iterazione percHé non c'è del codice che ne aggiorna il valore al termine del ciclo. Specie epr cicli lunghi o complicati, questo tipo di bug è notoriamente difficile da individuare.

Un altro modo comune per approcciare questo problema è usare range() combinato con len() per creare automaticamente un indice. In questo modo, non dobbiamo ricordarci di aggiornare l'indiice:

```py
>>> for index in range(len(values)):
...     value = values[index]
...     print(index, value)
...
0 a
1 b
2 c
```

In questo esempio, `len(values)` restituisce la lunghezza di `values`, che è $3$. Quindi, `range()` crea un iteratore che va dal valore di default di partenza di `0` fino a quando non arriva a `len(values)` meno uno. In questo caso, `index` diventa la variabile su cui si cicla. Nel loop, impostiamo il valore uguale all'oggetto nei valori al valore attuale dell'indice. Successivamente, stampiamo l'indice ed il valore.

Con questo esempio, un bug comune che può avvenire è quando ci dimentichiamo di aggiornare il valore all'inizio di ogni iterazione. Questo è simile al bug precedente in cui ci dimentichiamo di aggiornare l'indice. Questa è una delle ragioni per le quali questo loop non viene considerato Pythonic.

Questo esempio è anche in qualche modo ristretto perché values deve permettere l'accesso ai suoi uggetti usando indici interi. Gli iterabili che permettono questo tipo di accessi sono chiamati sequenze in Python.


!!!note "Dettaglio tecnico"
    Secondo la documentazione Python, un iterabile è un *qualsiasi* oggetto che può restituire i suoi membri uno alla volta. Per definizione, gli iterabili supportano il protocollo iterator, che specifica come i membri dell'oggetto sono restituiti quando un oggetto è usato in un iteratore. Python ha due tipi comuni di iteraotri: sequenze e generatori.

Un qualsiasi iterabile può essere usato in un ciclo for, ma solo le sequenze possono essere accedute da indici interi. Provare ad accedere agli oggetti per indice da un generatore o un iteratore lancerà un TypeError:

```py
>>> enum = enumerate(values)
>>> enum[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'enumerate' object is not subscriptable
```

In questo esempio, assegnamo il valore di ritorno di `enumerate()` ad `enum`. `enumerate()` è un iteratore, per cui provare ad accedere ai suoi valori per indice lancia un `TypeError`.

Fortunatamente, il metodo `enumerate()` di Python ci permette di evitare tutti questi problemi. E' una funzione integrata, il che significa che è stato disponibile in ogni versione di Python dal momento in cui è stato aggiunto in Python 2.3, nel 2003.

## Usare il metodo enumerate()

Possiamo usare enumerate() in un loop allo stesso modo in cui si usa l'oggetto iterabile originario. Invece di inserire l'iterabile direttamente dopo `in` nel loop, lo mettiamo tra le parentesi di `enumerate()`. Dobbiamo anche cambiare la variabile di iterazione:

```py
>>> for count, value in enumerate(values):
...     print(count, value)
...
0 a
1 b
2 c
```

QUando usiamo `enumerate()`, la funzione ci restituisce due variabili su cui iterare:

* il conteggio dell'iterazione attuale
* il valore ell'oggetto all'attuale iterazione

Proprio come nel caso di un normale ciclo for, le variabili di loop possono essere chiamate come vogliamo. Possiamo usare `count` e `value` dell'esempio precedente, ma potremmo ad esempio usare `i` e `v`, o ogni altro nome Python valido.

Con `enumerate()`, non dobbiamo ricordare l'accesso all'oggetto dall'iterabile, e non dobbiamo ricordare di aumentare l'indice alla fine del ciclo. Tutto viene gestito automaticamente.

!!!note "Dettaglio tecnico"
    L'uso di di due variabili di loop, `count` e `value`, separate da una virgola è un esempio di *argument unpacking*. Questa feature Python sarà discussa in seguito.

La funzione `enumerate()` ha un ulteriore argomento che possiamo usare per controllare il valore di partenza del conteggio. Di default, il valore di partenza è `0` perché le sequenze Python sono indicizzati partendo da zero. In altre parole, quando vogliamo recuperare il primo elemento di una lista, usiamo l'indice `0`:

```py
>>> print(values[0])
a
```

Possiamo vedere in questo esempio che accedere a `values` con indice `0` restituisce il primo elemento, `a`. Tuttavia, ci sono molte volte quando non vogliamo che il conteggio di `enumerate()` parta a `0`. Ad esempio, potremmo voler stampare a schermo un contatore come output per l'utente. IN questo caso, possiamo usare l'argomento `start` passato ad `ennumerate()` per cambiare il contatore di partenza:

```py
>>> for count, value in enumerate(values, start=1):
...     print(count, value)
...
1 a
2 b
3 c
```

In questo esempio, passiamo `start=1`, che inizia il conteggio con il valore `1` sulla prima iterazione del loop. Se compariamo questo con gli esempi precedenti, nei quali `start` aveva il valore di default di `0`, e possiamo vedere la diffferenza.

## Pratica

Dovremmo usare `enumerate()` ogni volta che dobbiamo usare il contatore ed un oggetto in un ciclo. Teniamo a mente che `enumerate()` aumenta il conteggio di uno ad ogni iterazione. Tuttavia, questo limita soltanto leggermente la nostra flessibilità. Dato che `count` è un intero standard, possiamo usarlo in molti modi. Vediamo alcuni esempi.

### Conteggio naturale di oggetti iterabili

Nella sezione precedente, abbiamo visto come usare `enumerate()` per iniziare a creare un contatore naturale da stampare a schermo per l'utente. `enumerate()` è usato anche in questo modo all'interno della codebase Python. Possiamo vedere un esempio in uno script che legge i file reST e dice all'utente se ci sono problemi di formattazione.

!!!note "Nota"
    reST, detto anche reStructured Text, è un formato standard per i file di testo che Python usa per la documentazione. Vedremo spesso delle stringhe formattate secondo reST incluse come docstring nelle classi e funzioni Python. Gli script che leggono i file del codice sorgente e dicono all'utente dei problemi di formattazione sono chiamati *linter* perché cercano i *metaphorical lint* (TODO: TRADURRE) nel codice.
  
Questo esempio è leggermente modificato da rstlint.py. Non ci preoccupiamo come questa funzione controlla i problemi: il punto è quello di mostrare un uso vero di enumerate().

```py
def check_whitespace(lines):
    """Check for whitespace and line length issues."""
    for lno, line in enumerate(lines):
        if "\r" in line:
            yield lno+1, "\\r in line"
        if "\t" in line:
            yield lno+1, "OMG TABS!!!1"
        if line[:-1].rstrip(" \t") != line[:-1]:
            yield lno+1, "trailing whitespace"
```

`check_whitespae()` prende un argomento, `lines`, che sono le linee del file che deve essere valutato. Alla terza riga di `check_whitespace()`, enumerate() è usato in un loop su `lines`. Questo restituisce il numero di linea, abbreviato in `lno`, e la linea stessa. Dal momento che `start` non èusato, `lno` è un contatore che parte da zero delle righe nel file. `check_whitespaces()` fa diversi controlli per individuare i caratteri fuori psoto:

* il carriage return \r
* il carattere tab \t
* un qualsiasi spazio o tab alla fine della riga

Quando uno di questi oggetti è presente, `check_whitespace()` restituisce il numero di riga attuale ed un messaggio utile all'utente. La variabile contatore `lno` vi aggiunge uno in modo che restituisca il numero di contatore di linea piuttosto che un idnice preso a partire da zero. QUando un utente di `rslint.py` legge il messaggio, saprà a quale riga andare e quello da controllare.

## Istruzioni condizionali per saltare oggetti

Usare le istruzioni condizionali per elaborare gli oggetti può essere una tecnica molto potetne. Alle volte, dobbiamo effettuare un'azione soltanto alla prima iterazione di un loop, come in questo esempio:

```py
>>> users = ["Test User", "Real User 1", "Real User 2"]
>>> for index, user in enumerate(users):
...     if index == 0:
...         print("Extra verbose output for:", user)
...     print(user)
...
Extra verbose output for: Test User
Real User 1
Real User 2
```

In questo esempio, usiamo una lista come mock di un database di utenti. Il primo utente è il nostro utente di test, per cui vogliamo creare delle informazioni di diagnostica su quell'utente. Dal momento che abbiamo impostato il sistema in modo che l'utente di test sia il primo, possiamo usare il primo valore dell'indice del loop per stampare dell'output verboso extra.

Possiamo anche combinare delle operazionimatematiche con delle condizioni per il conteggio o l'indice. PEr esempio, possiamo restituire degli oggetti da un iterabile, ma soltanto se hanno un indice pari. Possiamo far questo usando enumerate().

```py
>>> def even_items(iterable):
...     """Return items from ``iterable`` when their index is even."""
...     values = []
...     for index, value in enumerate(iterable, start=1):
...         if not index % 2:
...             values.append(value)
...     return values
...
```

La funzione `even_items()` prende un argomento, chiamato `iterable`, che dovrebbe essere un qualche tipo di oggetto su cui Python può ciclare. Per prima cosa, `values` viene inizializzato ad una lista vuota. Quindi possiamo creare un ciclo for sull'iterabile con `enumerate()` ed impostare `start=1`.

All'interno del ciclo for, controlliamo se il resto della divisione per due è zero. Se questo è vero, aggiungiamo l'oggetto a values. Infine, restituiamo values.

Possiamo rendere il codice più Pythonic usando una list comprehension per fare la stessa cosa in una riga senza inizializzare una lista vuota:

```py
>>> def even_items(iterable):
...     return [v for i, v in enumerate(iterable, start=1) if not i % 2]
...
```

In questo codice di esempio, `even_items()` usa una list comprehension piuttosto che un ciclo for per estrarre ogni oggetto dalla ista il cui indice è un numero pari.

Possiamo verificare che `even_items()` funziona come atteso ottenendo gli oggetti con indice pari da un range di interi da 1 a 10. Il risultato sarà:

```py
>>> seq = list(range(1, 11))

>>> print(seq)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

>>> even_items(seq)
[2, 4, 6, 8, 10]
```

Come atteso, `even_items()` restituisce gli oggetti ad indice pari da `seq`. Questo non è il modo più efficienti per ottenere i numeri pari quando stiamo lavorando con gli interi. Tuttavia, ora che abbiamo verificato che `even_items()` lavora propriamente, possiamo ottenere le lettere ad indice pari dell'alfabeto ASCII:

```py
>>> alphabet = "abcdefghijklmnopqrstuvwxyz"

>>> even_items(alphabet)
['b', 'd', 'f', 'h', 'j', 'l', 'n', 'p', 'r', 't', 'v', 'x', 'z']
```

In questo caso, `alphabet` è una stringa che ha tutte le ventisei lettere minuscole dell'alfabeto ASCII. Chiamare `even_items()` e passare `alphabet` restituisce una lista di lettere alternate dall'alfabeto.

Le stringhe Python sono sequenze, che possono essere usate in cicli così come nell'indicizzazione intera e nello slicing. In caso di stringhe, possiamo usare delle parentesi quadre per ottenere la stessa funzionalità di `evne_items()` in modo più efficiente:

```py
>>> list(alphabet[1::2])
['b', 'd', 'f', 'h', 'j', 'l', 'n', 'p', 'r', 't', 'v', 'x', 'z']
```

Usando lo string slicing qui, diamo all'indice di partenza `1`, che corrisponde al secondo elemento. Non vi è un indice finale dopo la prima virgola, per cui Python va fino alla fine della stringa. Quindi aggiungiamo la seconda virgola seguita da un 2, in modo che Python prenda ogni elemento pari.

Tuttavia, come visto in precedenza, i generator e gli iterator non possono essere indicizzati o con slicing, per cui troveremo sempre utile `enumerate()`. Per continuare l'esempio precedente, possiamo creare una funzione generator che restituisce le lettere dell'alfabeto su richiesta:

```py
>>> def alphabet():
...     alpha = "abcdefghijklmnopqrstuvwxyz"
...     for a in alpha:
...         yield a

>>> alphabet[1::2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'function' object is not subscriptable

>>> even_items(alphabet())
['b', 'd', 'f', 'h', 'j', 'l', 'n', 'p', 'r', 't', 'v', 'x', 'z']
```

In questo esempio, definiamo `alphabet()`, una funzione generator che restituisce le lettere dell'alfabeto una ad una quando la funzione è usata in un loop. Le funzioni Python, siano esse generator o funzioni regolari, non possono essere accedute mediante l'indicizzazione con parentesi quadre. Questo viene provato sulla seconda riga e lancia un TypeError.

Possiamo usare le funzioni generator in dei loop, tuttavia, e lo facciamo sull'ultima riga passando `alphabet()` ad `even_items()`. Possiamo vedere che i risultati sono gli stessi dei due esempi precedenti.

## Comprendere la funzione enumerate()

Nell'ultima parte abbiamo visto esempi di quando e come usare enumerate() a nostro vantaggio. Ora che abbiamo visto un assaggio degli aspetti pratici di enumerate(), possiamo capire di più su come la funzione lavora internamente.

Per ottenere un migliore comprensione di come funziona enumerate(), possiamo implementare la nostra versione con Python. La nostra versione di enumerate() ha due requisiti:

* accettare un iterabile ed un valore di conteggio iniziale come argomenti
* mandare indietro una tupla con l'attuale valore di conteggio e l'oggetto associato dall'iterabile

Un modo di scrivere una funzione che rispetti queste specifiche è data nella documentazione Python:

```py
>>> def my_enumerate(sequence, start=0):
...     n = start
...     for elem in sequence:
...         yield n, elem
...         n += 1
...
```

La funzione `my_enumerate()` prende due argomenti, `sequence` e `start`. Il valore di default di start è 0. All'interno della definizione di funzione, si inizializza `n` per essere il valore di start ed eseguire un ciclo for nella sequenza.

Per ogni elem nella sequenza, ci dà il controlo alla posizione chiamante ed invia all'indietro il valore attuale di `n` ed `elem`. Infine, incrementiamo `n` per essere pronti all'iterazione successiva. Possiamo vedere `my_enumerate()` in azione:

```py
>>> seasons = ["Spring", "Summer", "Fall", "Winter"]

>>> my_enumerate(seasons)
<generator object my_enumerate at 0x7f48d7a9ca50>

>>> list(my_enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]

>>> list(my_enumerate(seasons, start=1))
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
```

Per prima cosa, creiamo una lista di quattro stagioni con cui lavorare. Inoltre, mostriamo che chiamare `my_enumerate()` con `seasons` in quanto la sequenza crea un generator. Questo è perché usiamo la parola chaive `yield` per inviare i valori indietro al chiamante.

Infine, creiamo due liste da `my_enumrate()`, uno nel quale il valore `start` è lasciato di default (0) ed uno nel quale start è cambiato ad 1. In entrambi i casi, finiamo con una lista di tuple nella quale il primo elemenot di ogni tupla è il conteggio ed il secondo elemento è il valore da seasons.

Anche se possiamo implementare una funzione di equivalente per enumerate() in poche righe di codice Python, il codice vero e proprio di enumerate() è scritto in C. Questo significa che è molto veloce ed efficiente.

## Spacchettare gli argomenti con enumerate()

Quando usiamo enumeratre() in un ciclo for, diciamo a Python di usare due variabili, uno per il conteggio ed uno per il valore. Siamo abile di fare qeusto usando un concetto Python chiamato argument unpacking.


TODO DA QUI


Unpacking Arguments With enumerate()
When you use enumerate() in a for loop, you tell Python to use two variables, one for the count and one for the value itself. You’re able to do this by using a Python concept called argument unpacking.

Argument unpacking is the idea that a tuple can be split into several variables depending on the length of the sequence. For instance, you can unpack a tuple of two elements into two variables:

>>> tuple_2 = (10, "a")
>>> first_elem, second_elem = tuple_2
>>> first_elem
10
>>> second_elem
'a'
First, you create a tuple with two elements, 10 and "a". Then you unpack that tuple into first_elem and second_elem, which are each assigned one of the values from the tuple.

When you call enumerate() and pass a sequence of values, Python returns an iterator. When you ask the iterator for its next value, it yields a tuple with two elements. The first element of the tuple is the count, and the second element is the value from the sequence that you passed:

>>> values = ["a", "b"]
>>> enum_instance = enumerate(values)
>>> enum_instance
<enumerate at 0x7fe75d728180>
>>> next(enum_instance)
(0, 'a')
>>> next(enum_instance)
(1, 'b')
>>> next(enum_instance)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
In this example, you create a list called values with two elements, "a" and "b". Then you pass values to enumerate() and assign the return value to enum_instance. When you print enum_instance, you can see that it’s an instance of enumerate() with a particular memory address.

Then you use Python’s built-in next() to get the next value from enum_instance. The first value that enum_instance returns is a tuple with the count 0 and the first element from values, which is "a".

Calling next() again on enum_instance yields another tuple, this time with the count 1 and the second element from values, "b". Finally, calling next() one more time raises StopIteration since there are no more values to be returned from enum_instance.

When an iterable is used in a for loop, Python automatically calls next() at the start of every iteration until StopIteration is raised. Python assigns the value it retrieves from the iterable to the loop variable.

If an iterable returns a tuple, then you can use argument unpacking to assign the elements of the tuple to multiple variables. This is what you did earlier in this tutorial by using two loop variables.

Another time you might have seen argument unpacking with a for loop is with the built-in zip(), which allows you to iterate through two or more sequences at the same time. On each iteration, zip() returns a tuple that collects the elements from all the sequences that were passed:

>>> first = ["a", "b", "c"]
>>> second = ["d", "e", "f"]
>>> third = ["g", "h", "i"]
>>> for one, two, three in zip(first, second, third):
...     print(one, two, three)
...
a d g
b e h
c f i
By using zip(), you can iterate through first, second, and third at the same time. In the for loop, you assign the element from first to one, from second to two, and from third to three. Then you print the three values.

You can combine zip() and enumerate() by using nested argument unpacking:

>>> for count, (one, two, three) in enumerate(zip(first, second, third)):
...     print(count, one, two, three)
...
0 a d g
1 b e h
2 c f i
In the for loop in this example, you nest zip() inside enumerate(). This means that each time the for loop iterates, enumerate() yields a tuple with the first value as the count and the second value as another tuple containing the elements from the arguments to zip(). To unpack the nested structure, you need to add parentheses to capture the elements from the nested tuple of elements from zip().

There are other ways to emulate the behavior of enumerate() combined with zip(). One method uses itertools.count(), which returns consecutive integers by default, starting at zero. You can change the previous example to use itertools.count():

>>> import itertools
>>> for count, one, two, three in zip(itertools.count(), first, second, third):
...     print(count, one, two, three)
...
0 a d g
1 b e h
2 c f i
Using itertools.count() in this example allows you to use a single zip() call to generate the count as well as the loop variables without nested argument unpacking.


Remove ads
Conclusion
Python’s enumerate() lets you write Pythonic for loops when you need a count and the value from an iterable. The big advantage of enumerate() is that it returns a tuple with the counter and value, so you don’t have to increment the counter yourself. It also gives you the option to change the starting value for the counter.

In this tutorial, you learned how to:

Use Python’s enumerate() in your for loops
Apply enumerate() in a few real-world examples
Get values from enumerate() using argument unpacking
Implement your own equivalent function to enumerate()
You also saw enumerate() used in some real-world code, including within the CPython code repository. You now have the superpower of simplifying your loops and making your Python code stylish!