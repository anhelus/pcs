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

Le diverse parti di un path sono disponibili sotto forma di property. Deglie sempi basilari includono:

* .name: il nome del fiel senza alcuna directory
* .parent: la cartella che contiene il file, o la cartella padre se il path è una cartella
* .stem: il nome del file senza l'estensione
* .suffix: l'estensione del file
* .anchor: la parte del path prima delle cartelle

Ecco degli esempio:

```py
>>> path
PosixPath('/home/gahjelle/realpython/test.md')
>>> path.name
'test.md'
>>> path.stem
'test'
>>> path.suffix
'.md'
>>> path.parent
PosixPath('/home/gahjelle/realpython')
>>> path.parent.parent
PosixPath('/home/gahjelle')
>>> path.anchor
'/'
```

Da notare che .parent restituisce un nuovo oggetto di tipo Path, metnre le altre proprietà restituiscono delle stringhe. Questo significa ad esempio che .parent può essere concatenato come nell'ultimo esempio, o anche combinato con / per creare dei nuovi path:

```py
>>> path.parent.parent / ('new' + path.suffix)
PosixPath('/home/gahjelle/new.md')
```

## Spostare e cancellare dei file

Attraverso pathlib, avremo accesso anche ad operazioni base a livello di file system, come muovere, aggiornare ed anche cancellare i file. Per la maggior parte, questi metodi non ci danno un feedback prima di spostare o cancellare informazioni, quindi conviene fare attenzione.

Per spostar eun file, usiamo .replace(). Notiamo che se la destinazione esiste già, .replace() la sovrascriuverà. Sfortunatamente, pathlib non supporta esplcitiamente lo spsotamenteo safe dei file. Per evitrare di sovrascirvere il path di destinazione, il modo più semplice è quello di testare se la destinazione esiste prima di rimpiazare:

```py
if not destination.exists():
    source.replace(destination)
```

Tuttavia, questo lascia aperta la porta ad una possibile race condition. Un altro processo potrebbe agigungere un path di destinazione tra l'esecuzione dell'istruzione if ed il metodo .replace(). Se questo è un problema, un podo più semplice è quello di aprire il percorso di destinazione per la creazione esclusiva e copiare esplicitamente i dati sorgenti:

```py
with destination.open(mode='xb') as fid:
    fid.write(source.read_bytes())
```

Questo codice lancerà un `FileExistsError` se la destinazione esiste già. Tecnicamente, questo copia un file. Per effettuare lo spostamento, limitiamoci a cancellare il sorgente dopo che la copia è stata fatta (vediamod i seguito). Assicuriamoci inoltre che non sia stata lanciata alcuna eccezione.

Quando stiamo rinominando i file, dei meotdi utili potrebbero essere `.whit_name()` e `.with_suffix()`. Entrambi restituiscono il path originario ma con il noem o o il suffisso rimpiazzato, rispettivamente.

Ad esempio:

```py
>>> path
PosixPath('/home/gahjelle/realpython/test001.txt')
>>> path.with_suffix('.py')
PosixPath('/home/gahjelle/realpython/test001.py')
>>> path.replace(path.with_suffix('.py'))
```

Le cartelle ed i file possono essere cancellati usando `.rmdir()` ed `.unlink()`, rispettivamente.

## Esempi

Vediamo alcuni esempi di come usare `pathlib` per affrontare alcune semplici sfide.

### Conteggio dei file

Ci sono alcuni modi differenti per elencare molti file. Il più semplice è il metodo `.iterdir()`, che itera su tutti i file in una data cartella. Il seguente esempio combina `.iterdir()` con la classe `collections.Counter` per contare quanti file ci sono di ogni tipo nella cartella attuale.

```py
>>> import collections
>>> collections.Counter(p.suffix for p in pathlib.Path.cwd().iterdir())
Counter({'.md': 2, '.txt': 4, '.pdf': 2, '.py': 1})
```

Un elenco più flessibile dei file può essere creato con i metodi `.glob()` ed `.rglob()` (recursive glob). Ad esempio, `pathlib.Path.cwd().glob('*.txt')` restituisce tutti i file con estensione `.txt` nella cartella attuale. Il seguente codice conta soltanto i tipi di file che iniziano con `p`:

