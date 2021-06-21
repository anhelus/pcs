# Risoluzione degli esercizi

1. Scriviamo una funzione `gestisci_eccezione` che accetta in ingresso un parametro intero. La funzione prova ad estrarne la radice quadrata, gestendo eventuali eccezioni.

```py
import math

def gestisci_eccezione(par):
	try:
		math.sqrt(par)
	except Exception as e:
		print('Eccezione: {}'.format(e))

gestisci_eccezione(4)
gestisci_eccezione('4')
```
