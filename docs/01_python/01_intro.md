# Introduzione a Python

!!!note "Nota"
	Queste lezioni seguono il percorso tracciato dal tutorial ufficiale di Python. Di conseguenza, aderiscono alle licenze [PSF e Zero-Clause BSD License](https://docs.python.org/3/license.html).

## Premessa: Python e tipizzazione

### Tipizzazione dinamica

Prima di partire con l'introduzione dei concetti fondamentali del linguaggio, è opportuna una premessa. Infatti Python, a differenza dei linguaggi C e C++, implementa il concetto di *tipizzazione dinamica*, il che significa che l'*interprete* valuta il tipo di ogni variabile a runtime, e che questo può cambiare nel corso dell'esecuzione del programma.

Questo semplifica apparentemente la vita al programmatore, che non dovrebbe (in teoria) più preoccuaprsi di concetti come il tipo della variabile, in quanto inferiti automaticamente dall'interprete. Tuttavia, questa è un'arma a doppio taglio, in quanto l'interprete Python adotta il (pilatesco) principio chiamato *duck typing*.

#### Duck Typing

Il duck typing deriva dalla massima secondo cui:

!!!quote "Duck Typing"
	*If it walks like a duck and it quacks like a duck, then it must be a duck.*
	(*Se cammina come un papero, e starnazza come un papero, deve essere un papero.*)

Traduciamo brevemente questa massima in informatichese. Immaginiamo di passare all'interprete Python una variabile che assume valore `1`. L'interprete si accorge che ha tutti i comportamenti assimilabili ad un numero di tipo intero: di conseguenza, inferirà che si tratta proprio di una variabile di questo tipo. Se però poi sommiamo in seguito il valore `1.1`, il risultato sarà un valore decimale, interpretato quindi come `float`, in quanto tutti i "comportamenti" sono assimilabili a quelli di una variabile di questo tipo.

Questo concetto sarà ancora più "forte" (per non dire *invadente*) quando parleremo delle classi: Python infatti non ci chiederà mai di esplicitare nel codice delle eventuali procedure di casting, ma le inferirà per noi, con tutte le comodità che questo comporta (oltre che i potenzialmente catrastrofici effetti).

## L'interprete Python

A differenza dei compilatori presenti in altri linguaggi di programmazione, Python offre un interprete accessibile al programmatore direttamente dalla riga di comando.

Dopo averlo installato, ed essersi assicurati che il launcher sia stato aggiunto al path di sistema, possiamo lanciare l'interprete da riga di comando. Per prima cosa, comunque, assicuriamoci che sia tutto a posto controllando la versione installata di Python:

```bash
$ python --version
python3.9.1
```

A questo punto, lanciamo l'interprete mediante il seguente comando:

```bash
python
```

Proviamo quindi ad usare Python per alcuni semplici comandi. Inizieremo a provare ad usarlo come calcolatrice; attendiamo che l'interprete ci chieda un input (sarà visualizzato il simbolo `>>>`).

## Calcoli e numeri

Proviamo ad usare l'interprete come una semplice calcolatrice.

```python
>>> 2 + 2
4
>>> 3 * 5
15
>>> 10 - 2 * 4
2
>>> 2 / 2
2.0
```

### Divisioni

La cosa importante da notare è che la divisione restituisce sempre un numero in virgola mobile. Notiamo che i primi tre risultati hanno tipo intero (int), mentre gli altri hanno tipo float. Ad ogni modo, possiamo ottenere il quoziente ed il resto della divisione usando rispettivamente gli operatori `//` e `%`.

```python
>>> 16 / 3
5.333333333333333
>>> 16 // 3
5
>>> 16 % 3
1
```

### Calcolo di potenza

Per calcolare la potenza di un numero, è necessario usare l'operatore `**`, che accetta a sinistra la base, ed a destra l'esponente:

```python
>>> 3 ** 2
9
>>> 2 ** 8
256
```

### Tipi numerici supportati"

Abbiamo accennato al fatto che Python supporta interi e float. Oltre questi, Python supporta anche altri tipi numerici, come i `Decimal` ed i `Fraction`, ed ha un supporto integrato ai numeri complessi, espressi usando il suffisso `j` o `J` per la parte immaginaria.

```python
>>> from decimal import *
>>> print(Decimal(1) / Decimal(7))
```

```python
>>> from fractions import Fraction
>>> Fraction(4, 6)
Fraction(2, 3)
```

```python
>>> a = 1 + 4j
>>> b = 2 + 3j
>>> print(a + b)
(3+7j)
```

## Stringhe

Python ovviamente supporta anche le stringhe, che possono essere indifferentemente racchiuse tra singole o doppie virgolette.

```python
>>> "una stringa"
'una stringa'
>>> 'un\'altra stringa'
"un'altra stringa"
```

Nella seconda espressione, notiamo l'uso del carattere di escape `\` che precede l'apostrofo. E' importante fare attenzione ad utilizzarlo, in quanto in caso contrario avremmo avuto un errore di sintassi da parte dell'interprete.

```python
>>> 'un'altra stringa'
  File "<stdin>", line 1
    'un'altra stringa
            ^
SyntaxError: invalid syntax
```

!!!note "Nota"
	E' importante sottolineare come *tutti* i caratteri preceduti da un simbolo `\` saranno interpretati come escape character, a meno che non si aggiunga una `r` prima dell'inizio della stringa, come ad esempio:
	> ```python
	  >>> print('C:\nuova_cartella')
	  C:
	  uova_cartella
	  >>> print(r'C:\nuova_cartella')
	  C:\nuova_cartella
	  ```

### Stringhe su righe multiple

Le stringhe possono articolarsi su più righe. Un modo per farlo è quello di usare le *triple-quotes*, ovvero tre virgolette di seguito (ovviamente sia in apertura, sia in chiusura):

```python linenums="1" hl_lines="1 3"
>>> print("""Questo è un esempio\
		 di
		riga multipla\
		""")
	Questo è un esempio di
	riga multipla
```

Notiamo anche qui la presenza del carattere `\`. In questo caso, il suo utilizzo è quello di evitare che venga posto, al termine di ogni riga, un carattere `\n`: infatti, si vede come il newline venga "ignorato" nelle righe evidenziate, ovvero la 1 e la 3, mentre non lo sia nella riga 2.

### Concatenazione di stringhe

Python offre anche un modo molto semplice per concatenare due stringhe: per farlo, infatti, basta usare l'operatore `+` su due stringhe.

```python linenums="1"
>>> stringa_a = "Prima stringa"
>>> stringa_b = "Seconda stringa"
>>> print(stringa_a + " - " + stringa_b)
Prima stringa - Seconda stringa
```

!!!note "Nota"
	E' anche possibile concatenere diverse volte una stessa stringa usando l'operatore `*`:
	> ```python
	  >>> 3 * 'co.'
	  'co.co.co.'
	  ```

Un altro modo per concatenare due stringhe è semplicemente metterle l'una subito dopo l'altra, in questo modo:

```python
>>> "Py" "thon"
'Python'
```

!!!warning "Attenzione"
	E' importante non concatenare un *literal* (ovvero una stringa racchiusa tra virgolette, sia singole, sia doppie) ad una variabile di tipo stringa. Se provassimo a farlo, l'interprete ci restituirebbe il seguente errore:
	> ```python
	  >>> py="Py"
	  >>> py "thon"
  	  File "<stdin>", line 1
      py "thon"
              ^
	  SyntaxError: invalid syntax
	  ```

	Lo stesso errore si presenterebbe se al posto della variabile `py` usassimo il risultato di una operazione di concatenazione:
	> ```python
      >>> ('p' + 'y') 'thon'
	  File "<stdin>", line 1
	      ('p' + 'y') 'thon'
						^
	  SyntaxError: invalid syntax
	  ```
	In questi casi "ibridi", è opportuno usare l'operatore standard di concatenazione, ovvero il `+`.

!!!note "Nota"
	Esistono modi più efficienti di concatenare delle stringhe, specialmente quando si ha a che fare con numerose operazioni di concatenazione in grossi cicli. Tuttavia, trattarli va oltre gli obiettivi di questo corso.

### Indicizzazione di stringhe

In Python, le stringhe possono essere indicizzate esattamente allo stesso modo del C e del C++. Sono, quindi, anche qui considerati come *array di char*.

!!!note "Nota"
	In realtà, sarebbe più corretto dire che Python le considera come delle *liste* di char.

```python
>>> stringa = 'Python'
>>> stringa[0]
'P'
```

E' importante notare anche come un singolo char sia considerato una stringa, in questo caso di lunghezza unitaria:

```python
>>> lettera = 'P'
>>> lettera[0]
'P'
```

Python ammette anche degli indici negativi: in questo caso, l'indicizzazione andrà da destra verso sinistra, piuttosto che da sinistra verso destra:

```python
>>> stringa[-1]
'n'
```

!!!note "Nota"
	Dato che possiamo assumere, con un certo grado di sicurezza, che $-0 = 0$, l'indicizzazione negativa parte da $-1$.

### Slicing su stringhe (e liste)

L'operazione di *slicing* semplifica (e di molto) l'estrazione di determinate parti di una stringa. In generale, assume la seguente forma:

```python
>>> stringa[i:j]
```

dove `i` è l'indice iniziale, e `j` quello finale. E' importante sottolineare come **l'elemento all'indice iniziale sarà incluso, mentre quello all'indice finale sarà escluso**.

!!!note "Nota"
	Tutte le considerazioni su indicizzazione e slicing si applicano anche alle liste. Anzi, per essere corretti, derivano proprio dalle liste, in quanto, come già detto, Python considera una stringa un particolare tipo di lista.

Ad esempio:

```python
>>> stringa[0:2]
'Py'
>>> stringa[2:5]
'tho'
```

Se volessimo considerare *tutti i caratteri fino a `j`* (escluso), dovremmo usare la seguente notazione:

```python
>>> stringa [:j]
```

Se invece volessimo considerare *tutti i caratteri a partire da `i`* (incluso), dovremmo usare la seguente notazione:

```python
>>> stringa [i:]
```

Ad esempio:

```python
>>> stringa[1:]
'ython'
>>> stringa[:5]
'Pytho'
```

!!!note "Nota"
	Anche in questo caso, è possibile usare degli indici negativi. Ad esempio, se volessimo prendere tutti i caratteri dalla terzultima lettera fino alla fine, potremmo scrivere:
	> ```python
	  >>> stringa[-3:]
	  'hon'
	  ```

	mentre se volessimo prendere tutti i caratteri fino alla terzultima lettera (esclusa):
	> ```python
	  >>> stringa[:-3]
	  'Pyt'
	  ```

!!!tip "Suggerimento"
	E' possibile ottenere un'intera stringa mediante l'operazione di slicing in questo modo:
	> ```python
	  >>> stringa[:]
	  'Python'
	  ```

### Lunghezza di una stringa (o di una lista)

Per ottenere la lunghezza di una stringa (o di una lista) possiamo usare la funzione `len()`:

```python
>>> len(stringa)
6
```

### Immutabilità di una stringa

Le stringhe in Python si dicono *immutabili*. Ciò significa che non possono essere cambiate: se, ad esempio, provassimo a ridefinirne uno o più elementi, acceduti magari mediante indexing o slicing, avremmo un errore.

```python
>>> stringa[0] = 'C'	# Errore!
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

## Liste

Abbiamo già visto alcuni dei concetti fondamentali legati alle liste mentre parlando delle stringhe. Come già detto, infatti, una stringa altro non è che un caso particolare di lista.

Le liste in Python hanno la stessa funzione degli array negli altri linguaggi di programmazione. E' importante sottolineare che **Python non supporta nativamente gli array**: per farlo, è necessario utilizzare delle librerie esterne alla libreria standard, ma comunque ampiamente diffuse e supportate (una tra tutte, [**NumPy**](https://numpy.org/)).

Definire una lista in Python è estremamente semplice:

```python
>>> lista = [1, 2, 3, 4, 5]		# Dichiarazione di una lista di interi
[1, 2, 3, 4, 5]
```

### Concatenazione, indicizzazione e slicing su liste

Sulle liste sono possibili le operazioni di indicizzazione, slicing e concatenazione:

```python
>>> lista[0]					# Slicing ed indicizzazione
1
>>> lista[2:]
[3, 4, 5]
>>> lista_due = [6,7]
>>> lista + lista_due
[1, 2, 3, 4, 5, 6, 7]
>>> lista + [6]
[1, 2, 3, 4, 5, 6]
```

### Mutabilità di una lista

A differenza delle stringhe, le liste sono oggetti *mutabili*, e quindi possiamo cambiarne il contenuto:

```python
>>> lista[0] = 99				# Mutabilità
>>> lista
[99, 2, 3, 4, 5]
```

### Operazioni sulle liste

Possiamo anche eliminare elementi da una lista usando l'operatore `[]` combinato all'operazione di slicing:

```python
>>> lista[4:] = []				# Eliminazione di un elemento di una lista
>>> lista
[99, 2, 3, 4]
```

!!!note "Nota"
	I lettori più attenti avranno notato che l'operatore `[]` non fa altro che indicare una lista vuota.

!!!tip "Suggerimento"
	Possiamo provvedere a "pulire" una lista (ovvero ad eliminarne tutti gli elementi) usando in maniera opportuna lo slicing e l'operatore `[]`:
	> ```python
	  >>> lista[:] = []
	  >>> lista
	  []
	  ```

Le liste Python sono estremamente versatili, e ciascun elemento può essere di ogni tipo consentito. E' addirittura possibile inserire delle liste all'interno di altre liste:

```python
>>> lista.append([1,2,3])		# Aggiunta di elementi ad una lista
>>> lista
[99, 2, 3, 4, [1, 2, 3]]
```

Nell'esempio precedente, abbiamo usato la funzione `append()` per inserire un elemento in coda alla lista. E' interessante notare come questo elemento **sia esso stesso una lista**, e "conviva" tranquillamente con gli altri elementi presenti, questi ultimi di tipo numerico. Per enfatizzare questo concetto, vediamo cosa succede inserendo una stringa al primo elemento:

```python
>>> lista [0] = stringa
>>> lista
['Python', 2, 3, 4, [1, 2, 3]]
```
