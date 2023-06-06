# 5.5.1 - Introduzione alla object detection

Quello della *object detection* è un campo applicativo della computer vision il cui duplice obiettivo è quello di *identificare* e *localizzare* determinate classi di oggetti  all'interno di immagini o video. In particolare, la object detection ci permette di identificare la posizione degli oggetti mediante una *bounding box*, che altro non è se non un rettangolo che sarà "disegnato" attorno all'oggetto di interesse. 

<figure markdown>
  ![obj_det](./images/obj_det.png)
  <figcaption>Figura 1 - Un esempio di object detection. A bounding box di colore differente corrispondono oggetti di tipo differente; in particolare, nelle diverse figure riconosciamo pomodori, nodi e fiori.</figcaption>
</figure>

Tradizionalmente, il task di object detection veniva effettuato sfruttando tecniche di *template matching*: un esempio sono infatti gli approcci usati fino ai primi anni '00 per il riconoscimento facciale, come il *classificatore di Viola - Jones*, il quale prevedeva l'uso di particolari maschere, dette per l'appunto *template*, che venivano fatte "scorrere" sull'immagine alla ricerca di zone che rispettassero il pattern individuato.

A partire dalla seconda metà degli anni '10, tuttavia, si sono andati via via diffondendo gli approcci basati sulle deep neural network. In particolare, esistono due tipologie di algoritmo:

* nei *two-stages object detector* l'immagine viene dapprima passata attraverso una *Region Proposal Network*, che ha lo scopo di individuare le regioni "candidate" ad "ospitare" un determinato oggetto. A valle di questo primo stage, per ogni zona è determinato un punteggio che va a determinare se sia presente o meno una determinata tipologia di oggetto;
* nei *single-stage object detector* i due passaggi sono "condensati", e localizzazione e valutazione del tipo di oggetto sono effettuati in un unico passo.

Vediamo quindi nel dettaglio questi ultimi algoritmi, che sono anche i più utilizzati, soprattutto grazie alle performance che sono in grado di offrire.
