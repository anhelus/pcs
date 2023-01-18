## 1.3 - Calcoli e numeri

Proviamo ad usare l'interprete come una semplice calcolatrice; per farlo, scriviamo direttamente dopo il simbolo `>>>` le operazioni che vogliamo eseguire, e premiamo il tasto `Invio`. Ad esempio:

```py
>>> 2 + 2
4
>>> 3 * 5
15
>>> 10 - 2 * 4
2
```

### Divisioni

Le divisioni restituiscono sempre un numero in virgola mobile. Ad esempio:

```py
>>> 16 / 3
5.333333333333333
>>> 2 / 2
1.0
```

Proviamo ora ad usare altri due operatori, molto simili al classico operatore di divisione:

```py
>>> 16 // 3
5
>>> 16 % 3
1
```

Notiamo come in questi casi siano restituiti dei numeri interi. Il perché è presto detto: gli operatori `//` e `%` calcolano, rispettivamente, il *quoziente* ed il *resto* della divisione e, come sappiamo, entrambi sono dei valori interi.

### 1.3.2 - Elevazione a potenza

Per elevare un numero a potenza, è necessario usare l'operatore `**`, in cui l'operando sinistro è la base, mentre quello destro l'esponente:

```py
>>> 3 ** 2
9
>>> 2 ** 8
256
```

!!!note "Tipi numerici in Python"
	Abbiamo finora parlato soltanto di numeri interi e decimali; tuttavia, Python supporta anche altri tipi, come ad esempio `Decimal` e `Fraction`. E' inoltre presente un supporto nativo ai numeri complessi, esprimibili usando il suffisso `j` per indicare la parte immaginaria.