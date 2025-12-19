# 1.2.3 - Funzioni

## Definizione di funzione

Python permette di definire una funzione utilizzando la parola chiave `def`. La sintassi generica è la seguente:

```py
def nome_funzione(parametri):
	# istruzioni
	return valore_ritorno
```

E' importante notare che:

* anche se non è necessario definire un tipo di ritorno, è *fortemente consigliato farlo*. Qualora la funzione non restituisca alcun valore, potrà essere omessa l'istruzione `return`;
* è *fortemente consigliato* definire il tipo di ciascuno dei parametri passati;
* è consentito inserire dei parametri *opzionali*, con valori di default.

Ad esempio, la seguente funzione somma `1` al valore in ingresso e restituisce il nuovo valore:

```py
def aggiungi_uno(i: int) -> int:
	val = i + 1
	return val
```

Come possiamo vedere, abbiamo specificato il tipo del parametro in ingresso usando la sintassi `i: int`, ed il tipo dell'argomento di ritorno usando la notazione infissa (`-> int`).

!!!warning "Tipo dei parametri di ingresso"
	Il duck typing fa sì che non venga effettuato alcun controllo sui parametri in ingresso. Ciò però non significa che non si possa provare a chiamare (ad esempio) la funzione `aggiungi_uno()` passando come parametro una stringa; ciò tuttavia causerà un (prevedibile) errore.

## Passaggio di parametri a funzione

Python prevede che i parametri siano passati ad una funzione secondo una modalità ibrida chiamata *call-by-assignment*. In pratica, il passaggio avviene *esclusivamente per valore*, ma con effetti differenti su tipi mutabili ed immutabili.

Ad esempio, provando a passare un valore primitivo (come un intero), Python si comporterà come se si stesse effettuando un passaggio per valore:

```py
def raddoppia(intero: int) -> None:
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
def aggiungi_a_lista(lista: list, elemento: Any) -> None:
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

!!!warning "Il tipo `Any`"
	Il tipo `Any` non è built-in: per usarlo, dovremo ricordarci di aggiungere all'inizio del codice `from typing import Any`. Una versione più semplice potrebbe vedere l'utilizzo di `object` come tipo suggerito.

In questo caso, essendo la lista mutabile, il passaggio viene effettuato nei fatti per *reference*: ciò significa che le operazioni compiute all'interno della funzione `aggiungi_a_lista()` agiranno sulla lista originaria.

!!!note "Shallow e deep copy"
	Di default, Python copia le variabili per mezzo di una *shallow copy*: ciò significa che un'operazione di assignment del tipo `a = b` fa in modo che `a` punti allo stesso indirizzo di memoria di `b` e, di conseguenza, ogni modifica a `b` si rifletta su `a`. Per evitare un fenomeno di questo tipo occorre usare una *deep copy* grazie alla funzione `deepcopy()` della libreria `copy`.

### Passaggio di parametri opzionali

Nel caso si volessero passare dei parametri opzionali, dovremo specificare i valori di default all'interno della firma della funzione. Modifichiamo, ad esempio, la funzione `aggiungi_a_lista`:

```py
def aggiungi_a_lista(lista: list, elemento: Any = 1) -> None:
	lista.append(elemento)
	print(f'Valore all\'interno della funzione: {lista}')
```

In questo caso, staremo dando ad `elemento` il valore di default `1`. E' importante sottolineare come i parametri opzionali debbano *sempre* seguire quelli non opzionali nella firma della funzione.

!!!warning "I valori di default mutabili"
	Una situazione potenzialmente problematica è quella in cui usiamo dei valori di default mutabili. Potremmo, ad esempio, pensare di utilizzare una lista vuota come valore di default per una funzione. In questo caso, Python fa sì che il valore di default venga creato una sola volta, quando la funzione viene definita, e non ogni volta che viene chiamata, in quanto questo causerebbe la condivisione della stessa lista tra chiamate diverse. Di conseguenza, in questi casi è corretto utilizzare il valore `None`.

## Le funzioni lambda

Python ci offre la possibilità di utilizzare delle funzioni anonime, chiamate *funzioni lambda*. Ad esempio:

```py
def quadrato(x):
    return x ** 2

quadrato_lambda = lambda x: x ** 2

print(quadrato_lambda(5)) # 25
```

La sintassi generica dell'espressione lambda è quindi `lambda argomenti: espressione`. Un uso comune di questo tipo di funzioni è all'interno di altre funzioni, come `sort`, `map`, o `filter`, per lavorare in maniera rapida su una lista. Ad esempio, la seguente funzione permette di ordinare una lista di tuple in base al secondo elemento delle stesse.

```py
punti = [(1, 5), (3, 2), (2, 8)]

punti.sort(key=lambda x: x[1]) 

print(punti) # [(3, 2), (1, 5), (2, 8)]
```

## L'istruzione `pass`

Chiudiamo accennando all'istruzione `pass`. Questa non fa assolutamente nulla; è utile, ad esempio, quando vogliamo inserire una funzione (o una classe) vuota, che definiremo per qualche motivo in seguito:

```py
>>> def funzione_vuota():
...     pass
...
>>> funzione_vuota()
```

!!!note "Nota"
	Anche se di primo acchito potrebbe non essere evidente, esistono diverse situazioni in cui l'istruzione `pass` risulta essere estremamente utile.

## Documentare una funzione

Ricordiamo, infine, che dobbiamo *documentare le funzioni!* Per farlo, usiamo le docstring che abbiamo [introdotto in precedenza](01_syntax.md):

```py
def calcola_area(base: float, altezza: float) -> float:
    """
    Calcola l'area di un triangolo.
    
    Args:
        base (float): La base del triangolo.
        altezza (float): L'altezza del triangolo.
        
    Returns:
        float: L'area calcolata.
    """
    return (base * altezza) / 2
```

Notiamo che, nella docstring, definiamo:

* una prima sezione, all'interno della quale spieghiamo cosa fa la funzione;
* una sezione `Args` nella quale elenchiamo gli argomenti della funzione;
* una sezione `Returns` che dettaglia cosa viene restituito dalla funzione.