```py
>>> import collections
>>> collections.Counter(p.suffix for p in pathlib.Path.cwd().glob('*.p*'))
Counter({'.pdf': 2, '.py': 1})
```

## Mostare l'albero di una cartella

Il seguente esempio definisce una funzione, tree(), che manderà a schermo un albero che rappresenta la gerarchia di file, con radice una certa cartella. Qui, vogliamo elencare le sottocartelle anche, per cui useremo il metodo `.rglob()`.

```py
def tree(directory):
    print(f'+ {directory}')
    for path in sorted(directory.rglob('*')):
        depth = len(path.relative_to(directory).parts)
        spacer = '    ' * depth
        print(f'{spacer}+ {path.name}')
```

Notiamo che dobbiamo sapere quanto lontano dalla cartella radice è collocato un file. Per falro, usiamo per prima cosa `.relative_to()` per rappresentare un eprocros relativamente alla cartella radice. Quindi, contiamo il numero di cartelle (usando la proprietà `.parts`) nella rappresentazione. QUando eseguita, qeusta funzione crea un albero visu9ale come il seguente:

```py
>>> tree(pathlib.Path.cwd())
+ /home/gahjelle/realpython
    + directory_1
        + file_a.md
    + directory_2
        + file_a.md
        + file_b.pdf
        + file_c.py
    + file_1.txt
    + file_2.txt
```

## Trovare l'ultimo file modificato

Im metodi `.iterdir()`, `.glob()`, ed `.rglob` sono ottimi per i generator e le list comprehension. Per trovare il file in una cartella modificato per ultimo, possiamo usar eil metodo `.stat()` per ottenere informaizoni circa i file sottostanti. Per esempio, `.stat().st_mtime` ci dà il momento dell'ultima modifica ad un file:

```py
>>> from datetime import datetime
>>> time, file_path = max((f.stat().st_mtime, f) for f in directory.iterdir())
>>> print(datetime.fromtimestamp(time), file_path)
2018-03-23 19:23:56.977817 /home/gahjelle/realpython/test001.txt
```

Possiamo anche ottenere i contenuti del file che è stato modificato epr un'ultimo con una simile espressione:

```py
>>> max((f.stat().st_mtime, f) for f in directory.iterdir())[1].read_text()
<the contents of the last modified file in directory>
```

Il timestamp restituito dalle diverse proprietà `.stat().st_` rappresenta i secondi dal primo gennaio 1970. Oltre a `datetime.fromtimestamp`, `time.localtime` o `time.ctime` possono essere usati per convertire il timestamp in qualcosa di più utilizzabile.

## Creare un nome del file univoco

L'ultimo esempio ci mostra come costruire un file con numero univoco basato su una tempalte. Per prima cosa, specifichiamo un pattern per il nome del file, con spazio per un contatore. Quindi, controlliamo l'esistenza dle percorso del file creato unendo una cartella ed il nome del file (con un valore per il contatore). SE esiste già, aumentiamo il contatore e proviamo di nuovo:

```py
def unique_path(directory, name_pattern):
    counter = 0
    while True:
        counter += 1
        path = directory / name_pattern.format(counter)
        if not path.exists():
            return path

path = unique_path(pathlib.Path.cwd(), 'test{:03d}.txt')
```

Se la cartella contiene già i file test001.txt e test002.txt, il codice precedente imposterà il path a test003.txt.

## Differenze tra sistemi operativi

In precedenza, abbiamo notato che abbiamo istanziato pathlib.Path, ed abbiamo ottenuto in ritorno un WindowsPath o un PosixPath. Il tipo di oggetto dipende dal sistema operativo utilizzato. Questa feature rende semplice scrivere del codice cross-platform. E' possibile richiedere esplcitiamente un WindowsPath o un PosixPath, ma staremmo limitando il codice a quel sistema, senza alcun beneficio. Un path concreto come questo non può essere usato su un sistema differente:

```py
>>> pathlib.WindowsPath('test.md')
NotImplementedError: cannot instantiate 'WindowsPath' on your system
```

