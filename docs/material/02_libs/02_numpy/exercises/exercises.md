# Esercitazione 3 - NumPy

## Esercizi sugli array

!!!tip "Disponibilità soluzioni"
    Tutte le soluzioni sono disponibili in [questo notebook](./exercises.ipynb).

### Esercizio 3.1

Scrivere una funzione che restituisca il prodotto *riga per colonna* di due vettori `v1` e `v2`. Utilizzare in primis una list comprehension, verificando anche che la lunghezza dei due vettori sia coerente. Valutare inoltre il tempo necessario all'esecuzione.

Effettuare la stessa operazione in NumPy, valutando contestualmente il tempo necessario.

**Soluzione**: Definiamo innanzitutto la funzione `riga_per_colonna`, la quale accetta due array in ingresso e, se le dimensioni sono coerenti, effettua la moltiplicazione riga per colonna.

Una possibile forma per la funzione è la seguente:

```py linenums="1"
def riga_per_colonna(v1, v2):
	tic = time()
	if v1.shape[0] == 1:
		if v2.shape[1] == 1 and v1.shape[1] == v2.shape[0]:
			prod = sum([v1[0][i] * v2[i] for i in range(v2.shape[0])])
	elif v2.shape[0] == 1:
		if v1.shape[1] == 1 and v2.shape[1] == v1.shape[0]:
			prod = sum([v1[i] * v2[0][i] for i in range(v1.shape[0])])
	else:
		return 'Le dimensioni non sono coerenti!'
	toc = time()
	return prod, toc - tic
```

In particolare:

* alla riga 2, lanciamo il timer di inizio chiamata a funzione;
* alla riga 3, se il vettore `v1` è un vettore riga, allora andiamo a controllare che il vettore `v2` sia un vettore colonna;
* alla riga 4, se il controllo precedente è andato per il verso giusto, usiamo una list comprehension per fare il prodotto riga per colonna;
* alle righe 5-7, effettuiamo le operazioni duali alle precedenti;
* alla riga 10, lanciamo il timer di fine chiamata a funzione;
* alla riga 11, restituiamo il prodotto ed il tempo trascorso.

Proviamo la nostra funzione:

```py
v1 = np.array([[1,2,3,4]])
v2 = np.array([[1],[2],[3],[4]])

res, elapsed = riga_per_colonna(v1, v2)
print(elapsed)
```

L'equivalente operazione in NumPy è data da:

```py
res = np.dot(v1, v2)
```

## Esercizio E7.2.2

Scriviamo una funzione `crea_array(dim_1, dim_2, val_min, val_max)` che crei array di dimensioni arbitrarie `dim_1` $\times$ `dim_2` fatti di numeri interi casuali compresi tra `val_min` e `val_max`. Di default, la funzione dovrà creare dei vettori riga.

Provare ad effettuare la stessa operazione in NumPy.

### Soluzione S7.2.2

Ecco una possibile soluzione:

```py
import numpy as np
from random import randint

def crea_array(dim_1, dim_2=1, val_min=0, val_max=100):
	rows = [[randint(val_min, val_max) for i in range(dim_2)] for j in range(dim_1)]
	return np.array(rows)

a_1 = crea_array(4, 1)
a_2 = crea_array(2, 2)
```

Ovviamente, per NumPy ci basterà usare il metodo `randint`:

```py
from numpy import random

a_1 = random.randint(0, 100, (4, 1))
a_2 = random.randint(0, 100, (2, 2))
```
