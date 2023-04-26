# 1.2.4 - Strutture dati

In questa lezione approfondiremo alcune tecniche per manipolare le [liste](../01_intro/04_lists.md), oltre ad altre strutture dati fondamentali.

## List comprehension

Una delle tecniche più usate per creare una lista a partire da un'altra sequenza è la cosiddetta *list comprehension*, che sostituisce la sintassi definita dai classici cicli con costrutti decisamente più *pythonic*.

Nella forma base, una list comprehension ha una sintassi di questo tipo:

```py
lista_output = [f(elemento) for elemento in lista_input]
```

In altre parole, otterremo in output una lista (`lista_output`) applicando ad ogni `elemento` della lista originaria (`lista_input`) la funzione `f()`.

Ad esempio, prendendo una lista di interi, possiamo creare una lista che abbia all'$i$-mo elemento il doppio del valore $i$-mo della lista di ingresso.

```py
>>> lista_input = [1, 2, 3]
>>> lista_output = [x * 2 for x in lista_input]
[2, 4, 6]
```

### Forma estesa con if-else

La list comprehension può anche includere delle istruzioni condizionali. Un primo esempio è la seguente forma:

```py
lista_output_if = [f(elemento) for elemento in lista_input if condizione]
```

In questo caso, la funzione `f()` sarà chiamata esclusivamente sugli elementi che soddisfano la `condizione` indicata. Ad esempio, possiamo utilizzare una list comprehension per restituire tutti i valori pari in una lista:

```py
>>> lista_output_pari = [x for x in lista_input if x % 2 == 0]
[2]
```

Se invece volessimo integrare l'`else`:

```py
lista_output_if_else = [f(elemento) if condizione else g(elemento) for elemento in lista_input]
```

la funzione `f()` sarebbe invocata su tutti gli elementi che soddisfano la `condizione`, mentre la funzione `g()` su tutti quelli che non la soddisfano. Potremmo ad esempio restituire tutti gli elementi pari, raddoppiando contestualmente i dispari:

```py
>>> lista_output_complessa = [x if x % 2 == 0 else x * 2 for elemento in lista_input]
[2, 2, 6]
```

## Tuple

Le *tuple* permettono di rappresentano un insieme di valori eterogenei separadoli da una virgola. Ad esempio:

```py
tupla = ('hello', 'world', 12)
```

Un po' come avviene per le liste, uno dei valori della tupla può a sua volta essere un'altra tupla. Ad esempio:

```py
tupla = ('hello', 'world', (1, 2))
```

A differenza di una lista, però, le *tuple sono immutabili*. Ciò non implica però che non possano contenere al loro interno oggetti mutabili. Guardiamo il seguente esempio:

```py
tupla = ('hello', 'world', [1, 2, 3])
```

La tupla avrà al suo interno due stringhe (immutabili) ed una lista (mutabile). Proviamo a modificare la lista:

```py
tupla[2] = [2, 2, 3]
```

Apparirà un errore simile a questo:

