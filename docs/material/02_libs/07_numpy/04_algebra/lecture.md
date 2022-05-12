# 7.4 - Operazioni matriciali

NumPy mette a disposizione il package `linalg` per permettere di effettuare numerose operazioni matriciali. La maggior parte degli esempi che vedremo nel seguito prevedono l'utilizzo di questo package, per cui possiamo partire importandolo.

```py
from numpy import linalg
```

## 7.4.1 - Matrice trasposta

La prima operazione che vediamo *non* richiede l'uso del modulo `linalg`, ed è quella che ci permette di effettuare la trasposta di una matrice. Per farlo, usiamo la funzione `transpose`.

```py
x = np.array([[1, 2, 3], [4, 5, 6]])
np.transpose(x)

array([[1, 4],
       [2, 5],
       [3, 6]])
```

## 7.4.2 - Matrice inversa

Possiamo calcolare l'inversa di una matrice usando la funzione `inv(mat)` del package `linalg`, dove `mat` è la matrice da invertire. Ad esempio:

```py
mat = np.array([[5, 0, 0], [0, 2, 0], [0, 0, 4]])
linalg.inv(mat)

array([[0.2 , 0.  , 0.  ],
       [0.  , 0.5 , 0.  ],
       [0.  , 0.  , 0.25]])
```

Ovviamente, la matrice `mat` deve essere invertibile. Nel caso passassimo una matrice rettangolare, infatti,verrebbe lanciato un `LinAlgError`:

```py
mat = np.array([[1,2,3], [4,5,6]])
linalg.inv(mat)

Traceback (most recent call last):
numpy.linalg.LinAlgError: Last 2 dimensions of the array must be square
```

Lo stesso accade per una matrice singolare:

```py
mat = np.array([[1,1,1],[2,2,2],[0,0,1]])
linalg.inv(mat)

Traceback (most recent call last):
numpy.linalg.LinAlgError: Singular matrix
```

## 7.4.3 - Prodotti vettoriali e matriciali

### 7.4.3.1 - La funzione `dot()`

Nella scorsa lezione abbiamo visto un esempio di uso della funzione `dot(a, b)`, necessaria a calcolare il prodotto matriciale tra gli array `a` ed `b`. Ovviamente, si applicano tutte le regole valevoli per il calcolo del prodotto matriciale (ovvero quello relativo alla moltiplicazione righe per colonne); riassumiamole nella seguente tabella sulla base delle dimensionalità di `a` ed `b`.

| Dimensionalità `a` | Dimensionalità `b` | Risultato | Note |
| ---------------- | ----- | --------- | ---- |
| Monodimensionale (vettore) | Monodimensionale (vettore) | Prodotto scalare | / |
| Bidimensionale (matrice) | Bidimensionale (matrice) | Prodotto matriciale | Preferire la funzione `matmul` |
| Scalare | N-dimensionale | Prodotto scalare per array N-dimensionale | Preferire la funzione `multiply(a, b)` o l'operatore `*` |
| N-dimensionale | Scalare | Prodotto scalare per array N-dimensionale | Preferire la funzione `multiply(a, b)` o l'operatore `*` |

Nel caso entrambi gli array siano N-dimensionali, si applicano altre regole, che è possibile recuperare a [questo indirizzo](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot).

### 7.4.3.2 - Prodotto interno

Possiamo usare la funzione `inner(a, b)` per calcolare il *prodotto interno* (o *scalare*) tra i vettori `a` e `b`:

```py
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

np.inner(a, b)

32
```

!!!note "Definizione di prodotto interno"
	Ricordiamo che per due generici vettori monodimensionali $v_1 = [v_{11}, \ldots, v_{1j}], v_2 = [v_{21}, \ldots, v_{2j}]$ il prodotto scalare è dato da:
	$$p = \sum_{i=1}^j v_{1i} * v_{2i}$$

### 7.4.3.2 - Prodotto esterno

Possiamo usare la funzione `outer(a, b)` per calcolare il *prodotto esterno* tra due vettori. In particolare, dati due vettori $a = [a_1, a_2, \ldots, a_n]$ e $b = [b_1, b_2, \ldots, b_n]$, il prodotto esterno è definito come la matrice $P$ tale che:

$$
P = \left[
	\begin{array}{ccc}
		a_1 * b_1 & \ldots & a_1 * b_n \\
		\vdots & \ddots & \vdots \\
		a_n * b_1 & \ldots & a_n * b_n
	\end{array}
\right]
$$

Ad esempio:

```py
>>> np.outer(a, b)
array([[3, 4],
       [6, 8]])
```

### 7.4.3.3 - La funzione `matmul`

