# 1.1.1 - Introduzione al Python

Prima di iniziare a parlare del linguaggio Python, è opportuno verificare che l'interprete sia installato nel nostro sistema. Per farlo, apriamo un terminale (Shell o Command Prompt, a seconda del nostro sistema), e scriviamo:

```sh
python
```

Se apparirà una schermata simile a quella mostrata in figura 1, Python sarà già correttamente installato sul nostro sistema.

<figure markdown>
  ![interpreter](./images/python_interpreter.png)
  <figcaption>Figura 1 - Interprete Python</figcaption>
</figure>

In alternativa, dovremo provvedere ad installarlo seguendo la procedura indicata sul [sito ufficiale](https://www.python.org/), ed aggiungerlo al path di sistema.

## Python e tipizzazione

### Tipizzazione dinamica

Python è un linguaggio *interpretato* ed a *tipizzazione dinamica*. In breve, questo significa che l'interprete valuta il tipo di ciascuna variabile a runtime, e che questo può cambiare durante l'esecuzione del programma.

Ma, a conti fatti, in cosa si traduce per il programmatore? Beh, molto semplice.

Immaginiamo di dover definire ed inizializzare una variabile di tipo intero in un linguaggio a tipizzazione *statica*, come ad esempio il C++. Per farlo, scriveremo qualcosa simile a:

```c++
int var = 0;
```

In Python, potremo omettere il tipo, che sarà inferito direttamente dal valore assegnato alla variabile:

```py
var = 0
```

Immaginiamo ora che la nostra variabile debba diventare un decimale. In C++, dovremo effettuare il casting:

```c++
float fVar = float(var);
fVar + 1.1;
```

In Python questo non sarà necessario, e potremo effettuare direttamente le operazioni desiderate:

```py
var + 1.1			# Il risultato sarà 1.1
```

Questo può apparentemente semplificare di molto la vita, in quanto non è più necessario preoccuparsi del tipo della variabile. Non è però tutto oro ciò che luccica: per comprenderlo, infatti, è il momento di parlare del (pilatesco) principio del *duck typing*.

#### Duck Typing

Il duck typing è riassumibile nella seguente massima:

!!!quote "Duck Typing"
	*If it walks like a duck and it quacks like a duck, then it must be a duck.*

che in italiano suona più o meno *Se cammina come un papero, e starnazza come un papero, deve essere un papero*. Traduciamola brevemente in "informatichese". 

Immaginiamo di istruire il nostro interprete Python ad assegnare alla nostra variabile `var` il valore di `1`. L'interprete nota che la variabile si "comporta" come un numero intero, e quindi "stabilirà" che si tratti proprio di questo.

Proviamo ora a sommare a `var` un valore pari ad `1.1`. Il risultato, come ovvio, sarà un numero decimale, e quindi l'interprete "cambierà idea", in quanto i comportamenti assunti da `var` sono adesso assimilabili ad una variabile di tipo `float`.

L'utilità del duck typing è evidente: permette allo sviluppatore di "risparmiare" numerose operazioni di cast, rendendo il codice più semplice da scrivere e manutenere. Tuttavia, occorre tenerne conto nel momento in cui si usano classi ed oggetti, in quanto l'interprete proverà ad inferire ed usare automaticamente un tipo in base al contesto in cui viene usata la variabile, con le comodità (ed i potenziali disastri) che questo comporta.

## Tipi built-in in Python

Python prevede una [serie](https://docs.python.org/3/library/stdtypes.html) di tipi *built-in*, ovvero nativamente disponibili nel linguaggio. Ne esiste un gran numero; tuttavia, quelli che ci troveremo più frequentemente ad utilizzare sono riassunti in tabella 1.

| Tipo | Descrizione | Esempio |
| ---- | ----------- | ------- |
| [`int`](https://docs.python.org/3/library/functions.html#int) | Numeri interi | `1` |
| [`float`](https://docs.python.org/3/library/functions.html#float) | Numeri decimali | `1.0` |
| [`complex`](https://docs.python.org/3/library/functions.html#complex) | Numeri complessi | `1 + 1j` |
| [`list`](https://docs.python.org/3/library/stdtypes.html#list) | Liste di oggetti | `[1, 'pippo', [1, 2, 3]]` |
| [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple) | Tuple di oggetti | `(1, 'pippo', [1, 2, 3])` |
| [`str`](https://docs.python.org/3/library/stdtypes.html#str) | Stringhe | `'pippo'` |
| [`set`](https://docs.python.org/3/library/stdtypes.html#set) | Insiemi | `{1, 2, 3}` |
| [`dict`](https://docs.python.org/3/library/stdtypes.html#dict) | Dizionari | `{'a': 1, 2: 'b'}` |

Nella [prossima lezione](./02_operators.md), vedremo alcuni tra gli operatori più comunemente utilizzati sui dati di tipo numerico.
