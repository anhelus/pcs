Per predire e localizzare molti diversi oggetti in una immagine, molti tra i modelli di object detection allo stato ell'arte iniziano da una anchor box.

I modelli in particolare usano le bounding box come segue:

* formano migliaia di anchor box candidate sull'immagine
* per ogni anchor box, predicono dell'offset da questa box come *candidate box*
* calcolano una loss function basata sull'esempio del ground truth
* calcolano una probabilità che una certa candidate box si sovrapponga con un oggetto reale (quindi etichettato)
* se quella probabilità è maggiore di 0.5, allora la predizione contribuisce alla loss function
* premiando e penalizzando le box predette il modello si porta lentamente verso la localizzazione dei veri oggetti

Le anchor box sono un insieme di bounding box predefinite di una certa altezza ed ampiezza. Queste sono definite per catturare la scala e l'aspect ratio di una specifia classe di oggetti che vogliamo individuare, e sono normalmente scelte sulla base delle dimensioni degli oggetti nel nostro dataset di training. Durante la detection, le anchor box predefinite sono TILED lungo tutta l'immagine. La rete predice la probabiiilità ed altri attributi, come il background, l'intersection over union, e gli offset per ogni TILED anchor box. Le predizioni sono usate per rifinire ogni anchor box individuale. Possiamo definire diverse anchor box, una perr ciascuna dimensione dell'oggetto. Le anchor box sono in pratica dei guess iniziali di bounding box con dimensioni fisse.

la rete non predice direttamente le bounding box, ma piuttosto le probabilità e e rifiniture che corrispondono alle TILED anchor box. La rete restituisce un insieme univoco di predizioni per iascuna anchor box definita. La feature map finale rappresenta le object detection per ciascuna classe. L'uso delle anchor box permette ad una rete di individuare più pggetti, oggetti a diverse scale, ed oggetti sovrapposti.

https://it.mathworks.com/help/vision/ug/anchor-boxes-for-object-detection.html
