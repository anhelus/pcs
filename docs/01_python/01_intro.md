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

```py
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

```py
>>> 3 ** 2
9
>>> 2 ** 8
256
```

!!!note "Tipi numerici in Python"
	Abbiamo finora parlato soltanto di numeri interi e decimali; tuttavia, Python supporta anche altri tipi, come ad esempio `Decimal` e `Fraction`. E' inoltre presente un supporto nativo ai numeri complessi, esprimibili usando il suffisso `j` per indicare la parte immaginaria.

## Stringhe

In Python le stringhe possono indifferentemente essere racchiuse tra virgolette singole e doppie.

```py
>>> "una stringa"
'una stringa'
>>> 'un\'altra stringa'
"un'altra stringa"
```

Notiamo nella seconda istruzione l'uso del carattere di escape (`\`) che precede l'apostrofo; se lo omettessimo, l'interprete ci restituirebbe un errore sintattico (`SyntaxError`):

```py
>>> 'un'altra stringa'
  File "<stdin>", line 1
    'un'altra stringa
            ^
SyntaxError: invalid syntax
```

!!!note "Nota"
	Tutti i caratteri preceduti dal simbolo `\` saranno interpretati come escape character, a meno di aggiungere il simbolo `r` prima dell'inizio della stringa:
	> ```py
	  >>> print('C:\nuova_cartella')
	  C:
	  uova_cartella
	  >>> print(r'C:\nuova_cartella')
	  C:\nuova_cartella
	  ```

### Stringhe su righe multiple

!!!note "Stringhe e liste"
	La maggior parte dei concetti che vedremo nel seguito sono applicabili anche alle liste. Anzi, per essere precisi, derivano proprio dalle liste, in quanto Python considera una stringa un particolare tipo di lista.

Le stringhe possono articolarsi su più righe. Per farlo, possiamo usare le *triple-quotes*, ovvero tre virgolette di seguito, per indicare l'inizio e la fine della stringa:

```py linenums="1" hl_lines="1 3"
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

```py linenums="1"
>>> stringa_a = "Prima stringa"
>>> stringa_b = "Seconda stringa"
>>> print(stringa_a + " - " + stringa_b)
Prima stringa - Seconda stringa
```

!!!note "Nota"
	Se usiamo l'operatore `*` possiamo concatenare più volte la stessa stringa:
	> ```py
	  >>> 3 * 'co.'
	  'co.co.co.'
	  ```

Possiamo anche semplicemente porre le due stringhe l'una di seguito all'altra:

```py
>>> "Py" "thon"
'Python'
```

!!!warning "Attenzione"
	Bisogna fare particolare attenzione a non concatenare un *literal* (ovvero una stringa racchiusa tra virgolette) ad una *variabile di tipo stringa*. Se proviamo a farlo, l'interprete ci restituirà questo errore:
	> ```py
	  >>> py="Py"
	  >>> py "thon"
  	  File "<stdin>", line 1
      py "thon"
              ^
	  SyntaxError: invalid syntax
	  ```

	Lo stesso errore si presenterebbe se al posto della variabile `py` usassimo il risultato di una operazione di concatenazione:
	> ```py
      >>> ('p' + 'y') 'thon'
	  File "<stdin>", line 1
	      ('p' + 'y') 'thon'
						^
	  SyntaxError: invalid syntax
	  ```
	Il consiglio, in questi casi "ibridi", è quello di usare l'operatore standard di concatenazione, ovvero il `+`.

!!!note "Nota"
	Esistono modi più efficienti di concatenare delle stringhe, specialmente quando si ha a che fare con numerose operazioni di concatenazione in grossi cicli; l'approfondimento di tali metodi è demandato al lettore.

### Indicizzazione di stringhe

Python definisce le stringhe come degli *array di caratteri*; è quindi possibile indicizzarli. Ad esempio:

```py
>>> stringa = 'Python'
>>> stringa[0]
'P'
```

Anche i singoli caratteri sono considerati come delle stringhe, ovviamente di lunghezza unitaria:

```py
>>> lettera = 'P'
>>> lettera[0]
'P'
```

Python permette di accedere anche usando degli indici *negativi*, considerando quindi gli elementi che vanno da destra verso sinistra. In questo caso, l'indice del primo elemento da destra sarà indicato con `-1`:

```py
>>> stringa[-1]
'n'
```

### Slicing su stringhe

L'operazione di *slicing* permette di estrarre una certa parte di una stringa. In generale, assume la seguente forma:

```py
>>> stringa[i:j:s]
```

dove `i` è l'indice iniziale, `j` quello finale ed `s` lo step utilizzato. E' importante sottolineare come **l'elemento all'indice iniziale sarà incluso, mentre quello all'indice finale sarà escluso**.

Ad esempio:

```py
>>> stringa[0:2]
'Py'
>>> stringa[2:5]
'tho'
```

Se volessimo considerare *tutti i caratteri fino a `j`* (escluso), dovremmo usare la seguente notazione:

```py
>>> stringa [:j]
```

Se invece volessimo considerare *tutti i caratteri a partire da `i`* (incluso), dovremmo usare la seguente notazione:

```py
>>> stringa [i:]
```

Ad esempio:

```py
>>> stringa[1:]
'ython'
>>> stringa[:5]
'Pytho'
```

Anche in questo caso, è possibile usare degli indici negativi. Ad esempio, se volessimo prendere tutti i caratteri dalla terzultima lettera fino alla fine, potremmo scrivere:

```py
>>> stringa[-3:]
'hon'
```

mentre se volessimo prendere tutti i caratteri fino alla terzultima lettera (esclusa):

```py
>>> stringa[:-3]
'Pyt'
```

!!!tip "Suggerimento"
	E' possibile ottenere un'intera stringa mediante l'operazione di slicing in questo modo:
	> ```py
	  >>> stringa[:]
	  'Python'
	  ```

### Lunghezza di una stringa

La funzione `len()` ci restituisce la lunghezza di una stringa:

```py
>>> len(stringa)
6
```

### Immutabilità di una stringa

Le stringhe in Python sono *immutabili*. Come indica la parola stessa, questo significa che *non possono essere modificate*: se, ad esempio, provassimo a ridefinirne uno o più elementi, acceduti magari mediante indexing o slicing, avremmo un errore.

```py
>>> stringa[0] = 'C'# Errore!
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

!!!tip "Suggerimento"
	Possiamo comunque assegnare il nome `stringa` ad una nuova variabile.

## Liste

Abbiamo già detto che una stringa altro non è se non un caso particolare di *lista*. La domanda che sorge spontanea è quindi: *cosa è una lista*?

Le liste sono uno dei quattro tipi di strutture *built-in* che Python offre per memorizzare sequenze di dati. Da un punto di vista puramente "concettuale", potremmo considerarle alla stregua degli array presenti in altri linguaggi di programmazione, seppur con alcune, significative differenze.

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

### Alcuni esempi

Ecco alcuni esempi di slicing su lista, con annessi risultati ottenibili.

Consideriamo la seguente stringa:

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
>>> l[-3::2]
[4, 6]
```

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
>>> lista [0] = stringa
>>> lista
['Python', 2, 3, 4, [1, 2, 3]]
```

## Conclusioni

Abbiamo dato una rapida introduzione al linguaggio Python, soffermandoci su alcune dei tipi di dati più usati, come numeri, stringhe e liste. Nelle prossime sezioni, torneremo sulle liste, ed approfondiremo altri tipi di iterabili, come tuple e dizionari.
