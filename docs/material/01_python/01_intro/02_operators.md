# 1.3 - Operatori aritmetici

## Operatori aritmetici di base

### Addizione, moltiplicazione e sottrazione

Proviamo ad usare l'interprete come una semplice calcolatrice; per farlo, scriviamo direttamente dopo il simbolo `>>>` le operazioni che vogliamo eseguire, e premiamo il tasto `Invio`. Ad esempio:

```py
>>> 2 + 2
4
>>> 3 * 5
15
>>> 10 - 2 * 4
2
```

### Divisione

Le divisioni restituiscono sempre un numero in virgola mobile. Ad esempio:

```py
>>> 16 / 3
5.333333333333333
>>> 2 / 2
1.0
```

!!!note "Valutare il tipo di una variabile"
	Per valutare il tipo di una variabile `a` possiamo usare la funzione `type()` cui passeremo la variabile come argomento. Ad esempio:
	> ```py
	  >>> a = 10
	  >>> type(a)
	  int
	  >>> b = 3.3
	  >>> type(b)
	  float
	  ```

#### Quoziente e resto di una divisione

Esistono due operazioni contestuali, ma distinte, rispetto alla classica divisione. In particolare, possiamo utilizzare l'operatore `//` per ottenere il quoziente della divisione. Ad esempio, provando a dividere `16` per `3` avremo un quoziente di `5`:

```py
>>> 16 // 3
5
```

L'operatore `%`, invece, restituisce il resto della divisione. Nel caso precedente, restituirà quindi `1`:

```py
>>> 16 % 3
1
```

!!!note "Aritmetica modulare"
	Va da sè che l'operatore `%` può essere usato per applicazioni di aritmetica modulare.

E' importante sottolineare come gli operatori `//` e `%` restituiscano dei valori interi.

### Elevazione a potenza

Per elevare un numero a potenza, è necessario usare l'operatore `**`, in cui l'operando sinistro è la base, mentre quello destro l'esponente:

```py
>>> 3 ** 2
9
>>> 2 ** 8
256
```

!!!note "Tipi numerici in Python"
	Abbiamo finora parlato soltanto di numeri interi e decimali; tuttavia, Python supporta anche altri tipi, come ad esempio `Decimal` e `Fraction`. E' inoltre presente un supporto nativo ai numeri complessi, esprimibili usando il suffisso `j` per indicare la parte immaginaria.

### TODO operatori logici