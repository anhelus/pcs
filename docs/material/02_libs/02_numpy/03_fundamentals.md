# 2.2.3 - Operazioni fondamentali sugli array

Dopo averli introdotti nella [lezione precedente](./02_array.md), proseguiamo nella nostra trattazione sugli array andando a vedere tutta quella serie di operazioni fondamentali che è possibile effettuarvi.

## Operazioni algebriche di base

Partiamo dalle operazioni algebriche di base. Ad esempio, possiamo sommare *elemento per elemento* due array mediante l'operatore `+`:

```py
>>> a = np.array([1, 2])
>>> b = np.array([3, 4])
>>> a + b
array([4, 6])
```

Contestualmente, l'utilizzo degli operatori matematici di sottrazione, moltiplicazione e divisione ci permetterà di effettuare le omologhe operazioni, sempre elemento per elemento.

```py
>>> a - b
array([-2, -2])
>>> a * b
array([3, 8])
>>> a / b
array([0.33333333, 0.5])
>>> b / a
array([3., 2.])
```

## La funzione `numpy.sum()`

La funzione [`numpy.sum()`](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum) ci permette di sommare tutti gli elementi di un array. Ad esempio, per sommare tutti gli elementi di un vettore:

```py
>>> a = np.array([1, 2, 3, 4])
>>> a.sum()
10
```

In caso di array multidimensionale, potremo specificare il parametro `axis`, che indica l'asse lungo il quale gli elementi vengono sommati. In particolare, il valore passato può essere un intero a valore $i$, nel qual caso si andrà ad effettuare la somma lungo la dimensione $i$-ma, o una tupla di interi, in qual caso la somma sarà effettuata su ognuna delle dimensioni specificate. Facciamo alcuni esempi.

Supponiamo di avere un array bidimensionale di dimensioni $2 \times 3$ (ovvero, a due righe e tre colonne).

```py
>>> b = np.array([[1, 2, 3], [4, 5, 6]])
>>> b
array([[1, 2, 3],
       [4, 5, 6]])
```

Cerchiamo di capire a quale dimensione sono associate le righe, ed a quale le colonne. Per farlo, usiamo l'attributo `shape`.

```py
>>> b.shape
(2, 3)
```

Nella tupla associata a `shape`, notiamo come il primo elemento sia associato al numero di righe, mentre il secondo al numero di colonne. Proviamo quindi a sommare l'array per righe, passando il parametro `axis=0`:

```py
>>> b.sum(axis=0)
array([5, 7, 9])
```

Intuitivamente, dato che il secondo elemento è associato al numero di colonne, la somma per colonne avrà luogo valorizzando `axis` ad `1`:

```py
>>> b.sum(axis=1)
array([6, 15])
```

Proviamo a vedere cosa accade in più dimensioni. Creiamo un array tridimensionale:

```py
>>> c = np.random.rand(2, 3, 4)
>>> c
array([[[0.92287179, 0.46394039, 0.87332474, 0.74359334],
        [0.52656447, 0.6055654 , 0.74493945, 0.9349442 ],
        [0.90911935, 0.01961204, 0.66304527, 0.3025307 ]],

       [[0.86562763, 0.37544415, 0.4984404 , 0.74486371],
        [0.10910642, 0.24617353, 0.6237486 , 0.26432378],
        [0.37713232, 0.08804626, 0.21283048, 0.41133527]]])
>>> c.shape
(2, 3, 4)
```

Proviamo adesso ad effettuare la somma di tutti gli elementi per riga e colonna:

```py
>>> c.sum(axis=(0, 1))
array([3.71042197, 1.79878176, 3.61632893, 3.401591  ])
```

Abbiamo quindi visto la versatilità della funzione `sum()`, e la capacità della stessa di operare su array a qualsiasi dimensionalità.

!!!tip "Il parametro `axis`"
    Ritroveremo il parametro `axis` in ogni applicazione che coinvolge NumPy e le librerie basate su di essa.

## La funzione `dot()`

La funzione `dot()` ci permette di effettuare l'operazione di moltiplicazione matriciale *riga per colonna*. In particolare, la funzione sarà invocata sulla matrice *a sinistra* nella moltiplicazione, mentre il parametro passato sarà la matrice *a destra*.

