# Risoluzione degli esercizi

1. Scriviamo la funzione `rettifica(array)`, che restituisce un array delle stesse dimensioni di quello in ingresso ma che porta tutti i valori negativi a 0.

```py
def rettifica(array):
    array[array < 0] = 0
    return array

rettifica(np.array([-1, 2, -3, 4]))
```

2. Scriviamo la funzione `asort(vect)` che restituisce un vettore riga ordinato in modo discendente.

```py
def asort(array):
    s = np.sort(array)
    return s[-1::-1]

asort(np.array([3, 2, 5, -1]))
```
