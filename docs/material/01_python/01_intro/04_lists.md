# 1.1.4 - Liste

Abbiamo già detto che una stringa altro non è se non un caso particolare di *lista*. La domanda che sorge spontanea è quindi: *cosa è una lista*?

Le liste sono uno dei quattro tipi di strutture *built-in* che Python offre per memorizzare sequenze di dati. Da un punto di vista puramente "concettuale", potremmo considerarle alla stregua degli array presenti in altri linguaggi di programmazione, seppur con alcune, significative differenze.

Possiamo creare una lista in questo modo:

```py
>>> lista = [1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
```

## Concatenazione, indicizzazione e slicing su liste

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

Facciamo alcuni esempi. Consideriamo la seguente stringa:

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

## Mutabilità di una lista

A differenza delle stringhe, le liste sono oggetti *mutabili*. Di conseguenza, possiamo modificarne il contenuto:

```py
>>> lista[0] = 99
>>> lista
[99, 2, 3, 4, 5]
```

## Operazioni sulle liste

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
>>> lista [0] = stringa
>>> lista
['Python', 2, 3, 4, [1, 2, 3]]
```
