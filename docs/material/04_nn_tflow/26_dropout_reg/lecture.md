# 26 - Overfitting e regolarizzazione

Nella lezione precedente abbiamo limitato il training delle reti neurali a 10 epoche, usando come metrica di test esclusivamente l'accuratezza sui dati di training.

Tuttavia, se proseguissimo nel training e valutassimo anche l'accuratezza sui dati di validazione, noteremmo che ad una certa epoca questa raggiungerà un picco, per poi iniziare a stagnare o, in alcuni casi, *diminuire*: in altre parole, il nostro modello andrà incontro ad **overfitting**. Gestire correttamente questa situazione è molto importante: infatti, ottenere un'elevata accuratezza sui dati di training non è importante quanto sviluppare un modello in grado di generalizzare su dati che non ha visto durante l'addestramento.

L'opposto dell'overfitting è, abbastanza prevedibilmente, l'**underfitting**, situazione che si verifica quando vi è ancora la possibilità di migliorare il modello. Di solito, l'underfitting si verifica nel momento in cui un modello non è abbastanza descrittivo, oppure quando non è stato addestrato per un numero di epoche sufficienti, non permettendo alla rete di caratterizzare i pattern di rilievo presenti nei dati.

Ovviamente, trovare i parametri ottimali di addestramento significa trovare un equilibrio tra overfitting ed underfitting. In primis, infatti, è necessario scegliere accuratamente il numero di epoche di addestramento, per evitare una scarsa (o al contrario eccessiva) adesione del modello ai dati. Inoltre, è necessario verificare che i dati di training utilizzati siano adeguati, seguendo magari le indicazioni date in precedenza; infine, qualora questi passi siano già stati compiuti, può essere necessario utilizzare delle tecniche di **regolarizzazione**.

## 26.1 - Strategie di regolarizzazione

Abbiamo già discusso delle strategie di regolarizzazione quando abbiamo visto la regressione logistica.

In pratica, per comprendere il motivo per cui si usa la regolarizzazione possiamo usare il concetto di *rasoio di Occam*, ovvero, date due possibili spiegazioni per lo stesso fenomeno, quella che con tutta probabilità lo descrive in maniera migliore è anche la più semplice o, in altre parole, quella che assume il minor numero di ipotesi.

Questo concetto si applica anche ad un modello di rete neurale: data un'architettura, esistono diverse combinazioni di valori di pesi che possono spiegare i dati, ed in generale le combinazioni più semplici corrono meno il rischio di andare in overfitting se comparati a quelli più complessi.

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

## 26.2 - Dropout

Un altro metodo di regolarizzazione molto diffuso è dato dall'uso di uno strato di **dropout**.

L'idea alla base del dropout sta nel fatto che ogni nodo della rete deve restituire in output delle feature utili *a prescindere* da quelle restituite dagli altri nodi. Per ottenere questo risultato, si fa in modo che un certo numero di neuroni (scelti in maniera casuale ad ogni iterazione) dello strato precedente venga ignorato dal layer che implementa il dropout.

In questo modo, il layer modifica ad ogni iterazione la sua connettività, ottenendo in un certo senso un diverso "punto di vista" sui dati stessi: in tal senso, il dropout aggiunge in maniera artificiosa del rumore *sul processo di apprendimento*, forzando una maggiore o minore importanza delle connessioni a seconda dei nodi scartati, ed evitando quindi delle situazioni dove i layer di rete tendono ad adattarsi vicendevolmente per "correggere" gli errori di predizione. Di conseguenza, il modello acquisisce maggiore capacità di generalizzazione, visto e considerato che ogni neurone isolerà delle feature in maniera indipendente dagli altri.

Per quello che riguarda gli iperparametri usati dal layer di dropout, il più importante è quello che specifica la probabilità con la quale gli output dello strato precedente vengono scartati. Un valore comune in tal senso è $0.5$ per gli strati nascosti, e $0.8$ per lo strato di input.
