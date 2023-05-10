## Contractive autoencoders

In modo simle ad altri autoencoder, i contractive autoencoder effettuano il task diu apprendere una raprresentazione dell'immagine mentre la passano attraverso una bottleneck e la ricopstruiscono nel decoder.

I contaractive autoencoder ahnno anche untermine di regoalrizzazione che fa in modo che lar ete non apprenda la funzione identità mappando l'input nell'output.

I contractive autaoneder lavorano sulla base che input siili devono avere degli encoding simili e delle rappresentazioni nello spazio latente simili. Singifica che lo spazio latnete nonv arietà di un grosso quantitativo per variazioni minori dell'inputo.

Péer addestrare un modello che lavora con questi vincoli, dobibiamo assicuracri che le derivate deglle attivazioni deglis strati nascosti siano piccole rispetto agli intgressi, ovvero $\delta h / \delta x$ sia piccolo, dove $H$ è lo strato nascosto ed $x$ l'input.

Una cosa importnat eda notar enela funzione dic osto (formata dalla norma delle derivate e dalla reconstruction loss) è chje i due termini si contraddicono tra loro.

Mentre la reconstruction loss vuole che il modello idnichi dell diferenze tra due input e osservi le varizzioni nei dati, la nomra di Frobenius delle derivate dice che il modello deve essere in grado di gnorare variazioni nei dati di input.

M;ettere queste condizioni contradditorie in una funzioen di costo ci permette di addestare una rete dove gli strati nascoisti catturano soltanto le infomraizoni più essenziali. Questa informaizone e necessaria a separare i dati ed ingorare informazioni che non sono di natura discriminativa.

La fuinzione di costo totale può esser3e espressa matematicamente come:

$$
L = |x - \hat{x}|+\lambda \sum_i \| \nabla_x a_i^h x\|^2
$$

doive $h$ è lo strato anscosto per il quale il gradiente viene calcoalto e rappresentato rispetto all'input $x$ come $\nabla_x a_i^h x$.

Il gradieente viener sommato su tutti i campioni di training, e viene presa la normal di Frobeniu