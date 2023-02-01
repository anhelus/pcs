# Pathlib

In questa lezione, vedremo come lavorare con i file path (nomi di cartelle e file) in Python. Apprenderemo nuovi modi per scrivere e leggere file, manipolare percorsi ed il sottostante file system, così come alcuni esempi di come elencare i file d iterarvi.

## Il problema con la gestione del percorso dei file in Python

Lavorare con i file ed interagire con il file system è importante per diverse ragioni. Nei casi più semplici, dovremo soltanto leggere o scrivere file ma, alle volte, avremo a che fare con task più complesse. Forse dovremo elencare tutti i file in una caretella di un dato tipo, trovare la cartella padre di un dato file, o creare un nome di un file univoco che non esiste già.

Tradizionalemnte, Python ha rappresentato i percorsi dei file usando delle normali stringhe di testo. Grazie alla libreria standard os.path, questo è stato adeguato ancche se leggermente complesso.Tuttavia, dal moemnto che i percorsi *non* sono stringhe, diverse funzionalità vengono in realtà sparse qua e la per tutta la libreria standard, in librerie come os, glob e shutil. Il seguento esempio ha bisogno di tre import semplicemente per spoistare tutti i file di testo in un'altra cartella:

```py
import glob
import os
import shutil

for file_name in glob.glob('*.txt'):
    new_path = os.path.join('archive', file_name)
    shutil.move(file_name, new_path)
```

Con dei path rappresentati da delle stringhe, è possibile, anche se normalmente è una cattiva idea, usare i normali metodi usati sulle stringhe. Ad esempio, invece di unire due percorsi con un + come due stringhe normali, dovremmo usare os.path.join(), che unisce dei path usando il corretto separatore del sistema operativo. 

!!!tip "Suggerimento"
    Ricordiamo in tal senso che, ad esempio, Widnows usa il backslash \, mentre Mac e Linux usano il forward slash /. Questa differenza è spesso foriera di errori.

Il modulo pathlib è stato introdotto in Python 3.4 per affrontare queste sfide. Raccoglie le funzionalità necessarie in un unico posto, e le rende disponibili attraverso metodi e proprietàù un un oggetto Path.

Fino a Python 3.6, altri package usavano ancora le stringhe per i file path, ma da questa versione di Python il modulo pathlib è supportato nella standard library, in parte grazei all'aggiunga di un protocollo per il file system path (PEP 519).

## Creazione di Path

Tutto quello che dobbiamo sapere è sulla classe Path. Vi sono diversi modi di creare un path. Per priam cosa, ci sono dei metodi di classe come cwd() ed home che, rispettivamente, indicano la cartella attuale e la nostra home:

```py
>>> from pathlib import Path
>>> Path.cwd()
WindowsPath('C:/Users/acard/Documents/GitHub/Lavoro/Corsi/PCS')
>>> Path.home()
WindowsPath('C:/Users/acard')
```

Possiamo creare un path anche esplicitamente a partire da una stringa:

```py
>>> Path('C:/Users/acard/Documents')
WindowsPath('C:/Users/acard/Documents')
```

Un piccolo suggerimento qunado abbiamo a che fare con i path su Windows: abbiamo già visto che il separatore è il backslash, che però viene anche usato come *escape character*é per rappresentare dei caratteri che non è possibile stampare. Per eviotare problemi, usiamo dei *raw string literal* per rappresentare i percorsi Python; in altre parole, dobbiamo indicare a Python che stiamo usando delle stringhe pure anteponendo la lettera `r`:

```py
>>> Path(r'C:\Users\acard\Documents')  
WindowsPath('C:/Users/acard/Documents')
```

Un terzo modo per costruire un path è quello di unire le varie parti del path usando l'operatore `/`:

```py
>>> pathlib.Path.home() / 'Documents'
WindowsPath('C:/Users/acard/Documents')
```

L'operatore `/` può unider più di un path, oppure un insieme di path e stringhe (come sopra) fino a che vi almeno un oggetto di tipo `Path`. Se non ci piace la notazione `/`, possioamo fare la stessa cosa con il metodo `.joinpath()`:

```py
>>> Path.home().joinpath('Documents')     
WindowsPath('C:/Users/acard/Documents')
```

Notiamo che negli esempi precednti, `Path` è rappresentato o come un `WindowsPath` o come un `PosixPath`. L'oggettov ero e proprio che rappresenta il percorso dipende dal sistema operativo sottostante.

## Leggere e scrivere file

Tradizionalmente, il mdoo per leggere o scrivere un file in Python è stato mediatne il metodo `open()`. Questo è sempre vero, in qunato la funzione `open()` può usare dierttamente gli oggetto `Path`. Il seguente esempio trova tutti gli header in un file Markdown stampandoli a schermo:

```py
path = Path.cwd() / 'test.md'
with open(path, mode='r') as f:
    headers = [line.strip() for line in f if line.startswith('#')]
print('\n'.join(headers))
```

Un modo equivalente è quello di chiamare la funzione open direttamente sull'oggetto Path:

```py
with path.open(mode='r') as f:
    ...
```

Infatti, `Path.open()` sta chiuamando la funzione integrata `open()` dietor le scene. Quale opzione scegliamo di usare è semplicemente una questione di gusto.

Per la semplice lettura e scrittrura di file, ci sono un paio di metodi utili nella libreria `pathlib`:

* `.read_text()`: apre il percorso in modalità testuale e restituisce i contenuti come stirnga.
* `.read_bytes()`: apre il percros in modalità binaria e restituisce i contenuti come una byutestring.
* `.write_text()`: apre il percorso e scrive dei dati sotto forma di stringa
* `.write_bytes()`: apre il percorso in modalità bianria e vi scrive dei dati

Ognuno di questi meotdi gestisce l'apertura e la scrittura del file, rendendoli semplici da usare, ad esempio:

```py
>>> path = Path.cwd() / 'test.md'
>>> path.read_text()
<contenuti del file test.md>
```

I path possono anche essere specificati come semplici nomi dei file, nel qual caso sono interpertati relativamente all'attuale cartella di vlavoro. Il seguente esempio è equivalentne al precedente:

```py
>>> Path('test.md').read_text()
<contenuti del file test.md>
```

Il metodo `resolve()` trova il percorso completo ddel file.

```py
>>> path = Path('test.md')
>>> path.resolve()
TODO PATH
```

Possiamo anche comparare dei path. Ad esempio, possiamo confermare che il file test.md si trova nella cartella attuale:

```py
>>> path.resolve().parent == Path.cwd()
```

## Scegliere i componenti di un Path

https://realpython.com/python-pathlib/#picking-out-components-of-a-path
