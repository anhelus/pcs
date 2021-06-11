# Risoluzione degli esercizi

1. Scriviamo una funzione che iteri fino a che il valore associato ad un contatore intero è minore di 10. Usiamo un ciclo `while`.

```py
>>> def itera_while():
...     i=0
...     while i < 10:
...             i=i+1
...             print("{}-ma iterazione".format(i))
...
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

2. Scriviamo una funzione che iteri fino a che una condizione booleana non è `False`. Usiamo un ciclo `for`, ponendo come numero massimo di iterazioni 100 e se necessario, usando il metodo [`random.randint(a, b)`](https://docs.python.org/3/library/random.html#random.randint).

```py
>>> def itera_for():
...     cond=True
...     for i in range(100):
...             eval = random.randint(-10, 10)
...             print('Valuto numero {}'.format(eval))
...             if eval < 0:
...                     print('Esco')
...                     cond=False
...                     return cond
...             else:
...                     print('Continuo')
...     return cond
...
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