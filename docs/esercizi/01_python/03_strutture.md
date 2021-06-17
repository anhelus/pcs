# Risoluzione degli esercizi

1. Usiamo la list comprehension per generare una lista con tutti i numeri pari da 2 a 100.

```py
def genera_lista():
    l = [i for i in range(2, 101) if (i % 2 == 0)]
    return l

lista = genera_lista()
```

2. Usiamo la dict comprehension per associare alle prime cinque lettere dell’alfabeto i numeri che vanno da 1 a 5.

```py
def genera_dict():
    lettere = ['a', 'b', 'c', 'd', 'e']
    d = {lettere[i]:(i+1) for i in range(5)}
    return d

dizionario = genera_dict()
```

3. Scriviamo la funzione `lista_a_tupla()` che permetta di convertire una lista arbitraria in una tupla. Scriviamo poi la funzione duale, `tupla_a_lista()`. Entrambe le funzioni devono usare dei cicli.

```py
def lista_a_tupla(lista):
    t = ()
    for el in lista:
        t += (el,)
    return t

def tupla_a_lista(tupla):
    l = []
    for el in tupla:
        l += [el]
    return l
```
