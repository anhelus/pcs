# 6 Model-Agnostic methods

Separare le spiegazioni dal modello di machine learning (ovvero ottenere dei metodi di interpretazione *agnostici*, ed indipendenti dal modello) ha diversi vantaggi. Il più grande è quello di essere flessibili: gli sviluppatori di machine leranign sono in grado di usare un qualsiasi modello di machine learning quando i metodi di interpretazione possono essere applicati ad un qualsiasi modello.

Normalmente, non solo uno, ma molti tipi di modelli di machine learning vengono valutati per risolvere un task, e quando si comparano i modelli in termini di interpretabilità, è più semplice lavorare con delle spiegazioni agnostich, perché lo stesso metodo può essere usato per un qualsiasi tipo di modello.

Un'alternativa all'interpretazione agnostica è quella di usare soltanto dei modelli interpretabili, il che però hanno spesso delle performance in termini di predizione inferiore rispetto ad altri mdoelli di machine learning, e inoltre ci limitiamo ad usare un solo tipo di modello. L'altra alternativa è quella di usare dei metodi di interpretazione specifici per ciasun modello. Lo svantaggio in questo caso è che ci si sta fermando ad un tipo di modello, e sarà difficile cambiarlo.

Le caratteristiche quindi di un sistema di spiegazione agnostico sono:

* flessibilita di modello: il metodo di interpretazione deve funzionare con ogni modello di machine learning, come le random forest e le deep neural network;
* flessibilità delle spiegazioni: non siamo limitati ad una certa forma di spiegazione. In alcuni casi potrebbe essere utile avere una formula lineare, in altri casi un grafico con l'imporatnza delle feature;
* flessibilità delle rappresentazioni: il sistema di spiegazione dovrebbe essere in grado di usare una diversa rappresentazione delle feature in base al modello che viene spiegato.

Nel grande schema delle cose:

* a livello più basso abbiamo il mondo, che può essre la natura stessa, come la biologia del corpo umano, o cose più astratte come il mercato immobiliare. In questo livello abbiamo tutto quello che può essere osservato e risulta di interesse.
* poi abbiamo i dati: dobbiamo digitalizzare il mondo per renderlo elaborabile dai computer e memorizzare informazioni. Il layer dei dati contiene ogni cosa a partire da immagini, testo, dati tabellari e via discorrendo.
* a quel punto abbiamo il layer del Black Box Model. Gli algoritmi di machine learning apprendono a partire dai dati del mondo reale e in base a questi fanno predizioni o trovano delle strutture.
* sopra al Black Box MOdel layer vi è il layer dei meotdi interpretabilit, che ci aiuta ad osservare l'opacità dei modelli di machine learning. Quali sono le feature più importanti per una determinata diagnosi^ Perché una transazione finanziaria è stata classificata come frode?
* l'ultimo layer è occupato dall'essere umano. 

Questa astrazione ci aiuta anche a comprendere le differenze negli approcci tra gli statistici e chi fa machine learning. Gli statistici si occupano principalmente del layer dei dati: non considerano il black box model e vanno diretti al layer di interpretabilità. Chi fa mahcine learning si occupa anche esso del layer di dati, e addestra un modello a scatola nera. Questi saltano il layer di interpretabilità, e ci si trova direttamente ad avere a che fare con le predizioni. In questo senso, l'interpretable machine learning fonde il lavoro degli statistici con quello degli esperti di machine learning.

## TODO: da Example-based explaations

https://christophm.github.io/interpretable-ml-book/example-based.html

## 10. Neural Network interpretation

il deep learning ha riscosso grande successo, specialmente nei task che prevedono immagini e testi come la classificazione delle immagini e la traduzione del linguaggio. la storia di successo delle deep neural network inizia nel 2012, quando la sfida di classificazione delle immagini ImageNet venen vinta da un approccio basato sul deep learning. Da quel momento, abbiamo assistito ad un'esplosiioen di diverse architetture di deep neural network, con un trend verso reti sempre più profonde con più e più parametri.