Ad esempio, possiamo provare a moltiplicare un vettore riga per un vettore colonna, ottenendo un intero:

```py
>>> a = np.array([[1, 2]])
>>> b = np.array([[3], [4]])
>>> a.dot(b)
array([11])
```

Al contrario, moltiplicando un vettore colonna per un vettore riga, otterremo una matrice:

```py
>>> b.dot(a)
array([[3, 6],
       [4, 8]])
```

## La funzione `numpy.sort()`

La funzione [`numpy.sort()`](https://numpy.org/doc/stable/reference/generated/numpy.sort.html) permette di ordinare gli elementi di un array. Ad esempio:

```py
>>> arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
>>> np.sort(arr)
array([1, 2, 3, 4, 5, 6, 7, 8])
```

L'ordine avviene maniera *ascendente* (ovvero dall'elemento più piccolo al più grande). In caso di array $n$-dimensionale, possiamo anche specificare l'asse lungo il quale avviene l'ordinamento, specificando il parametro axis. Ad esempio:

```py
>>> mat = np.array([[2, 3, 1], [4, 2, 6], [7, 5, 1]])
>>> mat
array([[2, 3, 1],
       [4, 2, 6],
       [7, 5, 1]])
```

Per ordinare lungo le righe:

```py
>>> np.sort(mat, axis=0)
array([[2, 2, 1],
       [4, 3, 1],
       [7, 5, 6]])
```

Mentre per ordinare lungo le colonne:

```py
>>> np.sort(mat, axis=1)
array([[1, 2, 3],
       [2, 4, 6],
       [1, 5, 7]])
```

Possiamo anche specificare diversi algoritmi di ordinamento mediante l'argomento `kind`, che ci permette di scegliere tra il quick sort, il merge sort e l'heap sort.

!!!note "Ordinamento inplace"
    I più attenti noteranno che la funzione `sort()` può essere chiamata direttamente sull'oggetto `mat` (`mat.sort()`) oppure da NumPy (`np.sort()`). Nel primo caso, la matrice viene modificata *inplace*, mentre nel secondo caso non lo è, e ne viene modificata una copia.

!!!note "Altre funzioni per l'ordinamento"
    Esistono anche altre funzioni per l'ordinamento di un array, come [`argsort()`](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort), [`lexsort()`](https://numpy.org/doc/stable/reference/generated/numpy.lexsort.html#numpy.lexsort), [`searchsorted()`](https://numpy.org/doc/stable/reference/generated/numpy.searchsorted.html#numpy.searchsorted) e [`partition()`](https://numpy.org/doc/stable/reference/generated/numpy.partition.html#numpy.partition).

## Concatenazione di due array

Per concatenare due array è necessario usare la funzione `concatenate()`:

```py
>>> a = np.array([1, 2, 3, 4])
>>> b = np.array([5, 6, 7, 8])
>>> np.concatenate((a, b))
array([1, 2, 3, 4, 5, 6, 7, 8])
```

Si può anche in questo caso usare il parametro `axis` per specificare l'asse lungo quale concatenare due diversi array:

```py
>>> x = np.array([[1, 2], [3, 4]])
>>> y = np.array([[5, 6], [7, 8]])
>>> np.concatenate((x, y), axis=0)
array([[1, 2],
       [3, 4],
       [5, 6],
       [7, 8]])
>>> np.concatenate((x, y), axis=1)
array([[1, 2, 5, 6],
       [3, 4, 7, 8]])
```

Ovviamente, le dimensioni degli array devono essere *coerenti* affinché vengano concatenati. Ad esempio:

```py
>>> z = np.array([[9, 10]])
```

la concatenazione per righe è ammissibile:

```py
>>> np.concatenate((x, z), axis=0)
array([[ 1,  2],
       [ 3,  4],
       [ 9, 10]])
```

mentre la concatenazione per colonne lancerà un errore:

```py
>>> np.concatenate((x, z), axis=1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<__array_function__ internals>", line 5, in concatenate
ValueError: all the input array dimensions for the concatenation axis must match exactly, but along dimension 0, the array at index 0 has size 2 and the array at index 1 has size 1
```

## Rimozione ed inserimento di elementi in un array