Quando abbiamo parlato della funzione `dot(a, b)` abbiamo visto come sia possibile usarla per effettuare il prodotto matriciale tra le matrici `mat_1` e `mat_2`. Tuttavia, esiste un'altra possibilità, che è anche quella *consigliata*, ovvero usare la funzione `matmul(a, b)`:

```py
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

np.matmul(a, b)
array([[19, 22],
       [43, 50]])
```

La funzione `matmul()` ha una differenza fondamentale rispetto alla funzione `dot()`, in quanto non accetta scalari come parametro (anche se è possibile passare vettori ed array N-dimensionali). Esiste in realtà un'altra differenza importante, che riguarda le operazioni N-dimensionali, ma che non tratteremo in questa sede.

## 7.4.4 - Potenza di matrice

La funzione `matrix_power(a, n)` del package `linalg` permette di elevare a potenza `n` della matrice `a`. Ad esempio:

```py
matrix_power(a, 5)

array([[1069, 1558],
       [2337, 3406]])
```

## 7.4.5 - Decomposizione ai valori singolari

La *decomposizione ai valori singolari*, detta anche *SVD* dall'acronimo inglese *Singular Value Decomposition*, è una tecnica di decomposizione di una matrice che permette di scomporla in modo da semplificarci la vita in alcune situazioni.

!!!tip "Approfondimento"
	Per un'approfondimento sui principi alla base della SVD, consultare l'[appendice E.1](../../../appendix/06_algorithms/01_svd/lecture.md).

L'implementazione da zero della SVD è estremamente complessa; tuttavia, NumPy ci viene quindi in aiuto con la funzione `svd(mat)` del package `linalg`:

```py
(u, s, v) = linalg.svd(a)

u: [[-0.40455358 -0.9145143 ]
 [-0.9145143   0.40455358]] 
s: [5.4649857  0.36596619] 
v: [[-0.57604844 -0.81741556]
 [ 0.81741556 -0.57604844]]
```

## 7.4.6 - Autovalori ed autovettori

Per calcolare gli autovalori e gli autovettori di una matrice, NumPy ci mette a disposizione la funzione `eig(a)`, sempre appartenente al package `linalg`, che restituisce gli autovalori e gli autovettori destri di una matrice quadrata:

```py
(w, v) = linalg.eig(mat)

w
array([15.23391422,  0.08412242,  4.68196336])

v
array([[-0.66930729, -0.82394712, -0.68445786],
       [-0.16856631,  0.44469209, -0.70619627],
       [-0.72361119,  0.35122656,  0.18111947]])
```

## 7.4.7 - Norma

La funzione `linalg.norm(a)` ci permette di calcolare la norma di una matrice. Opzionalmente, possiamo specificare tre parametri, ovvero:

* `ord`, che rappresenta l'ordine della norma da calcolare (di default, viene calcolata la norma di Frobenius);
* `axis`, che indica l'asse (o gli assi, in caso di array multidimensionale) su cui operare;
* `keepdims`, usata per restituire, opzionalmente, l'asse su cui viene calcolata la norma.

Per calcolare la norma di Frobenius della matrice `mat` possiamo usare questa sintassi:

```py
linalg.norm(mat)				# Il risultato sarà 16.97...
```

## 7.4.8 - Determinante, rango e traccia

Possiamo calcolare rapidamente determinante, rango e traccia di una matrice mediante le funzioni `det(a)`, `matrix_rank(a)` e `trace(a)`, quest'ultima **non** appartenente al package `linalg`. Ad esempio:

```py
linalg.det(mat)					# Il risultato sarà 6
linalg.matrix_rank(mat)			# Il risultato sarà 3
np.trace(mat)					# Il risultato sarà 20
```

La funzione `trace` può anche essere usata per calcolare la sommatoria delle sovra/sotto diagonali specificando il parametro `offset`. Ad esempio:

```py
mat = np.array([[ 5,  2,  9],
	[ 2,  3,  1],
	[ 4, -2, 12]])

np.trace(mat, offset=1)			# Il risultato sarà 3
np.trace(mat, offset=-1)		# Il risultato sarà 0
```

## 7.4.9 - Risoluzione di sistemi di equazioni lineari

Chiudiamo questa (necessariamente breve!) carrellata sulle operazioni di algebra lineare con la funzione `solve(a, b)`, che permette di risolvere un sistema di equazioni lineari nel quale la matrice `a` è la matrice dei coefficienti, mentre il vettore `b` è il vettore dei termini noti. Ad esempio:

```py
b = np.array([3, 2, 3])
linalg.solve(mat, b)			# Il risultato sarà array([-7.5,  4.5,  3.5])
```

Ovviamente, la matrice `a` deve essere quadrata, mentre il vettore `b` deve avere esattamente `n` elementi, con `n` ordine di `a`!
