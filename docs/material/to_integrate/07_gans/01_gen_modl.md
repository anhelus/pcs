# Cosa è un modello generativo?

Cosa indica la parola "generativa" nel nome "Generative Adversarial Network"? "Generative" descreive una classe di modelli statistich che è in contrasto con i modelli discriminativi.

Informalmente:

* i modleli generativi pososno generare nuoive istanze dei dati
* i modelli discriminativi discriminano tra diversi tipi di istanze dati

Un modello tgenerativo può generare nuove foto di animali che sembrano vere, mentre un modello discrimnativo può distinguere un cane da un gato. Le GAN sono un tipo di modello generativo.

Più formalmente, dato un set di istanze $X$ ed un insieme di label $Y$:

* i modelli generativi cattuirano la probabilitàc congiunta $p(X, Y)$, o semplicemente $P(X)$ se non vi sono delle label
* i modelli discriminativi catturano la probabilità condizionale $P(Y | X)$

Un modello generativo include la distribuzione dei dati stesdsi, e ci indica qunaot è probabile un dato esempio. Per esempio, i modelli che predicono la parola successiva in una frase sono tipicamente di tipo generativo (molto più semplici delle GAN) perché possono assegnare una probabilità ad un insieme di parole.

Un omoddello discriminativo ignora la questione del fatto che uan data istanza è probabile, e ci dice soltanto quanto è probabile che una label si applichi all'istanza.

Notiamo che quhesto è una definizione molto generica. Ci sono molti tipi di modelli generativi. Lçe GAN sono soltanto un tipo di questo tipo di modelli.

## Modellare le probabilità

Nessun tipo di modello deve restituire necessariamente un numero che rappresenta una probabilità. Possiamo modellare la distrribuzione dei dati imitandoq uesta distrubuzione.

Ad esempio, un classificaortre discriminativo come un albero decsionale può etichettare un'istanza senza assegnare una rbabilitàò a questa label. Un classificatrore di questo tipo è+ comunque un modello perché la distribuizione di tutti i label predetti modella la distribuzione reale delle label nei dati.

In modo simile, un modello generativo può modelare una distribuzione producendo dei dati falsi (ma convincenti) che appaiono come quelli estratti da quella distribuzione.

## I modelli generativi sono complessi

I modelli generativi si occupano di un task più complesso dei modelli discrimin ativi. I modelli generativi infatti devono modellare piùd ettagli.

Un modello generativo per le immagini potrebbe catturare delle correlazioni come "cose che sembrano barche e probabilmente appaiono vicino ad oggetti che ricordano l'acquia" e "gli occhi probabilmente non appaiono sulla fronte". Queste sono distribuzioni estremamente complesse da modellare.

Di contro, un modello discriminativo può apprendere la differenza tra "barca" e "non barca" guardando a dei pattern nell'iummagine. Potrebbe ignorare molte delle correlazioni che il modello generativo deve invece comprendere.

I modelli discrimniativi provano a disegnare dei contorni nello spazio dei dati, mentre i modelli generativi provano a modellare come i dati sono piazzati nello spazio. Per esempio, il seguente diagramma mostra i modelli discriminativi e genrativi per cifre scritte a mano:

TODO: INTEGRARE GENERARTIVE_V_DISCRIMINATIVE

Il modello discriminativo prova a stabilire la differenza tra gli 0 e gli 1 scritti a mano tracciando una linea nello spazio dei dati. Se la linea è corretta, può doistinguere tra gli 0 e gli 1 senza dovefr sapere come si caratterizza esattamente un'istanza nello spazio dei dati su una qualsiasi parte della riga.

Di contro, il modello generativo prova a produrre degli 1 e degli 0 convincenti generando delle cifre che sono vicine alle loro controparti reali nello spazio dei dati. Deve modellare la distribuzione nello spaizo dei dati.

Le GAN offrono un modo efficace di addestrare questi modelli per ricordare una distribuzione reale. PEr comprendere come funzionano dobbiamo imparare a comprender ela struttura base di una GAN.
