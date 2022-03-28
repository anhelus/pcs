# Alcune applicazioni delle liste

## Liste, pile e code

Python ci offre una grande varietà di metodi per gestire le liste; troviamo un elenco esaustivo a [questo indirizzo](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists). Grazie a questi metodi, è possibile costruire una pila o una coda in modo molto più semplice rispetto ad altri linguaggi.

### Pila

Una *pila* (in inglese *stack*) adotta una strategia di accesso ai dati di tipo *Last-In, First-Out* (*LIFO*). Questo significa che il primo elemento ad uscire (ovvero ad essere analizzato) è quello in cima alla pila, ovvero l'ultimo ad esservi entrato.

!!!tip "Esempio di pila"
	Un tipico esempio di pila è quella dei piatti da lavare. Quasi sicuramente, il piatto in cima alla pila sarà l'ultimo che avremo preso dal tavolo; tuttavia, sarà anche il primo ad essere lavato.

Per implementare una pila a partire da una lista possiamo usare due metodi:

* il metodo `append()` ci permette di inserire un nuovo elemento in cima alla pila (ovvero alla posizione $n-1$-ma, con una lista ad $n$ componenti);
* il metodo `pop(pos)` ci permette di estrarre l'elemento in posizione `pos`. Di default, non specificando alcun valore di `pos`, estrarremo l'elemento in posizione $n-1$-ma.

```py
>>> s = [1,2,3]
>>> s.append(4)
>>> s
[1, 2, 3, 4]
>>> e = s.pop()
>>> e
4
>>> s
[1, 2, 3]
```

### Coda

Una *coda* (in inglese *queue*) adotta una strategia di accesso ai dati di tipo *First-In, First-Out* (*FIFO*). In questo caso, il primo elemento ad uscire è presente da più tempo in coda.

!!!tip "Esempio di coda"
	Un tipico esempio di coda è quella che tutti quanti, prima o poi, abbiamo fatto alle Poste: il primo ad arrivare è il primo ad essere servito, poi il secondo, il terzo, e via così, sempre che non ci si trovi in Italia.

Per implementare una coda a partire da una lsita, possiamo usare il metodo `pop(pos)` con `pos = 0`, che ci permetterà quindi di estrarre il primo elemento della coda, ed il metodo `insert(pos, el)` ci permette di inserire alla posizione `pos` l'elemento `el`.

```py
>>> q = [1, 2, 3]
>>> q.insert(0, 4)
>>> q
[4, 1, 2, 3]
>>> e = q.pop(0)
>>> e
4
>>> q
[1, 2, 3]
```

Questo approccio, per quanto semplice, ha uno svantaggio: infatti, i metodi `insert()` e `pop()` sono computazionalmente onerosi, in quanto fanno in modo di riallocare lo spazio occupato dagli elementi della lista.

In alternativa, possiamo usare una struttura contenuta nella libreria `collections` e chiamata `deque`. Il vantaggio sta nel fatto che la `deque` è progettata specificamente per eseguire in maniera efficiente i metodi `append()` e `pop()` *da entrambi i capi* della struttura dati:

```py
>>> from collections import deque
>>> q = deque([1, 2, 3])
>>> q.appendleft(4)
>>> q
deque([4, 1, 2, 3])
>>> e = q.popleft()
>>> e
4
>>> q
deque([1, 2, 3])
```

#### Esercizio: tempo di confronti!

Proviamo a comparare i due approcci che abbiamo visto per la costruzione di una coda. Per farlo, usiamo la libreria `time`:

```py
from time import time
from collections import deque

def queue(queue, pushed=1):
	t1 = time()
	queue.insert(0, 4)
	queue.pop()
	t2 = time()
	print(t2 - t1)

def queue_con_deque(queue, pushed=1):
	t1 = time()
	queue.appendleft(pushed)
	queue.popleft()
	t2 = time()
	print(t2-t1)
```

Proviamo a chiamare le due funzioni:

```py
queue = list(range(10000000))
queue_d = deque(queue)

queue_classica(queue)
queue_con_deque(queue_d)
```

Avremo il seguente output:

```sh
Tempo necessario con lista: 0.08756685256958008
Tempo necessario con deque: 0.0
```

## Conclusioni

In questa lezione, abbiamo visto due applicazioni del concetto di lista. Nella prossima, introdurremo la tecnica della *list comprehension*.


# List comprehension

## Forma base

Una delle tecniche più usate per effettuare delle operazioni sugli elementi di una lista è usare la tecnica della *list comprehension*, che permette di sostituire *quasi* completamente i classici cicli.

Nella forma base, una list comprehension ha una sintassi di questo tipo:

```py
lista_output = [f(elemento) for elemento in lista_input]
```

In altre parole, otterremo in output una lista (`lista_output`) applicando ad ogni `elemento` della lista originaria (`lista_input`) la funzione `f()`.

