# 1.2 - Operatori aritmetici e logici

Come brevemente accennato nella [scorsa lezione](01_intro.md), vediamo di seguito quelli che sono gli operatori aritmetici e logici, e come possono essere utilizzati sui tipi numerici di base.

## Operatori aritmetici

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

### Sommario

Terminiamo questa sezione con un breve sommario dei diversi tipi di operatore aritmetico, e degli effetti che hanno sulle variabili di tipo numerico.

| Operatore | Descrizione | Esempio | Risultato |
| --------- | ----------- | ------- | --------- |
| `+` | Somma | `1 + 1` | `2` |
| `-` | Sottrazione | `1 - 1` | `0` |
| `*` | Moltiplicazione | `2 * 1` | `2` |
| `**` | Elevazione a potenza | `2 ** 3` | `8` |
| `/` | Divisione | `2 / 1` | `2` |
| `//` |  Quoziente | `4 // 3` | `1` |
| `%` | Modulo | `5 % 3` | `2` |

## Operatori logici

Gli operatori logici permettono di implementare le operazioni base dell'[algebra booleana](https://it.wikipedia.org/wiki/Algebra_di_Boole).

In tal senso, è opportuno riassumere brevemente i principi e le operazioni alla base di questo tipo di algebra.

1. Nell'algebra booleana, le variabili possono assumere solo due possibili valori: *vero*, o $1$, e *falso*, o $0$.
2. Combinando i valori di più variabili, è possibile valutare condizioni più o meno complesse partendo dalle operazioni $AND$, $OR$ e $NOT$.
3. I valori assunti da una condizione sono esprimibili mediante le tabelle di verità.

!!!warning "L'operazione XOR"
	Esiste una quarta operazione fondamentale, la *XOR*, che però non tratteremo in questa sede.

### Tabelle di verità delle operazioni logiche fondamentali

Vediamo brevemente le tabelle di verità per le tre operazioni logiche fondamentali descritte al punto $2$ del paragrafo precedente. Per ciascuna di queste tabelle, considereremo due variabili booleane $A$ e $B$, le quali potranno assumere valore $0$ o $1$. Nelle colonne $AND$ ed $OR$ saranno quindi riportati i risultati della rispettiva operazione logica.

| $A$ | $B$ | $AND$ | $OR$ |
| - | - | --- | -- |
| $0$ | $0$ | $0$ | $0$ |
| $0$ | $1$ | $0$ | $1$ |
| $1$ | $0$ | $0$ | $1$ |
| $1$ | $1$ | $1$ | $1$ |

In particolare, notiamo che il risultato dell'$AND$ è pari ad $1$ quando *entrambe* le variabili sono $1$; altrimenti, il risultato è $0$. Per quello che riguarda invece la $OR$, il risultato è $1$ quando *almeno una* delle variabili è pari ad $1$.

Trasponendo questo concetto nella verifica di una o più condizioni:

* un *AND* è vero se e solo se entrambe le condizioni sono vere;
* un *OR* è vero se e solo se almeno una delle condizioni è vera.

In ultimo, l'operazione $NOT$ agisce su un'unica variabile, negandola. Di conseguenza, la tabella di verità è riassumibile come segue:

| $A$ | $NOT$ |
| --- | ----- |
| $0$ | $1$ |
| $1$ | $0$ |

Di conseguenza, la $NOT$ di una condizione è vera se la condizione è falsa, e viceversa.

Facciamo un esempio pratico. Immaginiamo di voler verificare che un numero intero $x$ sia compreso tra $0$ e $10$. Ragionando mediante l'algebra booleana, potremo scrivere:

$$
cond_{min} = x < 10 \\
cond_{max} = x > 0 \\
res = cond_{min} AND cond_{max}
$$

In altri termini, il risultato finale ($res$) sarà vero se e solo se sia $cond_{min}$ e $cond_{max}$ sono vere.

### Operazioni logiche in Python

Per realizzare le operazioni logiche, Python ci mette a disposizione tre parole chiave, ovvero `and`, `or` e `not`. L'associazione tra parola chiave ed operazione logica è lasciata al lettore come esercizio.
