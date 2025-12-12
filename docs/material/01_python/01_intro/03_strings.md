# 1.1.3 - Stringhe

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

!!!note "Raw Strings"
	Tutti i caratteri preceduti dal simbolo `\` saranno interpretati come escape character, a meno di aggiungere il simbolo `r` prima dell'inizio della stringa:
	> ```py
	  >>> print('C:\nuova_cartella')
	  C:
	  uova_cartella
	  >>> print(r'C:\nuova_cartella')
	  C:\nuova_cartella
	  ```

## Stringhe su righe multiple

!!!note "Stringhe e sequenze"
	La maggior parte dei concetti che vedremo nel seguito sono applicabili anche ad ogni tipo di *sequenza*. Anzi, per essere precisi, Python considera una stringa un particolare tipo di sequenza!

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

## Concatenazione di stringhe

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

### Le f-strings

Sebbene la concatenazione con l'operatore `+` svolga il suo lavoro, nelle versioni più recenti di Python è stato introdotto il concetto di *f-string* (*formatted string literals*), che richiama i concetti utilizzati dalla libreria standard C per la funzione `printf`. Nella pratica, è necessario anteporre una `f` alla stringa, ed inserire tra parentesi graffe le variabili che si vogliono formattare, le quali saranno formattate in maniera automatica. Ad esempio:

```py
>>> nome = "Mario"
>>> eta = 30
>>> print(f"{nome} ha {eta} anni.")
Mario ha 30 anni.
```

Qualora si voglia gestire in maniera più "granulare" la formattazione, ad esempio per un tipo numerico, potremo specificare la formattazione che riteniamo più opportuna:

```py
>>> accuratezza = 0.87564
>>> print(f"Accuratezza del modello: {accuratezza:.2f}") # Arrotonda a 2 decimali
Accuratezza del modello: 0.88
```

## Indicizzazione di stringhe

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

## Slicing su stringhe

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

## Lunghezza di una stringa

La funzione `len()` ci restituisce la lunghezza di una stringa:

```py
>>> len(stringa)
6
```

## Immutabilità di una stringa

Le stringhe in Python sono *immutabili*. Come indica la parola stessa, questo significa che *non possono essere modificate*: se, ad esempio, provassimo a ridefinirne uno o più elementi, acceduti magari mediante indexing o slicing, avremmo un errore.

```py
>>> stringa[0] = 'C'# Errore!
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

!!!tip "Suggerimento"
	Possiamo comunque assegnare il nome `stringa` ad una nuova variabile.

## Funzioni fondamentali per le stringhe

Chiudiamo questa panoramica introducendo alcuni metodi che è possibile usare sulle stringhe, richiamati nella seguente tabella.

| Metodo | Descrizione | Esempio | Risultato |
| ------ | ----------- | ------- | --------- |
| `.lower()` | Converte tutto in minuscolo | `'Ciao'.lower()` | `'ciao'` |
| `.upper()` | Converte tutto in maiuscolo | `'Ciao'.upper()` | `'CIAO'` |
| `.strip()` | Rimuove spazi a inizio/fine | `'  x  '.strip()` | `'x'` |
| `.replace(old, new)` | Sostituisce sottostringhe | `'1,5'.replace(',', '.')` | `'1.5'` |
| `.split(sep)` | Divide la stringa in una lista | `'a-b-c'.split('-')` | `['a', 'b', 'c']` |
| `.join(iterable)` | Unisce una lista in stringa | `'-'.join(['a', 'b'])` | `'a-b'` |