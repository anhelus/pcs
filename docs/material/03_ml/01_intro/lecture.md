# 12 - Introduzione al machine learning

Il *machine learning* è alla base di alcune tra le più importanti tecnologie odierne. Le sue applicazioni sono molteplici: si va dagli strumenti di traduzione automatica fino ai veicoli autonomi, passando per sistemi di videosorveglianza e software per scrivere codice.

In pratica, l'avvento del machine learning ha offerto un modo alternativo, e *più efficace*, di risolvere problemi estremamente complessi. Volendo riassumere il concetto alla base del machine learning, potremmo dire che questo rappresenta il procedimento che insegna ad un software, chiamato *modello*, a fare predizioni significative a partire da un insieme di dati. In altri termini:

!!!quote "Modello di machine learning"
    Un modello di machine learning rappresenta la relazione matematica intercorrente tra i dati che il sistema derivante utilizza per effettuare predizioni.

Come esempio, immaginiamo di creare un software che effettui la predizione del quantitativo di pioggia che cadrà in una zona. Per farlo, possiamo usare due approcci:

* nell'approccio *tradizionale*, creeremo una rappresentazione fisica dell'atmosfera e della superficie terrestre, risolvendo equazioni estremamente complesse come le Navier-Stokes;
* nell'approccio *basato sul machine learning*, daremo ad un modello un quantitativo adeguato (e, molto spesso, *enorme*) di dati riguardanti le condizioni meteorologiche, fino a che il modello stesso non apprenderà le relazioni sottostanti i diversi pattern di feature meteorologiche che permettono di produrre diversi quantitativi di pioggia.

In entrambi i casi, una volta completata l'implementazione (per l'approccio tradizionale) o l'addestramento (per l'approccio basato su machine learning) passeremo al software i dati sulla condizione meteorologica attuale, per poi predire il quantitativo di pioggia previsto.

## 12.1 - Tipi di sistemi di machine learning

I sistemi di machine learning ricadono in tre diverse categorie, distinte sulla base di come "apprendono" a fare determinate predizioni.

### 12.1.1 - Sistemi ad apprendimento supervisionato

I sistemi ad *apprendimento supervisionato* (*supervised learning*) effettuano una predizione dopo aver appreso le relazioni intercorrenti tra un numero più o meno grande di dati ed i corrispondenti valori da predire. Per intenderci, un sistema di questo tipo è un po' come uno studente di matematica che, dopo aver appreso i metodi per la risoluzione di un problema di analisi mediante la risoluzione di un gran numero degli stessi, si prepara a sostenere l'esame.

!!!note "Perché supervisionato?"
    L'appellativo *supervisionato* deriva dal fatto che è (di solito) un esperto di dominio a fornire al sistema i dati con i risultati corretti.

I più importanti approcci all'apprendimento supervisionato sono la *regressione* e la *classificazione*.

#### 12.1.1.1 - Modelli di regressione

Un *modello di regressione* predice un valore numerico. Ad esempio, un modello meteorologico di regressione potrebbe predire il quantitativo di pioggia in millimetri, mentre un altro modello di regressione potrebbe valutare l'andamento dei prezzi delle proprietà immobiliari sulla base di dati come i metri quadri, la posizione e le caratteristiche della casa, nonché la situazione attuale dei mercati finanziario ed immobiliare.

#### 12.1.1.2 - Modelli di classificazione

A differenza dei modelli di regressione, il cui output è rappresentato da un numero, i *modelli di classificazione* restituiscono in uscita un valore che stabilisce la possibilità che un certo campione appartenga ad una data categoria. Ad esempio, un modello di classificazione potrebbe essere usato per predire se un'email è un messaggio di spam, o se una foto contiene invece un gatto o un cane.

Esistono due macrocategorie di modelli di classificazione, ovvero quelli *binari* e quelli *multiclasse*. In particolare, i modelli di classificazione binaria distinguono esclusivamente tra due valori: ad esempio, un modello di classificazione delle email potrebbe indicare se il messaggio è di spam o meno. I modelli di classificazione multiclasse invece riescono a distinguere tra più classi: ad esempio, il nostro modello di riconoscimento delle foto potrebbe riconoscere oggetti di "classe" gatto, cane, gallina ed oca.

### 12.1.2 - Sistemi ad apprendimento non supervisionato

I *sistemi di apprendimento non supervisionato* compiono delle predizioni a partire da dati che non contengono alcuna informazione sulla classe di appartenenza o sul valore di regressione. In pratica, i modelli non supervisionati hanno il compito di identificare pattern significativi *direttamente nei dati*, senza alcun "indizio" a priori, ma limitandosi ad inferire automaticamente le proprie regole.

Algoritmi comunemente utilizzati in tal senso sono quelli di *clustering*, nei quali il modello individua come i dati vanno a "disporsi" utilizzando delle regole basate su distanze o capacità di "agglomerarsi".

Il clustering differisce dagli algoritmi supervisionati, ed in particolare dalla classificazione, principalmente perché le categorie non sono definite a priori da un esperto di dominio. Ad esempio, un algoritmo di clustering potrebbe raggruppare i campioni in un dataset meteo sulla base esclusivamente delle temperature, rivelando delle suddivisioni che definiscono le diverse stagioni, oppure ancora gli orari del giorno. Sarà poi nostro compito "provare" a dare un nome a questi cluster sulla base della nostra interpretazione del dataset.

### 12.1.3 - Sistemi di reinforcement learning

I sistemi di reinforcement learning effettuano delle predizioni a partire da ricompense o penalità basate sulle azioni effettuate da un *agente* all'interno di un *ambiente*. Sulla base di queste osservazioni, il sistema di reinforcement learning genera una *policy* che definisce la strategia migliore per raggiungere lo scopo prefissato.

Le applicazioni dei sistemi di questo tipo sono varie, e spaziano dall'addestramento dei robot per svolgere task anche complessi, alla creazione di programmi come Alpha Go che sfidino (e battano) gli umani al gioco del Go.
