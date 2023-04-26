# 1.2.3 - Funzioni

## Definizione di funzione

Python permette di definire una funzione utilizzando la parola chiave `def`. La sintassi generica è la seguente:

```py
def nome_funzione(parametri):
	# istruzioni
	return valore_ritorno
```

E' importante notare che:

* non è necessario definire un tipo, ma soltanto un *valore* di ritorno. Qualora la funzione non restituisca alcun valore, potrà essere omessa l'istruzione `return`;
* non è (strettamente) necessario definire il tipo di ciascuno dei parametri passati;
* è consentito inserire dei parametri *opzionali*, con valori di default.

Ad esempio, la seguente funzione somma `1` al valore in ingresso e restituisce il nuovo valore:

```py
def aggiungi_uno(i):
	val = i + 1
	return val
```

!!!warning "Tipo dei parametri di ingresso"
	Il duck typing fa sì che non venga effettuato alcun controllo sui parametri in ingresso. Ciò però non significa che non si possa provare a chiamare (ad esempio) la funzione `aggiungi_uno()` passando come parametro una stringa; ciò tuttavia causerà un (prevedibile) errore.

## Passaggio di parametri a funzione

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

Ciò è legato al fatto che il passaggio viene effettuato per valore, per cui la funzione `raddoppia()` agirà su una *copia* della variabile passata come argomento, e non sulla variabile originaria. Se invece usassimo una funzione che modifica una lista:

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

In questo caso, essendo la lista mutabile, il passaggio viene effettuato nei fatti per *reference*: ciò significa che le operazioni compiute all'interno della funzione `aggiungi_a_lista()` agiranno sulla lista originaria.

!!!note "Shallow e deep copy"
	Di default, Python copia le variabili per mezzo di una *shallow copy*: ciò significa che un'operazione di assignment del tipo `a = b` fa in modo che `a` punti allo stesso indirizzo di memoria di `b` e, di conseguenza, ogni modifica a `b` si rifletta su `a`. Per evitare un fenomeno di questo tipo occorre usare una *deep copy* grazie alla funzione `deepcopy()` della libreria `copy`.

## L'istruzione `pass`

Chiudiamo accennando all'istruzione `pass`. Questa non fa assolutamente nulla; è utile, ad esempio, quando vogliamo inserire una funzione (o una classe) vuota, che definiremo per qualche motivo in seguito:

```py
>>> def funzione_vuota():
...     pass
...
>>> funzione_vuota()
```

!!!note "Nota"
	Anche se di primo acchitto potrebbe non essere evidente, esistono diverse situazioni in cui l'istruzione `pass` risulta essere estremamente utile.
