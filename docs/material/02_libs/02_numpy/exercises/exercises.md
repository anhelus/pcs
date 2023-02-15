# Esercitazione 3 - NumPy

## Esercizi sugli array

!!!tip "Disponibilità soluzioni"
    Tutte le soluzioni sono disponibili in [questo notebook](./exercises.ipynb).

### Esercizio 3.1

Scrivere una funzione che restituisca il prodotto *riga per colonna* di due vettori `v1` e `v2`. Utilizzare in primis una list comprehension, verificando anche che la lunghezza dei due vettori sia coerente. Valutare inoltre il tempo necessario all'esecuzione.

Effettuare la stessa operazione in NumPy, valutando contestualmente il tempo necessario.

**Soluzione**: Definiamo innanzitutto la funzione `riga_per_colonna`, la quale accetta due array in ingresso e, se le dimensioni sono coerenti, effettua la moltiplicazione riga per colonna.

Una possibile forma per la funzione è la seguente:

```py linenums="1"
def riga_per_colonna(v1, v2):
	tic = time()
	if v1.shape[0] == 1:
		if v2.shape[1] == 1 and v1.shape[1] == v2.shape[0]:
			prod = sum([v1[0][i] * v2[i] for i in range(v2.shape[0])])
	elif v2.shape[0] == 1:
		if v1.shape[1] == 1 and v2.shape[1] == v1.shape[0]:
			prod = sum([v1[i] * v2[0][i] for i in range(v1.shape[0])])
	else:
		return 'Le dimensioni non sono coerenti!'
	toc = time()
	return prod, toc - tic
```

In particolare:

* alla riga 2, lanciamo il timer di inizio chiamata a funzione;
* alle righe 3-4, se il vettore `v1` è un vettore riga, allora andiamo a controllare che il vettore `v2` sia un vettore colonna;
* alla riga 5, se il controllo precedente è andato per il verso giusto, usiamo una list comprehension per fare il prodotto riga per colonna;
* alle righe 6-8, effettuiamo le operazioni duali alle precedenti;
* alla riga 11, lanciamo il timer di fine chiamata a funzione;
* alla riga 12, restituiamo il prodotto ed il tempo trascorso.

Proviamo la nostra funzione:

```py
v1 = np.array([[1,2,3,4]])
v2 = np.array([[1],[2],[3],[4]])

res, elapsed = riga_per_colonna(v1, v2)
print(elapsed)
```

L'equivalente operazione in NumPy è data da:

```py
res = np.dot(v1, v2)
```

### Esercizio 3.2

Scrivere la funzione `crea_array(dim_1, dim_2, val_min, val_max)` che crea array di dimensione arbitraria `dim_1` $\times$ `dim_2` composti da numeri interi casuali compresi tra `val_min` e `val_max`. Di default, la funzione dovrà creare dei vettori riga.

Provare ad effettuare la stessa operazione in NumPy.

**Soluzione**: Una possibile soluzione è la seguente:

```py linenums="1"
def crea_array(dim_1, dim_2=1, val_min=0, val_max=100):
	rows = [[randint(val_min, val_max) for i in range(dim_2)] for j in range(dim_1)]
	return np.array(rows)
```

Alla riga 2 utilizziamo due list comprehension, l'una annidata nell'altra. In particolare, nella list comprehension più interna, andremo a generare `dim_2` valori interi casuali compresi tra `val_min` e `val_max`, mentre in quella più esterna ripeteremo l'operazione definita dalla lista più interna `dim_1` volte. Il valore ottenuto è quindi restituito alla riga 3.

Con NumPy potremo ovviamente utilizzare il metodo [`randint`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html):

```py
from numpy import random

a_1 = random.randint(0, 100, (4, 1))
a_2 = random.randint(0, 100, (2, 2))
```

### Esercizio 3.3

Scrivere la funzione `rettifica(array)` che restituisce un array analogo a quello in ingresso, ma con tutti i valori negativi "rettificati" a $0$.

