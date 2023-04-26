# 2.2.4 - Operazioni algebriche in NumPy

!!!tip "Notebook di accompagnamento"
	Per questa lezione esiste un *notebook di accompagnamento*, reperibile a [questo indirizzo](https://github.com/anhelus/pcs-exercises/blob/master/01_libs/01_numpy/01_algebra.ipynb).

Dopo aver trattato le [operazioni fondamentali](03_fundamentals.md) in NumPy, facciamo un breve approfondimento sulle operazioni di algebra lineare, alcune delle quali sono integrate nel package [`linalg`](https://numpy.org/doc/stable/reference/routines.linalg.html).

Gli esempi che vedremo nel seguito prevederanno tutti l'uso di questo package, per cui è necessario importarlo prima di procedere nella lezione.

```py
from numpy import linalg
```

## Matrice trasposta

In realtà, la prima operazione che descriveremo *non* richiede l'uso del modulo `linalg`, ed è quella che ci permette di effettuare la trasposta di una matrice. 

Ricordiamo che la trasposta $A^T$ di una matrice $A$ è definita come la matrice in cui il generico elemento con indice $(i,j)$ è l'elemento con indici $(j,i)$ della matrice originaria. In pratica:

$$
(A^T)_{ij} = A_{ji} \forall A \in \mathbb{R}^{m,n}, 1 \leq i \leq m, 1 \leq j \leq n
$$

Per farlo, dovremo semplicemente usare la funzione [`numpy.transpose()`](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html).

```py
>>> x = np.array([[1, 2, 3], [4, 5, 6]])
>>> np.transpose(x)
array([[1, 4],
       [2, 5],
       [3, 6]])
```

## Matrice inversa

Il calcolo della matrice inversa, invece, prevede l'utilizzo della funzione [`linalg.inv()`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.inv.html), che accetta come parametro la matrice da invertire. 

Ricordiamo che la matrice inversa $A_{inv}$ di una matrice invertibile $A$ è quella matrice per cui vale la seguente relazione:

$$
A_{inv}A=AA_{inv}=I
$$

In altri termini, il prodotto matriciale tra $A$ e la sua inversa è commutativo e pari alla matrice identità di eguale rango.

Ad esempio:

```py
>>> mat = np.array([[5, 0, 0], [0, 2, 0], [0, 0, 4]])
>>> linalg.inv(mat)
array([[0.2 , 0.  , 0.  ],
       [0.  , 0.5 , 0.  ],
       [0.  , 0.  , 0.25]])
```

Ovviamente, *la matrice `mat` deve essere invertibile*, ovvero quadrata e a rango massimo. Nel caso passassimo una matrice rettangolare, infatti, verrebbe lanciato un errore di tipo `LinAlgError`:

```py
>>> mat = np.array([[1, 2, 3], [4, 5, 6]])
>>> linalg.inv(mat)
Traceback (most recent call last):
numpy.linalg.LinAlgError: Last 2 dimensions of the array must be square
```

Lo stesso accade se `mat` è singolare:

```py
>>> mat = np.array([[1, 1, 1], [2, 2, 2], [0, 0, 1]])
>>> linalg.inv(mat)
Traceback (most recent call last):
numpy.linalg.LinAlgError: Singular matrix
```

## Prodotti vettoriali e matriciali

### La funzione `dot()`

Nella [scorsa lezione](03_fundamentals.md#operazioni-algebriche-di-base) abbiamo visto un esempio di utilizzo della funzione `dot(a, b)` utilizzata per calcolare il prodotto matriciale tra gli array `a` e `b`. A questa funzione si applicano tutte le regole del calcolo matriciale, così come riassunto nella seguente tabella.

| Dimensionalità `a` | Dimensionalità `b` | Risultato |
| ---------------- | ----- | --------- |
| Monodimensionale (vettore) | Monodimensionale (vettore) | Prodotto scalare |
| Bidimensionale (matrice) | Bidimensionale (matrice) | Prodotto matriciale |
| Scalare | $n$-dimensionale | Prodotto scalare per array $n$-dimensionale |
| $n$-dimensionale | Scalare | Prodotto scalare per array $n$-dimensionale |

Notiamo che:

* in caso di moltiplicazione di due vettori, il risultato sarà il prodotto scalare;
* in caso di moltiplicazione di due matrici, il risultato sarà il prodotto matriciale e, di conseguenza, si consiglia di preferire la funzione [`matmul()`](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html);
* in caso di prodotto tra scalare e matrice, si consiglia di utilizzare la funzione [`multiply()`](https://numpy.org/doc/stable/reference/generated/numpy.multiply.html) o, in alternativa, l'operatore `*`.

Nel [notebook della lezione](https://github.com/anhelus/pcs-exercises/blob/master/01_libs/01_numpy_algebra.ipynb) vedremo alcuni esempi di prodotti matriciali.

!!!note "Moltiplicazione di array multidimensionali"
       Nel caso entrambi gli array da moltiplicare siano $n$-dimensionali, si applicano altre regole, che è possibile recuperare a [questo indirizzo](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot).

### Prodotto interno

Ricordiamo che per due generici vettori monodimensionali $a = [a_{1}, \ldots, a_{j}], b = [b_{1}, \ldots, b_{j}]$, entrambi a $j$ elementi, il *prodotto scalare*, o *prodotto interno*, è dato da:

$$
p = \sum_{i=1}^j a_{i} \cdot b_{i}
$$

Per calcolare il prodotto scalare tra i vettori `a` e `b` possiamo usare la funzione [`numpy.inner(a, b)`](https://numpy.org/doc/stable/reference/generated/numpy.inner.html):

```py
>>> a = np.array([1, 2, 3])
>>> b = np.array([4, 5, 6])
>>> np.inner(a, b)
32
```

#### Le Funzioni `inner()` e `dot()`

Un lettore attento avrà notato che, nella pratica, per vettori monodimensionali, le funzioni `inner()` e `dot()` restituiscono lo stesso risultato:

```py
np.inner(a, b)      # Output: 32
a.dot(b)            # Output: 32, stesso di b.dot()
```

La differenza tra le due funzioni è visibile quando si utilizzano array a dimensionalità maggiore di 1:

```py
>>> a = np.array([[1, 2], [3, 4]])
>>> b = np.array([[5, 6], [7, 8]])
>>> np.inner(a, b)   # Risultato con inner()
array([[17, 23],
      [39, 53]])
>>> a.dot(b)   # Risultato con dot()
array([[19, 22],
      [43, 50]])
```

In pratica, riprendendo la documentazione:

* per quello che riguarda la funzione `dot()`, questa è equivalente a `matmul()`, e quindi rappresenta una moltiplicazione matriciale che, nel caso di vettori monodimensionali, equivale al prodotto vettoriale, mentre per $n$ dimensioni è la somma dei prodotti tra l'ultima dimensione del primo vettore e delle dimensioni che vanno da $2$ ad $n$ del secondo;
* per quello che riguarda la funzione `inner()`, rappresenta il prodotto vettoriale nel caso ad una dimensione, mentre nel caso di $n$ dimensioni rappresenta la somma dei prodotti lungo l'ultima dimensione.

In altri termini:

```py
a.dot(b) == sum(a[i, :] * b[:, j])
np.inner(a, b) == sum(a[i, :] * b[j, :])
```

Andando a rapportare il tutto all'esempio precedente:

$$
dot = \left(\begin{array}{cc}
1 & 2\\
3 & 4
\end{array}\right)
\left(\begin{array}{cc}
5 & 6\\
7 & 8
\end{array}\right) = \\
= \left(\begin{array}{cc}
1 \cdot 5 + 2 \cdot 7 & 1 \cdot 6 + 2 \cdot 8   \\
3 \cdot 5 + 4 \cdot 7 & 1 \cdot 6 + 4 \cdot 8
\end{array}\right)
= \left(\begin{array}{cc}
19 & 22\\
43 & 50
\end{array}\right)
$$

$$
inner = \left(\begin{array}{cc}
1 & 2\\
3 & 4
\end{array}\right)
\left(\begin{array}{cc}
5 & 6\\
7 & 8
\end{array}\right) = \\
= \left(\begin{array}{cc}
17 & 23\\
39 & 53
\end{array}\right)
$$

### Prodotto esterno

Il *prodotto esterno* tra due vettori $a = [a_1, a_2, \ldots, a_j]$ e $b = [b_1, b_2, \ldots, b_j]$ è definito come la matrice $P$ tale per cui:

$$
P = \left[
	\begin{array}{ccc}
		a_1 \cdot b_1 & \ldots & a_1 \cdot b_n \\
		\vdots        & \ddots & \vdots        \\
		a_n \cdot b_1 & \ldots & a_n \cdot b_n
	\end{array}
\right]
$$

Per calcolarlo, NumPy ci mette a disposizione la funzione [`numpy.outer(a, b)`](https://numpy.org/doc/stable/reference/generated/numpy.outer.html).

Ad esempio:

```py
a = np.array([1, 2])
b = np.array([3, 4])

np.outer(a, b)
```

### La funzione `matmul`

Quando abbiamo parlato della funzione `dot()` abbiamo visto come sia possibile usarla per effettuare il prodotto matriciale tra le matrici `mat_1` e `mat_2`. Tuttavia, esiste un'altra possibilità, che è anche quella *consigliata*, ovvero usare la funzione [`numpy.matmul()`](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html):

```py
>>> a = np.array([[1, 2], [3, 4]])
>>> b = np.array([[5, 6], [7, 8]])
>>> np.matmul(a, b)
array([[19, 22],
       [43, 50]])
```

La funzione `matmul()` ha una differenza fondamentale rispetto alla funzione `dot()`, in quanto non accetta scalari come parametro (anche se è possibile passare vettori ed array $n$-dimensionali). Esiste in realtà un'altra differenza importante, che riguarda le operazioni $n$-dimensionali, ma che non tratteremo in questa sede.

!!!note "L'operatore `@`"
    L'operatore `@` è delegato alla moltiplicazione diretta di array bidimensionali, ed è utilizzato "sotto al cofano" dalla funzione `matmul()`.

## Potenza di matrice

La funzione [`np.linalg.matrix_power(a, n)`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_power.html) permette di elevare a potenza `n` della matrice `a`. Ad esempio:

```py
>>> linalg.matrix_power(a, 5)
array([[1069, 1558],
       [2337, 3406]])
```

## Autovalori ed autovettori

Per calcolare gli autovalori e gli autovettori di una matrice, NumPy ci mette a disposizione la funzione [`np.linalg.eig()`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eig.html), che restituisce gli autovalori e gli autovettori destri di una matrice quadrata:

```py
>>> (v, w) = linalg.eig(a)
>>> v
array([-0.37228132,  5.37228132])
>>> w
array([[-0.82456484, -0.41597356],
       [ 0.56576746, -0.90937671]])
```

Esistono anche altre funzioni per il calcolo degli autovalori ed autovettori. In particolare:

* [`np.linalg.eigh()`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigh.html) calcola gli autovettori e gli autovettori di una matrice simmetrica a valori reali o complessi;
* [`np.linalg.eigvals()`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigvals.html#) calcola gli autovalori di una matrice quadrata;
* [`np.linalg.eigvalsh()`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigvalsh.html#) calcola gli autovalori di una matrice simmetrica a valori reali o complessi.

## Norma, rango, determinante e traccia

La funzione [`np.linalg.norm(a)`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html) ci permette di calcolare la norma di una matrice. Opzionalmente, possiamo specificare tre parametri, ovvero:

* `ord`, che rappresenta l'ordine della norma da calcolare (di default, viene calcolata la norma di Frobenius);
* `axis`, che indica l'asse (o gli assi, in caso di array multidimensionale) su cui operare;
* `keepdims`, usata per restituire, opzionalmente, l'asse su cui viene calcolata la norma.

Per calcolare la norma di Frobenius della matrice `mat` possiamo usare questa sintassi:

```py
>>> linalg.norm(a)
5.477225575051661
```

Per calcolare determinante, rango e traccia di una matrice mediante le funzioni [`np.linalg.det()`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.det.html), [`np.linalg.matrix_rank()`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_rank.html) e [`np.trace()`](https://numpy.org/doc/stable/reference/generated/numpy.trace.html). Ad esempio:

```py
>>> linalg.det(a)
-2.0000000000000004
>>> linalg.matrix_rank(a)
2
>>> np.trace(a)
5
```

La `trace()` può anche essere usata per calcolare la sommatoria delle sovra/sotto diagonali specificando il parametro `offset`. Ad esempio:

```py
>>> mtrx = np.array([[ 5,  2,  9], [ 2,  3,  1], [ 4, -2, 12]])
>>> np.trace(mtrx, offset=1)
3
>>> np.trace(mtrx, offset=-1)
0
```

## Risoluzione di sistemi di equazioni lineari

Chiudiamo questa (*necessariamente* breve!) carrellata sulle operazioni di algebra lineare con la funzione [`np.linalg.solve(a, b)`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html), che permette di risolvere un sistema di equazioni lineari nel quale la matrice `a` è la matrice dei coefficienti, mentre il vettore `b` è il vettore dei termini noti. Ad esempio:

```py
>>> b = np.array([3, 2, 3])
>>> linalg.solve(mat, b)
array([-7.5,  4.5,  3.5])
```

Ovviamente, la matrice `a` deve essere quadrata, mentre il vettore `b` deve avere esattamente `n` elementi, con `n` ordine di `a`!

!!!note "Operazioni su tensori"
    NumPy mette a disposizione la versione per tensori ad $N$ dimensioni di alcune funzioni. In particolare, ricordiamo la funzione per il prodotto tensoriale ([`np.tensordot()`](https://numpy.org/doc/stable/reference/generated/numpy.tensordot.html#numpy.tensordot)) e quella per risolvere equazioni tensoriali ([`np.linalg.tensorsolve()`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.tensorsolve.html)).

## Reference

Come detto più volte, la nostra carrellata è stata inevitabilmente molto breve e limitata. Per una panoramica più completa, il consiglio è sempre quello di riferirsi all'[ottima documentazione di NumPy](https://numpy.org/doc/stable/reference/routines.linalg.html).
