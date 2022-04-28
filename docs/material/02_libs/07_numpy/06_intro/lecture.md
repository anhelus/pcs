# 6. Introduzione a NumPy

La libreria **NumPy**, nome derivante dalla crasi tra *Num*erical *Py*thon, è una tra le più utilizzate nelle applicazioni di calcolo scientifico in Python.

Nella pratica, possiamo pensare a NumPy come ad uno standard *de facto*: infatti, le classi ed i metodi messi a disposizione dalla libreria sono estensivamente utilizzate nella quasi totalità degli altri tool Python per le scienze matematiche, chimiche e fisiche, oltre che per l'ingegneria.

Partiamo nella nostra disamina dalla procedura di installazione della libreria.

!!!note "Nota"
    In realtà, partiremo sempre dalla procedura di installazione, qualunque sia la libreria che analizzeremo.

## 6.1 Installare NumPy

Ricordiamo che le diverse opzioni utilizzabili per installare una libreria sono descritte nel dettaglio nell'[appendice B](../../appendix/02_libraries/lecture.md). Nel nostro caso, installeremo NumPy mediante 

### 6.1.1

La prima, e forse la più utilizzata universalmente, è quella di utilizzare il *package manager* (ovvero, il gestore di pacchetti) integrato in Python, chiamato `pip`.

Possia

