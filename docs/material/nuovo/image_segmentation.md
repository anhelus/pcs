# Image Segmentation

La *instance segmentation* permette ai nostri modelli di computer vision di conoscere i specific contorni di un'oggetto in un'immagine.

La instance segmentation, conosciuta anche come *image segmentation*, è il task che riconosce gli oggetti in immagini assieme alla loro forma associata. è un'estenseione della [object detection](./object_detection.md) dove ogni predizione inclue anche una forma, in modo differente a semplicemente una bounding box defintia da un punto centrale, un'altezza ed una larghezza.

Grazie alla instance segmentation, l'applicazione può determinare il numero di oggetti in un'immagine, la classificazione, ed il loro contorno.

E' utile nei casi dove dobbiamo misurare la dimensione degli oggetti individuati (ad esempio una foglia di pomodoro), tagliarli fuori dal background (ad esempio, per la rimopzione del background) o individuare oggetti ruotati ed oblunghi (ad esempio un ponte in un'immagine satellitare).

## Comparare la instance segmentation ad altri algoritmi di computer vision

Come si confronta la instance segmentation ad altri algoritmi utili a risolvere problemi di computer vision?

##### Instance Segmentation vs Object Detection

Sia la instance segmentation sia la object detection identificano la posizione di un oggetto in un'immagine. tuttavia, l'object detection predice soltanto la bounding box dell'oggetto, e non il contorno.

Ecco alcune cose da sapere:

* il labeling per la segmentation richiede più tempo
* è più complesso addestrare dei modelli di instance segmentation
* i modelli per  l'instance segmentation sono normalmente più grandi, lenti, e meno ottimizzati
* i modelli di instance segmentation possono richiedere dataset più grandi per ottenere la stessa accuracy dei mdoelli di object detection.

Il consiglio è di usare la instance segmentation se la specifictà del contorno dell'oggetto è richiesta dall'applciazione specifica. Spesso è meglio provare la object detection prima, èerché è piùà semplice e facile da testare, e più veloce ed accurata in fase di esecuzione.

Ad esempio, l'intance segmentation può essere usata per misurare l'area di un LAWN da immagini satellitari. Tuttavia, se dobbiamo identificare tutti gli alberi su un LAWN, un modello più prudente da usare sarebbe quello di object detection

##### Instance segmentation vs Semantic segmentation

La semantic segmentation etichetta ogni pixel in un'immagine con una label di classe. In modo simile all'instance semgentation, possiamo vedere i controrni di un oggetto in un'immagine, ma  adifferenza della intance segmantation, non possiamo contare o differenziare tra oggetti separati se questi sono sovrapposti.

## COme effettuare il labeling

Le imagini per i problemi di instance segmentation devono essere etichettate nella maniera più precisa possibile, evidenziando il contorno dell'oggetto da annotare e quindi assegnando l'oggettoa d una classe.

Una volta etichettato il dataset, si pulò addestrare il modello.

Il formato più comune per i dataset di instance semgentation è COCO, che registra i punti della segmentazione in una serie di coppie x, y.
