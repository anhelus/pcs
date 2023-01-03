# Cosa è il clustering?

Quando proviamo ad apprendere qualcosa, diciamo, ad esempio, uno strumento musicale, un approccio potrebbe essere quello di cercare gruppi o collezioni significative. Potremmo organizzare la musica per genere, mentre i nostri amici potrebbero organizzare la musica per decenni. Come scegliamo di raggruppare gli oggetti ci permette di comprendere di più su di essi come pezzi individuali di musica. POtremmo scoprire che abbiamo una profonda affinità per il prog rock, e qundi suddividere ulteriormente il genere in diversi approcci o musica da diversi luoghi. D'altro canto, i nostri amici potrebbero vedere la muscia degli anni 80 e comprendere la diffusione dei generi all'epoca in base all'influenza del clima sociopolitico. In entrambi i casi, noi ed i nostri amici abbiamo appreso qualcosa di interessante sulla musica, anche se abbiamo scelto approcci differenti.

Anche nel machine learnign, spesso raggruppiamo dei campioni come primo passo per comprendere un soggetto (dataset) in un sistema di machine learning. Raggruppare dei campioni senza label è chiamato *clustering*.

Dato che i campioni non sono etichettati, il clustering si affida a machine learning non supervisionato. Se i campioni sono etichettati, il clustering diventa classificazione.

TODO FIGURA CLUSTER ESEMPIO

Prima che si possano raggruppare campioni simili, dobbiamo per prima cosa trovarli. Possiamo misurare la similarità tra campioni combinando le feature dei dati dei campioni in una metrica chiamata *misura di similarità*. Quando ogni campione è definito da una o due feature, è facile misurare la similarità. Per esempio, possiamo trovare dei libri simili in base ai loro autori. Man mano che il numero di feature aumenta, creare una misura di similitarità diventa più complesso. Vedremo come creare una misura di similarità in diversi scenari.

## Quali sono gli usi del clustering?

Il clustering ha molti usi in un ampia varietà di industrie. Alcune applicazioni comuni per il clustering includono i seguenti:

* segmentazione del mercato
* analisi dei social network
* raggruppamento dei risultati di ricerca
* immagini mediche
* segmentazione delle immagini
* anomaly detection

Dopo il clustering, ad ogni cluster viene assegnato un identificativo. Ora, possiamo condensare l'intero insieme di feature per un campione nel suo identificativo. Rappresentare un complesso esempio mediante un semplice identificativo rende il clustering potente. Estendendo l'idea, i dati di clustering possono semplificare dei grossi dataset.

Per esempio, possiamo raggruppare gli oggetti medianti diverse feature come dimostrato da esempi come il raggruppamento di stelle mediante la luminosità, oppure di documenti in base al loro argomento.

Il clustering può essere usato per diversi task:

* generalizzazione: quando alcuni esempi in un cluster hanno delle feature mancanti nei dati, possiamo inferire i dati mancanti da altri campioni del cluster. Ad esempio, dei video meno popolari possono essere clusterizzati con video più popolari per migliroare le raccomandazioni;
* data compression: le feature per tutti i campioni in un cluster possono essere rimpiazzate dall'identificativo rilevante. Questo rimpiazzo semplfiica i dati delle feature e salva della memoria. Questi benefici diventano significativi quando scalati per grosse dataset. Inoltre, i sistemi di machine leranign possono usare l'identificativo come input invece dell'intero dataset delle feature. Riducendo la complessità dei dati di input rende i modelli di machine learnign e più veloci da addestrare. Ad esempio, il clustering di video YouTube permette di rimpiazzare diverse feature, come lunghezza, commenti, descrizione, e via dicendo, in un singolo identificativo.
* privacy preservation: possiamo preservare la privacy per il clustering degli utenti, ed associando i dati degli utenti con gli identificativi dei cluster invece degli utenti specifici. Per assicurarci che non si possa associare i dati degli utenti con un utente specifico, il cluter deve raggruppare un numero sufficiente di utenti. Ad esempio, diciamo di voler aggiungere la storia degli utenti che hanno visto il video. Invece di affidarci all'identiifcativo, possiamo usare ed affidarci all'id del cluster. Ora, il modello non può associare lo storico a specifici utenti, ma soltanto con dei cluster che rappresentano un grosso gruppo di utenti.
