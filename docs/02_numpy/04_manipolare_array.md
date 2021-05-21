https://numpy.org/doc/stable/user/absolute_beginners.html#adding-removing-and-sorting-elements

FONO A "How to convert a D array into a 2D array

Ordinare un elemento è semplice con np.sort(). Si possono specificare gli assi, tipo ed ordine quando si chiama la funzione.

Se si inizia con questo array:

```py
>>> arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
```

si può rapidamente ordinare i numeri in ordine ascendente con:

```py
>>> np.sort(arr)
array([1, 2, 3, 4, 5, 6, 7, 8])
```

Oltre all'ordinamento, che restituisce una copia ordinata di un array, si possono usare le seguenti funzioni:

* argsort, che è un ordinamento indiretto lungo un certo asse
* lexosrt, che è un ordinamento indiretto con più chiavi
* searchsorted, che trova gli elementi in un array ordinato e
* partition, che è un ordinamento parziale

Se iniziamo con questi array:

```py
>>> a = np.array([1, 2, 3, 4])
>>> b = np.array([5, 6, 7, 8])
```

possiamo concatenarli usando `np.concatenate()`.

```py
>>> np.concatenate((a, b))
array([1, 2, 3, 4, 5, 6, 7, 8])
```

O, se iniziamo con questi array:

>>> x = np.array([[1, 2], [3, 4]])
>>> y = np.array([[5, 6]])

possiamo concatenarli con:

>>> np.concatenate((x, y), axis=0)
array([[1, 2],
       [3, 4],
       [5, 6]])
    
per rimuovere un elemento in un array, è facile usare l'indicizzazione per scegliere gli elementi che si vogliono mantenere.

## come si fa a sapere la dimensione e forma di un array

ndarray.ndim ci dice il numero di assi, o dimensioni, dell'array

ndarray.size ci dice il numero totale di elementi dell'array. Questo è il prodotto degli elementi della forma dell'array.

ndarray.shape ci mostra una tupla di interi che indicano il numero di elmeenti memorizzati in ogni dimensione dell'array. Se, per esempio, si ha un array bidimensioanle con due righe e tre colonne, la forma dell'array è (2, 3).

per esempio, se si crea questo array:

>>> array_example = np.array([[[0, 1, 2, 3],
...                            [4, 5, 6, 7]],
...
...                           [[0, 1, 2, 3],
...                            [4, 5, 6, 7]],
...
...                           [[0 ,1 ,2, 3],
...                            [4, 5, 6, 7]]])

Per trovare il numero di dimensioni dell'array, si esegue:

>>> array_example.ndim
3

per trovare il numero totale di elementi nell'array, si esegue:

>>> array_example.size
24

e per trovare la dimensione del nostro array, eseguiamo:

>>> array_example.shape
(3, 2, 4)


## cambiare le dimensioni di un array

usare arr.reshape() darà una nuova forma all'array senza cambiare i dati. Ricordiao che quando si usa il metodo reshape, l'array che vogliamo produrre deve avere lo stesso numero di elementi dell'array originario. Se iniziamo con un array con 12 elementi, dovremo assicuracri che il nostro nuovo array ha un totale di 12 elementi.

Se iniziamo con questo array:

>>> a = np.arange(6)
>>> print(a)
[0 1 2 3 4 5]

possiamo usare reshape() per cambiare le dimensioni dell'arary. Ad esempio, possiamo ridimensionare questo array in un array con tre righe e due colonne:

>>> b = a.reshape(3, 2)
>>> print(b)
[[0 1]
 [2 3]
 [4 5]]

con np.reshape, possiamo specificare alcuni parametri opzionali:

>>> numpy.reshape(a, newshape=(1, 6))
array([[0, 1, 2, 3, 4, 5]])

a è l'array che verrà ridimensionato.

newshape è la nuova forma che vogliamo. POssiamo specificare un intero o una tupla di interi. Se specifichiamo un intero, il risultato sarà un array di quella lunghezza. La fomra deve essere compatibile con quella originaria.