!!!note "Nota"
	Per essere precisi, più che di lista, sarebbe opportuno parlare di iterabile di input.

## Forma estesa con if-else

La list comprehension può anche includere delle istruzioni condizionali. Un primo esempio è la seguente forma:

```py
lista_output_if = [f(elemento) for elemento in lista_input if condizione]
```

In questo caso, la funzione `f()` sarà chiamata esclusivamente sugli elementi che soddisfano la `condizione` indicata. Invece, se usassimo questa forma:

```py
lista_output_if_else = [f(elemento) if condizione else g(elemento) for elemento in lista_input]
```

la funzione `f()` sarebbe invocata su tutti gli elementi che soddisfano la `condizione`, mentre la funzione `g()` su tutti quelli che non la soddisfano.

Vediamo adesso qualche esempio di applicazione.

## Esempio 1: selezionare i nomi da una lista

Supponiamo di voler selezionare tutti i nomi che iniziano con la lettera "B". Se usassimo un classico ciclo `for`, potremmo scrivere:

```py
>>> lista_nomi = ["Jax Teller", "Walter White", "Billy Butcher", "Luke Skywalker", "Bobby Singer", "Johnny Lawrence"]
>>> output = []
>>> for nome in lista_nomi:
		if nomi[0] == "B":
			output.append(nome)
>>>	print(output)
['Billy Butcher', 'Bobby Singer']
```

Decidendo di usare invece una list comprehension:

```py
>>> output = [nome for nome in lista_nomi if nome[0] == "B"]
>>> print(output)
['Billy Butcher', 'Bobby Singer']
```

## Esempio 2: calcolo dei quadrati

Vediamo come usare una list comprehension per ottenere una nuova lista applicando a tutti gli elementi di una sequenza una certa funzione. Ad esempio, potremmo voler ottenere la lista dei quadrati di una certa sequenza:

```py
>>> def quadrato(numero):
		return numero ** 2
>>> output = []
>>> for i in range(10):
		output.append(quadrato(i))
>>> output
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Utilizzando la list comprehension:

```py
>>> output = [quadrato(i) for i in range(10)]
>>> output
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

## Esempio 3: lista dei numeri pari e dispari

Facciamo un ultimo esempio usando una list comprehension per "contrassegnare" tutti i numeri da 0 a 10 in base al fatto che siano pari o dispari. Al solito, vediamo come farlo usando un ciclo:

```py
>>> output = []
>>> for i in range(1, 10):
		if i % 2 == 0:
			output.append("{} è pari".format(i))
		else:
			output.append("{} è dispari".format(i))
>>> output
['1 è dispari', '2 è pari', '3 è dispari', '4 è pari', '5 è dispari', '6 è pari', '7 è dispari', '8 è pari', '9 è dispari']
```

Usando una list comprehension, invece:

```py
>>> output = ["{} è pari".format(i) if i % 2 == 0 else "{} è dispari".format(i) for i in range(1, 10)]
>>> output
['1 è dispari', '2 è pari', '3 è dispari', '4 è pari', '5 è dispari', '6 è pari', '7 è dispari', '8 è pari', '9 è dispari']
```

## In definitiva...

Le list comprehension sono utili e versatili, e permettono, in molti casi, di sostituire i classici cicli con una sintassi più snella. Tuttavia, bisogna fare attenzione a non abusare di questo strumento: infatti, facendolo si rischia di complicare inutilmente il nostro programma, rendendolo poco leggibile e manutenibile.

Come regola generale, quindi, ricordiamo il principio del rasoio di Occam: anche se è facile innamorarsi delle list comprehension, è bene ricordarsi che anche i cicli sono *leciti e funzionali*, per cui non è sempre necessario trovare a tutti i costi una soluzione usando una list comprehension.

## Post scriptum: assignment expressions

Come apparso dalla trattazione, le list comprehension sono state pensate per approcci puramente iterativi. Di conseguenza, risulta complesso implementare forme di ricorsione. Per ovviare a questo inconveniente, Python introduce, a partire dalla versione 3.8, le *assignment expression*.

Da un punto di vista "formale", un'assignment expression permette di *assegnare* e *restituire* un valore all'interno di un'unica istruzione mediante il cosiddetto *walrus operator*:

```py
>>> print(enjoy := True)
True
```