```sh
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

Come prevedibile, abbiamo avuto un errore di assegnazione legato all'immutabilità della tupla. Proviamo adesso però a modificare *direttamente la lista*:

```py
tupla[2][0] = 2 		# La tupla sarà ('hello', 'world', [2, 2, 3])
```

L'operazione è evidentemente ammissibile, ed il risultato è stato proprio quello atteso.

!!!tip "Tuple e liste"
	Ad un attento osservatore non sfuggirà come tuple e liste siano simili dal punto di vista sintattico, e differiscano in buona sostanza per la mutabilità. Da qui discende che le tuple sono estremamente efficaci nel caso si debba esclusivamente accedere agli elementi contenuti, mentre le liste devono essere usate quando è anche necessario modificare all'occorrenza detti elementi.

## Set

Anche i *set* sono molto simili alle liste dal punto di vista sintattico, ma offrono una significativa differenza: infatti, in un set *non possono esserci elementi ripetuti*.

!!!note "Nota"
	Notiamo un'evidente analogia con il concetto matematico di insieme.

La sintassi da usare per creare un set è la seguente.

```py
insieme = {1, "stringa", 2}
```

Il set ammette al suo interno dati eterogenei, tuttavia non può contenere al suo interno delle liste o dei dizionari. Questo è legato al fatto che i set (così come gli stessi dizionari) sono delle [hash table](https://it.wikipedia.org/wiki/Hash_table), e quindi sfruttano il concetto di *hash* per rappresentare i dati contenuti in maniera compatta ed efficiente. Il fatto che le liste ed i dizionari non possano essere rappresentati in questo modo li esclude in automatico dall'includibilità all'interno di un set.

Un'altra considerazione da fare è che il set *non è ordinato*: ciò rende impossibile accedere ad (e *modificare*) un elemento del set mediante il suo indice, come succedeva per liste e tuple.

!!!tip "Suggerimento"
	I set possono essere usati per isolare gli elementi univoci presenti in una lista. Per farlo, basta convertire la lista in set:
	> ```py
	  l = [1, 2, 2, 3]		# La lista sarà [1, 2, 2, 3]
  	  s = set(l)			# Il set sarà [1, 2, 3]
	  ```

## Dizionari

Il quarto ed ultimo tipo di contenitore per sequenze di dati è il *dizionario*, presente anche in altri linguaggi di programmazione con il nome di *array associativo* o *hash map*.

L'elemento base di un dizionario è la *coppia chiave - valore*, nella quale un certo valore (di qualsiasi tipo) è associato ad una determinata chiave (di tipo immutabile).

I dizionari hanno diverse caratteristiche comuni ai set, dall'inutilizzabilità delle liste come chiavi al fatto di non permettere chiavi ripetute. Inoltre, le coppie chiave - valore sono accedute, per l'appunto, per chiave, e non in base all'ordine delle coppie.

!!!note "Nota"
	Una differenza tra set e dizionari sta nel fatto che questi ultimi sono *ordinati* a partire da Python 3.7.

Per creare un dizionario, possiamo usare una sintassi simile a quella usata per i set. Ad esempio, per creare un dizionario vuoto:

```py
>>> dizionario = {}
```

Possiamo quindi inserire delle coppie chiave - valore in questo modo:

```py
>>> dizionario['k'] = 'v'
>>> dizionario[1] = 'n'
{'k': 'v', 1: 'n'}
```

Per accedere al valore associato ad una determinata chiave:

```py
>>> dizionario[1]
'n'
```

### Chiavi e valori

E' possibile recuperare la lista di tutte le chiavi presenti in un dizionario usando il metodo `keys()`, che restituisce un oggetto di tipo `dict_keys`, a sua volta convertibile in lista:

```py
>>> chiavi = dizionario.keys()
dict_keys(['k', 1])
>>> list(chiavi)
['k', 1]
```

In modo analogo, si può accedere a tutti i valori presenti nel dizionario mediante il metodo `values()`, che restituirà un oggetto di tipo `dict_values`, da convertire anch'esso in lista:

```py
>>> valori = dizionario.values()
dict_values(['v', 'n'])
>>> list(valori)
['v', 'n']
```

Possiamo accedere anche a tutte le coppie chiave - valore mediante il metodo `items()`, che ci restituisce un oggetto di tipo `dict_items`, il quale può essere convertito in una lista di tuple:

```py
>>> coppie = dizionario.items()
dict_items([('k', 'v'), (1, 'n')])
>>> list(coppie)
[('k', 'v'), (1, 'n')]
```

### Creazione di un dizionario (non vuoto)

Abbiamo diversi modi per creare un dizionario non vuoto.

#### Uso dell'operatore `{}`

Il più semplice, che è quello che useremo più spesso, è quello di dichiarare nell'operatore `{}` le coppie chiave - valore iniziali:

```py
>>> dizionario = {'k1': 1, 'k2': 2}
>>> dizionario
{'k1': 1, 'k2': 2}
```

#### Uso del costruttore `dict()`

Un altro modo è usare il metodo costruttore `dict()`:

```py
>>> dizionario = dict(k1=1, k2=2)
```

#### Uso della funzione `zip`

Possiamo poi usare la funzione `zip` per creare un dizionario a partire da due liste:

```py
>>> chiavi = ['k1', 'k2']
>>> valori = [1, 2]
>>> dizionario = dict(zip(chiavi, valori))
```

#### Dict comprehension

Un modo per ottenere un dizionario a partire da un altro oggetto iterabile è la *dict comprehension*, che ha una forma del tipo:

```py
>>> output = {chiave: valore for valore in iterabile}
```

Possiamo ad esempio creare un dizionario contenente come chiave i numeri da 1 a 9, e come valori corrispondenti i quadrati degli stessi:

```py
>>> quadrati = {str(i): i ** 2 for i in range(1, 10)}
```
