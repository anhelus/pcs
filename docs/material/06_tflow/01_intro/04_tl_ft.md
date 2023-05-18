# 6.1.4 - Transfer learning e fine tuning

Le reti neurali, e soprattutto le CNN, presentano un'interessante caratteristica: infatti, apprendono delle feature *generiche* nei primi strati, specializzandosi sullo specifico problema man mano che si va in profondità nella rete.

Partendo da questa considerazione è stata elaborata la tecnica del **transfer learning**, che consiste nel prendere il modello addestrato su un problema, e riconfigurarlo per risolverne uno nuovo ma, ovviamente, simile (ad esempio, un tool che permette di valutare la razza di un gatto può essere usato mediante transfer learning per distinguere tra leopardi e tigri). Questa tecnica permette anche di addestrare un numero limitato di parametri, per cui è possibile utilizzarla quando si ha a che fare con dataset di dimensioni limitate.

In tal senso, il transfer learning segue di solito questi step:

* consideriamo i layer ed i pesi di un modello addestrato in precedenza;
* effettuiamo il *freezing* (congelamento) di questi layer, fissando i valori dei pesi;
* creiamo ed inseriamo alcuni layer successivi a quelli congelati per adattarli al nostro problema;
* addestriamo i nuovi layer sul nostro problema.

Opzionalmente, è possibile effettuare un passaggio di *fine tuning*, "sbloccando" il modello ottenuto in precedenza e riaddestrandolo sull'intero dataset con un basso learning rate.
