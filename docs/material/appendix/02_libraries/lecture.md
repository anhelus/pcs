# Appendice B: Setup dell'ambiente di lavoro

Per effettuare il setup dell'ambiente di lavoro avremo a disposizione diverse opzioni. Vediamole nel dettaglio, immaginando di voler installare la libreria NumPy.

## Opzione A: utilizzare `pip`

La prima opzione, e probabilmente quella maggiormente utilizzata, è utilizzare il *package manager* (ovvero, il gestore di pacchetti) integrato in Python, chiamato `pip`.

Per farlo, apriamo un terminale assicurandoci di avere i diritti di amministratore; in Linux, dovremo usare l'istruzione `sudo`, a meno che non siamo utenti rott, mentre in Windows ci basterà aprire la shell come amministratori. Una volta aperto il terminale, dovremo scrivere:

```shell
pip install numpy
```

Installare una libreria in questo modo è sicuramente molto semplice, ma porta con sè uno svantaggio: infatti, l'installazione della stessa avviene *globalmente*, ovvero risulta essere valida per l'intera macchina.

Ciò potrebbe non sembrare rilevante; tuttavia, in ben determinate situazioni, si può rendere necessario installare particolari combinazioni di versioni di librerie, per usufruire di funzionalità successivamente deprecate o, al contrario, non presenti in versioni antecedenti. In tal senso, se installiamo una certa libreria globalmente, *tutti* i nostri programmi dovranno necessariamente utilizzare quella libreria in quella specifica versione, il che ci può vincolare fortemente a lungo andare.

## Opzione B: utilizzare `pip` ed un ambiente virtuale

Un'altra opzione è quella di utilizzare `pip` in un opportuno *ambiente virtuale*.

Quest'ultimo altro non è se non un ambiente "separato" all'interno del nostro calcolatore, nel quale andremo ad inserire tutte le librerie che utilizzeremo per i progetti da inserire all'interno dell'ambiente (con le versioni specifiche).

Per utilizzare questa opzione, dovremo innanzitutto creare un ambiente virtuale. Per farlo, dobbiamo usare un'opportuna libreria Python, che dovremo installare *globalmente* mediante `pip`.

!!!tip "Nota"
    L'installazione globale delle librerie per la gestione dell'ambiente virtuale è strettamente necessaria, e non contraddice il principio descritto nelle righe precedenti: infatti, l'idea è che si possa creare un ambiente virtuale in *qualsiasi momento*.

Installiamo quindi la libreria [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/), o l'equivalente porting per Windows [virtualenvwrapper-win](https://pypi.org/project/virtualenvwrapper-win/):

==="Linux"
    ```sh
    pip install virtualenvwrapper
    ```
==="Windows"
    ```sh
    pip install virtualenvwrapper-win
    ```

Una volta completata l'installazione, utilizzeremo il comando `mkvirtualenv`, seguito da un nome a nostra scelta, per creare l'ambiente virtuale. Ad esempio:

```sh
mkvirtualenv pcs
```

Noteremo che, a sinistra del terminale, sarà apparsa la scritta `(pcs)`:

```sh
(pcs) current_working_directory/
```

Questo ci indica che siamo all'interno del nostro ambiente virtuale. Procediamo adesso all'installazione della libreria NumPy mediante `pip`:

```sh
(pcs) current_working_directory/ pip install numpy
```

In questo modo, avremo installato NumPy *esclusivamente* all'interno del nostro ambiente virtuale. Per verificarlo, basta eseguire l'istruzione `pip freeze`, che restituisce tutte le librerie presenti nell'ambiente in cui siamo attualmente, assieme alle loro versioni.

!!!note "Il file `requirements.txt`"
    Pratica comune è quella di memorizzare tutte le librerie presenti in un ambiente virtuale in un file chiamato `requirements.txt`. Così facendo, un altro programmatore sarà in grado di "clonare" il nostro ambiente virtuale.
    Per salvare il file `requirements.txt`, dovremo usare i seguenti comandi:
    > ```sh
      pip freeze > requirements.txt
      ```
    Per creare un ambiente virtuale come descritto dal file dei requisiti, invece, dovremo eseguire:
    > ```sh
      pip install -r requirements.txt
      ```
    dove il flag `-r` sta per *recursively*, ed indica a `pip` di installare in maniera ricorsiva le librerie indicate nel file `requirements.txt`.

