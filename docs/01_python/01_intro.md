# Introduzione a Python

## Premessa: Python e tipizzazione

### Tipizzazione dinamica

Python è un linguaggio *interpretato* ed a *tipizzazione dinamica*. In breve, questo significa che l'interprete valuta il tipo di ciascuna variabile a runtime, e che questo può cambiare durante l'esecuzione del programma.

Ma, a conti fatti, in cosa si traduce per il programmatore? Beh, molto semplice.

Immaginiamo di dover definire ed inizializzare una variabile di tipo intero in un linguaggio a tipizzazione *statica*, come ad esempio il C++. Per farlo, scriveremo qualcosa simile a:

```c++
int var = 0;
```

In Python, potremo omettere il tipo, che sarà inferito direttamente dal valore assegnato alla variabile:

```py
var = 0
```

Immaginiamo ora che la nostra variabile debba diventare un decimale. In C++, dovremo effettuare il casting:

```c++
float fVar = float(var);
fVar + 1.1;
```

In Python questo non sarà necessario, e potremo effettuare direttamente le operazioni desiderate:

```py
var + 1.1
```

Questo può apparentemente semplificare di molto la vita, in quanto non è più necessario preoccuparsi del tipo della variabile. Non è però tutto oro ciò che luccica: per comprenderlo, infatti, è il momento di parlare del (pilatesco) principio del *duck typing*.

#### Duck Typing

Il duck typing è riassumibile nella seguente massima:

!!!quote "Duck Typing"
	*If it walks like a duck and it quacks like a duck, then it must be a duck.*

che in italiano suona più o meno *Se cammina come un papero, e starnazza come un papero, deve essere un papero*. Traduciamola brevemente in "informatichese". 

Immaginiamo di istruire il nostro interprete Python ad assegnare alla nostra variabile `var` il valore di `1`. L'interprete nota che la variabile si "comporta" come un numero intero, e quindi "stabilirà" che si tratti proprio di questo.

Proviamo ora a sommare a `var` un valore pari ad `1.1`. Il risultato, come ovvio, sarà un numero decimale, e quindi l'interprete "cambierà idea", in quanto i comportamenti assunti da `var` sono adesso assimilabili ad una variabile di tipo `float`.

L'utilità del duck typing è evidente: permette allo sviluppatore di "risparmiare" numerose operazioni di cast, rendendo il codice più semplice da scrivere e manutenere. Tuttavia, occorre tenerne conto nel momento in cui si usano classi ed oggetti, in quanto l'interprete proverà ad inferire ed usare automaticamente un tipo in base al contesto in cui viene usata la variabile, con le comodità (ed i potenziali disastri) che questo comporta.

## L'interprete Python

Python offre un interprete accessibile al programmatore direttamente dalla riga di comando.

Dopo averlo installato (è possibile farlo seguendo le istruzioni presenti sul [sito ufficiale](https://www.python.org/)) ed essersi assicurati che il launcher sia stato aggiunto al path di sistema, possiamo lanciarlo tramite riga di comando. Per prima cosa, comunque, assicuriamoci che sia tutto a posto controllando la versione installata di Python:

```sh
$ python --version
python3.9.1
```

A questo punto, lanciamo l'interprete:

```sh
python
```

Possiamo quindi iniziare ad usare Python.

## Calcoli e numeri

Proviamo ad usare l'interprete come una semplice calcolatrice; per farlo, scriviamo direttamente dopo il simbolo `>>>` le operazioni che vogliamo eseguire, e premiamo il tasto `Invio`. Ad esempio:

```python
>>> 2 + 2
4
>>> 3 * 5
15
>>> 10 - 2 * 4
2
```

### Divisioni

Le divisioni restituiscono sempre un numero in virgola mobile. Ad esempio:

```py
>>> 16 / 3
5.333333333333333
>>> 2 / 2
2.0
```

Proviamo ora ad usare altri due operatori, molto simili al classico operatore di divisione:

```py
>>> 16 // 3
5
>>> 16 % 3
1
```

Notiamo come in questi casi siano restituiti dei numeri interi. Il perché è presto detto: gli operatori `//` e `%` calcolano, rispettivamente, il *quoziente* ed il *resto* della divisione e, come sappiamo, entrambi sono dei valori interi.

### Elevazione a potenza

Per elevare un numero a potenza, è necessario usare l'operatore `**`, in cui l'operando sinistro è la base, mentre quello destro l'esponente:

```python
>>> 3 ** 2
9
>>> 2 ** 8
256
```

!!!note "Tipi numerici in Python"
	Abbiamo finora parlato soltanto di numeri interi e decimali; tuttavia, Python supporta anche altri tipi, come ad esempio `Decimal` e `Fraction`. E' inoltre presente un supporto nativo ai numeri complessi, esprimibili usando il suffisso `j` per indicare la parte immaginaria.

## Stringhe

In Python le stringhe possono indifferentemente essere racchiuse tra virgolette singole e doppie.

```python
>>> "una stringa"
'una stringa'
>>> 'un\'altra stringa'
"un'altra stringa"
```

Notiamo nella seconda istruzione l'uso del carattere di escape (`\`) che precede l'apostrofo; se lo omettessimo, l'interprete ci restituirebbe un errore sintattico (`SyntaxError`):

```python
>>> 'un'altra stringa'
  File "<stdin>", line 1
    'un'altra stringa
            ^
SyntaxError: invalid syntax
```

!!!note "Nota"
	Tutti i caratteri preceduti dal simbolo `\` saranno interpretati come escape character, a meno di aggiungere il simbolo `r` prima dell'inizio della stringa:
	> ```python
	  >>> print('C:\nuova_cartella')
	  C:
	  uova_cartella
	  >>> print(r'C:\nuova_cartella')
	  C:\nuova_cartella
	  ```

### Stringhe su righe multiple

Le stringhe possono articolarsi su più righe. Per farlo, possiamo usare le *triple-quotes*, ovvero tre virgolette di seguito, per indicare l'inizio e la fine della stringa:

```python linenums="1" hl_lines="1 3"
>>> print("""Questo è un esempio\
		 di
		riga multipla\
		""")
	Questo è un esempio di
	riga multipla
```

!!!note "Nota"
	Notiamo nel precedente snippet il carattere `\`, usato per evitare che venga automaticamente inserito dall'interprete il carattere *newline* (`\n`) al termine di ogni riga. Infatti, si vede come il newline non sia stato aggiunto nelle righe evidenziate, mentre sia presente nella riga 2.

### Concatenazione di stringhe

Concatenare due stringhe in Python è estremamente semplice, e basta usare l'operatore `+`:

```python linenums="1"
>>> stringa_a = "Prima stringa"
>>> stringa_b = "Seconda stringa"
>>> print(stringa_a + " - " + stringa_b)
Prima stringa - Seconda stringa
```

!!!note "Nota"
	Se usiamo l'operatore `*` possiamo concatenare più volte la stessa stringa:
	> ```python
	  >>> 3 * 'co.'
	  'co.co.co.'
	  ```

Possiamo anche semplicemente porre le due stringhe l'una di seguito all'altra:

```python
>>> "Py" "thon"
'Python'
```

TODO: da qui

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
