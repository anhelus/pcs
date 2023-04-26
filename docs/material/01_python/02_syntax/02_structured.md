
# 1.2.2 - Programmazione strutturata

Come tutti i linguaggi derivati da C, anche Python offre il supporto ai principali costrutti della programmazione strutturata. Vediamoli brevemente.

## Istruzione condizionale

Partiamo dall'istruzione condizionale che, come in tutti i linguaggi di programmazione, è espressa dalle parole chiave `if` ed `else`.

La sintassi base è di questo tipo:

```py
if condizione_verificata:
	istruzioni
else:
	altre_istruzioni
```

In pratica, se `condizione_verificata` è vero, allora saranno eseguite le `istruzioni`. In alternativa, se `condizione_verificata` è falso, allora saranno eseguite le `altre_istruzioni`. Ad esempio:

```py
>>> if a < 5:
>>> 	print('a è minore di 5')
>>> else:
>>> 	print('a è maggiore di 5')
```

Per utilizzare la notazione `else if` dovremo ricorrere alla parola chiave `elif`. Ad esempio:

```py
>>> if a < 5:
>>> 	print('a è minore di 5')
>>> elif a == 5:
>>> 	print('a è uguale a 5')
>>> else:
>>> 	print('a è maggiore di 5')
```

!!!note "Switch/case in Python"
	Fino alla versione 3.10, Python non offriva un'implementazione per il costrutto `switch/case`. A partire da quest'ultima, però, è stato implementato il cosiddetto *pattern matching* mediante la sintassi `match/case`:
	> ```py
	  match command:
	      case "caso 1":
			  istruzioni()
		  case "altro caso":
			  print("Comando sconosciuto")
	  ```
	Approfondiremo questo costrutto nell'[apposita lezione]().

## Cicli

### Ciclo `for`

Il ciclo `for` itera su una *sequenza*, come una lista o una stringa, ed ha una sintassi del tipo:

```py
for elemento in sequenza:
	istruzioni()
```

Per fare un esempio, nel seguente blocco di codice vediamo come mostrare a schermo in maniera iterativa i numeri che vanno da 0 a 5 (escluso):

```py
vals = [0,1,2,3,4]
for i in vals:
    print(i)
```

Il risultato che sarà stampato a schermo è:

```bash
0
1
2
3
4
```

Rispetto ai linguaggi "classici", quindi, il ciclo `for` opera esclusivamente sugli *iterabili*, per cui potrebbe in qualche caso occorrere una riprogettazione del codice. Tuttavia, questa caratteristica di Python comporta anche una maggiore semplicità del codice; ad esempio, vediamo come è molto semplice iterare su una stringa:

```py
string = "Python"
for char in string:
    print(char)
```

A schermo vedremo in entrambi i casi il seguente risultato:

```bash
P
y
t
h
o
n
```

!!!warning "No free lunches!"
	Come ci ricorda il *no free lunches theorem*, **non esistono pasti gratuiti**! Infatti, la maggiore semplicità sintattica offerta da Python non è indolore, ma ha un costo. Uno script Python, infatti, per quanto ottimizzato, non potrà quasi mai offrire performance paragonabili ad un codice ottimizzato in C o C++, a meno di non usare particolari (ed avanzati) accorgimenti.

### Ciclo `while`

A differenza del ciclo `for`, il funzionamento del `while` è analogo a quello delle controparti negli altri linguaggi di programmazione. La sintassi generica è:

```py
while(condizione):
	istruzioni()
```

Ad esempio:

```py
import random
i = True
while (i):
    if random.randint(-5, 5) > 0:
        print("Continuo!")
    else:
        print("Esco!")
		i = False
```

Il codice nel blocco precedente non fa altro che generare un valore numerico intero casuale nell'intervallo $[-5, 5]$ mediante la funzione `randint`. Se tale valore è superiore a $0$, il ciclo continua, altrimenti si esce dallo stesso.

A schermo vedremo, ad esempio:

```bash
Continuo!
Continuo!
Esco!
```

!!!note "I valori booleani in Python"
	I più attenti avranno notato come i valori booleani in Python siano stati scritti come `True` e `False`. Questo non è un refuso: la prima lettera è proprio una maiuscola.

## La funzione `range()`

Riprendiamo adesso il ciclo `for` visto in precedenza.

```py
vals = [0, 1, 2, 3, 4]
for i in vals:
    print(i)
```

Nonostante il codice sia già compatto, scrivere manualmente la sequenza da iterare può facilmente diventare un'operazione abbastanza complessa. Python ci viene quindi in aiuto tramite la funzione `range(i, j, s)`, che genera una sequenza avente tutti i numeri compresi tra `i` (incluso) e `j` (escluso) a passo `s`. Ad esempio, per generare i numeri compresi tra 0 e 4 scriveremo:

```pycon
>>> r = range(0, 5, 1)
>>> print(list(r))
[0, 1, 2, 3, 4]
```

!!!note "Nota"
	Notiamo che per mandare in output i valori di `r` dovremo convertirlo in lista (`list(r)`).

Qualora omessi, `i` ed `s` assumono valori di default rispettivamente 0 ed 1:

```py
>>> r = range(5)
>>> print(list(r))
[0, 1, 2, 3, 4]
```

E' anche possibile specificare una sequenza *decrementale* ponendo `i > j` ed `s < 0`:

```py
>>> r = range(5, 1, -1)
>>> print(list(r))
[5, 4, 3, 2]
```

## Istruzioni `break` e `continue`

Le istruzioni `break` e `continue` permettono rispettivamente di *uscire dal ciclo* o di *saltare all'iterazione successiva*. Ad esempio:

```py
while (True):
    if randint(-5, 5) > 0:
        print("Continuo!")
		continue
    else:
        print("Esco!")
        break
print("Sono uscito!")
```

Le istruzioni precedenti *usciranno* dal ciclo quando viene generato casualmente un numero negativo, mentre continueranno ad iterare quando viene generato casualmente un numero positivo.
