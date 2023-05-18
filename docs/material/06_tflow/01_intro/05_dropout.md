# 6.1.5 - Regolarizzazione in TensorFlow

Abbiamo già visto i concetti alla base della [regolarizzazione](../../03_ml/01_intro/07_regularization.md) in una delle lezioni precedenti, ma può comunque essere utile richiamarli brevemente.

L'uso della regolarizzazione può essere spiegato con il concetto di *rasoio di Occam*, per il quale, date due possibili spiegazioni per lo stesso fenomeno, quella che lo descrive meglio è molto probabilmente la più semplice (o, più formalmente, *quella che assume il minor numero di ipotesi*).

Questo concetto si applica anche ai modelli di machine e deep learning: data (ad esempio) un'architettura di reti neurali, esistono diverse combinazioni di pesi che possono spiegare i dati ma, in linea generale, le combinazioni più semplici sono meno soggette all'overfitting se comparate a quelle più complesse.

Dalla precedente affermazione discende che un modo comune di mitigare l'overfitting del modello ai dati è inserire degli opportuni vincoli sulla complessità della rete, "forzando" i pesi ad assumere valori ridotti, e rendendo implicitamente la distribuzione di detti valori maggiormente uniforme. Questo procedimento, chiamato *weight regularization*, è ottenuto aggiungendo alla funzione di costo della rete un termine direttamente proporzionale al valore del peso. Di solito, si utilizzano due tecniche di regolarizzazione:

* nella *regolarizzazione L1* il costo aggiunto è proporzionale al valore assoluto dei coefficienti dei pesi, ovvero alla norma $L^1$;
* nella *regolarizzazione L2* il costo aggiunto è proporzionale al quadrato del valore dei coefficienti dei pesi, ovvero alla norma $L^2$. 

!!!note "Nota"
    In generale, la regolarizzazione L1 favorisce la "sparsità" dei dati, forzando il valore di alcuni pesi a $0$. Ciò non avviene con la regolarizzazione L2.

In Keras, possiamo aggiungere un parametro di regolarizzazione usando il package `regularizers` ed il parametro `kernel_regularizers` del layer da regolarizzare:

```py
from keras import regularizers

layers.Dense(
    64,
    activation='relu',
    kernel_regularizers=regularizers.l2(0.001))
```

In questo caso, stiamo usando un valore di regolarizzazione pari a $0.001$, il che significa che ogni peso del layer regolarizzato aggiungerà un valore pari a $0.001 \cdot w_i^2$ al costo totale della rete, con $w_i$ valore del peso dell'$i$-mo coefficiente.

## Dropout

Un'altra tecnica di regolarizzazione molto diffusa nelle reti neurali è legata all'uso di un layer di **dropout**.

L'idea alla base del dropout sta nel fatto che ogni nodo della rete deve restituire in output delle feature utili *a prescindere* da quelle restituite dagli altri nodi. Per far ciò, si fa in modo che un certo numero di neuroni (scelti in maniera casuale ad ogni iterazione) dello strato precedente venga ignorato dal layer che implementa il dropout.

In questo modo, il layer dovrà cambiare ad ogni iterazione la sua connettività, ottenendo in un certo senso un diverso "punto di vista" sui dati stessi. Si può quindi dire che il dropout in un certo senso aggiunga del "rumore" al processo di apprendimento, forzando le connessioni a modificare la loro importanza a seconda dei nodi scartati, ed evitando quindi situazioni dove i layer di rete tendono ad adattarsi vicendevolmente per "correggere" gli errori di predizione. Di conseguenza, dato che ogni neurone isolerà delle feature in maniera indipendente dagli altri, il modello acquisisce maggiore capacità di generalizzazione.

Per quello che riguarda gli iperparametri usati dal layer di dropout, il più importante è quello che specifica la probabilità con la quale gli output dello strato precedente vengono scartati. Un valore comune in tal senso è $0.5$ per gli strati nascosti, e $0.8$ per lo strato di input.
