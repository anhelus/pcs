# Risoluzione degli esercizi

1. Scriviamo la funzione `crea_array(dim_1, dim_2)` che crea due array di elementi interi casuali, uno di dimensioni $4 \times 1$, ed uno di dimensioni $2 \times 2$. Se possibile, generalizzare i parametri accettati dalla funzione. Usare inoltre la funzione [`concatenate`](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate) per concatenare i diversi array.

```py
import numpy as np
from random import randint

def crea_array(dim_1, dim_2=1):
	if dim_2 == 1:
		# Array monodimensionale
		return np.array([randint(0, 100) for i in range(dim_1)])
	elif dim_2 > 1:
		# Array bidimensionale
		base = np.array([[randint(0, 100) for i in range(dim_1)]])
		for i in range(dim_2-1):
			base = np.concatenate((
				base,
				np.array([[randint(0, 100) for i in range(dim_1)]])), 
			axis=0)
		return base

a_1 = crea_array(4, 1)
a_2 = crea_array(2, 2)
```

2. Scriviamo la funzione array_a_tupla che salva i valori contenuti negli array precedenti in tuple di dimensioni $4 \times 1$. Usare la funzione [`flatten`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flatten.html); provare ad usare un’unica istruzione sfruttando il casting a tupla.

```py
def array_a_tupla(array):
	return tuple(array.flatten())

array_a_tupla(a_1)
array_a_tupla(a_2)
```
