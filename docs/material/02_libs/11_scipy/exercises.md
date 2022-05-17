# Risoluzione degli esercizi

1. Scrivere due funzioni tali che:
    * la prima restituisca un booleano se una matrice passata in ingresso è invertibile;
    * la seconda inverta la matrice in base ai risultati della funzione precedente.
Usare SciPy.

```py
from scipy import linalg

def invertibile(mat):
	if linalg.det(mat) != 0.:
		return True
	else:
		return False


def inverti_se_invertibile(mat):
	if invertibile(mat):
		return linalg.inv(mat)
	else:
		return None
```