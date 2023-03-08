# Yolo

prima di Yolo: R-CNN, two stage detectors

Questi generano numrose region proposal, ovvero candidate buonding box, e quindi vanno ad individuare gli oggetti all'interno di ogni regione. YOLO propone di unificare i due step.

1. YOLO suddivide l'immagine di ingresso in una griglia $S \times S$. Se il centro di un oggetto ricade all'interno di una cella nella griglia, quella cella sarà incaricata di effettuare la detection di quell'oggetto.
2. Ogni cella predice $B$ bounding box con il relativo confidence score. Questi punteggi di confidenza rifletto quanto è "certo" il modello che la bounding box contenga un oggetto, ovvero P(obj) (la probabilità che ci sia un oggetto nella bounding box).

ogni bounding box consiste di $5$ predizioni: $x, y, w,h$ ed il confidence score.

le coordinate (x, y) rappresentano il centro della box relativamente ai confini della cella.

l'ampiezza w e l'altezza h sono predette rispetto all'intera immagine

la confidenza rappresenta l'IoU tra la box predetta ed il ground truth

Ogni cella predice anche le probabilità di classe condizionali: $P(Class|Obj)$.

# Struttura del modello

YOLO ha 24 layer onvoluzionali seguiti da due fully connected. La presenza di layer $1 \times 1$ permette di ridurre lo spazio delle feature rispetto ai layer precedenti.

### loss function

5 termini nella funzione di costo:

1. il primo termine è (x,y): le coordinate x ed y della bounding box sono parametrizzate rispetto alla griglia, di modo da essere comprese tra 0 ed 1. Inoltre, la somma degli errore quadratico è stimata solo dove vi è la presenza dell'oggetto.

2. il termine (w, h): l'ampiezza e l'altezza della bounding box sono normalizzate per l'ampiezza ed altezza dell'immagine in modo che ricadano tra 0 ed 1. l'SSE è stimato solo dove c'è la presenza dell'oggetto. DAl momento che piccole deviazioni in grosse box contano meno che in piccole box, la radice quadrata di w e di h invece di w e h direttamente sono usate per risolvere parzialmente il problema.

3. il terzo ed il quarto termine (la confidenza), ovvero la IoU tra il box predetto ed uno qualsiasi dei box per il ground truth: in ogni immagine ci sono molte celle che non contengono alcun oggetto. Questo spinge i punteggi di confidenza di queste celle verso lo zero, spesso dando maggior risalto al gradiente dalle celle che contengono un oggetto, e rendendo il modello instabile. Quindi, il costo dalle predizioni di confidenza per le bxo che non contengono alcun oggetto viene diminuito.

4. il quinto termine è la probabilità delle classi, ovvero l'SSE delle probabilità di classe quando vi è un oggetto.

## YOLO v2

1. uso del batch normalization
2. classificatori a risoluzione più alta (224 x 224 e 448 x 448)

3. YOLOv2 rimuove tutti i layer completamente connessi ed usa le *anchor boxes* per la predizione delle bounding box.

viene rimosso un pooling layer per aumentare la risoluzione dell'output.

Le immagini 416x416 sono usate per addestrare la rete

la feature map ottenuta è 13x13 (sottocampionata 32 volte)
Il batch norm

con le anchor box, si abbassa la mAP, ma aumenta molto il recall.

## Demo

Per la nostra demo, utilizzeremo YOLOv8.

Partiamo installando il package:

```sh
pipenv install ultralytics
```

Abbiamo a questo punto due possibilità. La prima è quella di utilizzare la CLI (Command Line Interface). L'altra è invece quella di utilizzare il tutto in un nostro script Python. Ovviamente, sceglieremo quest'ultima.
