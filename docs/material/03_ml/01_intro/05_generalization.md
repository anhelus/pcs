# 3.1.5 - Generalizzazione

L'obiettivo principale di un algoritmo di machine learning è quello di avere buone performance *anche su input non visti in precedenza*. In altre parole, l'algoritmo deve essere in grado di generalizzare la conoscenza acquisita sul dataset su cui è stato addestrato.

Tipicamente, un algoritmo viene addestrato su un *set di training*, sulla quale calcoliamo una serie di metriche che, a seconda del tipo di problema, vogliamo massimizzare o minimizzare. I lettori più attenti noteranno che questo altro non è se non un problema di ottimizzazione: tuttavia, quello che separa nei fatti il machine learning da un problema di questo tipo è che nel machine learning si desidera che l'*errore di generalizzazione* sia quanto più possibile ridotto. Questo errore è formalmente definito come il valore atteso dell'errore su tutti gli input non visti prima dal modello.

Tipicamente, l'errore di generalizzazione è stimato misurando le performance dell'algoritmo addestrato su di un insieme di esempi di test, chiamato per l'appunto *test set*, collezionati separatamente dai dati di addestramento. In tal senso, ci viene in aiuto il campo della statistica, che ci dice che nel caso in cui sia possibile fare delle ipotesi su come i set di training e di test sono stati collezionati possiamo mettere in relazione le performance sul test set anche se possiamo soltanto osservare il training set.

In particolare, i dati di training e di test vengono generati da un'unica distribuzione di probabilità chiamato *meccanismo di generazione dei dati*. Tipicamente, facciamo un insieme di ipotesi chiamate collettivamente *ipotesi i.i.d.*, ovvero:

* i campioni sono distribuiti *indipendentemente* gli uni dagli altri;
* gli insieme di training e di test sono *identicamente distribuiti*, ovvero estratti ciascuno dalla stessa distribuzione di probabilità.

Grazie all'ipotesi i.i.d., possiamo descrivere il processo di generazione dei dati mediante un'unica distribuzione, che possiamo indicare con $p_{data}$. Se questa ipotesi è vera, possiamo aspettarci che, dato un modello, il valore atteso dell'errore su campioni selezionati casualmente dal dataset di training è uguale a quello su campioni selezionati casualmente dal dataset di test.

Naturalmente, quando usiamo un algoritmo di machine learning, il modello non viene fissato *a priori*, ma a seguito del campionamento del dataset di training. Una volta acquisito detto dataset, i parametri del modello saranno addestrati su di esso, per cui l'errore atteso sul test set sarà maggiore di quello atteso sul training set. Di conseguenza, gli obiettivi dell'addestramento sono due:

1. minimizzare l'errore di training;
2. minimizzare il gap tra l'errore di training e quello di test.

Ciò comporta due sfide: l'*underfitting* e l'*overfitting*. L'underfitting avviene quando il modello non è in grado di ottenere un errore sufficientemente basso sul training set; l'overfitting avviene quando il gap tra l'errore di training e quello di test è troppo elevato.

Possiamo controllare se un modello è più prono ad overfitting o underfitting modificandone la *capacità*, ovvero l'abilità di adatatrsi ad un range più o meno elevato di funzioni e possibilità. In altre parole, un modello a basso capacità potrebbe avere problemi di underfitting, mentre un modello ad alta capacità è più prono all'overfitting, dato che memorizza delle proprietà del training set che non serve utilizzare sul test set.

Un modo per controllare la capacità di un modello è quello di scegliere il suo *spazio delle ipotesi*, ovvero l'insieme di funzioni che l'algoritmo di apprendimento può selezionare come possibile soluzione. Ad esempio, l'algoritmo di regressione lineare può scegliere una qualsiasi funzione lineare, e può essere generalizzato includendo dei polinomi nello spazio delle ipotesi, aumentando la capacità del modello.
