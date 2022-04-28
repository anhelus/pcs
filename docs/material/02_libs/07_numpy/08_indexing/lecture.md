# Accedere agli elementi di un array

Il modo più immediato per accedere al valore di un elemento in un array è usare l'operatore `[]`, specificando contestualmente l'indice dell'elemento cui si vuole accedere, proprio come avviene per le liste. 

Ad esempio, possiamo selezionare il primo elemento di un array con questa sintassi:

```py
>>> a = np.array([1,2,3,4])
>>> a[0]
1
```

Nel caso di array ad $n$ dimensioni, è necessario indicare l'indice per ciascuna delle dimensioni dell'array. Nel caso di un array bidimensionale, potremmo selezionare l'elemento alla prima riga e prima colonna con una sintassi di questo tipo:

```py
>>> b = np.array([[1,2], [3,4]])
>>> b[0][0]
1
```

## Maschere booleane

Possiamo accedere ad un sottoinsieme di elementi dell'array mediante una "maschera", che consiste in un array di dimensioni uguali a quelle di partenza, ma composto soltanto da valori booleani; ovviamente, saranno estratti solo gli elementi il cui indice nella maschera è a `True`.

Ad esempio, possiamo selezionare tutti gli elementi appartenenti alla prima colonna dell'array `b`:

```py
>>> mask = ([True, False], [True, False])
>>> b[mask]
array([1, 3])
```

Oppure possiamo scegliere tutti gli elementi che soddisfano una certa condizione logico/matematica:

```py
>>> mask = (b > 2)
>>> mask
array([[False, False],
       [ True,  True]])
>>> b[mask]
array([3, 4])
```

La precedente notazione può essere ulteriormente sintetizzata "prendendo in prestito" i principi della programmazione funzionale:

```py
>>> b[b > 2]
array([3, 4])
```

Volendo, possiamo adattare la forma precedente all'uso di espressioni arbitrariamente complesse:

```py
>>> b[b%2 == 0]
array([2, 4])
>>> b[(b > 1) & (b < 4)]
array([2, 3])
```

## Slicing degli array

Così come le liste, gli array consentono di effettuare lo slicing:

```py
>>> a = np.array([1,2,3,4])
>>> a[0:2]
array([1, 2])
```

Per gli array multidimensionali, lo slicing si intende sulla n-ma dimensione dell'array. Questo concetto è facile da comprendere se si visualizza l'array ad n-dimensioni come un array di array:

```py
>>> b
array([[1, 2],
       [3, 4]])
>>> b[0:1]              # Lo slicing avviene sulla seconda dimensione
array([[1, 2]])
```

## La funzione `nonzero()`

Possiamo usare la funzione `nonzero()` per selezionare gli elementi e gli indici di un array il cui valore non sia pari a zero. Ad esempio:

```py
>>> x = np.array([[3, 0, 0], [0, 4, 0], [5, 6, 0]])
>>> x
array([[3, 0, 0],
       [0, 4, 0],
       [5, 6, 0]])
```

Applicando la funzione `nonzero()`, avremo una tupla con gli indici per riga e colonna degli elementi diversi da zero:

```py
>>> np.nonzero(x)
(array([0, 1, 2, 2], dtype=int64), array([0, 1, 0, 1], dtype=int64))
```

Notiamo che nella tupla è presente un array per ciascuna delle dimensioni dell'array `x`. In questo caso, il primo array rappresenta gli indici relativi alla prima dimensione dei valori non nulli (in questo caso, gli indici di riga), mentre il secondo gli indici relativi alla seconda dimensione (indici di colonna). 

Volendo, è possibile ottenere una lista di tuple rappresentative delle coppie di indici rappresentative dei valori non nulli, ad esempio mediante la funzione `zip()`:

```py
>>> coords = list(zip(s[0], s[1]))
>>> coords
[(0, 0), (1, 1), (2, 0), (2, 1)]
```

## Fancy indexing

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

<!-- ## Conclusioni

In questa lezione, abbiamo visto alcuni metodi per l'accesso agli elementi di un array NumPy. Nella [prossima](./05_manipolazione.md), inizieremo a parlare della manipolazione e trasformazione degli array ai nostri scopi. -->