Vediamo brevemente come aggiungere o rimuovere un elemento in un array.

### La funzione `numpy.delete()`

La funzione [`numpy.delete()`](https://numpy.org/doc/stable/reference/generated/numpy.delete.html) ci permette di rimuovere uno o più elementi di un array specificandone gli indici. La funzione accetta i seguenti parametri:

* `arr`: l'array sul quale vogliamo effettuare l'operazione di rimozione;
* `obj`: gli indici degli elementi da rimuovere;
* `axis`: l'asse su cui vogliamo operare.

Ad esempio, immaginiamo di voler rimuovere il primo elemento di un vettore:

```py
>>> arr = np.array([1, 2, 3, 4])
>>> np.delete(arr, 0)
array([2, 3, 4])
```

La funzione può essere anche applicata su più indici usando una sequenza:

```py
>>> np.delete(arr, range(2))
array([3, 4])
```

Possiamo anche usare lo slicing:

```py
>>> idx = range(4)
>>> np.delete(arr, idx[0:2])
array([3, 4])
```    

!!!warning "Modifiche inplace"
    Nei casi precedenti la modifica *non* avviene inplace, per cui `arr` non sarà modificato.

#### Array multidimensionali e `delete()`

La funzione `delete()` può essere usata anche su array multidimensionali. In questo caso, è opportuno specificare l'asse su cui operare.

Ad esempio, se vogliamo rimuovere la prima riga dal seguente array, dobbiamo dare il valore `0` al parametro `axis`:

```py
>>> mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
>>> np.delete(mat, 0, 0)
array([[4, 5, 6],
       [7, 8, 9]])
```

Invece, se vogliamo rimuovere la prima colonna, dobbiamo passare il valore `1`:

```py
>>> np.delete(mat, 0, 1)
array([[2, 3],
       [5, 6],
       [8, 9]])
```

Se non specificassimo alcun valore per il parametro `axis`, otterremmo questo risultato:

```py
>>> np.delete(mat, 0)
array([2, 3, 4, 5, 6, 7, 8, 9])
```

In altre parole, non specificando un valore per `axis`, rimuoveremmo il primo elemento dell'array "vettorizzato".

!!!tip "Altre tecniche di rimozione elementi"
    Esistono altri modi di rimuovere elementi da un array. Ad esempio, si potrebbe usare la funzione `slice(start, stop, step)`, che crea un oggetto di classe `slice` sugli indici che vanno da `start` a `stop` con passo `step`. Questo può essere usato per scopi analoghi ai precedenti; ad esempio:
    > ```py
      >>> np.delete(a, slice(0, 2, 1))
      array([3, 4])
      ```

    Un altro modo è usare una maschera booleana:
    > ```py
      >>> mask = np.array([[True, False, True], [False, False, True], [False, True, True]])
      >>> mtrx[mask]
      array([1, 3, 6, 8, 9])
      ```

### La funzione `numpy.insert()`

La funzione [`numpy.insert()`](https://numpy.org/doc/stable/reference/generated/numpy.insert.html) permette di inserire un elemento all'interno di un array. I parametri accettati dalla funzione sono:

* `arr`: l'array sul quale vogliamo effettuare l'operazione di inserzione;
* `obj`: gli indici su cui inserire i nuovi valori;
* `values`: i valori da inserire agli indici specificati da `obj`;
* `axis`: l'asse su cui vogliamo operare.

Ad esempio, per inserire una nuova riga nella matrice precedente, dovremo specificare l'indice di riga (`3`), gli elementi della riga da inserire (`[10, 11, 12]`) e l'asse (`0`):

```py
>>> np.insert(mat, 3, [10, 11, 12], 0)
array([[ 1,  2,  3],
       [ 4,  5,  6],
       [ 7,  8,  9],
       [10, 11, 12]])
```

Cambiando l'asse in `1`, si effettua l'inserzione sulle colonne:

```py
>>> np.insert(mat, 3, [10, 11, 12], 1)
array([[ 1,  2,  3, 10],
       [ 4,  5,  6, 11],
       [ 7,  8,  9, 12]])
```

Non specificando alcun asse, infine, si inserisce l'elemento specificato nella matrice vettorizzata:

```py
>>> np.insert(mat, 9, 10)
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
```

### La funzione `numpy.append()`

La funzione [`numpy.append()`](https://numpy.org/doc/stable/reference/generated/numpy.append.html) permette di inserire in coda ad un array i valori specificati. I parametri accettati dalla funzione sono:

* `arr`: l'array sul quale vogliamo effettuare l'operazione di inserzione;
* `values`: i valori da inserire in coda all'array;
* `axis`: l'asse su cui vogliamo operare.

Al solito, non specificando l'asse effettuiamo la concatenazione sulla matrice vettorizzata:

```py
>>> np.append(mat, [[10, 11, 12]])
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12])
```

Se specifichiamo il valore 0 sul parametro `axis`, effettuiamo la concatenazione per righe:

```py
>>> np.append(mat, [[10, 11, 12]], axis=0)
array([[ 1,  2,  3],
       [ 4,  5,  6],
       [ 7,  8,  9],
       [10, 11, 12]])
```

Se specifichiamo il valore 1 sul parametro `axis`, invece, effettuiamo la concatenazione per colonne:

```py
>>> np.append(mat, [[10], [11], [12]], axis=1)
array([[ 1,  2,  3, 10],
       [ 4,  5,  6, 11],
       [ 7,  8,  9, 12]])
```

!!!warning "Attenzione"
    Nell'ultima istruzione, abbiamo usato un vettore *colonna*, mentre nella penultima un vettore *riga*.

## Dimensioni e forma di un array

Esistono diverse proprietà di un array che ne descrivono dimensioni e forma.

Tornando alla nostra matrice `mat`, possiamo conoscere il numero di assi mediante l'attributo `ndarray.ndim`:

```py
>>> mat.ndim
2
```

Il numero di elementi è invece definito dall'attributo `ndarray.size`:

```py
>>> mat.size
9
```

L'attributo `ndarray.shape`, che abbiamo brevemente visto in precedenza, restituisce invece una tupla di interi che indica il numero di elementi per ciascuno degli assi dell'array:

```py
>>> mat.shape
(3, 3)
```

## Modificare le dimensioni di un array

Possiamo modificare le dimensioni di un array mediante la funzione [`numpy.reshape()`](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html). I parametri passati alla funzione sono:

* `arr`: l'array di cui modificare le dimensioni;
* `new_shape`: le nuove dimensioni dell'array.

Se volessimo modificare le dimensioni di una matrice da $4 \times 4$ a $2 \times 8$, potremmo usare la funzione `reshape()` come segue:

```py
>>> mat = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
>>> np.reshape(mat, (2, 8))
array([[ 1,  2,  3,  4,  5,  6,  7,  8],
       [ 9, 10, 11, 12, 13, 14, 15, 16]])
```

!!!tip "Suggerimento"
    Una forma alternativa è la seguente:
    > ```py
      >>> mat.reshape((2, 8))
      array([[ 1,  2,  3,  4,  5,  6,  7,  8],
             [ 9, 10, 11, 12, 13, 14, 15, 16]])
      ```
    
    Ciò significa che la funzione `reshape()` è sia disponibile nella libreria NumPy, sia come metodo sugli oggetti di classe `ndarray`.

!!!warning "Attenzione"
    Le nuove dimensioni dell'array devono essere coerenti con quelle dell'array di partenza!

## Flattening di un array

Abbiamo già visto in precedenza la *vettorizzazione* di un array, effettuata in automatico in alcune situazioni (come ad esempio la chiamata di `delete()` o `insert()` senza specificare il parametro `axis`). Tuttavia, possiamo usare la funzione [`numpy.flatten()`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flatten.html) per effettuare manualmente questa operazione:

```py
>>> mat.flatten()
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16])
```

Un altro modo per effettuare la vettorizzazione è utilizzare la funzione [`numpy.ravel()`](https://numpy.org/doc/stable/reference/generated/numpy.ravel.html).

Le funzioni `ravel()` e `flatten()` possono apparentemente sembrare analoghe. Tuttavia, vi è una differenza fondamentale: infatti, `flatten()` restituirà *sempre* una copia dell'array originario, mentre `ravel()`, laddove possibile, restituirà una *vista*, ovvero una variabile che punta allo stesso indirizzo di memoria dell'oggetto originario.