Per effettuare delle predizioni con una rete neurale, i dati in ingresso sono passati attraverso diversi layer di moltiplicazioni con i pesi appresi ed attraverso delle trasformazioni non lineari. Una singola predizione può coinvolgere milioni di operazioni matematiche a seconda dell'architettura della rete neurale. Non c'è alcun modo in cui un umano può seguire il mapping esatto dei dati dall'ingresso alla predizione. Dovremmo considerare milioni di pesi che interagiscono in maniera complessa per comprendere la predizione di una rete neurale. Per comprendere il comportamento e le predizioni delle reti neurali, dobbiamo usare specifici metodi di interpetazione.

Possiamo certamente usare dei meotdi model-agnostici, come i modelli locali o i partial dependence plots, ma ci sono due motivi per cui ha senso considerare dei metodi di interpretazione sviluppati specificamente per le reti neurali. In primisi, le reti neurali apprendono feature e concetti negli strati nascosti, ed abbiamo bisogno di strumenti specifici per comprenderli. Secondo, il *gradeinte* può essere usato per implementare dei metodi di interpretazione che sono più efficienti dal punto di vista computazionale dei meotdi model agnostici che guardano al modello "dall'esterno".

## 10.1 Learned features (TODO: Da qui)

Le CNN apprendono delle feature e dei concetti astratti a partire dai pixel dell'immagine. Le tecniche di feature visualization visualizzao le feature apprese in base a quanto viene "attivata" la rete. Invece, le tecniche di network dissetion etichettano le unità della rete neurale (ad esempio i channel) mediante concetti umani.

Le deep neural network apprendono feature ad alto livello nei layer nascosti. Questa è una delle forze migliori e riduce la necessità di feature engineering. Presupponiamo di voler creare un classificatore di immagini medinate una SVM. Le matrici di pixel grezzi non rappresentano i migliori input per l'addestramento della SVM, per cui creiamo delle nuove feature basate su colore, dominio di frequenza, edge detector e via dicendo. Con le CNN, l'immagine viene immessa nella rete nella sua forma raw (ovvero i pixel). La rete trasfroma l'immagine diverse volte. Per prima cosa, l'immagine va attraverso molti layer convoluzionali, nei quali la rete apprende nuove feature di complessità incrementale. Quindi le informazioni trasformate sull'immagine vanno attraverso i layer completamenti connessi e si trasformano in una classificazione o predizione.

Di solito:

* i primi layer convoluzionali apprendono delle feature come edge e semplici tessiture.
* i layer convoluzionali più in fondo apprendono feature come texture e pattern più complessi.
* gli ultimi layer convoluzionali apprendono feature come oggetti o parti di oggetti.
* i layer completamente connessi apprendono a connettere le attivazioni dalle feature ad alto livello alle classi individuali da predire.

### 10.1.1 - Feature visualization

L'approccio di rendere le feature apprese esplicite viene chiamato **Feature Visualization**. La feature visualization per un'unità di una rete neurale viene fatta trovando l'input che massimizza l'attivazione di quella unità.

Il concetto di unità si riferisce sia a neuroni individalui, canali (chiamati anche feature maps), interi layer o la probabilità finale nella classificazione (o il corrispondente neurone pre-softmax, il che è raccomandato). I neuroni individuali sono unità atomiche della rete, per cui otterremo la maggiro parte delle finromarzioni creando delle feature visualization per ogni neurone. Ma purtroppo c'è un probelma: le reti neurali spesso contengono milioni di neuroni. Vedere la feature visualziation di ogni neurone richiedrerebbe troppo tempo. I canali (alle volte chiamate mappe di attivazione) come unità sono una buona scelt aper la feature visualization. Possiamo adare uno step oltre e visualizare un intero layer convoluzionale. I layer come unità sono usate per il DeepDream di Google, che agiunge ripetutamentele feature visuazilzzate di un layer all'immagine originale, risultando in una versione "sognante" dell'input.

#### 10.1.1.1 Visualizzazione delle feature attraverso l'ottimizzazione

In termini matematici, la feature visualization è un problema di ottimizzazione. Si presuppone che i pesi della rete neurale siano fissati, il che significa che la rete è addestrata. Stiamo cercando una nuova immagine che massimizza l'attivazione media di una unità, qui un singolo neurone:

$$
img^* = arg max_{img} h_{n,x,y,z} (img)
$$

