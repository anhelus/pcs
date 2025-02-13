# 3.1.1 - Introduzione al machine learning

Il *machine learning* è l'insieme di approcci alla base di alcune tra le più importanti e diffuse tecnologie odierne. Le sue applicazioni sono molteplici: si va dagli strumenti di traduzione automatica, [che tutti utilizziamo più o meno spesso](https://translate.google.com/translate_t), ai chatbot, [ormai estremamente evoluti](https://openai.com/blog/chatgpt/), passando per sistemi di videosorveglianza e riconoscimento facciale, e tanto altro ancora. In altre parole, la pervasiva diffusione del machine learning ha offerto un'alternativa più efficace alla risoluzione di problemi che, un tempo, venivano trattati esclusivamente mediante complessi modelli di equazioni matematiche.

Volendo riassumere quello che è il "flusso di lavoro" di un algoritmo di machine learning, possiamo dire che questo è il procedimento che permette ad un *modello* di imparare a fare *predizioni* significative a partire da un insieme di dati. In altri termini:

!!!quote "Modello di machine learning"
    Un modello di machine learning rappresenta la relazione matematica intercorrente tra i dati che il sistema derivante utilizza per effettuare predizioni.

Come esempio, immaginiamo di creare un software che effettui la predizione del quantitativo di pioggia che cadrà in una zona. Per farlo, possiamo usare due approcci:

* nell'approccio *tradizionale*, creeremo una rappresentazione fisica dell'atmosfera e della superficie terrestre, risolvendo equazioni estremamente complesse come le Navier-Stokes;
* nell'approccio *basato sul machine learning*, daremo ad un modello un quantitativo adeguato (e, molto spesso, *enorme*) di dati riguardanti le condizioni meteorologiche, fino a che il modello stesso non apprenderà le relazioni sottostanti i diversi pattern di feature meteorologiche che permettono di produrre diversi quantitativi di pioggia.

In entrambi i casi, una volta completata l'implementazione (per l'approccio tradizionale) o l'addestramento (per l'approccio basato su machine learning) passeremo al software i dati sulla condizione meteorologica attuale, per poi predire il quantitativo di pioggia previsto.

