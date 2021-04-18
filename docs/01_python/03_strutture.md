# Ancora sulle strutture dati in Python

## Liste come stack e code

Python mette a disposione un'estesa serie di metodi di accesso, inserimento e gestione delle liste, disponibili a [questo indirizzo](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists).

E' interessante quindi notare come sia possibile costruire uno stack o una coda in maniera estremamente semplice; vediamo come.

### Stack

Ricordiamo che uno stack adotta una strategia di accesso del tipo LIFO; ciò significa quindi che il primo elemento ad essere servito sarà quello in cima allo stack. Potremo quindi usare il metodo `append()` per inserire l'elemento in cima alla lista, ed il metodo `pop()` per recuperarlo.

```python
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

Per le code, che ricordiamo adottare una strategia del tipo FIFO, abbiamo due possibilità. La prima è quella di usare i metodi `insert()` e `pop()` come segue:

```python
from time import time

def queue_classica(queue, pushed=1):
	t1 = time()
	queue.insert(0, pushed)
	queue.pop(0)
	t2 = time()
	print(t2-t1)
```

Notiamo che stiamo usando `insert(0, pushed)` per inserire l'elemento `pushed` in cima alla coda, ed il metodo `pop(0)` per estrarre detto elemento.

Lo svantaggio principale di questo approccio sta nel fatto che le operazioni di `insert()` e di `pop()` possono essere rallentate dalla necessità di riallocare lo spazio occupato dagli elementi della lista.

Un altro modo è quello di usare una `deque`, definita nella libreria `collections`, ovvero una struttura Python progettata specificamente per "velocizzare" le operazioni di `append()` e `pop()` *da entrambi i capi* della struttura dati:

```python
from collections import deque

def queue_con_deque(queue, pushed=1):
	t1 = time()
	queue.append(pushed)
	queue.popleft()
	t2 = time()
	print(t2-t1)
```

Proviamo a chiamare le due funzioni (abbiamo già integrato nel corpo ciò che serve a cronometrarle):

```python
queue = list(range(1000000000))
queue_d = deque(queue)

queue_classica(queue)
queue_con_deque(queue_d)

>>> Tempo necessario con queue classica: 0.016004323959350586
>>> Tempo necessario con deque: 0.0
```

Notiamo quindi che l'uso di una lista classica richiede un tempo maggiore rispetto all'uso di una deque.

!!!note "Nota"
	E' importante notare che stiamo considerando soltanto le operazioni su coda. Qualora considerassimo anche il cast di tipo, potremmo avere risultati differenti; è per questo consigliabile usare una struttura di tipo deque soltanto qualora ci siano *numerose* operazioni di `push()` e `pop()` dalla coda.

## List comprehension

Un modo "rapido" ed efficace per la creazione di una lista è dato dalla tecnica chiamata *list comprehension*, permettendo di sostituire (quasi completamente) l'uso del classico ciclo `for`.

La list comprehension "base" assume questa forma:

```python
lista_output = [f(elemento) for elemento in lista_input]
```

In pratica, la lista di uscita (`lista_output`) sarà ottenuta applicando ad ogni `elemento` della lista di ingresso (`lista_input`) la funzione `f()`.

La sintassi può essere estesa incorporando un'istruzione condizionale. Ad esempio, l'istruzione nella forma:

```python
lista_output_if = [f(elemento) for elemento in lista_input if condizione]
```

farà in modo che `f()` sia chiamata esclusivamente sugli elementi che soddisfano `condizione`. Invece:

```python
lista_output_if_else = [f(elemento) if condizione else g(elemento) for elemento in lista_input]
```

invocherà `f()` sugli elementi che soddisfano `condizione`, e la funzione `g()` su tutti gli elementi che non la soddisfano.

!!!note "Nota"
	Per essere precisi, più che `lista_input`, sarebbe opportuno parlare di *sequenza*, o *iterabile*, di input.

Facciamo qualche esempio.

### Esempio 1: estrazione dei nomi

Supponiamo di voler selezionare tutti i nomi che iniziano con la lettera "B". Vediamo come farlo con un classico ciclo `for`:

```python
# Estrazione dei nomi che iniziano con "B" mediante ciclo for
lista_nomi = ["Jax Teller", "Walter White", "Billy Butcher", "Luke Skywalker", "Bobby Singer", "Johnny Lawrence"]

output = []
for nome in lista_nomi:
	if nomi[0] == "B":
		output.append(nome)
print(output)
['Billy Butcher', 'Bobby Singer']
```

Vediamo ora una notazione più compatta usando una list comprehension:

```python
# Estrazione dei nomi che iniziano con "B" mediante list comprehension
output = [nome for nome in lista_nomi if nome[0] == "B"]
print(output)
['Billy Butcher', 'Bobby Singer']
```

### Esempio 2: calcolo dei quadrati

Possiamo usare una list comprehension anche per calcolare una lista di numeri passando una funzione precedentemente definita. Ad esempio, se volessimo calcolare una successione di quadrati, potremmo usare un ciclo `for`:

```python
# Estrazione dei quadrati mediante ciclo for
def quadrato(numero):
	return numero ** 2

