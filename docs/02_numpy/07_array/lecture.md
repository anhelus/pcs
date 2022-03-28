# Introduzione agli array

Nella [scorsa lezione](./01_intro.md), abbiamo introdotto gli *array*, ovvero la struttura dati "centrale" all'interno dell'ecosistema di NumPy. In questa lezione e nelle successive ne approfondiremo gli aspetti e le caratteristiche principali.

## Array e liste

La prima impressione che si può avere è che gli array siano molto simili alle classiche liste. Esistono però alcune differenze, cui abbiamo già accennato nella scorsa lezione.

In linea di massima, però, è preferibile usare un array quando si ha a che fare con operazioni di tipo *matematico* su dati *omogenei*, ovvero dello stesso tipo. Questo è collegato essenzialmente a questioni di *ottimizzazione*: NumPy sfrutta per le operazioni matematiche del codice precompilato in C, ed inoltre gli array sono più compatti e veloci da utilizzare rispetto alle liste.

## La classe `ndarray`

Alle volte, ci si può riferire ad un array con il termine `ndarray`, abbreviazione che sta per $n$-dimensional array. Questa è, in realtà, la rappresentazione più generica degli array di NumPy, e permette di caratterizzare delle strutture dati con un numero arbitrario di dimensioni ($n$, per l'appunto).

!!!note "Vettori, matrici e tensori"
    Una struttura di tipo algebrico ad $n$ dimensioni, con $n > 2$, è detta *tensore*. Se $n = 1$, abbiamo un *vettore*, mentre con $n = 2$ abbiamo una *matrice*.

## Creazione ed inizializzazione

Il primo passo per utilizzare un `ndarray` è, ovviamente, crearlo! Per farlo, ci sono diversi metodi, ma il più semplice è sicuramente quello di passare al metodo `array()` di NumPy una lista di elementi. Ad esempio:

```py
>>> a = np.array([1, 2, 3, 4, 5, 6])
>>> a
array([1, 2, 3, 4, 5, 6])
```

Possiamo passare anche una "lista di liste", in modo da ottenere un array multidimensionale:

```py
>>> b = np.array([[1, 2, 3], [4, 5, 6]])
>>> b
array([[1, 2, 3],
       [4, 5, 6]])
```

Gli array non sono necessariamente numerici. Possiamo, ad esempio, creare un array di stringhe:

```py
>>> c = np.array(["s1", "s2"])
>>> c
array(['s1', 's2'], dtype='<U2')
```

### Array eterogenei

Abbiamo già detto che gli array, a differenza delle stringhe, devono contenere dati *omogenei*, ovvero dello stesso tipo. Cosa succede se proviamo a passare al metodo `numpy.array()` una lista composta da dati di tipo differente? Facciamo un esempio.

```py
>>> d = np.array([1, 1.])
>>> d
array([1., 1.])
```

Abbiamo passato al metodo `array()` un valore intero ed un float. Possiamo notare che è stato effettuato un *casting* in maniera implicita, e *tutti* i valori passati sono stati convertiti in float. Vediamo cosa accade se provassimo a passare un intero ed una stringa.

```py
>>> e = np.array([1, "s3"])
>>> e
array(['1', 's3'], dtype='<U11')
```

Anche in questo caso, è stata effettuata la conversione dei dati in automatico, passando stavolta da intero a stringa.

La regola da tenere a mente, ad ogni modo, è che NumPy (e, in generale, Python) seguono il principio dell'*upcasting*: in altre parole, quando deve essere fatta una conversione tra diversi tipi di dati, si farà in modo da convertire tutte le variabili nel tipo *a più alta precisione*, allo scopo di evitare perdite di informazioni.

## Il numero di elementi di un array

Abbiamo detto che un array è un "contenitore", a dimensione prefissata, per oggetti di un ben determinato tipo e dimensione. Il numero di dimensioni e gli oggetti contenuti all'interno di un array sono definiti a partire da una proprietà chiamata `shape`, liberamente traducibile in "forma". Quest'ultima è una tupla di numeri interi, ovviamente non negativi, che permette di determinare la dimensionalità dell'array lungo ogni *asse* (ovvero $x$, $y$, $z$, etc.).

Ad esempio, potremo dire che il seguente array bidimensionale ha due assi, il primo di lunghezza due, il secondo di lunghezza tre:

```py
>>> a = np.array([[1,2,3],[4,5,6]])
>>> a
array([[1, 2, 3],
       [4, 5, 6]])
```

Proviamo a valutare la proprietà `shape` del precedente array:

```py
>>> a.shape
(2, 3)
```

## Conclusioni

In questa lezione, abbiamo dato una breve panoramica introduttiva sugli array. Nella [prossima lezione](./03_costruzione.md), approfondiremo ulteriormente le loro modalità di creazione ed indicizzazione.


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
array([[0.00000000e+000, 0.00000000e+000, 0.00000000e+000],
       [0.00000000e+000, 0.00000000e+000, 1.67982320e-321],
       [5.96555652e-302, 1.14188703e-104, 9.91401238e-278]])
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
    In questo caso, notiamo come non si possa passare una tupla o una lista per indicare le dimensioni dell'array. Tuttavia, possiamo specificare sia il numero delle righe (con il primo parametro) che il numero delle colonne (con il secondo parametro).

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

