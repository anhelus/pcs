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

## Accesso agli elementi degli array

Il modo più immediato di accedere ad un elemento presente in un array è usare l'operatore `[]` assieme all'indice cui si vuole accedere, esattamente come avviene per le liste. Ad esempio, possiamo selezionare il primo elemento di un array mediante la seguente sintassi:

```py
>>> a = np.array([1,2,3,4])
>>> a[0]
1
```

Nel caso di array ad $n$ dimensioni, è necessario indicare l'indice per ciascuna delle dimensioni dell'array. Nel caso di un array bidimensionale, potremmo selezionare l'elemento alla prima riga e prima colonna con una sintassi di questo tipo:

```py
>>> b = np.array([[1,2], [3,4]])
>>> b[0][0]
1
```

Oltre al metodo "standard", è possibile usare una maschera di valori booleani. Nel prossimo esempio, selezioniamo tutti gli elementi della prima colonna dell'array:

```py
>>> mask = ([True, False], [True, False])
>>> b[mask]
array([1, 3])
```

Possiamo poi scegliere tutti gli elementi che soddisfano una determinata condizione logica o matematica:

```py
>>> mask = (b > 2)
>>> mask
array([[False, False],
       [ True,  True]])
>>> b[mask]
array([3, 4])
```

## Conclusioni

In questa lezione, abbiamo dato una breve panoramica introduttiva sugli array. Nella [prossima lezione](./03_build_indexing.md), approfondiremo ulteriormente le loro modalità di creazione ed indicizzazione.
