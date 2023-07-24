# 5.5.1 - Generative Adversarial Networks

## Modelli generativi e discriminativi

I modelli che abbiamo visto fino a questo momento ci permettono di valutare se, ad esempio, un'immagine rappresenta un cane o un gatto, oppure se una certa lettura risulta essere anomala. Abbiamo associato a questi modelli nomi come *classificatore* o *regressore*; tuttavia, in un senso più generico, possiamo riferirci ad essi come a modelli *discriminativi*, ovvero modelli che permettono di *discriminare* tra diversi tipi di istanze di dati.

Oltre ai modelli discriminativi, negli ultimi anni si sono andati diffondendo i cosiddetti modelli *generativi*, in grado di generare nuove istanze a partire da una modellazione statistica del meccanismo di generazione dei dati.

In altre parole, laddove i modelli discriminativi permettono di discernere il tipo di dato sotto analisi, i modelli generativi sono in grado di generare nuove istanze dati: un modello generativo può creare una foto verosimile di un cane o un gatto, mentre un modello discriminativo può dirci se l'immagine rappresenta l'uno o l'altro tipo di animale.

Più formalmente, dato un dataset $X$ con il corrispondente insieme di label $Y$:

* i modelli discriminativi rappresentano la *probabilità condizionale* $P(Y|X)$, ovvero la probabilità che ad un certo elemento di $X$ sia associata una certa label in $Y$;
* i modelli generativi rappresentano la *probabilità congiunta* $P(X, Y)$ o, in assenza di label, $P(X)$.

I modelli generativi sono quindi in grado di rappresentare la distribuzione dei dati. Tale distribuzione di probabilità viene invece ignorata dai modelli discriminativi, che tengono conto soltanto della probabilità che una determinata label sia associata ad una certa istanza.

!!!tip "Tipi di modello generativo"
    Notiamo che la definizione di modello generativo è *volutamente* generica, e include molti tipi di modello. Ad esempio, i modelli in grado di predire la parola successiva in una frase, come ChatGPT o Bard, possono essere considerati di tipo generativo, perché assegnano una probabilità all'occorrenza di un insieme di parole.

!!!note "Modelli discriminativi e probabilità"
    Il lettore più attento avrà notato come non tutti i modelli discriminativi si occupino di modellare una probabilità condizionale. Alcuni, come gli alberi decisionali, si limitano infatti a stabilire una serie di regole deterministiche per giungere ad un risultato.

##### Complessità dei modelli generativi

Appare chiaro come i modelli generativi si occupino di un task più complesso rispetto ai modelli discriminativi. Ad esempio, un modello generativo per le immagini deve catturare correlazioni come *gli oggetti che hanno la forma di barca devono apparire in prossimità di oggetti che assomigliano ad uno specchio d'acqua*, oppure ancora *gli occhi appaiono sul volto vicino al naso e sotto alla fronte*. I modelli discriminativi devono invece limitarsi ad apprendere la differenza tra *barca* e *non barca* osservando i pattern presenti nell'immagine: al modello non interessa quindi che la barca sia sull'acqua, ma semplicemente che siano presenti strutture riconducibili ad un'imbarcazione.

In modo più formale, i mdoelli discriminativi creano delle partizioni nello spazio edi dati, mentre i modelli generativi provano a modellare il piazzamento dei dati nello spazio, come mostrato in figura.

TODO: INTEGRARE GENERARTIVE_V_DISCRIMINATIVE

Per fare un esempio, il modello discriminativo sulle barche crea un contorno nell'iperspazio delle feature che stabilisce se l'immagine passata rappresenta una barca o meno. Nell'ipotesi ideale di correttezza del contorno, il modello potrà distinguere tra barche e non barche senza avere alcuna conoscenza sulle caratteristiche intrinseche di una barca. Di contro, un modello generativo dovrà invece generare delle feature che siano vicine alle loro controparti reali, per cui dovrà modellare la distribuzione dello spazio delle feature.

Le **Generative Adversarial Network**, o **GAN**, sono dei modelli in grado di approssimare una distribuzione di questo tipo. Introduciamone brevemente l'architettura.

## Anatomia di una GAN

Una generica GAN è composta da due parti:

* il **generatore** (*generator*) è la parte della rete che impara a generare dei dati plausibili;
* il **discriminatore** (*discriminator*) è la parte della rete che distingue i dati generati da quelli reali.

Sia il generatore sia il discriminatore sono delle reti neurali. In pratica, i campioni generati sono degli esempi *negativi* per il discriminatore, che penalizza il generatore ogni volta questo genera un campione riconosciuto come artefatto.

L'addestramento di una GAN procede quindi a grande linee come segue. Alle prime epoche, il generatore produce dei dati che sono palesemente falsi, e quindi facilmente penalizzabili dal discriminatore.

BAD_GAN

Man mano che il training procede, il generatore crea un output sempre più plausibile, confondendo sempre più il discriminatore.

OK_GAN

Al termine dell'addestramento, il discriminatore non sarà (idealmente) più in grado di individuare alcuna differenza tra un dato reale ed uno sintetico; di conseguenza, l'accuracy nell'occuparsi del problema binario diminuirà.

GOOD_GAN

Nella figura sottostante è rappresentata l'intera architettura di una generica GAN. In particolare, l'output del generatore è l'input del discriminatore, e l'intero insieme dei pesi della rete viene modificato in backpropagation per fare in modo che l'accuratezza del discriminatore converga verso lo zero.

GAN_DIAGRAM
