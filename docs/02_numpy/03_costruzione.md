# Costruzione di un array

Nella lezione precedente abbiamo visto come sia possibile creare un array NumPy usando la funzione `np.array()`, che ci permette di crearlo a partire da una semplice lista:

```py
>>> a = np.array([1, 2, 3])
```

Volendo, però, possiamo usare anche il costruttore della classe `ndarray`, cui dovremo passare come minimo la `shape` desiderata:

```py
>>> a = np.ndarray([3,3])       # oppure a = np.ndarray(shape=(3,3))
>>> a
array([[0.00000000e+000, 0.00000000e+000, 0.00000000e+000],
       [0.00000000e+000, 0.00000000e+000, 3.02368175e-321],
       [6.69431255e+151, 1.68534231e+246, 6.69431467e+151]])
```

!!!note "Nota"
    I numeri con cui viene "riempito" l'array sono casuali, ed andranno definiti solo in seguito.

Al di là di questi metodi base, esistono altri modi per costruire tipi di array ben specifici. Vediamoli brevemente.

## Costruire un array: alcuni modi alternativi

### Array con valori zero ed unitari

Possiamo creare un array di dimensioni arbitrarie in cui tutti gli elementi sono pari ad 1. Per farlo, usiamo la funzione `ones()`:

```py
>>> u = np.ones(shape=(3,3))
>>> u
array([[1., 1., 1.],
       [1., 1., 1.],
       [1., 1., 1.]])
```

In modo simile, possiamo creare array di dimensioni arbitrarie in cui tutti gli elementi sono pari a zero mediante la funzione `zeros()`:

```py
>>> z = np.zeros(shape=(3,3))
>>> z
array([[0., 0., 0.],
       [0., 0., 0.],
       [0., 0., 0.]])
```

### Array vuoti

Possiamo creare un array vuoto mediante la funzione `empty()`:

```py
>>> e = np.empty(shape=(3,3))
>>> e
array([[0., 0., 0.],
       [0., 0., 0.],
       [0., 0., 0.]])
```

Questa funzione può risultare utile quando vogliamo preallocare spazio per un array.

!!!note "Nota"
    I più attenti avranno notato che, in realtà, l'array generato da `empty()` non è vuoto, ma contiene valori casuali.

### Matrice identità

Possiamo creare una matrice identità usando la funzione `eye()`:

```py
>>> i = np.eye(3)
>>> i
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])
```

!!!warning "Attenzione" 
    In questo caso, notiamo come non si possa passare una tupla o una lista per indicare le dimensioni dell'array, ma soltanto un intero rappresentativo dell'ordine della matrice. Questo perché, *come ovvio*, le matrici identità *sono quadrate*.

### Matrici diagonali

La funzione `diag()` viene usata sia per *creare* una matrice diagonale a partire da un vettore (che, ovviamente, sarà poi la diagonale della matrice), sia per *estrarre* la diagonale di una matrice. Facciamo alcuni esempi.

#### Da vettore a matrice

Immaginiamo di avere un vettore riga a tre elementi.

```py
>>> x = np.array([5, 2, 3])
>>> x
array([5, 2, 3])
```

Possiamo creare una matrice diagonale passando questo vettore come argomento alla funzione `diag()`:

```py
>>> d = np.diag(x)
>>> d
array([[5, 0, 0],
       [0, 2, 0],
       [0, 0, 3]])
```

#### Da matrice a vettore

Affrontiamo adesso il problema duale. Immaginiamo di avere il seguente array, e volerne estrarre la diagonale:

```py
>>> x
>>> x
array([[5, 2, 2],
       [2, 1, 3],
       [4, 3, 6]])
```

Per farlo, dovremo anche questa volta usare la funzione `diag()`, passando però l'array:

```py
>>> d = np.diag(x)
>>> d
array([5, 1, 6])
```

!!!tip "Suggerimento"
    Il fatto che la funzione `diag()` sia usata per operazioni duali può, a ragione, causare confusione. Basta però ricordare che passando un vettore si ottiene una matrice, mentre passando una matrice si ottiene un vettore, ed il gioco è fatto.

!!!warning "Attenzione"
    La funzione `diag()` accetta solo input monodimensionali (vettori) e bidimensionali (matrici)!

### Matrici triangolari

Concludiamo questa breve carrellata mostrando due metodi in grado di estrarre la matrice triangolare, rispettivamente superiore ed inferiore.

Supponiamo di avere la matrice x definita in precedenza. Per estrarre la matrice triangolare superiore, dovremo usare la funzione `triu()`:

```py
>>> tu = np.triu(x)
>>> tu
array([[5, 2, 2],
       [0, 1, 3],
       [0, 0, 6]])
```

Per estrarre invece la matrice triangolare inferiore, dovremo usare la funzione `tril()`:

```py
>>> tl = np.tril(x)
>>> tl
array([[5, 0, 0],
       [2, 1, 0],
       [4, 3, 6]])
```

!!!tip "Suggerimento"
    In questo caso, le funzioni `tril()` e `triu()` possono tranquillamente essere applicate agli array n-dimensionali. Inoltre, non è richiesto che l'array sia quadrato.

## Conclusioni

In questa lezione, abbiamo visto alcuni metodi standard per la costruzione di un array in NumPy. Nella [prossima](./04_indicizzazione.md), vedremo come accedere ad uno o più elementi sulla base di specifiche condizioni.
