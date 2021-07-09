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
