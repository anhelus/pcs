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
