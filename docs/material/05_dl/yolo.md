# X.X - You Only Look Once (YOLO)

## Architettura

L'archiettura di YOLO consta di 24 layer convoluzionali, quattro layer di max pooling, e due layer completamente connessi.

Il funzionamento è come segue:

* le immagini sono ridimensionate in $448 \times 448$ prima di attraversare la rete convoluzionale;
* una convoluzione $1 \times 1$ viene per prima cosa applicata per ridurre il numero di canali, seguita quindi da una convoluzione $3 \times 3$;
* la funzione di attivazione è la ReLU, ad eccezione del layer finale, che usa una funzione di attivazione lineare;
*tecniche di regolarizzazione come batch normalization e dropout sono utilizzate per far ein modo che il modello non vada in overfitting.

L'algoritmo lavora sulla base di quattro step.

##### Step 1: residual blocks

Il primo step divide l'immagine originaria in $N \times N$ griglie di forma uguale. Ogni cella nella griglia è responsabile per la localizzazione e la predizione della classe di oggetti che copre, assieme ad un punteggio di confidenza.

TODO IMMAGINE

##### Step 2: bounding box regression

Il passo successivo consiste nel determinare le bounding box, ovvero i rettangoli che contengono al loro interno tutti gli oggetti presenti nell'immagine. Possiamo avere tanti bounding box quanti sono gli oggetti all'interno di una certa immagine.

YOLO determina gli attributi di questi bounding box usando un singolo modulo di regressione nel seguente formato, dove $Y$ è il vettore che rappresenta ciascun bounding box:

$$
Y = [p_c, b_x, b_y, b_h, b_w, c_1, c_2]
$$

Questo è importante specialmente durante la fase di addestramento del modello.

* p_c corrisponde al punteggio di probabilità associato al fatto che la griglia contenga un oggetto. Ad esempio, tutte le griglie mostrate in rosso in FIGURA 2 hanno un punteggio più alto di zero, mentre quelle in giallo hanno un punteggio pari a zero.
* b_x e b_y sono le coordinate $(x, y)$ del centro della bounding box rispetto alla cella che racchiude l'oggetto;
* $b_h, b_w$ sono invece l'altezza e l'ampiezza della bounding box che contiene l'oggetto di interesse;
* $c_1, c_2$ corrispondono alle due classi (giocatore e palla). Ovviamente, possiamo avere tante classi quante richieste dal caso d'uso specifico.

FIGURA

##### Step 3: Intersection Over Unions (IoU)

La maggior parte delle volte, un singolo oggetto in un'immagine può avere più candidati per la stessa griglia, anche se non tutti sono rilevanti. L'obiettivo della IoU, valore compreso tra $0$ ed $1$, è quello di scartare le bounding box non rilevanti, mantendo solo quelle rilevanti. In pratica:

* l'utente definisce la soglia per la IoU (di solito, $0.5$);
* YOLO quindi calcola la IoU di ogni cella, ovvero il rapporto tra l'area delle intersezioni e quella dell'unione;
* infine, sono ignorate le predizioni che hanno una IoU minore o uguale alla soglia, e considerano quelle con una IoU maggiore o uguale alla soglia.

TODO FIGURA 4

##### Step 4: Non-Max Suppression (NMS)

Impostare una soglia per la IoU non sempre basta, perché un oggetto può avere più bounding box con una IoU al di sopra della soglia, e lasciare tutte queste soglie può causare del rumore. Qui, possiamo usare il NMS per mantenere solo le box con lo score di detection più alto.

## Oltre YOLO

La prima versione di YOLO ha comportato numerose innovazioni in ambito di object detection grazie alla sua capacità di riconoscere oggetti in maniera rapida ed efficiente.

Tuttavia, così come per molte altre soluzioni, la prima versione di YOLO aveva le sue limitazioni:

* non era in grado di indiivudare immagini di piccole dimensioni all'intertno di un gruppo di immagini, come un gruppo di persone in uno stadio. Questo è legato al fatto che ogni griglia nell'archiettura YOLO è progettata per individuare singoli oggetti;
* quindi, YOLO non è in grado di individuare forme nuove o non usuali;
* infine, la funzione di costo usata per approssimare le performance di detectiontratta gli errori allo stesso modo per le bounding box di piccole e grandi dimensioni, il che crea delle localizzazioni non corrette.


