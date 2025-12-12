# 1.1.4 - Liste e tuple

## Liste

Le *liste* sono una delle strutture dati fondamentali di Python. Da un punto di vista puramente "concettuale", potremmo considerarle alla stregua degli array presenti in altri linguaggi di programmazione, seppur con alcune, significative differenze.

Possiamo creare una lista in questo modo:

```py
>>> lista = [1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
```

### Concatenazione, indicizzazione e slicing su liste

Come sulle stringhe, sulle liste è possibile effettuare operazioni di indicizzazione, slicing e concatenazione:

```py
>>> lista[0]
1
>>> lista[2:]
[3, 4, 5]
>>> lista_due = [6,7]
>>> lista + lista_due
[1, 2, 3, 4, 5, 6, 7]
>>> lista + [6]
[1, 2, 3, 4, 5, 6]
```

Facciamo alcuni esempi. Consideriamo la seguente lista:

```py
>>> l = [1, 2, 3, 4, 5, 6]
```

Prendiamo gli elementi sugli indice pari (ovvero 0, 2 e 4):

```py
>>> l[0::2]
[1, 3, 5]
```

Prendiamo tutti gli elementi a partire dal terzultimo e con indice pari:

```py
>>> l[(-3 + 1)::2]
[5]
```

!!!note "Nota"
	Nell'esempio precedente, usato un piccolo "trucco" per tenere in conto il fatto che l'indicizzazione parte da 0 e non da 1.

Partiamo dal terzultimo elemento, e proseguiamo all'indietro verso l'origine:

```py
>>> l[-3::-1]
[4, 3, 2, 1]
```

Partiamo dall'ultimo elemento e proseguiamo sino al terz'ultimo dall'origine:

```py
>>> l[:3:-1]
[6, 5]
```

Prendiamo gli ultimi tre elementi in ordine inverso:

```py
>>> l[len(l)-1:len(l)-4:-1]
[6, 5, 4]
```

Prendiamo gli elementi agli indici pari in ordine inverso:

```py
>>> l[::-2]
[6, 4, 2]
```

### Mutabilità di una lista

A differenza delle stringhe, le liste sono oggetti *mutabili*. Di conseguenza, possiamo modificarne il contenuto:

```py
>>> lista[0] = 99
>>> lista
[99, 2, 3, 4, 5]
```

### Operazioni sulle liste

Possiamo anche eliminare elementi da una lista usando l'operatore `[]` combinato all'operazione di slicing:

```py
>>> lista[4:] = []
>>> lista
[99, 2, 3, 4]
```

!!!note "Nota"
	I più attenti avranno notato che l'operatore `[]` non fa altro che indicare una lista vuota.

!!!tip "Suggerimento"
	Possiamo eliminare tutti gli elementi contenuti in una lista mediante lo slicing e l'operatore `[]`:
	> ```py
	  >>> lista[:] = []
	  >>> lista
	  []
	  ```

Una lista può contenere elementi tra loro eterogenei. E' addirittura consentito contenere degli *iterabili*, tra cui altre liste:

```py
>>> lista.append([1,2,3])
>>> lista
[99, 2, 3, 4, [1, 2, 3]]
```

Nell'esempio precedente, abbiamo usato la funzione `append()` per inserire un elemento in coda alla lista. E' interessante notare l'elemento inserito in coda sia esso stesso una lista, e "conviva" tranquillamente con gli altri elementi di tipo numerico.

Proviamo ad estendere ulteriormente la lista cambiando il primo elemento con una stringa:

```py
>>> lista[0] = "Python"
>>> lista
['Python', 2, 3, 4, [1, 2, 3]]
```

### Controllo di appartenenza mediante l'operatore `in`

Per verificare  se un elemento è presente o meno in una lista possiamo usare l'operatore `in`, il quale restituisce un booleano, e che risulta essere molto più leggibile ed efficiente di un ciclo `for`. Ad esempio:

```py
>>> players = ['mario', 'luigi', 'wario']
>>> 'luigi' in players
True
>>> 'waluigi' in players
False
```

### Metodi fondamentali sulle liste

Concludiamo questo excursus andando ad elencare alcuni dei metodi ottimizzati offerti da Python per la modifica delle liste.

| Metodo | Descrizione | Esempio | Risultato (su `l=[1, 2]`) |
| ------ | ----------- | ------- | ------------------------- |
| `.append(x)` | Aggiunge `x` alla fine | `l.append(3)` | `[1, 2, 3]` |
| `.extend(iter)` | Aggiunge tutti gli elementi di un iterabile | `l.extend([3, 4])` | `[1, 2, 3, 4]` |
| `.insert(i, x)` | Inserisce `x` all'indice `i` | `l.insert(0, 0)` | `[0, 1, 2]` |
| `.pop(i)` | Rimuove e *restituisce* l'elemento ad `i` (default ultimo) | `val = l.pop()` | `l=[1]`, `val=2` |
| `.remove(x)` | Rimuove la *prima* occorrenza di `x` | `l.remove(1)` | `[2]` |
| `.clear()` | Rimuove tutti gli elementi | `l.clear()` | `[]` |
| `.count(x)` | Conta quante volte `x` appare | `l.count(1)` | `1` |

## Tuple

Le *tuple* sono sequenze molto simili alle liste, anche se presentano una differenza fondamentale: sono **immutabili**, per cui non possono essere modificate una volta create. La creazione di una tupla avviene in questo modo:

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

Ricapitolando, quindi:

* le tuple sono immutabili, ma possono contenere oggetti mutabili...
* ...mentre le liste sono mutabili, ma possono contenere oggetti immutabili!

### Tuple unpacking

Una delle feature più interessanti messe a disposizione di Python è l'*unpacking*, ovvero l'assegnazione multipla dei valori di una tupla a diverse variabili in un'unica istruzione. Ad esempio:

```py
coordinate = (41.90, 12.49)
lat, lon = coordinate # Unpacking

print(f"Latitudine: {lat}")
print(f"Longitudine: {lon}")
```

!!!tip "Quando usare le tuple, quindi?"
	Preferiamo le tuple ad altre strutture dati quando abbiamo a che fare con dati che non devono cambiare nel codice, oppure per avere dei minimi guadagni in termini di performance.

