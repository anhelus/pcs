# 2 - Programmare in Python

## 2.1 - Alcuni concetti sintattici fondamentali

Oltre al duck typing, esistono altri concetti che caratterizzano la sintassi di Python. Vediamoli brevemente.

### 2.1.1 - Uso delle parentesi

1. Le **parentesi tonde** sono usate soltanto nel caso di chiamata a funzione, oltre che per esprimere la precedenza nelle operazioni. In tutti gli altri casi, sono opzionali e possono essere omesse. Ad esempio:

	```py
	a = 2
	b = 3
	c = 4
	r_1 = a + b * c 	# Valore restituito: 14
	r_2 = (a + b) * c	# Valore restituito: 20

	if a > 2:
		# Questa notazione è valida, ed è equivalente ad (a > 2)
	```
2. Le **parentesi quadre** sono usate per la creazione e l'accesso agli elementi di una struttura dati.

	```py
	# Creo una lista
	lista = [1, 2, 3]
	# Accedo al secondo elemento della lista
	lista[1]			# Il valore acceduto è 2
	```
3. Le **parentesi graffe** sono usate per la creazione di un dizionario.
	```py
	dizionario = {'a': 1, 'b': 2}
	# Notiamo che per accedere ad una chiave di un dizionario useremo comunque la parentesi quadra.
	dizionario[a]		# Il valore acceduto è 1, ovvero quello relativo alla chiave 'a'
	```

### 2.1.2 - Ambito e termine di un'istruzione

A differenza del C, che prevede che ogni istruzione sia terminata da un punto e virgola, Python prevede che un'istruzione termini quando si va a capo. Quindi:

```py
a = 1			# L'istruzione di assegnazione è terminata!
```

In altre parole, si può omettere il punto e virgola.

Per quello che riguarda invece la definizione di un ambito, ad esempio locale all'interno di una funzione, Python si affida ai *due punti*, che sostituiscono la parentesi graffa di apertura, ed al numero di *indentazioni*.

!!!tip "Ambito e indentazioni"
	In generale, possiamo dire che le istruzioni allo stesso livello di indentazione sono considerate dall'interprete Python come istruzioni appartenenti al medesimo ambito.

Quindi:

```py
# L'inizio della funzione, e quindi dell'ambito
# che questa delimita, è contrassegnato dai due punti
def funzione():	# Inizio ambito
	# Il codice deve essere allo stesso livello di indentazione
	a = 1
	a + 1
	# ...
	return 0
```

!!!tip "Le indentazioni"
	Per ottenere l'indentazione, occorre usare il tasto *tab* sulla tastiera, oppure quattro spazi. E' comunque *estremamente importante* non mescolare le due tecniche.

## 2.2 - Programmazione strutturata

Il linguaggio Python utilizza una sintassi per le strutture di controllo differente da quella usata nei tipici linguaggi C-like.

### 2.2.1 - Istruzioni condizionali (`if`)

Partiamo dall'istruzione condizionale `if`. Questa, in Python, ha una sintassi di questo tipo.

```py
if condizione:
	istruzioni()
elif altra_condizione:
	altre_istruzioni()
else:
	ultime_istruzioni()
```

Notiamo l'utilizzo della keyword `elif` come crasi della forma `else if` utilizzata in altri linguaggi di programmazione. Ad esempio, se volessimo verificare il valore di una variabile intera, potremmo scrivere:

```py
a = 5
if a < 5:
	print('a è minore di 5')
elif a == 5:
	print('a è uguale a 5')
else:
	print('a è maggiore di 5')
```

L'output di questo controllo sarà:

```bash
a è uguale a 5
```

### 2.2.2 - Pattern matching

Fino alla versione 3.10, Python non offriva il costrutto `switch/case`. A partire da quest'ultima, però, il *pattern matching* è stato implementato usando questa sintassi:

```py
match command:
	case "caso 1":
		istruzioni()
	case "altro caso":
		print("Comando sconosciuto")
```

### 2.2.3 - Cicli

#### 2.2.3.1 - Ciclo `for`

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

#### 2.2.3.2 - Ciclo `while`

A differenza del ciclo `for`, il funzionamento del `while` è analogo a quello delle controparti negli altri linguaggi di programmazione. La sintassi generica è:

```py
while(condizione):
	istruzioni()
```

Ad esempio:

```py
i = True
while (i):
    if randint(-5, 5) > 0:
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

## 2.4 - La funzione `range()`

Riprendiamo adesso il ciclo `for` visto in precedenza.

```py
vals = [0,1,2,3,4]
for i in vals:
    print(i)
```

Nonostante il codice sia già compatto, scrivere manualmente la sequenza da iterare può facilmente diventare un'operazione abbastanza complessa. Python ci viene quindi in aiuto tramite la funzione `range(i, j, s)`, che genera una sequenza avente tutti i numeri compresi tra `i` (incluso) e `j` (escluso) a passo `s`. Ad esempio, per generare i numeri compresi tra 0 e 4 scriveremo:

```py
r = range(0, 5, 1)
print(list(r))
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

**Esercizio**: Proviamo ad iterare su tutti i valori della lista `['Pippo', 'Pluto', 5, 'Paperino']`.

**Soluzione**: Usiamo la funzione `range()` assieme alla funzione `len()`:

