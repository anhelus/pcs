# Operazioni matriciali

La maggior parte delle operazioni matriciali possono essere svolte usando il package `linalg` di NumPy. Tutti gli esempi che faremo nel prosieguo, quindi, prevederanno l'importazione di questo package; facciamolo scrivendo l'opportuna istruzione `import`.

```py
from numpy import linalg
```

## Trasposta di una matrice

un'operazione comune è fare la trasporta delle nostre matrici. gli array numpy hanno la proprietà T che ci permette di trasporre una matrice.

si può anche dover cambiare le dimensioni di una matrice. questo può accadere quando, ad esempio, si ha un modello che si attende una certa forma di input che è diversa dal nostro dataset. questo è dove il meotodo reshape può essere utile. abbiamo infatti bisogno semplicemente di passare le nuove dimensioni che vogliamo per la matrice.

## Matrice inversa

Possiamo calcolare l'inversa di una matrice usando la funzione `inv(mat)` del package `linalg`, dove `mat` è la matrice da invertire. Ad esempio:

```py
>>> mat = np.array([[5, 0, 0], [0, 2, 0], [0, 0, 4]])
>>> mat_inv = linalg.inv(mat)
>>> mat_inv
array([[0.2 , 0.  , 0.  ],
       [0.  , 0.5 , 0.  ],
       [0.  , 0.  , 0.25]])
```

Ovviamente, la matrice `mat` deve essere invertibile. Nel caso passassimo una matrice rettangolare, infatti,verrebbe lanciato un `LinAlgError`:

```py
>>> mat = np.array([[1,2,3], [4,5,6]])
>>> linalg.inv(mat)
Traceback (most recent call last):
numpy.linalg.LinAlgError: Last 2 dimensions of the array must be square
```

Lo stesso accade per una matrice singolare:

```py
>>> mat = np.array([[1,1,1],[2,2,2],[0,0,1]])
>>> linalg.inv(mat)
Traceback (most recent call last):
numpy.linalg.LinAlgError: Singular matrix
```

!!!note "Curiosità"
	La matrice inversa che viene calcolata dalla funzione `inv()` è quella che, moltiplicata per la matrice iniziale, restituisce la matrice identità. Verifichiamolo:
	> ```py
	  >>> mat.dot(mat_inv)
	  array([[1., 0., 0.],
		  [0., 1., 0.],
		  [0., 0., 1.]])
	  ```

## Prodotti vettoriali e matriciali

### La funzione `dot()`

Abbiamo già visto nella [lezione precedente](./05_manipolazione.md) un esempio di uso della funzione `dot(a, b)`, utile a calcolare il prodotto matriciale tra gli array `a` ed `b`. Ovviamente, si applicano tutte le regole valevoli per il calcolo del prodotto matriciale (ovvero quello relativo alla moltiplicazione righe per colonne); riassumiamole nella seguente tabella sulla base delle dimensionalità di `a` ed `b`.

| Dimensionalità `a` | Dimensionalità `b` | Risultato | Note |
| ---------------- | ----- | --------- | ---- |
| Monodimensionale (vettore) | Monodimensionale (vettore) | Prodotto scalare | / |
| Bidimensionale (matrice) | Bidimensionale (matrice) | Prodotto matriciale | Preferire la funzione `matmul` |
| Scalare | N-dimensionale | Prodotto scalare per array N-dimensionale | Preferire la funzione `multiply(a, b)` o l'operatore `*` |
| N-dimensionale | Scalare | Prodotto scalare per array N-dimensionale | Preferire la funzione `multiply(a, b)` o l'operatore `*` |

Nel caso entrambi gli array siano N-dimensionali, si applicano altre regole che non approfondiremo in questa sede (è possibile recuperarle a [questo indirizzo](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot)).

### Prodotto interno

Possiamo usare la funzione `inner(a, b)` per calcolare il *prodotto interno* (o *scalare*) tra i vettori `a` e `b`:

```py
>>> np.inner(a, b)
11
```

### Prodotto esterno

Possiamo usare la funzione `outer(a, b)` per calcolare il *prodotto esterno* tra due vettori. In particolare, dati due vettori $a = [a_1, a_2, \ldots, a_n]$ e $b = [b_1, b_2, \ldots, b_n]$, il prodotto esterno è definito come la matrice $P$ tale che:

