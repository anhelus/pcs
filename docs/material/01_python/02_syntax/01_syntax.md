# 1.2.1 - Sintassi fondamentale

Vediamo alcuni dei concetti fondamentali che caratterizzano la sintassi del linguaggio Python.

## Commenti

Python prevede due tipi di commento. Il primo, e più semplice, è quello a singola riga, anteceduto da un carattere `#` (*asterisco*):

```py
>>> # Questo è un commento!
```

L'altro tipo di commento è un commento multilinea, ed è definito esattamente allo stesso modo in cui si definisce una [stringa multilinea](../01_intro/03_strings.md):

```py
""" Questo è un esempio
di commento multilinea!
"""
```

!!!note "Singole e doppie apici"
	Così come per le stringhe, è possibile usare indifferentemente (ma coerentemente!) singole o doppie apici.

## Uso delle parentesi

L'utilizzo delle parentesi in Python differisce da quello che ne si fa in molti linguaggi C-like. In particolare, vediamo come sono utilizzate (ed a cosa servono) le parentesi tonde, quadre e graffe.

### Parentesi tonde

Le parentesi tonde sono usate in tre casi:

* per le chiamate a funzione;
* per la creazione di una tupla;
* per esprimere la precedenza in un'operazione matematica.

Negli altri casi, sono opzionali, e possono essere tranquillamente omesse.

Vediamo un breve esempio di come esprimere la precedenza in un'operazione matematica:

```py
>>> a = 2
>>> b = 3
>>> c = 4
>>> r_1 = a + b * c
14
>>> r_2 = (a + b) * c
20
```

Nelle prossime lezioni vedremo come utilizzare le parentesi tonde [nelle tuple](02_structured.md) e nelle [chiamate a funzione](03_functions.md).

### Parentesi quadre

Le parentesi quadre sono usate per la creazione e l'accesso agli elementi di una struttura dati.

```py
# Creo una lista
lista = [1, 2, 3]
# Accedo al secondo elemento della lista
lista[1]			# Il valore acceduto è 2
```

Ne parleremo più diffusamente nella [prossima lezione](02_structured.md).

### Parentesi graffe

Le parentesi graffe sono usate per creare set e dizionari.

```py
dizionario = {'a': 1, 'b': 2}
insieme = {1, 2, 3}
```

Anche in questo caso, ne parleremo più diffusamente nella [prossima lezione](02_structured.md).

## Termine di un'istruzione

A differenza dei linguaggi C-like, che prevedono che la singola istruzione termini con un `;` (un punto e virgola), Python fa in modo che il carattere di terminazione di un'istruzione sia dato dal newline `\n`. In altri termini, l'interprete associerà il termine dell'istruzione all'andata a capo.

## Blocchi di codice

Per delimitare un blocco di codice Python ricorre al carattere `:` (*due punti*) ed all'*indentazione*. In particolare, tutto il codice che segue un carattere `:` ed è ad uno stesso livello di indentazione risulta far parte di uno stesso blocco. Ad esempio:

```py
>>> a = 1				# Codice non in un blocco
>>> if a < 10:			# Inizia il blocco if esterno
>>> 	b = 5
>>> 	print('blocco esterno')
>>> 	if b > 1:		# Inizia il blocco if annidato
>>> 		print('blocco interno')
```

!!!note "Indentazioni e parentesi graffe"
	I più attenti avranno notato che le indentazioni svolgono, in buona sostanza, un ruolo analogo a quello delle parentesi graffe nei linguaggi C-like.
