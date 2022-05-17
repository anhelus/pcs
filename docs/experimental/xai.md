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

## 11. Learned features (TODO: Da qui)
