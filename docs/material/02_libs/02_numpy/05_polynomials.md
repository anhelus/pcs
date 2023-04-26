# 2.2.5 - Operazioni polinomiali in NumPy

!!!tip "Notebook di accompagnamento"
	Per questa lezione esiste un *notebook di accompagnamento*, reperibile a [questo indirizzo](https://github.com/anhelus/pcs-exercises/blob/master/01_libs/01_numpy/02_polynomials.ipynb).

Come abbiamo visto nella [scorsa lezione](04_algebra.md), NumPy ci offre un'ampia gamma di funzioni per il calcolo matriciale. Tuttavia, è anche possibile utilizzarlo per altri scopi, non ultimo il calcolo polinomiale, mediante il modulo [`numpy.polynomial`](https://numpy.org/doc/stable/reference/routines.polynomials.html). Vediamo quindi alcuni tra i principali utilizzi di questo modulo.

## La classe `Polynomial`

Immaginiamo di avere due diversi polinomi, cui non associamo alcun significato fisico. I due sono espressi dalle seguenti equazioni:

$$
\begin{cases}
p_1: y = 2x + 1 \\
p_2: y = x^2 + 3x + 2
\end{cases}
$$

NumPy ci permette di rappresentare il polinomio mediante gli oggetti di classe [`Polynomial`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.html#numpy.polynomial.polynomial.Polynomial). In particolare, un oggetto di questo tipo può essere istanziato a partire dai coefficienti del polinomio (ma non solo). Ad esempio, considerando i polinomi visti in precedenza, assieme ai loro coefficienti, possiamo scrivere:

```py
>>> from numpy.polynomial import Polynomial
>>> p_1_coef = [2, 1]       # lista dei coefficienti per p_1
>>> p_2_coef = [1, 3, 2]    # lista dei coefficienti per p_2
>>> p_1 = Polynomial(p_1_coef[::-1])
>>> p_2 = Polynomial(p_2_coef[::-1])
```

!!!warning "Ordine dei coefficienti"
    La caratteristica più importante (e controintuitiva) della classe `Polynomial` (e di tutti i metodi di gestione dei polinomi in NumPy) è che i coefficienti vengono trattati *in ordine crescente*. In pratica, viene considerato innanzitutto il termine noto (ovvero il termine per $x^0$), poi il coefficiente di primo grado, quello di secondo, e così via. Per questo motivo, nel codice precedente viene considerata la lista dei coefficienti in ordine inverso.

## Somma di polinomi

Per sommare due polinomi, è possibile utilizzare il metodo [`polyadd()`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyadd.html#numpy.polynomial.polynomial.polyadd), il quale accetta come parametri due vettori `c1` e `c2` rappresentativi dei coefficienti dei due polinomi da sommare. Ad esempio, volendo sommare due polinomi, potremo scrivere:

```py
>>> from numpy.polynomial import polynomial as P
>>> c1 = [1, 2, 3]
>>> c2 = [2, 5, 1]
>>> poly_sum = P.polyadd(c1, c2)
```

Il risultato di questa operazione sarà un array numpy a valori `[3, 7, 4]`, equivalente al polinomio $4x^2 + 7x + 3$.

## Sottrazione di polinomi

La sottrazione tra due polinomi è possibile mediante la funzione [`polysub()`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polysub.html#numpy-polynomial-polynomial-polysub), il cui funzionamento è molto simile a quello di `polyadd()`, con l'ovvia differenza che il risultato sarà il polinomio risultante dalla differenza tra i coefficienti di `c1` e `c2`.

```py
>>> poly_sub = P.polysub(c1, c2)
```

## Moltiplicazione di polinomi

Le considerazioni precedenti possono essere estese alla moltiplicazione tra polinomi mediante la funzione [`polymul()`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polymul.html):

```py
>>> poly_mul = P.polymul(c1, c2)
```

Nel caso si debba moltiplicare un polinomio per una variabile indipendente $x$, andrà utilizzata la funzione [`polymulx()`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polymulx.html).

## Divisione tra polinomi

La divisione tra polinomi è un'operazione leggermente più complessa delle altre, e prevede l'uso della funzione [`polydiv()`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polymulx.html), che restituirà stavolta due array: il primo rappresenta i coefficienti del polinomio quoziente, mentre il secondo i coefficienti del polinomio resto. Ad esempio:

```py
>>> poly_q, poly_r = P.polydiv(c1, c2)
```

Anche in questo caso, i coefficienti sono ordinati da quello a grado più basso a quello a grado più alto.

## Elevazione a potenza

Per elevare a potenza un polinomio, possiamo usare la funzione [`polypow()`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polypow.html), la quale accetta due parametri: un vettore dei coefficienti `c` al primo argomento, ed uno scalare `pow` al secondo, rappresentativo della potenza alla quale effettuare l'elevazione. Ad esempio:

```py
>>> poly_pow = P.polypow(c1, 2)
array([0., 0., 4., 4., 1.])
```

## Valore assunto da un polinomio

Il valore $y$ assunto da un polinomio $p$ ad un certo valore di $x$ può essere determinato mediante la funzione [`polyval()`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyval.html), che accetta come argomento un intero (o una lista di interi) `x` ed un polinomio `p`. Ad esempio, volendo valutare il valore assunto da $y$ per $x \in [1, 2]$ sulla retta rappresentata dal polinomio `c1`:

```py
>>> P.polyval([1, 2], c1.coef)
```

!!!warning "Coefficienti e polinomio"
    E' molto importante notare come non stiamo usando un oggetto di classe `Polynomial`, ma i coefficienti dello stesso, estraibili accedendo alla proprietà `coef`.

!!!note "Operazioni a dimensionalità 2 e 3"
    Nel caso occorra valutare i polinomi nei casi a due e tre dimensioni, NumPy ci mette a disposizione le funzioni [`polyval2d()`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyval2d.html) e [`polyval3d()`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyval3d.html).
   

## Derivata ed integrale di funzioni polinomiali

Concludiamo questa breve carrellata con due metodi in grado di calcolare, rispettivamente, la derivata e l'integrale di una funzione polinomiale.

La funzione [`numpy.polyder()`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyder.html#numpy.polynomial.polynomial.polyder), infatti, permette di calcolare la derivata di ordine `m` (passato come secondo argomento, di default pari ad `1`) dei coefficienti del polinomio `p` (passati come primo argomento). Ad esempio, per calcolare la derivata di `c1`:

```py
>>> P.polyder(c1.coef)
```

Il metodo duale è [`numpy.polyint()`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyint.html#numpy.polynomial.polynomial.polyint), che (prevedibilmente) calcola l'integrale di ordine `m` dei coefficienti del polinomio `p`:

```py
>>> P.polyint(c1.coef)
```
