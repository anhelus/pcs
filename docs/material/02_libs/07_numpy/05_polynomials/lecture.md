# Il modulo `polynomial`

Il modulo `numpy.polynomial.polynomial` ci offre numerose classi e funzionalità per il trattamento dei polinomi. Vediamo insieme quali sono le principali.

## Operazioni tra polinomi

Immaginiamo di avere due diversi polinomi (cui non associeremo alcun significato fisico), ovvero:

$$
y = 2x + 1 \\
y = x^2 + 3x + 2
$$

Vediamo come usare dei metodi forniti dal modulo `polynomial` per effettuare delle operazioni su di loro.

### Addizione di polinomi

Per effettuare l'addizione di due polinomi, possiamo usare il metodo `polyadd(c1, c2)`, che accetta come parametri due vettori `c1` e `c2` che rappresentano, rispettivamente, i coefficienti del polinomio 1 e 2. Volendo sommare il primo ed il secondo polinomio, potremo scrivere:

```py
>>> import numpy.polynomial.polynomial as poly
>>> c1 = (0, 2, 1)
>>> c2 = (1, 3, 2)
>>> poly.polyadd(c1, c2)
array([1., 5., 3.])
```

che è il risultato atteso, ovvero $x^2 + 5x + 3$.

Notiamo come le dimensioni di `c1` e di `c2` debbano essere tra loro *coerenti*. Se infatti omettessimo il coefficiente $0$ al termine di secondo grado in `c1`, il risultato sarebbe il seguente:

```py
>>> c1 = (2, 1)
>>> poly.polyadd(c1, c2)
array([3., 4., 2.])
```

Ovviamente, il risultato precedente è errato.

### Sottrazione di polinomi

Possiamo poi sottrarre due polinomi usando la funzione `polysub(c1, c2)`, i cui parametri sono identici a quelli passati a `polyadd`:

```py
>>> poly.polysub(c2, c1)
array([1., 1., 1.])
```

### Moltiplicazione di polinomi

Le considerazioni precedenti possono essere banalmente traslate al caso della moltiplicazione tra polinomi, ottenibile mediante la funzione `polymul(c1, c2)`.

```py
>>> poly.polymul(c1, c2)
array([0., 2., 7., 7., 2.])
```

!!!note "Nota"
    Notiamo che il coefficiente del termine di quarto grado viene comunque riportato, nonostante questo sia pari a zero.

### Divisione tra polinomi

La divisione tra polinomi è un'operazione leggermente più complessa delle altre, e prevede l'uso della funzione `polydiv(c1, c2)`, che restituirà stavolta due array: il primo, `q`, rappresenta i coefficienti del polinomio quoziente, mentre il secondo, `r`, indica i coefficienti del polinomio resto.

Nel nostro caso:

```py
>>> (q, r) = poly.polydiv(c1, c2)
>>> q
array([0.5])
>>> r
array([-0.5,  0.5])
```

### Elevazione a potenza

Chiudiamo questa breve panoramica parlando dell'elevazione a potenza di un polinomio, effettuabile mediante la funzione `polypow(c, pow)`, con `c` vettore dei coefficienti, e `pow` potenza a cui elevare:

```py
>>> poly.polypow(c1, 2)
array([0., 0., 4., 4., 1.])
```

Anche in questo caso, vengono riportati i termini pari a zero nei risultati.

## Visualizzazione di un polinomio

Il metodo che abbiamo usato finora per visualizzare i coefficienti di un polinomio è alquanto inefficace e poco rappresentativo. Possiamo quindi sfruttare la funzione `poly1d(p)` di NumPy, che ci offre un oggetto la cui rappresentazione è molto più simile a quella cui siamo abituati nella "realtà":

```py
>>> p = np.poly1d(c1)
>>> print(p)
2 x + 1
```

!!!tip "Suggerimento"
    Esistono diversi modi di sfruttare questa rappresentazione per mostrare a schermo i polinomi risultanti dalle operazioni che effettuiamo. Uno, banale, è convertire il polinomio risultante; altri invece prevedono l'utilizzo delle funzioni polinomiali di NumPy (e non del package `polynomial.polynomial`).

## Valutare un polinomio

Per valutare il valore $y$ assunto dal polinomio per un determinato valore di $x$, usiamo la funzione `polyval(x, p)`, che accetta come argomento un intero (o una lista di interi) `x` ed un polinomio `p`.

Se volessimo valutare il valore assunto da $y$ per $x \in [1, 2]$ sulla retta rappresentata dal polinomio `c1`, ad esempio, potremmo usare `polyval` come segue:

```py
>>> poly.polyval([1, 2], c1)
array([3., 8.])
```

## Derivata ed integrale di funzioni polinomiali

Concludiamo questa breve carrellata con due metodi in grado di calcolare, rispettivamente, la derivata e l'integrale di una funzione polinomiale.

Il metodo `polyder(p, m)`, infatti, permette di calcolare la derivata di ordine `m` del polinomio `p` (di default, `m=2`):

```py
>>> c1 = (2, 1)
>>> poly.polyder(c1)
array([1.])
```

!!!warning "Attenzione"
    Non inseriamo coefficienti "extra" usando `polyder` e `polyints`, in quanto potrebbero portare a risultati inattesi.

Il metodo duale è `polyint(p, m)`, che prevedibilmente calcola l'integrale di ordine `m` del polinomio `p`:

```py
>>> poly.polyint(c1)
array([0. , 2. , 0.5])
```

## Conclusioni

In questa lezione, abbiamo dato uno sguardo ad alcune delle funzioni per il trattamento dei polinomi messe a disposizione da NumPy. Nella prossima lezione, daremo uno sguardo ravvicinato alle funzioni statistiche.
