# Script e moduli

## Un approccio migliore

Finora abbiamo interagito direttamente con l'interprete Python, lanciandolo da terminale ed eseguendo di volta in volta le istruzioni necessarie. Ovviamente questo approccio, seppur immediato, presenta diversi svantaggi, tra cui:

* non abbiamo il *syntax highlighting*;
* non siamo in grado di recuperare il codice una volta chiuso l'interprete;
* non possiamo verificare facilmente il funzionamento del codice;
* non possiamo modificare facilmente il codice.

Appare evidente come quindi non si tratti di un modo *ottimale* di sviluppare codice Python. Per questo, oltre al supporto di una IDE (cfr. [Appendice A](../04_appendici/a_configurazioni.md)), dovremo definire dei veri e propri *script*, che saranno salvati sotto forma di file con estensione `py`, e conterranno le istruzioni relative al nostro programma.

## Il primo script

Possiamo quindi provare a creare il nostro primo script Python. Per farlo, apriamo Visual Studio Code (o la nostra IDE di riferimento), e creiamo un file chiamato `main.py`, all'interno del quale inseriremo questo codice:

```py
# main.py
def hello_world():
	print('Hello, world')

hello_world()
```

Adesso apriamo un terminale, spostiamoci nella cartella nel quale abbiamo salvato questo script, ed eseguiamolo:

```sh
$ cd cartella_dove_risiede_lo_script
$ python main.py
```

A schermo, dovrebbe apparire la scritta `Hello, world`:

```sh
Hello, world
```

## L'approccio modulare

Utilizzare gli script permette di ovviare a diversi tra gli inconvenienti evidenziati in precedenza; tuttavia, quando le dimensioni della nostra *code base* (ovvero, la quantità di codice che scriviamo nei nostri programmi) iniziano ad essere "ingombranti", è opportuno adottare un approccio *modulare*, che prevede una separazione "fisica", ancorché logica, di parti di codice delegate a funzioni differenti.

### Un esempio

Immaginiamo di voler scrivere un programma che definisca delle funzioni per calcolare l'area delle principali figure geometriche. Modifichiamo quindi il nostro file `main.py` come segue:

```py
def calcola_area_quadrato(lato):
	return lato * lato


def calcola_area_rettangolo(base, altezza):
	return base * altezza


def calcola_area_triangolo(base, altezza):
	return (base * altezza) / 2


area_quadrato = calcola_area_quadrato(4)
area_rettangolo = calcola_area_rettangolo(2, 3)
area_triangolo = calcola_area_triangolo(2, 3)
```

Immaginiamo di voler quindi aggiungere una funzione di calcolo trigonometrico:

```py
import math

def calcola_tangente(angolo):
	return math.sin(angolo) / math.cos(angolo)


tangente_pi = calcola_tangente(math.pi)
```

Il codice del nostro file `main.py` comprenderà adesso funzioni di tipo geometrico e trigonometrico.

Cosa succederebbe se volessimo integrare delle funzioni di calcolo integrale, o di altro tipo? Ovviamente, ci sarebbe da un lato un aumento delle dimensioni della code base, dall'altro un "mix" tra funzioni che afferiscono ad ambiti differenti (seppur simili tra loro). Una buona idea sarebbe quindi quella di *separare* le diverse parti del programma, magari raggruppando le funzioni geometriche nel file `geometria.py`, le funzioni trigonometriche nel file `trigonometria.py`, e via discorrendo.

Questi file, che conterranno al loro interno prevalentemente funzioni (ma non solo), sono chiamati *moduli*.

!!!note "Nota"
	La linea che contraddistingue gli script dai moduli è molto sottile, e nei fatti è facile fare confusione ed utilizzarli in maniera "intercambiabile". Sottolineamo però che, idealmente, gli script devono contenere al loro interno soltanto del codice che sarà *eseguito*, mentre i moduli solo del codice che sarà *invocato* da uno o più script.

!!!note "Interprete e nome di un modulo"
	L'interprete è in grado di risalire al nome di un modulo dal nome del file in cui è contenuto. Se, ad esempio, definiamo un modulo nel file `geometria.py`, l'interprete associerà a quel modulo il nome `geometria`. Detto nome è inoltre accessibile globalmente e dall'interno del modulo richiamando la variabile globale `__name__`.

#### I moduli `geometria` e `trigonometria`

Creiamo adesso il file `geometria.py`, all'interno del quale "sposteremo" le funzioni definite in precedenza per il calcolo geometrico.

```py
# geometria.py
def calcola_area_quadrato(lato):
	return lato * lato


def calcola_area_rettangolo(base, altezza):
	return base * altezza


def calcola_area_triangolo(base, altezza):
	return (base * altezza) / 2
```