Per installare NumPy è possibile optare per due opzioni. La prima è usare una distribuzione scientifica "predefinita" di Python (la più conosciuta è [Anaconda](https://www.anaconda.com)); la seconda, che è anche quella che seguiremo, è creare un apposito *ambiente virtuale* (cfr. Appendice B) con il gestore delle dipendenze [pipenv](https://pypi.org/project/pipenv/).

Creiamo quindi una nuova cartella all'interno della quale andremo ad ospitare tutti i nostri script, e spostiamoci all'interno della stessa:

```sh
$ mkdir python-data-science
$ cd python-data-science
```

A questo punto, usiamo pipenv per creare un nuovo ambiente virtuale ed installare NumPy:

==="Pip" 
	```sh
	pip install numpy
	```
==="Pipenv"
	```sh
	pipenv install numpy
	```

Una volta terminata la procedura, saranno presenti due file all'interno della cartella `python-data-science`:

* `Pipfile`, che conterrà l'elenco dei pacchetti che abbiamo installato in quello specifico ambiente virtuale;
* `Pipfile.lock`, che conterrà i riferimenti alle versioni dei singoli pacchetti installati.

!!!warning "Attenzione"
	**Non** modifichiamo **mai** direttamente questi due file. Per farlo, esistono comandi appositi, che saranno introdotti man mano che li useremo.

## Importare NumPy

Abbiamo visto in precedenza che per usare un package o un modulo Python all'interno dei nostri script dovremo per prima cosa renderli "visibili". Faremo ovviamente lo stesso con NumPy, anteponendo questa direttiva in ogni modulo nel quale lo useremo:

```py
import numpy as np
```

## Gli `ndarray`

La struttura dati alla base di NumPy è quella degli *array*. Più precisamente, NumPy mette a disposizione gli `ndarray`, che rappresentano degli array ad $n$ dimensioni contenenti dati di tipo *omogeneo*. 

!!!note "Il significato di `ndarray`"
    `ndarray` è un'abbreviazione che sta per *n*-*d*imensional *array*. 

La dichiarazione ed inizializzazione di un `ndarray` è in qualche modo simile a quella di una classica lista Python:

```py
>>> a = np.array([1, 2, 3])
```

In realtà, volendo essere precisi, possiamo affermare come esista un costruttore che crea un `ndarray` a partire da una lista, come mostrato nel codice precedente.

Questa sintassi, però, non deve trarre in inganno. Sono diverse le differenze che intercorrono tra un `ndarray` ed una classica lista; le principali possono essere riassunte nella seguente tabella.

| Caratteristica | `ndarray`                          | Lista                                 |
| -------------- | ---------------------------------- | ------------------------------------- |
| Dimensione     | Fissata al momento della creazione | Mutabile (ad esempio, con `append()`) |
| Elementi       | Omogenei (stesso tipo)             | Eterogenei (qualsiasi tipo)           |
| Ambito         | Operazioni algebriche              | General-purpose                       |

Commentiamo brevemente le differenze viste nella tabella precedente:

1. un `ndarray` ha una dimensione fissata al momento della creazione, a differenza della lista. Cambiare la dimensione di un array comporterà quindi la creazione di un *nuovo* array, con la cancellazione di quello originario. Nella lista, essendo mutabile, questo non avviene;
2. gli elementi di un `ndarray` devono essere dello stesso tipo, mentre le liste accettano qualsiasi tipo di elemento al loro interno;
3. gli array rendono più semplici ed efficienti le operazioni algebriche, specialmente su matrici di grosse dimensioni, mentre le liste sono progettate per supportare di ogni tipo.

### Efficienza di NumPy nelle operazioni algebriche

Il punto 3 dell'elenco precedente assume particolare rilevanza ai nostri fini. Per comprenderne il motivo, facciamo un semplice esempio, considerando una moltiplicazione *elemento per elemento* tra due vettori riga della stessa dimensione.

#### Approccio con liste

Usando due liste, potremmo usare un ciclo `for` o una list comprehension:

```py
# ciclo for
c = []
for i in range(len(a)):
    c.append(a[i]*b[i])
# list comprehension
c = [a[i] * b[i] for i in range(len(a))]
```

Il risultato dell'operazione sarà in entrambi i casi *corretto*. Tuttavia, i cicli sono computazionalmente *costosi*: ciò significa che, specialmente all'aumentare del numero di elementi contenuti nei vettori, sarà necessario pagare un costo crescente.

La soluzione sarebbe quindi quella di ricorrere ad un linguaggio più efficiente, come il C che, essendo compilato, riduce alcune delle inefficienze tipiche dei linguaggi interpretati. Il codice precedentemente diverrebbe quindi:

```c
for (i = 0; i < rows; i++) {
    c[i] = a[i] * b[i];
}
```

Problema risolto, dunque? Apparentemente sì. 

Immaginiamo però di voler estendere il caso precedente a due dimensioni; il codice diverrà:

```c
for (i = 0; i < rows; i++) {
    for (j = 0; j < columns; j++) {
        c[i][j] = a[i][j] * b[i][j];
    }
}
```

Il numero di cicli annidati aumenterà in maniera direttamente proporzionale alla dimensionalità degli array: ciò significa, ad esempio, che per un array a dieci dimensioni avremo altrettanti cicli annidati.

Appare quindi chiaro come anche un leggero aumento della complessità delle operazioni da effettuare comporti un significativo aumento della complessità in termini di codice. Ed è proprio qui che NumPy ci viene in aiuto.

Infatti, per moltiplicare due array in NumPy basta la seguente istruzione:

```py
c = a * b
```

La sintassi è evidentemente molto più concisa e semplice, *anche rispetto alle liste in Python*, ed è molto simile a quella che si trova sulle formule "reali" usate sui libri di testo. Infine, questa istruzione sfrutta codice *precompilato*: in questo modo, si potranno ottenere delle prestazioni (quasi) equivalenti a quelle del codice scritto direttamente in C.

!!!note "Vettorizzazione e broadcasting"
    Quello che abbiamo appena visto è formalmente riassumibile nei concetti di *vettorizzazione* (ovvero la possibilità di scrivere il codice senza usare esplicitamente dei cicli) e *broadcasting* (riguardante la possibilità di usare una sintassi comune ed indipendente dalla dimensionalità degli array coinvolti nelle operazioni).

## Conclusioni

In questa lezione, abbiamo dato un breve sguardo su quello che offre NumPy, e sul perché preferirlo in determinate situazioni all'uso delle normali tecniche messe a disposizione da Python. Nella [prossima lezione](./02_array), continueremo il discorso sugli array, scendendo maggiormente nel dettaglio di questa importante struttura dati.
