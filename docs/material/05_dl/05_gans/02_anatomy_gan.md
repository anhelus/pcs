# 5.5.2 - Generatore e discriminatore

Vediamo adesso nel dettaglio le singole parti dell'architettura della GAN.

## Discriminatore

Il discriminatore di una GAN è, semplicemente, una classica rete neurale utilizzabile come classificatore binario, il cui scopo è quello di distinguere i dati reali (*classe positiva*) da quelli generati (*classe negativa*).

GAN_DIAGRAM_DISCRIMINATOR

I dati per l'addestramento del discriminatore provengono da due sorgenti:

* *istanze reali*, come ad esempio foto di barche vere, ed usate come campioni di classe positiva;
* *istanze generate*, usate come campioni di classe negativa.

##### Addestramento del discriminatore

Durante l'addestramento del discriminatore, il generatore è "fermo", e non aggiorna i suoi pesi, che rimangono costanti man mano che produce i dati per l'addestramento del discriminatore. Ciò significa quindi che la funzione di costo del generatore viene ignorata, utilizzando soltanto quella del discriminatore. In particolare, la funzione di costo di quest'ultimo è tarata in modo che il discriminatore venga penalizzato per aver mal classificato un'istanza reale come falsa o, alternativamente, una falsa come reale.

## Generatore

Il generatore si addestra invece a creare dei dati falsi utilizzando il feedback ricevuto dal discriminatore; lo scopo ultimo è quello di fare in modo che il discriminatore sia portato a classificare l'output del generatore come *vero*. Tuttavia, come intuibile, l'addestramento del generatore richiede l'integrazione più stretta tra questo componente ed il discriminatore, in quanto è necessario l'output di quest'ultimo, in quanto la funzione di costo penalizza il generatore qualora questo non riesca ad ingannare il discriminatore.

GAN_DIAGRAM_GENERATOR

##### Addestramento del generatore

Per prima cosa, dovremo scegliere un input per inizializzare il generatore, che dovrà trasformarlo, a valle dell'addestramento, in un output significativo. In tal senso, possiamo scegliere un meccanismo di generazione casuale dei dati, come ad esempio un rumore; sperimentalmente, si è verificato che la distribuzione del rumore ha un impatto limitato sull'uscita finale, per cui è possibile scegliere una forma di facile campionamento, come ad esempio una distribuzione di tipo uniforme.

Scelto il dato in input, dovremo addestrare il generatore, il che è mediamente più complesso rispetto all'addestramento di una normale rete neurale. Infatti, il generatore dovrà inviare il suo output al discriminatore, il quale produrrà la predizione che vorremo influenzare. La funzione di costo del generatore penalizzerà quindi il generatore quando questo produrrà un campione che il discriminatore classifica come falso. L'algoritmo di backpropagation deve quindi includere questo meccanismo: per farlo, partiremo dall'output del discriminatore, fino all'input del generatore. Contestualmente, però, non vogliamo che il discriminatore venga modificato durante l'addestramento del generatore, in quanto staremmo di fatto cercando di colpire un bersaglio in movimento! Di conseguenza, addestreremo il generatore seguendo questi step:

1. campionamento di un rumore di casuale;
2. definizione dell'output del generatore a partire dal rumore campionato al passo $1$;
3. ottenimento dell'output di classificazione del determinatore (*vero*/*falso*);
4. calcolo della loss del discriminatore;
5. backpropagation dal discriminatore verso il generatore per aggiornare i gradienti;
6. aggiornamento dei pesi del solo generatore.

Vediamo adesso come mettere assieme i due pezzi, ed addestrare congiuntamente il discriminatore ed il generatore.

## Addestramento di una GAN

Dato che una GAN contiene, nei fatti, due reti addestrate separatamente, dovremo definire un algoritmo in grado di gestire due diverse tecniche di addestramento, e che sia contestualmente in grado di identificare la situazione di convergenza della rete.

In primis, l'addestramento procede su binari alternati. In particolare, si inizia addestrando il discriminatore per un certo numero di epoche, processo a cui segue l'addestramento del generatore. Questi due step vengono quindi ripetuti iterativamente. Sottolineamo come i pesi di ciascuna rete saranno mantenuti costanti mentre si addestra l'altra: ciò permette alle GAN di addestrare ciascuna delle sue parti nonostante meccanismi differenti, risolvendo problemi di tipo generativo altrimenti non affrontabili.

Ovviamente, man mano che il generatore migliora, le performance del disriminatore peggiorano, in quanto questo non sarà più in grado di distinguere tra i dati reali e quelli generati. Nel caso (ideale) in cui il generatore sia in grado di generare immagini che confondono il discriminatore nel $100\%$ dei casi, allora l'accuracy di quest'ultimo sarà del $50\%$: nei fatti, il discriminatore effettua le predizioni in maniera completamente casuale, proprio come se stesse lanciando una moneta.

Questa progressiva degenerazione delle performance del discriminatore è però un problema per la GAN: infatti, se l'addestramento continua oltre il punto in cui il discriminator sta dando risposte completamente casuali, allora il generatore dovrà addestrarsi a partire da un output non significativo, degradando quindi le sue performance. In generale, quindi, possiamo dire che per una GAN la convergenza non è mai uno stato "stabile", ma dipende sempre da un delicato equilibrio tra le perfomrance del discriminatore e quelle del generatore.

Nella [prossima lezione](03_loss_gan.md), vedremo quali sono le funzioni di costo che vengono utilizzate per l'addestramento di questo tipo di reti.
