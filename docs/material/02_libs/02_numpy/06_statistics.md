# 2.6 - Statistica in NumPy

!!!tip "Notebook di accompagnamento"
	Per questa lezione esiste un *notebook di accompagnamento*, reperibile a [questo indirizzo](https://github.com/anhelus/pcs-exercises/blob/master/01_libs/03_numpy_statistics.ipynb).

Oltre ai [polinomi](05_polynomials.md) ed alle [operazioni algebriche](04_algebra.md), NumPy ci mette a disposizione varie funzioni utili per i calcoli statistici; in questa lezione ne vedremo alcune.

## Minimo e massimo di un array

Per prima cosa, vediamo due funzioni utili a deterinare il valore massimo e minimo per un array, in particolare [`numpy.amax()`](https://numpy.org/doc/stable/reference/generated/numpy.amax.html) e [`numpy.amin()`](https://numpy.org/doc/stable/reference/generated/numpy.amin.html), che permettono di individuare il massimo lungo una particolare direzione di un array.

Ad esempio, se volessimo trovare il minimo ed il massimo di un vettore generato casualmente usando la funzione [`default_rng()`](https://numpy.org/doc/stable/reference/random/generator.html):

```py
>>> rng = np.random.default_rng(42)
>>> a = rng.integers(low=0, high=10, size=5)
>>> np.amin(a)
>>> np.amax(a)
```

Per una matrice, ed in generale per ogni array $N$-dimensionale, il procedimento da seguire è analogo:

```py
>>> b = rng.integers(low=0, high=10, size=(3, 3))
>>> np.amin(b)
>>> np.amax(b)
```

Se volessimo individuare il massimo ed il minimo sulle colonne di `b`, dovremmo specificare il parametro `axis`, che assumerà valore pari a `0`:

```py
>>> np.amin(b, axis=0)
>>> np.amax(b, axis=0)
```

Ovviamente, per trovare il minimo ed il massimo *per riga*, dovremo cambiare il valore di `axis` in `1`:

```py
>>> np.amin(b, axis=1)
>>> np.amax(b, axis=1)
```

Possiamo anche specificare una tupla per il valore del parametro `axis`; in tal caso, la ricerca del massimo o del minimo avverrà lungo tutti gli assi specificati dalla tupla. Ad esempio, specificando `(0, 1)`, effettueremo la ricerca del minimo (o del massimo) elemento nella matrice:

```py
>>> np.amin(b, axis=(0, 1))
>>> np.amax(b, axis=(0, 1))
```

!!!note "Le funzioni `argmax` ed `argmin`"
    Le funzioni [`numpy.argmax()`] e [`numpy.argmin()`] permettono di individuare l'*indice* del valore massimo e minimo, rispettivamente.

## Percentile e quantile

Ricordiamo che il *q-percentile* di un vettore $V$ di lunghezza $N$ è definito come il valore pari a $\frac{q}{100}$ calcolato a partire da una copia ordinata di $V$.

Per fare un esempio, supponiamo di avere un vettore ordinato di elementi che vanno da $1$ a $10$, e di calcolare il $50$-percentile mediante la funzione [`numpy.percentile()`](https://numpy.org/doc/stable/reference/generated/numpy.percentile.html) di NumPy.

```py
>>> a = np.arange(1, 11)
>>> np.percentile(a, 50)
```

Esistono diversi modi di calcolare il q-percentile; in tal senso, è opportuno consultare la [reference](https://numpy.org/doc/stable/reference/generated/numpy.percentile.html) e l'articolo [*Sample quantiles in statistical packages di Hyndman, R. J., & Fan, Y*](https://www.tandfonline.com/doi/abs/10.1080/00031305.1996.10473566).

In realtà, la funzione `percentile()` usa, per il $50$-percentile, il calcolo della mediana, per cui è equivalente alla funzione [`median()`](https://numpy.org/doc/stable/reference/generated/numpy.median.html). In questo caso specifico, avremo un discostamento dal risultato atteso, dovuto ad errori di interpolazione introdotti da NumPy:

```py
np.percentile(a, 50)
```

Il concetto di *quantile* è analogo a quello di percentile; tuttavia, in questo caso, non abbiamo a che fare con valori percentuali, bensì con valori normalizzati tra $0$ e $1$. Per cui, se usassimo la funzione [`numpy.quantile()`](https://numpy.org/doc/stable/reference/generated/numpy.quantile.html) come in precedenza:

```py
>>> np.quantile(a, .5)
```

Anche le funzioni `percentile()` e `quantile()` prevedono come argomento opzionale il parametro `axis`. Ad esempio:

```py
>>> np.percentile(b, 50, axis=0)
>>> np.percentile(b, 50, axis=1)
```

Come previsto, dando il valore `0` al parametro `axis` avremo il calcolo del percentile su ciascuna colonna, mentre passando il valore `1` avremo il calcolo del percentile su ciascuna riga.

## Media aritmetica e media pesata

Per il calcolo del valore medio di un array NumPy ci mette a disposizione due metodi. Il primo è la funzione [`numpy.average(a, weights)`](https://numpy.org/doc/stable/reference/generated/numpy.average.html), che viene usata per calcolare una media pesata degli elementi di `a` ponderati per gli elementi di `weights` (a patto che, ovviamente, le dimensioni dei due array siano coerenti).

Il calcolo che viene effettuato da NumPy con la funzione `average()` è quindi il seguente:

```py
>>> avg = sum(a * weights) / sum(weights)
```

Per cui, se volessimo assegnare un peso maggiore al primo ed al quarto elemento di un array `a` generato casualmente, potremmo fare come segue:

```py
>>> w = np.array([3, 1, 1, 3, 1])
>>> np.average(a, weights=w)
3.2222222222222223
```

Il risultato si discosta leggermente dalla semplice media, calcolata come:

```py
>>> np.average(a)
4.2
```

!!!tip "Suggerimento"
    Teniamo sempre a mente che la media è *ponderata* per la sommatoria dei valori assunti dai pesi!

La funzione [`numpy.mean(a)`](https://numpy.org/doc/stable/reference/generated/numpy.mean.html) è invece rappresentativa della media *aritmetica* degli elementi di un array, ed equivale alla funzione `average(a)` senza la specifica del vettore dei pesi. Ad esempio:

```py
>>> np.mean(a)
4.2
```

Concludiamo ricordando che anche in questo caso possiamo specificare il valore del parametro `axis`:

```py
>>> np.mean(b, axis=0)
array([6.33333333, 2.33333333, 6.        ])
>>> np.mean(b, axis=1)
array([4.66666667, 2.33333333, 7.66666667])
```

## Varianza e deviazione standard

Non possono mancare le funzioni [`numpy.std(a)`](https://numpy.org/doc/stable/reference/generated/numpy.std.html) e [`numpy.var(a)`](https://numpy.org/doc/stable/reference/generated/numpy.var.html), dedicate al calcolo della deviazione standard e della varianza di un vettore:

```py
>>> np.std(a)
2.4
>>> np.var(a)
5.76
```

Anche in questo caso, possiamo specificare gli assi lungo i quali effettuare l'operazione desiderata:

```py
>>> np.var(b, axis=0)
array([ 9.55555556, 10.88888889,  0.66666667])
>>> np.var(b, axis=1)
array([11.55555556,  4.22222222,  0.88888889])
```

## Istogramma

Un istogramma offre una visualizzazione grafica dei valori contenuti in un vettore, raggruppandoli all'interno di un certo numero di partizioni (*bin*).

Ad esempio, una possibile rappresentazione a due partizioni del vettore $A = [1, 2, 3, 4]$ è data dal vettore $[2, 2]$. Questo si spiega col fatto che le due partizioni suddividono il range di valori assunti da $A$ in due parti, con la prima inerente gli elementi $1$ e $2$, e la seconda gli elementi $3$ e $4$. Una volta calcolate le partizioni, queste andranno "riempite" contando il numero di elementi presenti in ciascuna partizione, il che ci riporta al vettore $[2, 2]$.

!!!note "Nota"
    Ovviamente, è possibile specificare, oltre al numero di partizioni, anche gli estremi delle stesse, che potrebbero non coincidere con quelli del vettore.

NumPy ci permette di ottenere l'istogramma di un vettore mediante l'insieme di funzioni [`numpy.histogram(a, bins, range)`](https://numpy.org/doc/stable/reference/generated/numpy.histogram.html), che ci permette di calcolare l'istogramma (monodimensionale) dell'array `a` in funzione del numero di partizioni (opzionale) e del range (opzionale). Ad esempio:

```py
>>> h, b = np.histogram(a)
```

In questo caso, abbiamo lasciato il valore di default di `bins`, ovvero 10.

Notiamo che la funzione `histogram()` restituisce due valori: il primo è dato dai valori assunti dall'istogramma (ovvero dal numero di elementi che ricade in ciascun bin), mentre il secondo è dato dai limiti di ogni bin.
