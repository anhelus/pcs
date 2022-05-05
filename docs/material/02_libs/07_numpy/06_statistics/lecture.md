# 7.6 - Statistica in NumPy

NumPy ci mette a disposizione diverse funzioni per il calcolo statistico. Vediamone assieme una breve carrellata. 

## 7.6.1 - Minimo e massimo di un array

Partiamo con due funzioni che possono essere utili per determinare il valore massimo ed il valore minimo di un array `a`, ovvero `amin(a)` ed `amax(a)`. Entrambe queste funzioni accettano (opzionalmente) un valore per il parametro `axis`, indicante al solito la direzione lungo la quale viene effettuata l'operazione.

Ad esempio, se volessimo trovare il minimo ed il massimo di un vettore generato casualmente:

```py
rng = np.random.default_rng(42)
a = rng.integers(low=0, high=10, size=5)
np.amin(a)
np.amax(a)
```

!!!tip "Attenzione"
    Nel codice precedente abbiamo usato la funzione `default_rng` del package `random` di NumPy per generare un vettore di numeri casuali.

Per una matrice, ed in generale per ogni array N-dimensionale, il procedimento da seguire è analogo:

```py
b = rng.integers(low=0, high=10, size=(3, 3))
np.amin(b)
np.amax(b)
```

Immaginiamo adesso di voler trovare il minimo ed il massimo *per colonna* per `b`. Al solito, specifichiamo il parametro `axis`, che assumerà valore pari a `0`:

```py
np.amin(b, axis=0)
np.amax(b, axis=0)
```

Ovviamente, per trovare il minimo ed il massimo *per riga*, dovremo cambiare il valore di `axis` in `1`:

```py
np.amin(b, axis=1)
np.amax(b, axis=1)
```

Possiamo anche specificare una tupla per il valore del parametro `axis`; in tal caso, la ricerca del massimo o del minimo avverrà lungo tutti gli assi specificati dalla tupla. Ad esempio, specificando `(0, 1)`, effettueremo la ricerca del minimo (o del massimo) elemento nella matrice:

```py
np.amin(b, axis=(0, 1))
np.amax(b, axis=(0, 1))
```

## 7.6.2 - Percentile e quantile

Ricordiamo che il *q-percentile* di un vettore $V$ di lunghezza $N$ è il valore sotto il quale ricade il $q$% degli elementi di $V$.

Per fare un esempio, supponiamo di avere un vettore ordinato di elementi che vanno da 1 a 10:

```py
a = np.arange(1, 11)
```

Possiamo calcolare il 50-percentile usando la formula classica, che ci dice che questo è pari a:

$$
n = \frac{q}{100} * N = \frac{50}{100} * 10 = 5
$$

In realtà, la funzione `percentile(a, q)` usa, per il 50-percentile, il calcolo della mediana, per cui è equivalente alla funzione `median(a)`. In questo caso specifico, avremo un discostamento dal risultato atteso, dovuto ad errori di interpolazione introdotti da NumPy:

```py
np.percentile(a, 50)
```

Il concetto di *quantile* è analogo a quello di percentile; tuttavia, in questo caso, non abbiamo a che fare con valori percentuali, bensì con valori normalizzati tra 0 ed 1. Per cui, se usassimo la funzione `quantile(a, q)` come in precedenza:

```py
np.quantile(a, .5)
```

Anche le funzioni `percentile` e `quantile` prevedono come argomento opzionale il parametro `axis`. Ad esempio:

```py
np.percentile(b, 50, axis=0)
np.percentile(b, 50, axis=1)
```

Come previsto, dando il valore `0` al parametro `axis` avremo il calcolo del percentile su ciascuna colonna, mentre passando il valore `1` avremo il calcolo del percentile su ciascuna riga.

## 7.6.3 - Media aritmetica e media pesata

Per il calcolo del valore medio di un array NumPy ci mette a disposizione due metodi. Il primo è la funzione `average(a, weights)`, che viene usata per calcolare una media pesata degli elementi di `a` ponderati per gli elementi di `weights` (a patto che, ovviamente, le dimensioni dei due array siano coerenti). 

Il calcolo che viene effettuato da NumPy con la funzione `average` è quindi il seguente:

```py
avg = sum(a * weights) / sum(weights)
```

Per cui, se volessimo assegnare un peso maggiore al primo ed al quarto elemento di un array `a` generato casualmente, potremmo fare come segue:

```py
w = np.array([3, 1, 1, 3])
np.average(a, weights=w)
```

Il risultato si discosta leggermente dalla semplice media, calcolata come:

```py
np.average(a)
```

!!!tip "Suggerimento"
    Teniamo sempre a mente che la media è *ponderata* per la sommatoria dei valori assunti dai pesi!

La funzione `mean(a)` è invece rappresentativa della media *aritmetica* degli elementi di un array, ed equivale alla funzione `average(a)` senza la specifica del vettore dei pesi. Ad esempio:

```py
np.mean(a)
```

Concludiamo ricordando che anche in questo caso possiamo specificare il valore del parametro axis:

