Supponiamo di stare apprendendo delle cose su qualcosa, magari sulla musica. UN approccio potrebbe essere vedere dei gruppi o delle collezioni significativi. Potremmo voler organizzare la musica per genere, mentre i nostri amici organizzano la musica per decadi. Come scegliamo i gruppi di oggetti ci aiuta a capire più di questi come parti individuali della musica. POtremmo vedere che abbiamo un'affinità abbastanza profonda con il punk rock e andare a suddividere ulterioremente il genere in diversi approcci o in musica da diverse località. D'altro canto, il nostor amico potrebbe vedere alla musica degli anni 80 ed essere in grado di capire come la musica a quell'epoca influenzava il clima sociale e politico. In entmrabi i casi, sia noi sia il nostro amico abbiamo appreso qualcosa di interessante sulla musica, anche se abbiamo considerato diversi approcci.

Anche nel machine learning, spesso categorizziamo i campioni come primo passo per comprendere un soggeto (il dataset). Raggruppare degli esempi senza label è chiamato *clustering*. 

Dato che gli esempi non hanno una label, il clustering si affida all'apprendimento non supervisionato. Se gli esempi fossero etichettati, allora il clustering diventerebbe *classificazione*.

pirma di raggrupapre tra loro campioni simili, dovremmo per prima cosa trovare il concetto di similitudine. Possiamo misurare la somiglianza tra gli esempi combiando i dati delle feature in una metrica chiamata *similarity measure*. Quano ogni campione è definito da uno o due feature, è facile misurare la similarità. Ade sempio, possiamo trovare dei libri simili a seconda degli autori. Man mano che il numero di feature aumetnta, creare una misura di simiglianza diventa più complesso. Vedremo dopo come creare una misura di somiglianza in diversi scenari.

## quali sono le applicazioni del clustering?

Il clustering ha una miriade di usi in diverse industrie. Alcune applicazioni comuni per il clustering includono le seguenti:

* segmentazione del mercato
* analisi delle reti sociali
* segmentazione delle immagini
* individuazione di anomalie

Dopo il clustering, ad ogni cluster viene assegnato un numero chiamato *cluster ID*. ORa, possiamo condensare l'intero isieme delle feature per esempio nel suo cluster ID. Rappresentare un esempio complesso mediante un unico ID rende il clustering estremamente potente. Estendendo l'idea, il clustering di dati può semplificare i grossi dataset.

ad esempio, possiamo raggruppare gli oggetti secondo diverse feature, come dimostrato nei seguenti esempi:

* raggruppare le stelle per luminosità
* raggruppare i documenti per topic

i sistemi di machine learning possono usare uesti ID per semplificare l'elaborazione di grossi dataset. Quindi, l'output del clustering serve come dei feature data per i sistemi ML in uscita.

## generalizzaizoni

quando alcuni campioni in un cluster hanno delle feature mancanti, possiamo inferire i dati mancanti da altri esempi nel cluster. 

## data compression

abbiamo detto che i feature data per tutti i campioni in un cluster possono essere rimpiazzati a partire dall'ID del cluster. questo rimpiazzo semplifica la feature data, e risparmia memoria. Questi benefici potrebbero diventare significativi quando si scala su grossi dataset. Inoltre, i sistemi di machine learning possono usare il cluster ID come ingresso invece dell'intero dataset delle feature. Ridurre la complessità dei dei dati di input rende il modello di machine learning semplice e veloce.

## tipi di clustering

quando scegliamo un algoritmo di clustering, dobbiamo considerare se il nostro algoritmo è in grado di essere scalabile a sufficienza per il nostro dataset. I dataset nel machine learning possono avere milioni di esempi, ma non tutti gli algoritmi di clustering sono in grado dis calare in maniera efficace. Molti algoritmi di clutering funzionano calcolando le similarità tra tutte le coppie di esempi. Questo significa che il lroo runtiem aumenta come il quadrato del numero di campioni $n$, ovvero $O(n^2)$. Un buon algoritmo per iniziare è invec il k-means, che ha un $O(n)$, il che significa che scala linearmente con $n$.

### centrod-based clustering

Il centroid-based clustering organizza i dati in cluster non gerarchici. Il k-means è la tecnica più usata in tal senso. Questo tipo di algoritmi è molto efficace, ma è sensibile alle condizioni inzialie ed agli outliers.

### dnesity based

il cluster density based connette aree di campioni ad alta densità in cluster. Questo permette a distribuzioni a forma arbitraria di essere connesse fino a che sono dense. Questi algoritmi hanno delle difficoltà con dati con densità variabili ed a alta dimensionalità. Inoltre, questi algoritmi non assegnano gli outlier ai cluster per questioni di design.

## distribution-based

questo approccio alclustering assume che i dati siano composti da distribuzioni come quelli gaussiana. Ad esempio, l'algoritmo in ifgura mostra tre cluster basati su tre distribuzioni gaussiane. Man mano che la distanza dal centro della distribuzione aumenta, la probabilità che un punto appartenga alla distribuzione decresce. Quando non sappiamo il tipo di distribuzione nei dati, dovremmo scegliere un algoritmo differente.

### hierarchical

il clustering gerarchico crea un albero di cluster. In maniera non sorprendente è adatto a dati gerarchici, come le tassonomie. Inoltre, un piccolo numreo di cluster può esserescelto tagliando l'albero al livello giusto.

## workflow del clustering

per effettuare il clustering, dobbiamo:

### preparare i dati

così come negli altri problemi di machine learnning, dobbiamo normalizzare, scalare e trasformare le feature. quando si effettua il clustering, tuttavia, occorre assicurarsi del fatto che i dati preparati ci permettano di calcolare in maniera accurata la similarità tra i campioni.

### creare una metrica di similiartà

prima che un algoritmo di clustering possa raggruppare i dati, deve sapere come individuare le coppie di esempi simili. Quantifichiamo la similarità tra i campioni creando una metrica di similiarità. Questo richiede di comprendere i dati e come derivare la similarità a partire dalle nostre feature.

### eseguire gli algoritmi di clustering

un algoritmo di clustering usa la metrica di simialrità per effettuare il clustering dei dati.

### interpretare risultati e modificare

controllare la qualità dell'output del clustering è un processo iterativo ed esplorativo in quanto il clustering non ha a disposizione delle label per verificare l'output. Di conseguenza, verifichiamo i risultati manualmente, e migliorare i risultati richiede un approccio di tipo iterativo.