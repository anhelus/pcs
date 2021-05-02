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
