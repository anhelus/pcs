

Le *tuple* sono il terzo tipo di sequenze "standard" disponibile in Python, e consistono di una serie di valori separati da una lettera.
Ad esempio:

```py
>>> tupla = ('hello', 'world', 12)
>>> tupla
('hello', 'world', 12)
```

Così come per le liste, uno dei valori della tupla può essere a sua volta una tupla:

```py
>>> tupla = ('hello', 'world', (1, 2))
>>> tupla
('hello', 'world', (1, 2))
```

E' però importante sottolineare che, a differenza delle liste (e come le stringhe), le tuple sono *immutabili*.

!!!note "Nota"
	Il fatto che le tuple siano immutabili non implica che non possano contenere al loro interno oggetti mutabili. Ad esempio:
	> ```py
 	  >>> tupla = ('hello', 'world', [1, 2, 3])
	  >>> tupla[2]
	  [1, 2, 3]
	  >>> tupla[2] = [1, 2, 3, 4] 				# errore!
	  Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	  TypeError: 'tuple' object does not support item assignment
	  >>> tupla[2][0] = 2						# ok
	  >>> tupla
	  ('hello', 'world', [2, 2, 3])
	  ```

!!!tip "Tuple e liste"
	E' facile osservare come tuple e liste siano tra loro molto simili a livello sintattico, e differiscano principalmente per il fatto che le prime sono immutabili, mentre le seconde no. Idealmente, è bene usare le tuple per elementi di tipo eterogeneo, che devono essere esclusivamente acceduti, mentre le liste vanno usate per elementi omogenei, che devono essere modificati all'occorrenza.

## Dizionari

L'ultimo tipo di dati che vale la pena affrontare in Python sono i *dizionari*, che abbiamo già visto in C e C++ con il nome di [array associativi](../02_dispense/programmazione/02_linguaggio_cpp/09_container/#associative-container).

I dizionari sono quindi indicizzati non mediante un classico indice numerico, ma mediante delle *chiavi*, che devono necessariamente essere immutabili (ovvero stringhe, numeri e tuple, che però al loro interno non possono contenere elementi mutabili come liste). Ad ogni chiave, come negli array associativi, corrisponde un determinato *valore*, che è arbitrario e può essere di qualsiasi tipo. Di conseguenza, un concetto comunemente associato ai dizionari è quello di *coppie chiave - valore*.

Vediamo come creare un dizionario:

```py
>>> dizionario = {}             			# creo un dizionario vuoto
>>> dizionario
{}
```

Possiamo quindi inserire una serie di chiavi, associandovi un determinato valore:

```py
>>> dizionario['k'] = 'v'			# aggiungo la chiave "k" a cui è associato il valore "v"
>>> dizionario
{'k': 'v'}
>>> dizionario[1] = 'n'				# aggiungo la chiave 1 a cui è associato il valore "n"
>>> dizionario
{'k': 'v', 1: 'n'}
```

Per accedere al valore associato ad una chiave:

```py
>>> dizionario[1]
'n'
```

### Accedere a chiavi e valori

E' possibile avere la lista delle chiavi di un dizionario mediante il metodo `keys()`, che restituisce un oggetto di tipo `dict_keys`, convertibile in lista:

```py
>>> chiavi = dizionario.keys()
>>> chiavi
dict_keys(['k', 1])					# non è una lista!
>>> list(chiavi)
['k', 1]							# è una lista!
```

In modo analogo, si può accedere a tutti i valori presenti nel dizionario mediante il metodo `values()`, che restituirà un oggetto di tipo `dict_values`, da convertire anch'esso in lista:

```py
>>> valori = dizionario.values()
>>> valori
dict_values(['k', 'n'])				# non è una lista!
>>> list(valori)
['k', 'n']							# è una lista!
```

Possiamo accedere anche a tutte le coppie chiave - valore mediante il metodo `items()`, che ci restituisce un oggetto di tipo `dict_items`, il quale può essere convertito in una lista di tuple:

```py
>>> coppie = dizionario.items()
>>> coppie
dict_items([('k', 'v'), (1, 'n')])	# non è una lista!
>>> list(coppie)
[('k', 'v'), (1, 'n')]				# lista di tuple!
>>>
```

### Creare un dizionario non vuoto

Abbiamo diversi modi per creare un dizionario non vuoto. Il primo, più semplice, è quello di dichiarare nell'operatore `{}` le coppie chiave - valore iniziali:

```py
>>> dizionario = { 'k1': 1, 'k2': 2 }
>>> dizionario
{'k1': 1, 'k2': 2}
```

#### Uso della funzione `zip`

Possiamo poi usare la funzione `zip` per creare un dizionario a partire da due liste:

```py
>>> chiavi = ['k1', 'k2']
>>> valori = [1, 2]
>>> dizionario = dict(zip(chiavi, valori))
>>> dizionario
{'k1': 1, 'k2': 2}
```

#### Dict comprehension

Possiamo ottenere un dizionario a partire da un altro oggetto iterabile (sia esso una sequenza o un altro dizionario) usando la *dict comprehension*, che ha una forma del tipo:

```py
output = { chiave: valore for valore in iterabile }
```

Possiamo ad esempio creare un dizionario contenente come chiave i numeri da 1 a 9, e come valori corrispondenti i quadrati degli stessi:

```py
>>> quadrati = {str(i): i ** 2 for i in range(1, 10)}
>>> quadrati
{'1': 1, '2': 4, '3': 9, '4': 16, '5': 25, '6': 36, '7': 49, '8': 64, '9': 81}
```

Oppure, possiamo creare un dizionario a partire da un altro dizionario, usando le stesse regole condizionali viste con la list comprehension:

```py
>>> dizionario = {'Jax Teller': 27, 'Walter White': 52, 'Billy Butcher': 41, 'Luke Skywalker': 79, 'Bobby Singer': 68, 'Johnny Lawrence': 49}
>>> vecchio_o_giovane = { k: 'vecchio' if v > 50 else 'giovane' for (k, v) in dizionario.items() }
>>> vecchio_o_giovane
{'Jax Teller': 'giovane', 'Walter White': 'vecchio', 'Billy Butcher': 'giovane', 'Luke Skywalker': 'vecchio', 'Bobby Singer': 'vecchio', 'Johnny Lawrence': 'giovane'}
```

!!!note "Nota"
	Per iterare sul dizionario originale, usiamo il metodo `items()` che, come visto in precedenza, ci restituisce un oggetto di tipo `dict_items` il quale è, per l'appunto, iterabile.