```py
l = ['Pippo', 'Pluto', 5, 'Paperino']
for i in range(len(l)):
    print(l[i])
# Output
Pippo
Pluto
5
Paperino
```

In pratica, dato che la funzione `len(l)` ci restituisce il numero di elementi nella lista, ovvero $4$, stiamo andando a definire un range che va da 0 a 3. A questo punto, ci basterà *elemento per elemento* ai valori contenuti all'interno della lista, ed avremo ottenuto il risultato sperato.

## 2.5 - Istruzioni `break` e `continue`

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

## 2.6 - Definire una funzione

In Python è possibile definire una funzione in questo modo:

```py
def nome_funzione(parametri):
	# istruzioni
	return valore_ritorno
```

E' importante notare che:

* non è necessario definire un tipo, ma soltanto un *valore* di ritorno. Qualora la funzione non restituisca alcun valore, potrà essere omessa l'istruzione `return`;
* non è (strettamente) necessario definire il tipo di ciascuno dei parametri passati;
* è consentito inserire dei parametri *opzionali*, con valori di default.

**Esercizio**: Creiamo una funzione che concateni ad una lista il doppio dei singoli valori presenti nella stessa.

**Soluzione**: usiamo la funzione `append` per mettere in coda i nuovi elementi della lista.

```py
def raddoppia_lista(lista):
    for i in range(len(lista)):
        lista.append(l[i] * 2)
l = [1,2]
raddoppia_lista(l) 			# Risultato atteso: [1, 2, 2, 4]
```

**Esercizio**: Creiamo una funzione che generi una lista di elementi casuali tra $0$ e $10$, usando un parametro *opzionale* per specificarne la lunghezza.

**Soluzione**: usiamo la funzione `append()` in accoppiata alla funzione `randint()`.

```py
def genera_lista_casuale(lunghezza=5):
    l = []
    for i in range(lunghezza):
        l.append(randint(0, 10))
    return l
...
genera_lista_casuale() 		# Possibile risultato: [3, 1, 2, 0, 6]
genera_lista_casuale(10)	# Possibile risultato: [7, 9, 1, 10, 2, 4, 9, 1, 4, 8]
```

!!!warning "Tipo dei parametri di ingresso"
	Il duck typing fa sì che non venga effettuato alcun controllo sui parametri in ingresso. Ciò però non significa che non si possa provare a chiamare (ad esempio) la funzione `genera_lista_casuale()` passando come parametro una stringa; ciò tuttavia causerà un (prevedibile) errore.

### 2.6.1 - Passaggio di parametri a funzione

Python prevede che i parametri siano passati ad una funzione secondo una modalità ibrida chiamata *call-by-assignment*. In pratica, il passaggio avviene *esclusivamente per valore*, ma con effetti differenti su tipi mutabili ed immutabili.

Ad esempio, provando a passare un valore primitivo (come un intero), Python si comporterà come se si stesse effettuando un passaggio per valore:

```py
def raddoppia(intero):
	intero = intero * 2
	print(f'Valore all\'interno della funzione: {intero}')
```

Il risultato sarà:

```py
>>> intero = 1
>>> raddoppia(intero)
"Valore all'interno della funzione: 2"
>>> print(f'Valore all\'esterno della funzione: {intero}')
"Valore all'interno della funzione: 1"
```

Ciò è legato al fatto che il passaggio viene effettuato per valore, per cui la funzione `raddoppia` agirà su una *copia* della variabile passata come argomento, e non sulla variabile originaria. Se invece usassimo una funzione che modifica una lista:

```py
def aggiungi_a_lista(lista, elemento):
	lista.append(elemento)
	print(f'Valore all\'interno della funzione: {lista}')
```

Il risultato sarà:

```py
>>> lista = [1, 2]
>>> aggiungi_a_lista(lista, 3)
"Valore all'interno della funzione: [1, 2, 3]"
>>> print(f'Valore all\'esterno della funzione: {lista}')
"Valore all'interno della funzione: [1, 2, 3]"
```

In questo caso, essendo la lista mutabile, il passaggio viene effettuato nei fatti per *reference*: ciò significa che le operazioni comppiute all'interno della funzione `aggiungi_a_lista` agiranno sulla lista originaria.

!!!note "Shallow e deep copy"
	Di default, Python copia le variabili per mezzo di una *shallow copy*: ciò significa che un'operazione di assignment del tipo `a = b` fa in modo che `a` punti allo stesso indirizzo di memoria di `b` e, di conseguenza, ogni modifica a `b` si rifletta su `a`. Per evitare un fenomeno di questo tipo occorre usare una *deep copy* grazie alla funzione `deepcopy` della libreria `copy`.

### 2.6.2 - L'istruzione `pass`

Chiudiamo accennando all'istruzione `pass`. Questa non fa assolutamente nulla; è utile, ad esempio, quando vogliamo inserire una funzione (o una classe) vuota, che definiremo per qualche motivo in seguito:

```py
>>> def funzione_vuota():
...     pass
...
>>> funzione_vuota()
```

!!!note "Nota"
	Anche se di primo acchitto potrebbe non essere evidente, esistono diverse situazioni in cui l'istruzione `pass` risulta essere estremamente utile.
