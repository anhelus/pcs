# 1.3.2 - Pathlib

In questa lezione vedremo come lavorare direttamente con i *percorsi* (*path*) di cartelle, file, o librerie. Ciò sarà molto importante per leggere e scrivere su file, oltre che navigare tra le cartelle e, in generale, manipolare il file system della macchina su cui girerà il nostro codice.

Fino a qualche anno fa, il percorso di un file veniva rappresentato in Python mediante delle stringhe. Ad esempio, se volessimo spostare tutti i file di testo presenti nella cartella di lavoro in un'altra cartella chiamata `archivio` avremmo bisogno di usare tre import:

```py
import glob
import os
import shutil

for file in glob.glob('*.txt'):
    new_path = os.path.join('archivio', file)
    shutil.move(file, new_path)
```

Nonostante questa semplificazione funzioni, tuttavia, il percorso di un file *non è realmente una stringa*, quanto piuttosto una "foglia" in un albero gerarchico che rappresenta la struttura delle cartelle da navigare per raggiungere al file richiesto. Questo ha comportato la necessità di suddividere diverse funzionalità tra loro legate tra diverse librerie della libreria standard Python, tra cui [`os`](https://docs.python.org/3/library/os.html), [`glob`](https://docs.python.org/3/library/glob.html) e [`shutil`](https://docs.python.org/3/library/shutil.html).

Inoltre, la rappresentazione del percorso di un file cambia a seconda del sistema operativo utilizzato: ricordiamo infatti che il separatore in Windows è rappresentato dal carattere di backslash (`\`), mentre nei sistemi Unix-like dal forward slash (`/`). Di conseguenza, usare delle stringhe per caratterizzare il percorso di uno o più file rende la nostra rappresentazione non generalizzabile.

!!!tip "La funzione join()"
    Esiste un rudimentale modo di affrontare questo problema utilizzando il metodo `join()` del modulo `os.path`, unendo quindi due percorsi mediante il separatore adatto al nostro sistema operativo.

Per questi (ed altri) motivi, quindi, è stato necessario introdurre nella libreria standard un modo che permettesse al codice Python di approcciarsi ai percorsi per quello che effettivamente sono: tale metodo è stato introdotto a partire da Python 3.4 grazie alla libreria [`pathlib`](https://docs.python.org/3/library/pathlib.html).

## La classe Path

La libreria `pathlib` mette a disposizione la classe [`Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path) per la gestione del percorso di un file. Per creare un oggetto di questa classe potremo usare diversi approcci; vediamone alcuni, non prima però di aver importato la classe `Path`.

```py
>>> from pathlib import Path
```

##### Metodo `cwd()`

Il metodo `cwd()` ci restituisce il percorso della cartella in cui è collocato lo script da cui stiamo richiamando l'istruzione. Supponendo di essere nella cartella `Documents` dell'utente `user` su Windows, allora:

```py
>>> Path.cwd()
WindowsPath('C:/Users/user/Documents')
```

##### Metodo `home()`

Il metodo `home()` restiuisce la cartella Home dell'utente attuale. Nel caso precedente:

```py
>>> Path.home()
WindowsPath('C:/Users/user')
```

##### Creazione di un path in modo esplicito

Possiamo creare un path in maniera esplicita passando una stringa al costruttore della classe `Path`:

```py
>>> Path('C:/Users/user/Documents')
WindowsPath('C:/Users/user/Documents')
```

!!!warning "Backslash su Windows"
    Abbiamo visto che il separatore dei percorsi in Windows è il backslash. Tuttavia, questo simbolo viene usato anche come escape character per rappresentare dei caratteri che, altrimenti, non è possibile stampare a schermo. In tal senso, per evitare l'insorgere di errori, è possibile utilizzare dei *raw string literal*, ovvero delle stringhe "grezze" (*raw*). Ad esempio, nel caso precedente scriveremo:
    > ```py
      >>> Path(r'C:\Users\user\Documents')  
      WindowsPath('C:/Users/user/Documents')
      ```

Un altro modo per costruire un path è unire le varie parti dello stesso usando l'operatore `/`:

```py
>>> pathlib.Path.home() / 'Documents'
WindowsPath('C:/Users/user/Documents')
```

Da notare che l'operatore `/` permette di unire anche più di un path, oltre che un insieme di oggetti di tipo `Path` e stringhe (a patto che, ovviamente, vi sia almeno un oggetto di tipo `Path`). In alternativa, possiamo ottenere lo stesso effetto con il metodo `joinpath()`:

```py
>>> Path.home().joinpath('Documents')     
WindowsPath('C:/Users/user/Documents')
```

!!!note "Path, WindowsPath e PosixPath"
    Negli esempi precedenti, utilizzare la classe `Path` ha sempre portato in output un `WindowsPath`. Ciò è legato al fatto che questi esempi sono stati scritti su un sistema Windows; se si fosse utilizzaton un sistema Unix-like, i path risultanti sarebbero stati dei `PosixPath`. In pratica, la classe vera e propria che caratterizza il path dipende dal sistema operativo su cui viene eseguito il nostro programma.

### 9.2.2 I/O su file

#### Apertura di un file

Per leggere da o scrivere su un file Python si è utilizza il metodo `open()` che, convenientemente, può essere usato direttamente con gli oggetti di classe `Path`. Ad esempio, se volessimo leggere tutti i commenti in un file Python, potremmo usare la seguente funzione:

```py
def leggi_commenti(file_path):
    with open(file_path, 'r') as f:
        commenti = [line.strip() for line in f if line.startswith('#')]
    return '\n'.join(commenti)

leggi_commenti('test.py')
```

In realtà, possiamo anche chiamare la funzione `open()` messa a disposizione dall'oggetto `Path`:

```py
with path.open(mode='r') as f:
    # ...
```

In pratica, `Path.open()` chiama internamente la `open()`. Di conseguenza, l'utilizzo dell'una o dell'altra funzione è semplicemente una questione di preferenze personali.

#### Lettura e scrittura

Per le operazioni di lettura e scrittura su file `pathlib` mette a disposizione i metodi mostrati nella tabella 9.1.

| Metodo | File aperto come... | Tipo di interazione |
| ------ | -------------------- | ------------------- |
| `.read_text()` | File di testo | Contenuti restituiti come stringa |
| `.read_bytes()` | File binario | Contenuti restituiti come binario |
| `.write_text()` | File di testo | Scrittura di contenuti come stringa |
| `.write_bytes()` | File binario | Scrittura di contenuti come binari |

Tutti i metodi gestiscono autonomamente l'apertura e l'interazione con il file. Ad esempio, per leggere i contenuti di un file di testo:

```py
>>> path = Path.cwd() / 'test.txt'
>>> path.read_text()
<contenuti del file test.txt>
```

I path possono essere specificati anche come semplici nomi di file. In questo caso, ovviamente, Python assumerà che siano all'interno dell'attuale cartella di lavoro. Ad esempio, un'altra forma di esprimere il codice precedente è questa:

```py
>>> Path('test.txt').read_text()
<contenuti del file test.md>
```

#### Percorso di un file

Per avere il percorso completo (assoluto) di un file possiamo usare il metodo resolve():

```py
>>> path = Path('test.txt')
>>> path.resolve()
WindowsPath('C:/Users/user/Documents/test.txt')
```

## 9.3 - Attributi di un path

TODO DA QUI

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
