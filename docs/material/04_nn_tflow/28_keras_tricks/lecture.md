# 27

## Callback modello

Un *callback* è un oggetto che può effettuare un'azione durante diversi stage del training.

Si può usare un callback epr:

* scrivere i log di tensorboard dopo ogni batch di training per monitorare le nostre metriche
* salvare periodicamente il modello su disco
* fare l'early stopping
* avere una vista sugli stati e statistiche interne di un modello durante il training

Per usarli, possiamo passare una lista di callback al parametro callbacks al metodo fit() di un modello.

### ModelCheckpoint

Questo callback ci permette di salvare un modello Keras o i suoi pesi con una certa frequenza, in modo che il modello o i pesi possano essere caricati successivamente per continuare il training dallo stato raggiunto.

Alcune opzioni importnati del ModelCheckpoint sono le seguenti:



## Visualizzazione su TensorBoard

## Transfer learning e fine tuning

Il transfer learning consiste nel prendre dellef eature apprese su un problema e sfruttarle per risolvere un nuovo (e simile) problema. Ad esempio, le feature che sono state apprese per apprendere la razza di un felino possono essere usate epr apprendere la razza di un canide.

Il transfer learning è spesso effettuato per i task dove il dataset ha pochi dati per permettere un addestramento da zero del nostro modello.

L'incarnazione più conosciuta in tal senso del workflow da seguire è la seguetne:

1. prendiamo i layer da un modello precedentemente addestrato;
2. congeliamo detti layer, in modo da evitare di distruggere l'informazione che contengono durante futuri round di addestramento;
3. aggiungiamo alcuni layer addestrabili sull'ultimo dei layer freezati. Questi impareranno quindi a modificare le vecchie feature in predizioni sul nuovo dataset.
4. addestriamo i nuovi layer del nostro dataset

Un ultimo step opzionale è il fine tuning, che prevede di "sbloccare" l'intero modello ottenuto in precedenza (o parte di esso) e riaddestrarlo sui nuovi dati con un learning rate molto blando. Questo può potenzialmente ottenre dei miglioramenti significativi adattando in maniera incrementale le feature precedentemente ottenute ai nuovi dati.
