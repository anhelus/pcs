**Esercizio**: Creiamo una funzione che concateni ad una lista il doppio dei singoli valori presenti nella stessa.

**Soluzione**: usiamo la funzione `append` per mettere in coda i nuovi elementi della lista.

```py
def raddoppia_lista(lista):
    for i in range(len(lista)):
        lista.append(lista[i] * 2)
    return print(lista)


l = [1,2]
raddoppia_lista(l) 			# Risultato atteso: [1, 2, 2, 4]
```

**Esercizio**: Creiamo una funzione che generi una lista di elementi casuali tra $0$ e $10$, usando un parametro *opzionale* per specificarne la lunghezza.

**Soluzione**: usiamo la funzione `append()` in accoppiata alla funzione `randint()`.

```py
import random
def genera_lista_casuale(lunghezza=5):
    l = []
    for i in range(lunghezza):
        l.append(random.randint(0, 10))
    return print(l)
...
genera_lista_casuale() 		# Possibile risultato: [3, 1, 2, 0, 6]
genera_lista_casuale(10)	# Possibile risultato: [7, 9, 1, 10, 2, 4, 9, 1, 4, 8]
```