## Opzione C: utilizzare una distribuzione di Python per il calcolo scientifico

La terza opzione è quella di utilizzare una distribuzione di Python specificamente pensata per il calcolo scientifico, come [Anaconda](https://www.anaconda.com/products/distribution). In questo caso, basterà scaricare l'installer dal sito ufficiale e seguire la normale procedura di installazione.

Il vantaggio di utilizzare una distribuzione di questo tipo sta nel fatto che avremo a disposizione *di default* la maggior parte delle librerie utilizzate nel calcolo scientifico. Tuttavia, occorre tenere in considerazione il fatto che la libreria è specificamente pensata soltanto per scopi scientifici, per cui dovremo considerarlo qualora intendessimo utilizzare Python per progetti di altro tipo.

!!!note "Il package manager di Anaconda"
    Nel caso si decida di optare per l'uso di Anaconda, è importante ricordare che questa distribuzione ha un suo package manager, chiamato `conda`. Questo andrà a sostituire `pip` nell'installazione delle librerie non presenti nella distribuzione.

## Opzione D: utilizzare un package manager come `pipenv`

L'ultima opzione, che è anche quella suggerita in caso di utilizzo professionale ed eterogeneo di Python, è quella di affidarsi ad un package manager evoluto, come `pipenv`.

Questo package manager, infatti, automatizza e semplifica la creazione di un ambiente virtuale, combinando la stessa con l'utilizzo di `pip` in pochi, semplici comandi; in generale, quindi, il tool ci fornisce un'interfaccia utente molto più snella, ed inoltre si occupa autonomamente di selezionare le ultime versioni disponibili per i package che utilizziamo.

Per utillizzare `pipenv`, dovremo per prima cosa installarlo globalmente sulla nostra macchina mediante `pip`:

```sh
pip install pipenv
```

Una volta installato, andiamo nella cartella dove vogliamo creare il nostro progetto, che ricordiamo includerà soltanto la libreria NumPy, e scriviamo:

```sh
pipenv install numpy
```

Vedremo che, al termine della procedura, saranno stati generati due file: il primo, chiamato `Pipfile`, avrà al suo interno tutte le dipendenze che abbiamo aggiunto al nostro progetto, mentre il secondo, `Pipfile.lock`, conterrà delle informazioni dettagliate sulle librerie usate, incluse versioni, repository, e via discorrendo.

Tuttavia, `pipenv` non si limita a creare questi due file, ma provvede anche a definire, in maniera automatica, un nuovo ambiente virtuale, all'interno del quale saranno (ovviamente) memorizzate tutte le librerie installate per il nostro progetto. Per accedere all'ambiente virtuale, dovremo usare il comando `pipenv shell`, mentre per eseguire un comando *senza* accedere all'ambiente virtuale dovremo usare il comando `pipenv run` seguito dal comando che vogliamo eseguire.

Ad esempio, se volessimo lanciare un ipotetico script `run.py` *accedendo* all'ambiente virtuale, dovremmo scrivere:

```sh
pipenv shell
python run.py
```

Se non volessimo accedere all'ambiente virtuale, invece, dovremmo scrivere:

```sh
pipenv run python run.py
```

## Bonus: opzione utilizzata nel corso

Nel corso, utilizzeremo l'approccio basato su [Miniconda](https://docs.conda.io/en/latest/miniconda.html) e `pip`, che è, ad oggi, quello suggerito per l'[installazione di TensorFlow](https://www.tensorflow.org/install/pip?hl=en).

Vediamo come impostare l'ambiente di sviluppo a seconda che si stia utilizzando Linux o Windows.


=== "Windows"
    
    #### 1. Requisiti di sistema

    

    ``` sh

    ```

=== "Linux"

    ``` sh
    curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o Miniconda3-latest-Linux-x86_64.sh
    bash Miniconda3-latest-Linux-x86_64.sh
    ```


