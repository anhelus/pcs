# E2 - Programmare in Python

## E2.1

Scriviamo una funzione che iteri fino a che il valore associato ad un contatore intero è minore di 10. Usiamo un ciclo `while`.

### S2.1 - Soluzione

```py
def itera_while():
    i=0
    while i < 10:
            i=i+1
            print("{}-ma iterazione".format(i))
```

Il risultato ottenuto sarà:

```py
>>> itera_while()
1-ma iterazione
2-ma iterazione
3-ma iterazione
4-ma iterazione
5-ma iterazione
6-ma iterazione
7-ma iterazione
8-ma iterazione
9-ma iterazione
10-ma iterazione
```

## E2.2

Scriviamo una funzione che iteri fino a che una condizione booleana non è `False`. Usiamo un ciclo `for`, ponendo come numero massimo di iterazioni 100 e se necessario, usando il metodo [`random.randint(a, b)`](https://docs.python.org/3/library/random.html#random.randint).

### S2.2 - Soluzione

```py
def itera_for():
    cond=True
    for i in range(100):
            eval = random.randint(-10, 10)
            print('Valuto numero {}'.format(eval))
            if eval < 0:
                    print('Esco')
                    cond=False
                    return cond
            else:
                    print('Continuo')
    return cond
```

Il risultato ottenuto sarà:

```py
>>> itera_for()
Valuto numero 6
Continuo
Valuto numero 7
Continuo
Valuto numero 8
Continuo
Valuto numero -4
Esco
False
```

## E2.3

Estraiamo tutti gli indici pari di una lista arbitraria di dieci elementi in ordine inverso. Per farlo, usiamo sia la funzione `range` sia lo slicing.

### S2.3 - Soluzione

```py
def estrai_con_slice(lista):
    if len(lista) != 10:
            print('Errore!')
            return []
    else:
            return lista[-2::-2]

def estrai_con_range(lista):
    if len(lista) != 10:
        print('Errore!')
        return []
    else:
        l_out = []
        for i in range(8, -1, -2):
            l_out.append(lista[i])
        return l_out
```

Il risultato ottenuto sarà:

```py
>>> l = [1,2,3,4,5,6,7,8,9,10]
>>> estrai_con_slice(l)
[10, 8, 6, 4, 2]
>>> estrai_con_range(l)
[10, 8, 6, 4, 2]
```