```py
P = [[a_1 * b_1 ... a_1*b_n],
	...,
	[a_n * b_1 ... a_n*b_n]]
```

Ad esempio:

```py
>>> np.outer(a, b)
array([[3, 4],
       [6, 8]])
```

### La funzione `matmul`

Quando abbiamo parlato della funzione `dot(a, b)` abbiamo visto come sia possibile usarla per effettuare il prodotto matriciale tra le matrici `mat_1` e `mat_2`. Tuttavia, esiste un'altra possibilità, che è anche quella *consigliata*, ovvero usare la funzione `matmul(a, b)`:

```py
>>> a = np.array([[1, 2], [3, 4]])
>>> b = np.array([[5, 6], [7, 8]])
>>> np.matmul(a, b)
array([[19, 22],
       [43, 50]])
```

La funzione `matmul()` ha una differenza fondamentale rispetto alla funzione `dot()`, in quanto non accetta scalari come parametro (anche se è possibile passare vettori ed array N-dimensionali). Esiste in realtà un'altra differenza importante, che riguarda le operazioni N-dimensionali, ma che non tratteremo in questa sede.

## Potenza di matrice

La funzione `linalg.matrix_power(a, n)` del package `linalg` permette di elevare a potenza `n` della matrice `a`. Ad esempio:

```py
>>> linalg.matrix_power(a, 5)
array([[1069, 1558],
       [2337, 3406]])
```

## Decomposizione di matrice

### Decomposizione QR

La *decomposizione* (o *fattorizzazione*) $QR$ di una matrice invertibile $A$ si definisce come il prodotto di una matrice ortogonale $Q$ è una matrice ortogonale per una matrice triangolare superiore $R$:

$$
A = QR
$$

!!!tip "Matrice ortogonale"
	Una matrice ortogonale è una matrice quadrata la cui inversa coincide con la trasposta.

NumPy ci offre un metodo per effettuare la decomposizione QR in un'unica istruzione mediante la funzione `qr(a)` del package `linalg`. Ad esempio:

```py
>>> (q, r) = linalg.qr(mat)
>>> q
array([[-0.74535599, -0.28151707, -0.60431166],
       [-0.2981424 , -0.67001063,  0.67985062],
       [-0.59628479,  0.68690166,  0.41546427]])
>>> r
array([[ -6.70820393,  -1.19256959, -14.16176386],
       [  0.        ,  -3.94686936,   5.03915561],
       [  0.        ,   0.        ,   0.22661687]])
```

Notiamo che il valore restituito dalla funzione è una tupla il cui primo elemento è la matrice $Q$, mentre il secondo è $R$.

## Decomposizione ai valori singolari

