# Operare sugli array

NumPy offre numerose modalità per operare sugli array e manipolarli. Vediamone alcune.

## Operazioni aritmetiche

Possiamo usare due array per effettuare diversi tipi di operazioni aritmetiche (elemento per elemento). Ad esempio, per sommare due array:

```py
>>> a = np.array([1, 2])
>>> b = np.array([3, 4])
>>> a + b
array([4, 6])
```

Possiamo ovviamente anche usare le altre operazioni aritmetiche:

```py
>>> a - b
array([-2, -2])
>>> a * b
array([3, 8])
>>> a / b
array([0.33333333, 0.5       ])
```

### La funzione `sum`

La funzione `sum(axis=None)` ci permette di sommare tutti gli elementi di un array lungo l'asse specificato.

Ad esempio, per sommare tutti gli elementi di un vettore:

```py
>>> a = np.array([1, 2, 3, 4])
>>> a.sum()
10
```

In caso di array multidimensionale, dovremo specificare, come già detto, l'asse. Ad esempio, per sommare gli elementi per colonna, dovremo passare il parametro `0`:

```py
>>> b = np.array([[1, 2], [3, 4]])
>>> b.sum(axis=0)
array([4, 6])
```

Per sommare gli elementi per riga, invece, dovremo passare il parametro `1`:

```py
>>> b.sum(axis=1)
array([3, 7])
```

## Ordinamento degli elementi di un array

Ordinare gli elementi di un array è possibile usando la funzione `sort()`. Ad esempio:

```py
>>> arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
>>> np.sort(arr)
array([1, 2, 3, 4, 5, 6, 7, 8])
```

L'ordine avviene, di default, in maniera *ascendente*.

In caso di array n-dimensionale, possiamo anche specificare l'asse lungo il quale avviene l'ordinamento, specificando il parametro axis. Ad esempio:

```py
>>> mat = np.array([[2,3,1], [4,2,6], [7,5,1]])
>>> mat
array([[2, 3, 1],
       [4, 2, 6],
       [7, 5, 1]])
```

Per ordinare lungo le colonne:

```py
>>> np.sort(mat, axis=0)
array([[2, 2, 1],
       [4, 3, 1],
       [7, 5, 6]])
```

Mentre per ordinare lungo le righe:

```py
>>> np.sort(mat, axis=1)
array([[1, 2, 3],
       [2, 4, 6],
       [1, 5, 7]])
```

!!!note "Nota"
    Esistono anche altre funzioni per l'ordinamento di un array, che però non tratteremo in questo corso.

## Concatenazione di più array

Possiamo concatenare due array usando la funzione `concatenate()`:

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

Ovviamente, le dimensioni degli array devono essere *coerenti* affinché vengano concatenati. Ad esempio, con questo array:

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

mentre la concatenazione per colonne non è possibile:

```py
>>> np.concatenate((x, z), axis=1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<__array_function__ internals>", line 5, in concatenate
ValueError: all the input array dimensions for the concatenation axis must match exactly, but along dimension 0, the array at index 0 has size 2 and the array at index 1 has size 1
```

## Rimozione ed inserimento di elementi in un array

### La funzione `delete`

La funzione `delete(arr, obj, axis=None)` ci permette di rimuovere uno o più elementi di un array specificandone gli indici. La funzione accetta i seguenti parametri:

* `arr`: l'array sul quale vogliamo effettuare l'operazione di rimozione;
* `obj`: gli indici degli elementi da rimuovere;
* `axis`: l'asse su cui vogliamo operare.

Ad esempio, immaginiamo di voler rimuovere il primo elemento di un vettore:

```py
>>> arr = np.array([1, 2, 3, 4])
>>> np.delete(arr, 0)
array([2, 3, 4])
>>> arr
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

!!!tip "Suggerimento"
    La precedente notazione può essere rimpiazzata dalla funzione `slice(start, stop, step)`, che crea un oggetto di classe `slice` sugli indici che vanno da `start` a `stop` con passo `step`. Questo può essere usato per scopi analoghi ai precedenti; ad esempio:
    > ```py
      >>> np.delete(a, slice(0, 2, 1))
      array([3, 4])
      ```

#### Array multidimensionali

La funzione può essere usata anche su array multidimensionali. In questo caso, è opportuno specificare l'asse su cui operare. 

Ad esempio, se vogliamo rimuovere la prima riga dal seguente array, dobbiamo dare il valore `0` al parametro `axis`:

```py
>>> mat = np.array([[1,2,3], [4,5,6], [7,8,9]])
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

Cosa è accaduto? In pratica, è stato rimosso il primo elemento *dell'array vettorizzato* (*flattened*).

#### Rimozione di elementi mediante maschere booleane

Spesso è preferibile usare, al posto della notazione precedente, una maschera booleana: 

```py
>>> mask = [False, False, True, True]
>>> arr[mask]
array([3, 4])
```

### La funzione `insert`

La funzione `insert(arr, obj, values, axis=None)` permette di inserire un elemento all'interno di un array. I parametri accettati dalla funzione sono:

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

### La funzione `append`

La funzione `append(arr, values, axis=None)` permette di inserire in coda ad un array i valori specificati. I parametri accettati dalla funzione sono:

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

L'attributo `ndarray.shape` restituisce invece una tupla di interi che indica il numero di elementi per ciascuno degli assi dell'array:

```py
>>> mat.shape
(3, 3)
```

## Modificare le dimensioni di un array

Possiamo modificare le dimensioni di un array mediante la funzione `reshape(arr, new_shape)`. I parametri passati alla funzione sono:

* `arr`: l'array di cui modificare le dimensioni;
* `new_shape`: le nuove dimensioni dell'array.

Se volessimo modificare le dimensioni di una matrice da $4 \times 4$ a $2 \times 8$, potremmo usare la funzione `reshape` come segue:

```py
>>> mat = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])
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
    Ciò significa che la funzione `reshape` è sia disponibile nella libreria NumPy, sia come metodo sugli oggetti di classe `ndarray`.

!!!warning "Attenzione"
    Le nuove dimensioni dell'array devono essere coerenti con quelle dell'array di partenza!

### Flattening (o vettorizzazione)

Abbiamo già visto in precedenza la *vettorizzazione* di un array, effettuata in automatico in alcune situazioni (come ad esempio la chiamata di `delete` o `insert` senza specificare il parametro `axis`). Tuttavia, possiamo usare la funzione `flatten` per effettuare manualmente questa operazione:

```py
>>> mat.flatten()
array([1, 2, 3, 4, 5, 6, 7, 8, 9])
```

## Il broadcasting

Concludiamo questa lezione accennando al *broadcasting*, che viene usato ogni volta che vogliamo effettuare un'operazione tra un array ed un singolo scalare, o tra array di dimensioni differenti (posto che, ovviamente, questa operazione sia algebricamente ammissibile).

Supponiamo di voler moltiplicare il nostro array per un certo scalare:

```py
>>> a = np.array([1, 2])
>>> a * 2
array([2, 4])
```

Appare evidente come NumPy "comprenda" che la moltiplicazione deve avvenire tra lo scalare `2` e tutti gli elementi del vettore `a`. Ovviamente, questo concetto è esteso ad ogni operazione di tipo matriciale, come vedremo nella prossima lezione.