**Soluzione**: Per risolvere questo problema, possiamo sfruttare il concetto di *maschera booleana*. In particolare, se provassimo a scrivere un'espressione del tipo:

```py
>>> a = np.array([1, 2, -1, 2])
>>> [a < 0]
```

l'interprete ci restituirebbe una maschera fatta di soli booleani:

```py
[array([False, False,  True, False])]
```

Questa maschera può essere utilizzata per accedere agli elementi dell'array `a` il cui corrispondente elemento nella maschera è a `True`. In pratica, nell'esempio precedente, accederemo esclusivamente all'elemento in posizione $3$:

```py
>>> a[a < 0]
array([-1])
```

Ovviamente, possiamo utilizzare questa maschera anche per assegnare dei nuovi valori agli elementi acceduti. Quindi, scrivendo:

```py
>>> a[a < 0] = 0
```

andremo a modificare l'array `a` come segue:

```py
array([1, 2, 0, 2])
```

Di conseguenza, potremo scrivere la funzione rettifica come segue:

```py
def rettifica(array):
    array[array < 0] = 0
    return array
```

## Esercizi sulle operazioni algebriche

### Esercizio 3.4

Verificare che il prodotto tra una matrice invertibile e la sua inversa sia la matrice identità.

**Soluzione**: Per verificare questo assunto ci basta utilizzare la funzione `inv` per calcolare la matrice inversa:

```py
mat = np.array([[5, 0, 1], [0, 2, 2], [0, 0, 3]])
mat_inv = np.linalg.inv(mat)
```

Conseguentemente, utilizzando la funzione `dot`, potremo fare il prodotto matriciale tra `mat`e `mat_inv`, verificando che sia pari alla matrice identità (in questo caso di ordine 3):

```py
np.eye(3) == mat.dot(mat_inv)
```

### Esercizio 3.5

Scrivere la funzione `calcola_determinante()` che accetta come parametro in ingresso una matrice $2 \times 2$ e ne calcola il determinante. Si supponga che la matrice sia invertibile.

**Soluzione**: Ricordiamo che il calcolo del determinante di una matrice $2 \times 2$ è dato dalla differenza tra il prodotto degli elementi sulla diagonale e quello dei restanti elementi.

Per cui, la funzione `calcola_determinante()` potrà essere scritta come segue:

```py linenums=1"
def calcola_determinante(mat):
    if len(mat.shape) == 2 and mat.shape[0] == mat.shape[1] and mat.shape[0] == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    raise ValueError('La matrice non ha le dimensioni attese.')
```

In particolare:

* alla riga 2, verifichiamo che la matrice sia bidimensionale ed abbia dimensioni $2 \times 2$;
* alla riga 3, calcoliamo il determinante;
* alla riga 4, lanciamo un errore nel caso la matrice non abbia dimensioni $2 \times 2$.

### Esercizio 3.6

Scrivere la funzione `inverti_se_invertibile(mat)` che, data una matrice bidimensionale, restituisca l'inversa soltanto se `mat` è bidimensionale, quadrata, e il determinante è diverso da zero. Utilizzare un'unica istruzione condizionale.

**Soluzione**: In questo caso, potremo utilizzare i metodi messi a disposizione da NumPy. Tuttavia, dovremo verificare contemporaneamente che:

* `shape` di `mat` sia pari a `2` (e, quindi, la matrice sia bidimensionale);
* la prima dimensione sia uguale alla seconda;
* che il determinante sia diverso da zero (e, quindi, la matrice risulti essere invertibile).

Di seguito, una possibile soluzione:

```py
def inverti_se_invertibile(mat):
    if len(mat.shape) == 2 \
        and mat.shape[0] == mat.shape[1] \
        and linalg.det(mat) != 0:
        return linalg.inv(mat)
    raise ValueError('La matrice passata non è invertibile.')
```