Vediamo come utilizzare questo concetto per combinare ricorsione e list comprehension. Definiamo i valori di $F_0$ ed $F_1$ per la [sequenza di Fibonacci](https://it.wikipedia.org/wiki/Successione_di_Fibonacci):

```py
>>> fib = [0, 1]
```

Vediamo cosa succede se proviamo ad usare una assignment expression in modo da restituire una lista che abbia come primo elemento il secondo della precedente (ovvero `1`), e come secondo la somma di tutti gli elementi della lista (ovvero `0 + 1`):

```py
>>> (fib := [fib[1], fib[0] + fib[1]])
>>> fib
[1, 1]
```

Notiamo che l'operazione ha modificato il valore della lista `fib`! A noi, però, interessa soltanto la somma degli elementi precedenti della lista (e quindi il secondo valore ottenuto). Per isolarlo, possiamo adoperare l'operatore booleano `and`:

```py
>>> (fib := [fib[1], fib[0] + fib[1]]) and fib[1]
1
```

Proviamo a combinare i due passaggi precedenti, ed usare una list comprehension per concatenare i risultati ottenuti per i numeri che vanno fino ad $F_9$:

```py
>>> fib = [0, 1]
>>> fib += [(fib := [fib[1], fib[0] + fib[1]]) and fib[1] for i in range(10)]
>>> fib
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```

# Le altre strutture per le sequenze

Quando abbiamo parlato delle liste abbiamo accennato al fatto che Python offre altre tre strutture built-in per memorizzare sequenze di dati. Scopriamole insieme.

## Tuple

Le *tuple* permettono di rappresentano un insieme di valori eterogenei separadoli da una virgola. Ad esempio:

```py
>>> tupla = ('hello', 'world', 12)
>>> tupla
('hello', 'world', 12)
```

Un po' come avviene per le liste, uno dei valori della tupla può a sua volta essere un'altra tupla. Ad esempio:

```py
>>> tupla = ('hello', 'world', (1, 2))
>>> tupla
('hello', 'world', (1, 2))
```

A differenza di una lista, però, le *tuple sono immutabili*. Ciò non implica però che non possano contenere al loro interno oggetti mutabili. Guardiamo il seguente esempio:

```py
>>> tupla = ('hello', 'world', [1, 2, 3])
>>> tupla[2]
[1, 2, 3]
```

La tupla avrà al suo interno due stringhe (immutabili) ed una lista (mutabile). Proviamo a modificare la lista:

```py
>>> tupla[2] = [2, 2, 3]
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

Come prevedibile, abbiamo avuto un errore di assegnazione legato all'immutabilità della tupla. Proviamo adesso però a modificare *direttamente la lista*:

```py
>>> tupla[2][0] = 2
>>> tupla
('hello', 'world', [2, 2, 3])
```

L'operazione è evidentemente ammissibile, ed il risultato è stato proprio quello atteso.

!!!tip "Tuple e liste"
	Ad un attento osservatore non sfuggirà come tuple e liste siano simili dal punto di vista sintattico, e differiscano in buona sostanza per la mutabilità. Da qui discende che le tuple sono estremamente efficaci nel caso si debba esclusivamente accedere agli elementi contenuti, mentre le liste devono essere usate quando è anche necessario modificare all'occorrenza detti elementi.

## Set

Anche i *set* sono molto simili alle liste dal punto di vista sintattico, ma offrono una significativa differenza: infatti, in un set *non possono esserci elementi ripetuti*.

!!!note "Nota"
	Notiamo un'evidente analogia con il concetto matematico di insieme.

La sintassi da usare per creare un set è la seguente.

```py
>>> insieme = { 1, "stringa", 2 }
>>> insieme
{1, 2, 'stringa'}
```

Il set ammette al suo interno dati eterogenei, tuttavia non può contenere al suo interno delle liste o dei dizionari. Questo è legato al fatto che i set (così come gli stessi dizionari) sono delle [hash table](https://it.wikipedia.org/wiki/Hash_table), e quindi sfruttano il concetto di *hash* per rappresentare i dati contenuti in maniera compatta ed efficiente. Il fatto che le liste ed i dizionari non possano essere rappresentati in questo modo li esclude in automatico dall'includibilità all'interno di un set.

Un'altra considerazione da fare è che il set *non è ordinato*: ciò rende impossibile accedere ad (e *modificare*) un elemento del set mediante il suo indice, come succedeva per liste e tuple.

!!!tip "Suggerimento"
	I set possono essere usati per isolare gli elementi univoci presenti in una lista. Per farlo, basta convertire la lista in set:
	> ```py
	  >>> l = [1, 2, 2, 3]
  	  >>> l
	  [1, 2, 2, 3]
	  >>> s = set(l)
	  >>> s
	  {1, 2, 3}
	  ```

## Dizionari

Il quarto ed ultimo tipo di contenitore per sequenze di dati è il *dizionario*, presente anche in altri linguaggi di programmazione con il nome di *array associativo* o *hash map*.

L'elemento base di un dizionario è la *coppia chiave - valore*, nella quale un certo valore (di qualsiasi tipo) è associato ad una determinata chiave (di tipo immutabile).

I dizionari hanno diverse caratteristiche comuni ai set, dall'inutilizzabilità delle liste come chiavi al fatto di non permettere chiavi ripetute. Inoltre, le coppie chiave - valore sono accedute, per l'appunto, per chiave, e non in base all'ordine delle coppie.

!!!note "Nota"
	Una differenza tra set e dizionari sta nel fatto che questi ultimi sono *ordinati* a partire da Python 3.7.

Per creare un dizionario, possiamo usare una sintassi simile a quella usata per i set. Ad esempio, per creare un dizionario vuoto:

```py
>>> dizionario = {}
>>> dizionario
{}
```

Possiamo quindi inserire delle coppie chiave - valore in questo modo:

```py
>>> dizionario['k'] = 'v'
>>> dizionario
{'k': 'v'}
>>> dizionario[1] = 'n'
>>> dizionario
{'k': 'v', 1: 'n'}
```

Per accedere al valore associato ad una determinata chiave:

```py
>>> dizionario[1]
'n'
```

### Chiavi e valori

E' possibile recuperare la lista di tutte le chiavi presenti in un dizionario usando il metodo `keys()`, che restituisce un oggetto di tipo `dict_keys`, a sua volta convertibile in lista:

```py
>>> chiavi = dizionario.keys()
>>> chiavi
dict_keys(['k', 1])					# non è una lista!
>>> list(chiavi)
['k', 1]							# è una lista!
```

In modo analogo, si può accedere a tutti i valori presenti nel dizionario mediante il metodo `values()`, che restituirà un oggetto di tipo `dict_values`, da convertire anch'esso in lista:

```py
>>> valori = dizionario.values()
>>> valori
dict_values(['k', 'n'])				# non è una lista!
>>> list(valori)
['k', 'n']							# è una lista!
```

Possiamo accedere anche a tutte le coppie chiave - valore mediante il metodo `items()`, che ci restituisce un oggetto di tipo `dict_items`, il quale può essere convertito in una lista di tuple:

```py
>>> coppie = dizionario.items()
>>> coppie
dict_items([('k', 'v'), (1, 'n')])	# non è una lista!
>>> list(coppie)
[('k', 'v'), (1, 'n')]				# lista di tuple!
>>>
```

### Creazione di un dizionario (non vuoto)

Abbiamo diversi modi per creare un dizionario non vuoto.

#### Uso dell'operatore `{}`

Il più semplice, che è quello che useremo più spesso, è quello di dichiarare nell'operatore `{}` le coppie chiave - valore iniziali:

```py
>>> dizionario = { 'k1': 1, 'k2': 2 }
>>> dizionario
{'k1': 1, 'k2': 2}
```

#### Uso del costruttore `dict()`

Un altro modo è usare il metodo costruttore `dict()`:

```py
>>> dizionario = dict(k1=1, k2=2)
>>> dizionario
{'k1': 1, 'k2': 2}
```

#### Uso della funzione `zip`

Possiamo poi usare la funzione `zip` per creare un dizionario a partire da due liste:

```py
>>> chiavi = ['k1', 'k2']
>>> valori = [1, 2]
>>> dizionario = dict(zip(chiavi, valori))
>>> dizionario
{'k1': 1, 'k2': 2}
```

#### Dict comprehension

Un modo per ottenere un dizionario a partire da un altro oggetto iterabile è la *dict comprehension*, che ha una forma del tipo:

```py
output = { chiave: valore for valore in iterabile }
```

Possiamo ad esempio creare un dizionario contenente come chiave i numeri da 1 a 9, e come valori corrispondenti i quadrati degli stessi:

```py
>>> quadrati = {str(i): i ** 2 for i in range(1, 10)}
>>> quadrati
{'1': 1, '2': 4, '3': 9, '4': 16, '5': 25, '6': 36, '7': 49, '8': 64, '9': 81}
```

Oppure, possiamo creare un dizionario a partire da un altro dizionario, usando le stesse regole condizionali viste con la list comprehension:

```py
>>> dizionario = {'Jax Teller': 27, 'Walter White': 52, 'Billy Butcher': 41, 'Luke Skywalker': 79, 'Bobby Singer': 68, 'Johnny Lawrence': 49}
>>> vecchio_o_giovane = { k: 'vecchio' if v > 50 else 'giovane' for (k, v) in dizionario.items() }
>>> vecchio_o_giovane
{'Jax Teller': 'giovane', 'Walter White': 'vecchio', 'Billy Butcher': 'giovane', 'Luke Skywalker': 'vecchio', 'Bobby Singer': 'vecchio', 'Johnny Lawrence': 'giovane'}
```

!!!note "Nota"
	Per iterare sul dizionario originale, usiamo il metodo `items()` che, come visto in precedenza, ci restituisce un oggetto di tipo `dict_items` il quale è, per l'appunto, iterabile.