output = []
for i in range(10):
	output.append(quadrato(i))
print(output)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

```python
# Estrazione dei quadrati mediante list comprehension
output = [quadrato(i) for i in range(10)]
print(output)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### Esempio 3: lista dei numeri pari e dispari

Vediamo infine come usare la list comprehension per caratterizzare tutti i numeri pari e dispari fino a 10. Partiamo, al solito, con il risultato ottenuto usando un ciclo `for`:

```python
# Lista dei pari e dispari mediante ciclo for
output = []
for i in range(1, 10):
	if i % 2 == 0:
		output.append("{} è pari".format(i))
	else:
		output.append("{} è dispari".format(i))
print(output)
['1 è dispari', '2 è pari', '3 è dispari', '4 è pari', '5 è dispari', '6 è pari', '7 è dispari', '8 è pari', '9 è dispari']
```

```python
# Lista dei pari e dispari mediante list comprehension
output = ["{} è pari".format(i) if i % 2 == 0 else "{} è dispari".format(i) for i in range(1, 10)]
print(output)
['1 è dispari', '2 è pari', '3 è dispari', '4 è pari', '5 è dispari', '6 è pari', '7 è dispari', '8 è pari', '9 è dispari']
```

#### Assignment expression

Le list comprehension sono pensate per favorire approcci puramente *iterativi*. E' pertanto abbastanza complesso (seppur non impossibile) implementare delle forme di ricorsione. Per ovviare a questo, è possibile usare una nuova funzionalità, introdotta a paritre da Python 3.8, e chiamata *assignment expression*.

Formalmente, l'assignment expression permette di *assegnare* e *restituire* un valore all'interno di una singola istruzione, mediante il cosiddetto *walrus operator*:

```python
>>> print(enjoy := True)
True
```

Usando in maniera opportuna questo operatore, possiamo usare una sorta di "approccio ricorsivo" alla list comprehension.

Partiamo definendo i valori di $F_0$ ed $F_1$ per la sequenza di Fibonacci:

```python
>>> fib = [0, 1]
```

Vediamo adesso cosa accade se proviamo ad usare una assignment expression, mediante la quale restituiamo una lista che ha come *primo valore* quello al *secondo* indice della precedente, ed al *secondo* la somma espressa da Fibonacci:

```python
>>> (fib := [fib[1], fib[0] + fib[1]])
>>> # Fibonacci ha cambiato valore!
>>> fib
[1, 1]
```

A questo punto, possiamo selezionare soltanto il secondo valore della lista ottenuta mediante assignment expression. Per farlo, usiamo la condizione booleana `and`:

```python
>>> (fib := [fib[1], fib[0] + fib[1]]) and fib[1]
1
```

Possiamo quindi combinare tutto usando una list comprehension e *concatenando* i risultati che abbiamo ottenuto:

```python
>>> fib = [0, 1]
>>> fib += [(fib := [fib[1], fib[0] + fib[1]]) and fib[1] for i in range(10)]
>>> fib
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```

!!!note "Nota"
	Esistono ovviamente altri approcci, alcuni dei quali sfruttano un modulo estremamente utile chiamato `itertools`.

## Tuple

Le *tuple* sono il terzo tipo di sequenze "standard" disponibile in Python, e consistono di una serie di valori separati da una lettera.
Ad esempio:

```python
>>> tupla = ('hello', 'world', 12)
>>> tupla
('hello', 'world', 12)
```

Così come per le liste, uno dei valori della tupla può essere a sua volta una tupla:

```python
>>> tupla = ('hello', 'world', (1, 2))
>>> tupla
('hello', 'world', (1, 2))
```

E' però importante sottolineare che, a differenza delle liste (e come le stringhe), le tuple sono *immutabili*.

!!!note "Nota"
	Il fatto che le tuple siano immutabili non implica che non possano contenere al loro interno oggetti mutabili. Ad esempio:
	> ```python
 	  >>> tupla = ('hello', 'world', [1, 2, 3])
	  >>> tupla[2]
	  [1, 2, 3]
	  >>> tupla[2] = [1, 2, 3, 4] 				# errore!
	  Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	  TypeError: 'tuple' object does not support item assignment
	  >>> tupla[2][0] = 2						# ok
	  >>> tupla
	  ('hello', 'world', [2, 2, 3])
	  ```

!!!tip "Tuple e liste"
	E' facile osservare come tuple e liste siano tra loro molto simili a livello sintattico, e differiscano principalmente per il fatto che le prime sono immutabili, mentre le seconde no. Idealmente, è bene usare le tuple per elementi di tipo eterogeneo, che devono essere esclusivamente acceduti, mentre le liste vanno usate per elementi omogenei, che devono essere modificati all'occorrenza.

## Dizionari

L'ultimo tipo di dati che vale la pena affrontare in Python sono i *dizionari*, che abbiamo già visto in C e C++ con il nome di [array associativi](../02_dispense/programmazione/02_linguaggio_cpp/09_container/#associative-container).

I dizionari sono quindi indicizzati non mediante un classico indice numerico, ma mediante delle *chiavi*, che devono necessariamente essere immutabili (ovvero stringhe, numeri e tuple, che però al loro interno non possono contenere elementi mutabili come liste). Ad ogni chiave, come negli array associativi, corrisponde un determinato *valore*, che è arbitrario e può essere di qualsiasi tipo. Di conseguenza, un concetto comunemente associato ai dizionari è quello di *coppie chiave - valore*.

Vediamo come creare un dizionario:

```python
>>> dizionario = {}             			# creo un dizionario vuoto
>>> dizionario
{}
```

Possiamo quindi inserire una serie di chiavi, associandovi un determinato valore:

```python
>>> dizionario['k'] = 'v'			# aggiungo la chiave "k" a cui è associato il valore "v"
>>> dizionario
{'k': 'v'}
>>> dizionario[1] = 'n'				# aggiungo la chiave 1 a cui è associato il valore "n"
>>> dizionario
{'k': 'v', 1: 'n'}
```

Per accedere al valore associato ad una chiave:

```python
>>> dizionario[1]
'n'
```

### Accedere a chiavi e valori

E' possibile avere la lista delle chiavi di un dizionario mediante il metodo `keys()`, che restituisce un oggetto di tipo `dict_keys`, convertibile in lista:

```python
>>> chiavi = dizionario.keys()
>>> chiavi
dict_keys(['k', 1])					# non è una lista!
>>> list(chiavi)
['k', 1]							# è una lista!
```

In modo analogo, si può accedere a tutti i valori presenti nel dizionario mediante il metodo `values()`, che restituirà un oggetto di tipo `dict_values`, da convertire anch'esso in lista:

```python
>>> valori = dizionario.values()
>>> valori
dict_values(['k', 'n'])				# non è una lista!
>>> list(valori)
['k', 'n']							# è una lista!
```

Possiamo accedere anche a tutte le coppie chiave - valore mediante il metodo `items()`, che ci restituisce un oggetto di tipo `dict_items`, il quale può essere convertito in una lista di tuple:

```python
>>> coppie = dizionario.items()
>>> coppie
dict_items([('k', 'v'), (1, 'n')])	# non è una lista!
>>> list(coppie)
[('k', 'v'), (1, 'n')]				# lista di tuple!
>>>
```

### Creare un dizionario non vuoto

Abbiamo diversi modi per creare un dizionario non vuoto. Il primo, più semplice, è quello di dichiarare nell'operatore `{}` le coppie chiave - valore iniziali:

```python
>>> dizionario = { 'k1': 1, 'k2': 2 }
>>> dizionario
{'k1': 1, 'k2': 2}
```

#### Uso della funzione `zip`

Possiamo poi usare la funzione `zip` per creare un dizionario a partire da due liste:

```python
>>> chiavi = ['k1', 'k2']
>>> valori = [1, 2]
>>> dizionario = dict(zip(chiavi, valori))
>>> dizionario
{'k1': 1, 'k2': 2}
```

#### Dict comprehension

Possiamo ottenere un dizionario a partire da un altro oggetto iterabile (sia esso una sequenza o un altro dizionario) usando la *dict comprehension*, che ha una forma del tipo:

```python
output = { chiave: valore for valore in iterabile }
```

Possiamo ad esempio creare un dizionario contenente come chiave i numeri da 1 a 9, e come valori corrispondenti i quadrati degli stessi:

```python
>>> quadrati = {str(i): i ** 2 for i in range(1, 10)}
>>> quadrati
{'1': 1, '2': 4, '3': 9, '4': 16, '5': 25, '6': 36, '7': 49, '8': 64, '9': 81}
```

Oppure, possiamo creare un dizionario a partire da un altro dizionario, usando le stesse regole condizionali viste con la list comprehension:

```python
>>> dizionario = {'Jax Teller': 27, 'Walter White': 52, 'Billy Butcher': 41, 'Luke Skywalker': 79, 'Bobby Singer': 68, 'Johnny Lawrence': 49}
>>> vecchio_o_giovane = { k: 'vecchio' if v > 50 else 'giovane' for (k, v) in dizionario.items() }
>>> vecchio_o_giovane
{'Jax Teller': 'giovane', 'Walter White': 'vecchio', 'Billy Butcher': 'giovane', 'Luke Skywalker': 'vecchio', 'Bobby Singer': 'vecchio', 'Johnny Lawrence': 'giovane'}
```

!!!note "Nota"
	Per iterare sul dizionario originale, usiamo il metodo `items()` che, come visto in precedenza, ci restituisce un oggetto di tipo `dict_items` il quale è, per l'appunto, iterabile.
