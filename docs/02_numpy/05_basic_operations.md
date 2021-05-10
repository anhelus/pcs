una volta che abbiamo creato i  nostri array, possiamo iniziare a lavorarci. Diciamo, ad esempio, che abbiamo creato due array, uno chiamato *data* ed uno chiamato *ones*.

Posisamo sommare i due array mediante il segno più.

>>> data = np.array([1, 2])
>>> ones = np.ones(2, dtype=int)
>>> data + ones
array([2, 3])

Ovviamente, possiamo efettuare anche altre operazioni aritmentiche.

>>> data - ones
array([0, 1])
>>> data * data
array([1, 4])
>>> data / data
array([1., 1.])

Le operazioni base sono semplici con NumPy. Se vogliamo trovare la somma degli elementi in un array, useremo sum(). Questo funziona per gli array di qualsiasi dimensione.

>>> a = np.array([1, 2, 3, 4])

>>> a.sum()
10

Per aggiungere le righe o le colonne in un array bidimensionale, è necessario specificare l'asse.
 
se iniziamo con questo array:

>>> b = np.array([[1, 1], [2, 2]])

possiamo sommare le righe con:

>>> b.sum(axis=0)
array([3, 3])

e le colonne con:

>>> b.sum(axis=1)
array([2, 4])