Perché, dunque, preferire il machine learning agli approcci tradizionali? Per rispondere a questa domanda, ci viene in aiuto il principio di indeterminazione discendente dal paradosso del [demone di Laplace](https://en.wikipedia.org/wiki/Laplace%27s_demon), il quale afferma che l'unico modo di predire lo stato di un sistema chiuso, pur conoscendone *ogni dettaglio*, è quello di essere esterno al sistema stesso. Ciò comporta che, per complesso che sia, nessun modello a scatola trasparente è in grado di modellare con precisione la realtà: di conseguenza, i modelli fisici sono giocoforza *limitati* sia dal numero di variabili da considerare, sia dalla natura dell'universo fisico.

Un modello di machine learning, ovviamente, è soggetto agli stessi vincoli dei modelli tradizionali. Tuttavia, il modello non deriva le sue predizioni da complesse equazioni matematiche, bensì *deriva la relazione dai dati sotto osservazione*. Di conseguenza, con un numero adeguato di dati, e rispettando le opportune ipotesi di funzionamento, un modello di machine learning questo offre una rappresentazione della realtà più "vera" di quella offerta da qualsiasi modello classico.

## Machine learning, deep learning, IA...

Prendiamoci un attimo per cercare di comprendere la differenza tra discipline apparentemente sovrapposte, quali *machine learning*, *deep learning*, ed *intelligenza artificiale*. In particolare, tutte queste discipline discendono da un "antenato" comune, ovvero la *statistica*, che altro non è se non una branca della matematica che si occupa di *descrivere* le caratteristiche di una popolazione di dati (*statistica descrittiva*), eventualmente effettuando delle operazioni di *inferenza* a partire da una certa popolazione (*statistica inferenziale*)[^1].

La statistica è ampiamente utilizzata dall'*intelligenza artificiale*, il cui compito è quello di creare dei sistemi in grado di svolgere dei compiti che, in condizioni normali, richiedono l'interazione con degli esseri umani. Dal punto di vista "filosofico", esistono due tipologie di intelligenza artificiale: la prima è la cosiddetta *IA ristretta*, o *debole*, progettate per eseguire dei compiti ben precisi, come ad esempio individuare i volti in una foto, o rispondere a delle domande testuali. La seconda, invece, è chiamata *IA generale*, o *forte*, e rappresenta un'intelligenza che possiede capacità cognitive eterogenee ed assimilabili a quelle presenti negli organismi che riteniamo comunemente "intelligenti", come ad esempio scimmie o delfini (e, se non vi sentite particolarmente misantropi, esseri umani). 

Il *machine learning* è invece una branca dell'intelligenza artificiale che si concentra sullo sviluppo di algoritmi *data-driven*, ovvero che permettono ad una macchina di apprendere un determinato comportamento direttamente dai dati a disposizione del modello. A sua volta, il *deep learning*, che vedremo in seguito, è una branca del machine learning che utilizza uno specifico tipo di algoritmi, ovvero le *deep neural network*, per mimare la struttura del cervello umano e trattare, di conseguenza, problemi estremamente complessi e sfaccettati.

!!!tip "E ChatGPT?"
    Quello dell'IA generale è, nel 2025, ancora un *concetto teorico*. Non esiste niente di simile e, nonostante gli incredibili sviluppi che abbiamo avuto negli ultimi anni, non raggiungeremo questo livello ancora per un po' di tempo. Va da sè, quindi, che ChatGPT *et similia* non rappresentano esempi di IA generale, quanto piuttosto di IA debole applicata a contesti specifici di generazione di linguaggio naturale, sviluppata utilizzando degli approcci basati sul deep learning.

## Tipi di sistemi di machine learning

I sistemi di machine learning ricadono in tre diverse categorie, distinte sulla base di come "apprendono" a fare determinate predizioni.

### Sistemi ad apprendimento supervisionato

I sistemi ad *apprendimento supervisionato* (*supervised learning*) effettuano una predizione dopo aver appreso le relazioni intercorrenti tra un numero più o meno grande di dati ed i corrispondenti valori da predire. Per intenderci, un sistema di questo tipo è un po' come uno studente di matematica che, dopo aver appreso i metodi per la risoluzione di un problema di analisi mediante la risoluzione di un gran numero degli stessi, si prepara a sostenere l'esame.

!!!note "Perché supervisionato?"
    L'appellativo *supervisionato* deriva dal fatto che è (di solito) un esperto di dominio a fornire al sistema i dati con i risultati corretti.

I più importanti approcci all'apprendimento supervisionato sono la *regressione* e la *classificazione*.

#### Modelli di regressione

Un *modello di regressione* predice un valore numerico. Ad esempio, un modello meteorologico di regressione potrebbe predire il quantitativo di pioggia in millimetri, mentre un altro modello di regressione potrebbe valutare l'andamento dei prezzi delle proprietà immobiliari sulla base di dati come i metri quadri, la posizione e le caratteristiche della casa, nonché la situazione attuale dei mercati finanziario ed immobiliare.

#### Modelli di classificazione

A differenza dei modelli di regressione, il cui output è rappresentato da un numero, i *modelli di classificazione* restituiscono in uscita un valore che stabilisce la possibilità che un certo campione appartenga ad una data categoria. Ad esempio, un modello di classificazione potrebbe essere usato per predire se un'email è un messaggio di spam, o se una foto contiene invece un gatto o un cane.

Esistono due macrocategorie di modelli di classificazione, ovvero quelli *binari* e quelli *multiclasse*. In particolare, i modelli di classificazione binaria distinguono esclusivamente tra due valori: ad esempio, un modello di classificazione delle email potrebbe indicare se il messaggio è di spam o meno. I modelli di classificazione multiclasse invece riescono a distinguere tra più classi: ad esempio, il nostro modello di riconoscimento delle foto potrebbe riconoscere oggetti di "classe" gatto, cane, gallina ed oca.

Parleremo più approfonditamente di questi modelli in una delle [lezioni successive](04_base.md).

### Sistemi ad apprendimento non supervisionato

I *sistemi di apprendimento non supervisionato* compiono delle predizioni a partire da dati che non contengono alcuna informazione sulla classe di appartenenza o sul valore di regressione. In pratica, i modelli non supervisionati hanno il compito di identificare pattern significativi *direttamente nei dati*, senza alcun "indizio" a priori, ma limitandosi ad inferire automaticamente le proprie regole.

Algoritmi comunemente utilizzati in tal senso sono quelli di *clustering*, nei quali il modello individua come i dati vanno a "disporsi" utilizzando delle regole basate su distanze o capacità di "agglomerarsi".

Il clustering differisce dagli algoritmi supervisionati, ed in particolare dalla classificazione, principalmente perché le categorie non sono definite a priori da un esperto di dominio. Ad esempio, un algoritmo di clustering potrebbe raggruppare i campioni in un dataset meteo sulla base esclusivamente delle temperature, rivelando delle suddivisioni che definiscono le diverse stagioni, oppure ancora gli orari del giorno. Sarà poi nostro compito "provare" a dare un nome a questi cluster sulla base della nostra interpretazione del dataset.

### Sistemi di reinforcement learning

I sistemi di reinforcement learning effettuano delle predizioni a partire da ricompense o penalità basate sulle azioni effettuate da un *agente* all'interno di un *ambiente*. Sulla base di queste osservazioni, il sistema di reinforcement learning genera una *policy* che definisce la strategia migliore per raggiungere lo scopo prefissato.

Le applicazioni dei sistemi di questo tipo sono varie, e spaziano dall'addestramento dei robot per svolgere task anche complessi, alla creazione di programmi come Alpha Go che sfidino (e battano) gli umani al gioco del Go.

[^1]: [Statistics versus machine learning](https://www.nature.com/articles/nmeth.4642), Nature