Analogamente, nel file `trigonometria.py` andremo a definire la funzione per il calcolo della tangente.

```py
import math

def calcola_tangente(angolo):
	return math.sin(angolo) / math.cos(angolo)
```

Riscriviamo ora il file `main.py`:

```py linenums="1"
import geometria
import trigonometria

if __name__ == "__main__":
	print(geometria.calcola_area_quadrato(4))
	print(trigonometria.calcola_tangente(math.pi))
```

Possiamo notare due cose.

1. In primis, stiamo richiamando le funzioni `calcola_area_quadrato()` e `calcola_tangente()` definite nei moduli `geometria` e `trigonometria`, rispettivamente. Questi moduli sono importati all'interno del nostro script mediante la direttiva `import`.
2. Alle righe 5 e 6, la "strana" sintassi mostrata serve a dichiarare quello che è il `main`, ovvero il punto di "accesso" al codice del nostro programma. Il `main` è normalmente presente in tutti i linguaggi di programmazione, alle volte sotto forme un po' differenti da quella qui mostrata; tuttavia, nel caso di script particolarmente semplici, il `main` può essere tranquillamente omesso, in quanto l'interprete riuscirà ad eseguirlo in maniera autonoma.

Proviamo a lanciare lo script; per farlo, digitiamo l'istruzione `python main.py` da terminale. A schermo, se tutto è andato per il verso giusto, vedremo i valori dell'area di un quadrato e della tangente di $\pi$.

## Usare gli import

Relativamente al modulo `geometria`, abbiamo usato esclusivamente la funzione `calcola_area_quadrato()`, "trascurando" le altre due funzioni comunque presenti nel modulo. In queste circostanze, possiamo usare una versione modificata della direttiva `import`, che assume la seguente forma:

```py
from modulo import funzione_o_classe
```

il che, nel nostro caso specifico, diventa:

```py
from geometria import calcola_area_quadrato
```

In questo modo, possiamo importare solamente quello che ci serve, il che risulta particolarmente utile a migliorare l'efficienza del nostro codice; il perché sarà chiaro a breve.

### Alias

La direttiva `import` ci permette di definire anche degli alias, particolarmente utili nel caso si usino dei nomi di package complessi. Ad esempio:

```py
import trigonometria as tr

print(tr.calcola_tangente(math.pi))
```

### La funzione dir()

La funzione `dir()` restituisce una lista con tutti i nomi (sia di funzione, sia di classe) definiti da un modulo. Ad esempio:

```py
>>> dir(geometria)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'calcola_area_quadrato', 'calcola_area_rettangolo', 'calcola_area_triangolo']
```

E' interessante notare come, oltre a funzioni, classi e variabili da noi definite, nel modulo `geometria` siano automaticamente definite *altre* variabili, che saranno importate usando import:

```py
import geometria

if __name__ == "__main__":
	print(geometria.__file__)
	print(geometria.calcola_area_quadrato(4))
```

Notiamo che saremo in grado di accedere alla variabile `__file__` del modulo `geometria`, che indica il percorso relativo dello stesso all'interno del file system. Ovviamente, questa variabile non è quasi mai utile, ma comporta un ulteriore carico sul codice, da cui diventa evidente l'importanza dell'opportuno uso della direttiva `from`.

### Moduli della libreria standard

Python ha diversi moduli appartenenti ad una libreria standard, i quali sono automaticamente disponibili a valle dell'installazione dell'interprete. Alcuni tra i più utilizzati sono:

* `sys`: è il modulo integrato nell'interprete, ed offre diverse utility necessarie al suo funzionamento;
* `os`: modulo delegato all'interazione con il sistema operativo su cui gira l'interprete;
* `time`: modulo usato per tutte le utility riguardanti il "cronometraggio" del tempo di esecuzione di una funzione;
* `datetime`: modulo usato per le funzionalità di data ed ora;
* `copy`: modulo usato per gestire, tra le altre cose, la deep copy di un oggetto.

Per una lista esaustiva, si rimanda alla [Python Library Reference](https://docs.python.org/3/library/).

## Package

Chiudiamo la trattazione con un accenno ai *package*, ovvero a delle vere e proprie "collezioni" che raggruppano moduli tra loro coerenti, in modo da facilitarne il successivo accesso. In pratica, i package non sono altro se non delle cartelle contenenti più moduli (quindi, file con estensione `nome_modulo.py`), oltre ad un file, chiamato `__init__.py`, che permette all'interprete di riconoscere quella cartella come package e, occasionalmente, contiene delle istruzioni di inizializzazione del package.

Per poter accedere ad un modulo contenuto all'interno di un package, possiamo usare la direttiva `import`, modificandola come segue:

```py
import nome_package.nome_modulo
# oppure...
from nome_package.nome_modulo import nome_funzione
```
