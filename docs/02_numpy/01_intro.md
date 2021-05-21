# Introduzione a NumPy

La libreria **NumPy** (abbreviazione che sta per *Num*erical *Py*thon) è quella maggiormente usata nel campo del calcolo scientifico in Python, e ne rappresenta uno standard *de facto*, in quanto le API messe a disposizione da NumPy sono estensivamente utilizzate dalla quasi totalità degli altri package dedicati alle scienze ed all'ingegneria.

## Installazione

Al momento di installare NumPy, possiamo optare per due opzioni. La prima è quella di usare una distribuzione "scientifica" di Python; quella più usata è [Anaconda](https://www.anaconda.com).

La seconda strada, che è quella che seguiremo, è sfruttare un'installazione "standard" di Python, creando un apposito ambiente virtuale ed il *dependency manager* [pipenv](https://pypi.org/project/pipenv/).

Creiamo quindi una cartella, e creiamo un nuovo ambiente virtuale con NumPy usando questo comando:

```sh
mkdir python-data-science
cd python-data-science
pipenv install numpy
```

All'interno della cartella troveremo due file: 

* `Pipfile`, che conterrà l'elenco dei pacchetti che abbiamo installato in quello specifico ambiente virtuale;
* `Pipfile.lock`, che conterrà i riferimenti alle versioni dei singoli pacchetti installati.

!!!warning "Attenzione"
	**Non** modifichiamo **mai** direttamente i file generati da pipenv. Per farlo, esistono comandi appositi che illustreremo man mano che ne avremo bisogno.

## Importare NumPy

Abbiamo visto in precedenza che per usare un package o un modulo Python all'interno dei nostri script dovremo per prima cosa renderli "visibili". Faremo ovviamente lo stesso con NumPy, anteponendo questa direttiva in ogni modulo nel quale lo useremo:

```py
import numpy as np
```

## Gli `ndarray`

La struttura dati alla base di NumPy è quella degli *array*. Più precisamente, NumPy offre una struttura chiamata `ndarray`, rappresentante un array ad $n$ dimensioni contenente dati di tipo *omogeneo*. E' interessante notare come anche `ndarray` sia un'abbreviazione, stante per *n*-*d*imensional *array*. 

La dichiarazione ed inizializzazione di un `ndarray` è molto simile a quella di una classica lista Python:

```py
>>> a = numpy.array([1, 2, 3])
```

Questa sintassi, però, non deve trarci in inganno. Esistono, infatti, varie differenze che intercorrono tra un `ndarray` ed una classica sequenza Python, ovvero:

1. un `ndarray` ha una dimensione fissata al momento della creazione, a differenza della lista. Cambiare la dimensione di un array creerà quindi un *nuovo* array, cancellando quello originario;
2. gli elementi di un `ndarray` devono essere dello stesso tipo;
3. gli array rendono più semplici ed efficienti le operazioni algebriche, specialmente su matrici di grosse dimensioni.

## Efficienza di NumPy

Il terzo punto è particolarmente importante, sopratutto nell'ambito del calcolo scientifico. Come semplice esempio, consideriamo una moltiplicazione elemento per elemento tra due vettori della stessa dimensione.

Con due liste, potremmo usare un ciclo `for`:

```py
c = []
for i in range(len(a)):
    c.append(a[i]*b[i])
```

oppure una *list comprehension*:

```py
c = [a[i] * b[i] for i in range(len(a))]
```

In entrambi i casi, l'operazione verrà effettuata in maniera corretta; tuttavia, se i vettori sono di dimensioni importanti, avremo un costo da pagare legato all'inefficienza di Python nella gestione dei cicli.

Ovviamente, dato che le inefficienze sono legate al Python (e, quindi, all'*overhead* introdotto principalmente dall'interprete), la soluzione più semplice sarebbe quella di utilizzare un altro linguaggio, come ad esempio il C. In questo caso, l'operazione precedente sarebbe associata a questo codice:

```c
for (i = 0; i < rows; i++) {
    c[i] = a[i] * b[i];
}
```

Problema risolto, dunque? Per un caso così semplice, sì. Immaginiamo però di voler estendere il caso precedente a due dimensioni; il codice diverrà:

```c
for (i = 0; i < rows; i++) {
    for (j = 0; j < columns; j++) {
        c[i][j] = a[i][j] * b[i][j];
    }
}
```

Appare quindi chiaro come anche un leggero aumento della complessità delle operazioni da effettuare comporti un significativo aumento della complessità in termini di codice. Ed è proprio qui che NumPy ci viene in aiuto.

Infatti, l'operazione precedente può essere riassunta in NumPy come segue:

```py
c = a * b
```

La sintassi è evidentemente molto più concisa e semplice, sia rispetto al C, sia rispetto al caso in cui si usino delle liste in Python. Inoltre, è la stessa sintassi che viene solitamente usata nelle formule reali! Oltre a questo, NumPy sfrutta codice *precompilato* in C: questo significa che la precedente operazione sarà svolta *quasi* alla stessa velocità del codice scritto in linguaggio C.

Si tratta, quindi, di unire il "meglio" dei due mondi: da un lato, l'eleganza e semplicità sintattica del Python e, dall'altro, l'efficienza del C.

## Vettorizzazione e broadcasting

Due importanti concetti sfruttati da NumPy sono quelli di *vettorizzazione* e *broadcasting*.

La vettorizzazione ci permette di scrivere codice senza cicli o indici espliciti; ovviamente, *i cicli ci sono*, ma avvengono *sotto al cofano*, grazie al codice C precompilato. Il codice vettorizzato, inoltre, presenta diversi vantaggi, soprattutto in termini di leggibilità e manutenibilità.

Il concetto di *broadcasting* riguarda invece il comportamento implicito delle operazioni, e permette di usare la stessa sintassi *indipendentemente* dalle dimensioni degli `ndarray` coinvolti (e dall'operazione effettuata, sia essa algebrica, logica, etc.).