```py
np.mean(b, axis=0)
np.mean(b, axis=1)
```

## 7.6.4 - Varianza e deviazione standard

Non possono mancare le funzioni `std(a)` e `var(a)`, dedicate al calcolo della deviazione standard e della varianza di un vettore:

```py
np.std(a)
np.var(a)
```

Anche in questo caso, possiamo specificare gli assi lungo i quali effettuare l'operazione desiderata:

```py
np.var(b, axis=0)
np.var(b, axis=1)
```

## 7.6.5 - Matrice di covarianza

La *matrice di covarianza* è la matrice che racchiude tutti i *coefficienti di correlazione*, che ci permetteno di valutare come una certa variabile $x_i$ varia al variare di un'altra variabile $x_j$. 

In generale, esistono diversi tipi di coefficienti di correlazione; il più semplice è quello di Pearson, che stima una correlazione di tipo *lineare* (ovvero, è tanto più alto quanto le due variabili crescono secondo un rapporto lineare), ed è quello usato dalle funzioni `cov(a)` e `corrcoef(a)`, la seconda delle quali riporta i valori normalizzati dei risultati ottenibili anche con la prima. In questo caso, `a` può essere monodimensionale o bidimensionale, ma ogni *riga* di `a` rappresenta una *variabile*, mentre ogni *colonna* rappresenta una *osservazione*.

Facciamo qualche esempio. Immaginiamo di avere due variabili che assumono rispettivamente valori `[1, 2, 3]` e `[4, 5, 6]`. In questo caso, è evidente come la correlazione sia massima, in quanto le osservazioni della seconda variabile hanno un semplice *offset* (o *bias*) rispetto a quelle della prima. Proviamo a calcolare la matrice di correlazione:

```py
x = np.array([[1, 2, 3], [4, 5, 6]])
np.cov(x)
np.corrcoef(x)
```

Notiamo che, dato che i coefficienti di correlazione assumono valore pari ad 1, le due variabili sono fortemente correlate tra loro. Se invece avessimo una situazione di questo tipo:

```py
>>> x = np.array([[1, 2, 3], [-1, -2, -3]])
>>> np.cov(x)
array([[ 1., -1.],
       [-1.,  1.]])
>>> np.corrcoef(x)
array([[ 1., -1.],
       [-1.,  1.]])
```

In questo caso, è evidente come le variabili siano *anticorrelate*, il che significa che quando la prima sale, la seconda scende, e viceversa.

Per apprezzare le differenze tra le funzioni `cov` e `corrcoef`, dobbiamo usare valori differenti (e non banali) per `x`. Ad esempio:

```py
>>> x = np.array([[2, 3, -1], [1, 5, 2], [4, 2, 2]])
>>> np.cov(x)
array([[ 4.33333333,  2.16666667,  0.66666667],
       [ 2.16666667,  4.33333333, -1.66666667],
       [ 0.66666667, -1.66666667,  1.33333333]])
>>> np.corrcoef(x)
array([[ 1.        ,  0.5       ,  0.2773501 ],
       [ 0.5       ,  1.        , -0.69337525],
       [ 0.2773501 , -0.69337525,  1.        ]])
```

In sostanza, `corrcoef` restituisce la matrice dei coefficienti $R$, la cui relazione con la matrice di covarianza $C$ restituita da `cov` è:

$$
R_{ij} = \frac{C_{ij}}{\sqrt{C_{ii} * C_{jj}}}
$$

## 7.6.6 - Istogramma

Un istogramma offre una visualizzazione grafica dei valori contenuti in un vettore, raggruppandoli all'interno di un certo numero di partizioni (*bin*).

Ad esempio, una possibile rappresentazione a due partizioni del vettore $A = [1, 2, 3, 4]$ è data dal vettore $[2, 2]$. Questo si spiega col fatto che le due partizioni suddividono il range di valori assunti da $A$ in due parti, con la prima inerente gli elementi $1$ e $2$, e la seconda gli elementi $3$ e $4$. Una volta calcolate le partizioni, queste andranno "riempite" contando il numero di elementi presenti in ciascuna partizione, il che ci riporta al vettore $[2, 2]$.

!!!note "Nota"
    Ovviamente, è possibile specificare, oltre al numero di partizioni, anche gli estremi delle stesse, che potrebbero non coincidere con quelli del vettore.

NumPy ci permette di ottenere l'istogramma di un vettore mediante l'insieme di funzioni `histogram(a, bins, range)`, che ci permette di calcolare l'istogramma (monodimensionale) dell'array `a` in funzione del numero di partizioni (opzionale) e del range (opzionale). Ad esempio:

```py
h, b = np.histogram(a)
```

In questo caso, abbiamo lasciato il valore di default di `bins`, ovvero 10.

!!!note "Nota"
	Notiamo che la funzione `histogram` restituisce due valori: il primo è dato dai valori assunti dall'istogramma (ovvero dal numero di elementi che ricade in ciascun bin), mentre il secondo è dato dai limiti di ogni bin.