La *decomposizione ai valori singolari*, detta anche *SVD* (dall'inglese *Singular Value Decomposition*), è un tipo di fattorizzazione basato sul concetto di *autovalore* ed *autovettore*. In particolare, data una matrice $A$ di dimensioni $m \times n$, questa è decomponibile come segue:

$$
A = U \Sigma V^*
$$

dove $U$ è una matrice unitaria di dimensioni $m \times m$, $\Sigma$ è una matrice diagonale rettangolare di dimensioni $m \times n$, e $V^*$ è la trasposta coinugata di una matrice unitaria di dimensioni $n \times n$.

!!!tip "Trasposta coniugata"
	La trasposta coniugata di una matrice è ottenuta effettuandone la trasposizione e scambiando ogni elemento con il suo complesso coniugato.

Anche in questo caso, la SVD è estremamente complessa da implementare a partire dalle sue funzioni basilari. NumPy ci viene quindi in aiuto con la funzione `svd(mat)` del package `linalg`. Ad esempio:

```py
>>> (q, r) = linalg.qr(mat)
>>> q
array([[-0.74535599, -0.28151707, -0.60431166],
       [-0.2981424 , -0.67001063,  0.67985062],
       [-0.59628479,  0.68690166,  0.41546427]])
>>> r
array([[ -6.70820393,  -1.19256959, -14.16176386],
       [  0.        ,  -3.94686936,   5.03915561],
       [  0.        ,   0.        ,   0.22661687]])
>>> (u, s, v) = linalg.svd(mat)
>>> u
array([[-0.62732922, -0.48645199, -0.60813034],
       [-0.10481126, -0.72105629,  0.68490322],
       [-0.77166874,  0.49339871,  0.40135404]])
>>> s
array([16.33118238,  4.61369058,  0.07963155])
>>> v
array([[-0.39390556, -0.00157703, -0.91914956],
       [-0.41198638, -0.89361655,  0.17809178],
       [-0.82164812,  0.44882844,  0.35135082]])
```

## Autovalori ed autovettori

I concetti di autovalore ed autovettore hanno ampia applicazione in numerose discipline scientifiche, arrivando a definire la base su cui vengono elaborati alcuni degli approcci più avanzati al machine learning.

Formalmente, data una matrice quadrata $A$ di ordine $n$ con valori in uno spazio $\mathbb{K}$, uno scalare $\lambda_0 \in \mathbb{K}$ è definito *autovalore* di $A$ se esiste un vettore colonna non nullo $v_0 \in K^n$ tale che:

$$
Av = \lambda_0v
$$

Dal punto di vista "fisico", un autovettore non cambia la sua direzione a seguito dell'applicazione di una trasformazione lineare. Possiamo, ad esempio, ruotarlo, ma la sua direzione non verrà modificata; l'unico effetto che potremo notare sarà una modifica nel modulo o nel verso, a seconda del suo autovalore.

Per calcolare gli autovalori e gli autovettori di una matrice, NumPy ci mette a disposizione la funzione `eig(a)`, sempre appartenente al package `linalg`, che restituisce gli autovalori e gli autovettori destri di una matrice quadrata:

```py
>>> (w, v) = linalg.eig(mat)
>>> w
array([15.23391422,  0.08412242,  4.68196336])
>>> v
array([[-0.66930729, -0.82394712, -0.68445786],
       [-0.16856631,  0.44469209, -0.70619627],
       [-0.72361119,  0.35122656,  0.18111947]])
```

## Norma

La funzione `linalg.norm(a)` ci permette di calcolare la norma di una matrice. Opzionalmente, possiamo specificare tre parametri, ovvero:

* `ord`, che rappresenta l'ordine della norma da calcolare (di default, viene calcolata la norma di Frobenius);
* `axis`, che indica l'asse (o gli assi, in caso di array multidimensionale) su cui operare;
* `keepdims`, usata per restituire, opzionalmente, l'asse su cui viene calcolata la norma.

Per calcolare la norma di Frobenius della matrice `mat` possiamo usare questa sintassi:

```py
>>> linalg.norm(mat)
16.97056274847714
```

## Determinante, rango e traccia

Possiamo calcolare rapidamente determinante, rango e traccia di una matrice mediante le funzioni `det(a)`, `matrix_rank(a)` e `trace(a)`, quest'ultima **non** appartenente al package `linalg`. Ad esempio:

```py
>>> linalg.det(mat)
6.000000000000001
>>> linalg.matrix_rank(mat)
3
>>> np.trace(mat)
20
```

!!!note "Nota"
	La funzione `trace` può anche essere usata per calcolare la sommatoria delle sovra/sotto diagonali specificando il parametro `offset`. Ad esempio:
	> ```py
	  >>> mat
	  array([[ 5,  2,  9],
		  [ 2,  3,  1],
		  [ 4, -2, 12]])
	  >>> np.trace(mat, offset=1)
	  3
	  >>> np.trace(mat, offset=-1)
	  0
	  ```

## Risoluzione di sistemi

Chiudiamo questa (necessariamente breve!) carrellata sulle operazioni di algebra lineare con la funzione `solve(a, b)`, che permette di risolvere un sistema di equazioni lineari nel quale la matrice `a` è la matrice dei coefficienti, mentre il vettore `b` è il vettore dei termini noti. Ad esempio:

```py
>>> b = np.array([3, 2, 3])
>>> linalg.solve(mat, b)
array([-7.5,  4.5,  3.5])
```

!!!note "Nota"
	Ovviamente, la matrice `a` deve essere quadrata, mentre il vettore `b` deve avere esattamente `n` elementi, con `n` ordine di `a`!

## Conclusioni

In questa lezione, abbiamo visto come NumPy ci offra dei metodi per effettuare le operazioni base di algebra lineare in poche e semplici operazioni. Nella [successiva](./07_polinomi), vedremo i metodi che ci vengono dati per trattare i polinomi reali.

## Esercizi

1. Ricostruire una matrice $A$ a partire dalla sua decomposizione SVD.
