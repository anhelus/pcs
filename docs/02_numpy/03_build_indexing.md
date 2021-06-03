# Costruzione ed indicizzazione di un array

Nella precedente lezione, abbiamo visto come sia possibile creare un nuovo array mediante il ,etpappostio i precedenti 

### Costruire un array

I nuovi array possono essere creati mediante un apposito costruttore.

ndarray(shape, **kwargs)

E' però più semplice farlo tramite una delle funzioni messe a disposizione da NumPy. Ad esempio, possiamo farlo usando la funzione np.array(), che ci permette di crearlo usando una semplice lista e, opzionalmente, impostando il tipo di dato:

```py
>>> a = np.array([1, 2, 3])
```

Esistono ovviamente numerose altre funzioni per la creazione di un array. Ad esempio, se volessimo creare una matrice con valori unitari, potremmo usare np.ones():

```py
>>> u = np.ones(2)
array([1., 1.])
```

mentre per una matrice con tutti valori pari a zero usiamo np.zeros():

```py
>>> u = np.zeros(2)
array([0., 0.])
```

#### Creazione di un array vuoto

Possiamo anche creare un array vuoto. Questo può essere particolarmente utile quando vogliamo preallocare un array di una certa dimensione.

```py
>>> np.empty(2)
array([42., 42.])
```

!!!note "Nota"
    In realtà, possiamo osservare un fenomeno interessante: infatti, l'array vuoto sarà, in realtà, popolato da valori. Tuttavia, questi valori sono completamente casuali, e dipendenti dallo stato della memoria del sistema in un determinato istante.

https://numpy.org/doc/stable/user/absolute_beginners.html

https://numpy.org/doc/stable/user/absolute_beginners.html#indexing-and-slicing

è possibile fare l'indicizzazione e lo slice degli array NumPy nello stesso modo con cui lo si fa con le liste Python:

```py
>>> data = np.array([1, 2, 3])
>>> data[1]
2
>>> data[0:2]
array([1, 2])
>>> data[1:]
array([2, 3])
>>> data[-2:]
array([2, 3])
```

Possiamo voler prendere una sezione del nostro array, o specificarne gli elementi da usare in ulteriori analisi od operazioni. Per farlo, è necessario selezionare un sottoinsieme, fare lo slicing e/o specificare gli indici dei nostri array.

Se vogliamo selezionare dei valori dagli array che soddisfino certe condizioni, è facile farlo mediante Numpy.

Per esempio, se si inizia con questo array:

```py
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
```

Si può facilmente stampare a schermo tutti i valori nell'array che sono inferiori a 5:

```py
>>> print(a[a < 5>])
[1 2 3 4]
```

Possiamo anche scegliere, ad esempio, i numeri che sono maggiori o uguali a 5, ed usare questa condizione per indicizzare un array:

```py
>>> five_up = (a >= 5)
>>> print(a[five_up])
[5 6 7 8 9 10 11 12]
```

Posisamo scegliere gli elementi divisibili per 2:

```py
>>> divisible_by_2 = a[a%2 = 0]
>>> print(divisible_by_2)
[2 4 6 8 10 12]
```

O possiamo scegliere gli elmentic he soddisfano due condizioni usando gli oepratori logici booleani

```py
>>> c = a[(a > 2) & (a < 11)]
>>> print(c)
[ 3  4  5  6  7  8  9 10]
```

Possiamo anche suare le operazioni logiche per restituire valori booleani che specificano se i valori in un array rispettano una certa condizione. Questo può essere utile con gli array che contengono nomi o altri valori categorici:

```py
>>> five_up = (a > 5) | (a == 5)
>>> print(five_up)
[[False False False False]
 [ True  True  True  True]
 [ True  True  True True]]
```

Possiamo anche usare `np.nonzero()` per scegliere gli elementi o gli indici da un array.

Iniziamo con questo array:

```py
>>> a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
```

Possiamo usare `np.nonzero()` per selezionare gli indici degli elementi che sono, per esempio, inferiori a 5.

```py
>>> b = np.nonzero(a < 5)
>>> print(b)
(array([0, 0, 0, 0]), array([0, 1, 2, 3]))
```

In questo esempio, una tupla di array viene restituita: una per ogni dimensione. Il primo array rappresenta gli indici di riga dove si trovano qeusti valori, mentre il secondo rappresenta gli indici di colonna dove si trovano questi valori.

Se vogliamo generare una lista di coordinate dove esiste l'elemento, possiamo zippare gli array, iterare sulla lista di coordinate, e stamparli a schermo. Ad esempio:

```py
>>> list_of_coordinates= list(zip(b[0], b[1]))

>>> for coord in list_of_coordinates:
...     print(coord)
(0, 0)
(0, 1)
(0, 2)
(0, 3)
```

Possiamo anche usare np.nonzero() per stampare gli elementi in un array che siano inferiori a 5 con:

```py
>>> print(a[b])
[1 2 3 4]
```

Se l'elemento che stiamo cercando non esiste nell'array, l'array di indici restituito sarà vuoto. Ad esempio:

```py
>>> not_there = np.nonzero(a == 42)
>>> print(not_there)
(array([], dtype=int64), array([], dtype=int64))
```



### Fancy indexing

Una tecnica estremamente interessante è quella del *fancy indexing*. Concettualmente, questa indicizzazione prevede che venga passato un array di indici, in modo da accedere a più elementi di un array contemporaneamente.

Facciamo un esempio.

```py
>>> rand = np.random.RandomState(42)
>>> x = rand.randint(100, size=10)
>>> indexes = np.array([[1,4],[5,2]])
>>> x
array([51, 92, 14, 71, 60, 20, 82, 86, 74, 74])
>>> x[indexes]
array([[92, 60],
       [20, 14]])
```

Nel codice precedente, stiamo:

1. usando la funzione `randint` per generare un array di numeri interi casuali compresi tra 0 e 100;
2. generando un array bidimensionale `indexes`;
3. restituendo, mediante il fancy indexing, un array con le dimensioni di `indexes` e gli elementi di `x` presi nelle posizioni indicate da `indexes`.

La potenza del fancy indexing sta proprio in questo: non solo siamo in grado di accedere facilmente a più elementi di un array mediante un'unica operazione, ma possiamo anche ridisporre questi elementi come più ci aggrada!

!!!tip "Combinare i metodi"
    Alla bisogna, è possibile combinare i diversi metodi di indicizzazione tra loro.