Ci sono delle volte dove abbiamo bisogno della rappresentazione di un path senza accedere al file system sottostante (nel qual caso potrebbe aver senso rappresentare un percorso Windows su un sistema non-Windows, o viceversa). Questo può essere fatto con degli oggetti di tipo PurePath. Questi oggetti supportano le operazioni discusse nella sezione sui Path Components, ma non i metodi che accedono al file system.

```py
>>> path = pathlib.PureWindowsPath(r'C:\Users\gahjelle\realpython\file.txt')
>>> path.name
'file.txt'
>>> path.parent
PureWindowsPath('C:/Users/gahjelle/realpython')
>>> path.exists()
AttributeError: 'PureWindowsPath' object has no attribute 'exists'
```

Possiamo istanziare direttaqmente un `PureWindowsPath`o un PurePosixPath su ttutti i sistemi. Istanziare un PurePath restituirà uno di questi oggetti a seconda del sistema operativo utilizzato.

## Path come oggetti veri e propri

Nell'introduzione, abbiamo notato brevemente che i path non sono stringhe, ed una motivazione dietro a questo è che pathlib rappresenta il file system cond egli oggetti veri e propri. Infatti, la documenbtazione ufficiale di pathlib è intitolata "pathlib - Object-oriented filesystem paths". L'approccio orientato agli oggetti è abbastanza visibile negli esempi precedenti (specialmente se lo mettiamo a confronto con la vecchia maniera usatga da `os.path`). Tuyttavia, vediamo qualche ultimo spunto.

Indipendentemente dal sistema operativo utilizzato, i path sono rappresentati in stile Posix, con lo slash come separatore del path. Su Windows, vedremo qualcosa come questo:

```py
>>> pathlib.Path(r'C:\Users\gahjelle\realpython\file.txt')
WindowsPath('C:/Users/gahjelle/realpython/file.txt')
```

Quando il path viene convertito in stringa, userà la forma nativa, per esempio con delle backslash su Windows:

```py
>>> str(pathlib.Path(r'C:\Users\gahjelle\realpython\file.txt'))
'C:\\Users\\gahjelle\\realpython\\file.txt'
```

Questo risulta essere particolarmente utile se stiamo usando una libreria che non sa come usare gli oggetti pathlib.Path. Qeusto è un grosso problema sulle versioni di Python antecedendi la 3.6. Ad esempio, in Python 3.5, la libreria standard configparser può usare solo dei path sotto forma di stringa per leggere dei file. Il modo di gestire questi casi è fare la conversione ad una stringa in maniera esplcitia.

```py
>>> from configparser import ConfigParser
>>> path = pathlib.Path('config.txt')
>>> cfg = ConfigParser()
>>> cfg.read(path)                     # Error on Python < 3.6
TypeError: 'PosixPath' object is not iterable
>>> cfg.read(str(path))                # Works on Python >= 3.4
['config.txt']
```

In Python 3.6 e successovo è raccomandabile usare `os.fpath()` invece di `str()` se dobbiamo fare una conversione esplciita. Questo è più sicuro, in quando lancerà un errore se proviamo a convertire accidentalmente un oggetto che non è un path.

Probabilmente, la parte più inusuale della libreria pathlibe è data dall'uso dell'operatore `/`. Vediamo come è implementato. Questo è un esempio di un overloading di operatore: il comportamento di un operatore cambia a seconda del contesto. Python implementa l'overloading di operatori attraverso l'uso dei *dunder metrhods*, ovvero dei metodi circondati da un doppio underscore.

L'operatore `/` è definito dal metodo `.__truediv__()`. Infatti, se diamo un'occhiata al codice sorgente di `pathlib`, vedremo qualcosa come:

```py
class PurePath(object):

    def __truediv__(self, key):
        return self._make_child((key,))
```

## Conclusion

Da Python 3.4 in poi, pathlib è stato reso disponibile nella libreria standard. Con pathlib, i path dei file possono essere rappresentati da oggetti Path veri e propri, invece di stringhe come in precedenza. Questi oggetti rendono l'uso dei path:

* più facile da leggere, specie perché `/` è usato per unire tra loro i path;
* più potente, con la maggior parte dei metodi necessari e delle proprietà disponibili direttamente sull'oggetto;
* più consistenti tra sistemi operativi, in quanto le pecularietà dei diversi sistemi sono nascoste dall'oggetto `Path`.