La funzione $h$ è l'attivazione di un neurone, $img$ l'input della rete (un'immagine), x ed y descrivono la posizione spaziale del neurone, $n$ specifica il layer e z è l'indice del canale. Per l'attivazione media di un intero canale z nel layer n che massimizziamo:

$$
img^* = arg max_{img} \sum_{x, y} h_{n, x, y, z} (img)
$$

In questa formula, tutti i neuroni nel canale $z$ sono pesati in maniera uguale. In alternativa, possiamo anche massimizzare le direzioni casuali, il che significa che i neuroni saranno moltiplicati per differenti parametri, incluse direzioni negative. In questo modo, studiamo come i neuroni interagiscono all'interno del canale. INvece di massimizzare l'attivazione, possiamo anche minimizzarla (che corrisponde a massimizzare la direzione negativa). E' interessante che se massimizziamo la direzione negativa otteniamo feature molto differenti per la stessa unità.

Possiamo affrontare questo problema di ottimizzazione in modi differenti. Ad esempio, invece di generare nuove immagini, possiamo cercare nelle nostre immagini di training e selezionare quelle che massimizzano l'attivazione. Questo approccio è valido, ma usare i dati di training ha il problema che gli elementi dell'immagine possono essere correlati e non possiamo vedere ciò che la rete neurale sta cercando veramente. Se le immagini che emettono un'alta attivazione di un certo canale mostrano un cane ed una pallina da tennis, non sappiamo se la rete neurale guarda il cane, la pallina da tennis o entrambi.

Un altro approccio è quello di generare nuove immagini a partire da rumore casuale. Per ottenere visualizzazioni utili, ci sono normalmente dei vincoli sull'immagini, ad esempio che solo piccoli cambi siano permessi. Per ridurre il rumore nella feature visualization, possiamo applicare jittering, rotazione o scaling all'immagine prima dello step di ottimizzazione. Altre opzioni di regolarizzazione includono la frequency penaliszaiton (ovvero ridurre la varianza dei pixel vicini) o generare l'immagine con i primor appresi, ad esempio con delle generative adversarial networks (GANs) o denoising autoencoders.

**Connessione agli Adversarial Examples**

C'è una connessione tra la feature visualization e gli adversarial examples: entrambe le tecniche massimizzano l'attivazione di un'unità di una rete neurale.Per gli adversarial examples, guardiamo alla massima attivazione del neurone per le classi adversarial (ovvero incorrette). Una differenza è l'immagien dalla quale partiamo: per gli adversarial examples, questa è l'immagine per la quale vogliamo generare l'adversarial image. Per la feature visualization è, a seconda dell'approccio, rumore casuale.

**testo e dati tabellari**

La letteratura si focalizza sulla feature visualization per le CNN per l'image recognition. Tecnicamente, niente ci vieta da trovare l'input che attiva massima mente un neurone di una rete neurale completamente connessa per dati tabellari o una recurrent neural network per dati testuali. Non potremo più chiamarla feature visualization, dal momento che la feature sarà un input di tipo tabellare o testuale. Per esempio, per predire il rischio del credito, l'input potrebbe essere il numero di crediti precedenti, il numero di contratti di telefono, indirizzi e molte altre feature.  Le feature apprese di un neurone saranno quini una certa combinazione delle dozzine di feature. Per le RNN, è leggermente più facile visualizzare quello che la rete ha appreso: ad esmepio, le RNN hanno neuroni che apprendono delle feature interpretabile. Karpathy et al. addestrano un modello che predice il carattere successivo in una frase a partire dal carattere precedente. Ogni volta che c'+ una parentesi tonda d'apertura, uno dei neuroni viene attivato, e si deattiva quando la parentesi di chiusura corrispondente viene trovata. Altri neuroni sono invece lanciati al termine di una linea. Alcui neuroni si attivano in presenza di URL. La differenza rispetto alla feature visualization per le CNN è che gli esempi non sono stati trovati attraverso l'ottimizzazione, ma studiando le attivazioni dei neuroni nei dati di training.

Alcune delle immagini sembrano mostrare concetti ben conosciuti come cani o costruzioni. Ma come possiamo esserne sicuri^il metodo di netowrk dissectionc onnette i concetti umani alle singole unità della rete.
