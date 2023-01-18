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
