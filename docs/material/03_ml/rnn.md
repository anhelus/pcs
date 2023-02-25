LE *recurrent neural netrwork*, o RNN, sono una famioglia di reti neurali usate per elaborare dati sequenziali. Proprio come una rete convoluzionale è una rete neurale specializzata nell'elaborazione di una griglia di valori $X$ come un'immagine, una RNN è una rete neruale specializzata nell'elaboraziozne di una sequenza di valori $x^{(1)}, \ldots, x^{(\pi)}$. Proprio come le CNN possono prontamente scalare in immagini con grande ampiezza ed altezza, ed alcune CNN possono elaborare immagini di dimensione variabile, le RNN possono scalare a sequenze molto più lunghe di quelle gestibili da reti non specializzate. La maggior parte delle RNN pulò anche elabroare sequenze di lunghezza variabile.

Per Passare dalle reti multistrato alle RNN, dobbiamo sfruttare una delle prime idee nel machine learning e nei modelli statistici degli anni '80, ovvero quella di *condividere i parametri* tra diverse parti di un modello. Il parameter sharing rende possibile estendere ed applicare il modello ad esempi di diversa forma (lunghezza) e generalizzare. SE abbiiamo parametri separati per ogni valore dell'indice di tempo, non possiamo generalizzare a sequenzea di lunghezza non vista durante l'addestramento, né condividere punti statistici rilevanti lungo diverse lunghezza di sequenza e doiverse posizioni nel tempo. QUesta condivisione è particolarmente imporntae quando una specifica parte di informazione può avvenire a diverse posizioni nella sequenza. Ad esempio, consideriamo le due frasi:

* Sono andato in Nepal nel 2009* e *Nel 2009, sono andato in Nepal"

Se chiediamo ad un modello di machine learning di leggere ogni frase ed estrarre l'anno nel quale il narratore è andato in Nepal, vorremmo che l'anno 2009 venisse riconosciuto come la parte di informazione rilevante, sia che appaia nella sesta parola sia che appaia nella seconda parola della frase. Supponiamo di aver addestrato una rete feedforward che elabori frasi di lunghezza fissa. Una rete tradizionale compeltamente connessa avrebbe parametri separati per ogni feature di unput, per cui dovrebbe apprendere tutte le regole del liunguagguio separatamente in ogni posizione della frase. Per comparazione, una RNN condivide gli stessi pesi lugno vari step temporali.

Un'idea correlata è l'uso delle convoluzioni nelle sequenze temporali monodimensionali. QUesto approccio convoluzionale è alla base per le *time-delay* neural networks. L'operazione di convoluzione permette ad una rete di condividere i pamraetri nel tempo, ma è superficiale. L'usicta di una convoluzoien è ujna sequenza dove ogni membro dell'output è funzione di un piccolo numero di membri vicini dell'input. L'idea della convidivisione dei parametri si manifesta enll'applciazione dello stesso kernel convoluzionale ad ogni step temporale. Le RNN condividono i parametri in modod diferfrente. Ogni membro dell'output è una funzione dei precedneti membri dell'output. Ogni membro dell'output è prodotto suando la stessa regola di aggiornamento applicata agli output precedenti. Quewsta formulazione ricorrente risulta nella concidivisione di parma,metri attraverso un grafo computazionale estremamente profondo.

Per semplicità, ci riferiamop alle RNN come operanti su una sequenza che contiene vettori $x^{(t)}$ con l'indice dello step temporale $t$ che spazia da $1$ a $\tau$. In pratica, le RNN normalmente operano su minibatch di queste sequenze, con una diversa lunghezza di sequenza $\tau$ per ogni membro del minibatch. AAbbiamo omesso gli indici del minibatch per semplificare la notzione. Inoltre, l'indice dellos tep temporale non deve necessariamentre riferirsi al passaggio di tempo nel mondo reale. ALle volte si riferisce soltanto alla posziione nella sequenza. Le RNN possono essere anche applicate in due dimensioni su dati spaziali come le immagini, ed anche quando applicate ai dati che coinvolgono il tempo, la rete può avere connessioni che vanno indietro nel tempo, posto che l'intera sequenza sia osservata prima che sia stata fornita alla rete.

In questo capitolo, estendiamo l'idea di grafo computazionale per includere dei cicli. Questi rappresentano l'influenza del valore attuale di una varioabile sul suo valore in un futuro isntante temporale. Questi grafi computazionali ci permettono di definire le RNN. Descriviamo quindi diversi modi per costruire,a ddestra,re ed utilizzare le RNN.

## Esploriamo i grafi computazionali

Un grafo computazionale è un modo per formalizzare la struttura di un insieme di calcoli, come quelli coinvoltti nella mappatura degli input e dei parametri verso output e costi. In questa sezione, esploriamo l'idea di *svolgere* un calcolo ricorsivo o ricorrente in un grafo computazionale che aabbia una struttura ripetitiva, tipicamente coirrispondente all'insieme di evneti sotto analisi. Svolgere questo grafico permette di condividere i parametri in una struttura di deep network.

Ad esempioo, consideriamo la classifca forma di un sistema dinamico:

$$
s^{(t)}=f(s^{(t-1)}, \theta)
$$

dove $s^{(t)}$ è chiamato *stato* del sistema.

La precedente equazione è definita come *ricorrente* perchè la definizione di $s$ al tempo $t$ torna indietro alla stessa definizione al tempo $t-1$.

Per un numero finito di istanti temporali $\tau$, il grafo può essere dispiegato applicando la definziione $\tau - 1$ volte. Ad eesempio, per $\tau=3$ optteniamo:

$$
s^{(3)}=f(s^{(2)}, \theta) = f(f(s^{(1)}, \theta), \theta)
$$

Dispiegare l'equazione applicando ripetutatmente la definizione ci ha portato un'espressione che non prevede la ricorrenza. UN'espressione di questo tipo può essere adesso rappresentata da un grafo tradizionale aciclico. Nella figura successiva vediamo un esempio.

TODO: FIGURA DISPIEGAMENTO GRAFO

Le RNN possono esesre costruite in diversi modi. Così come quasi ognfi funzione può essere considerata una rete feedformard, opgni funzione che coinvolge la ricorrenza può essere considerata una RNN.

Molte RNN usano la sequenge equazione per definrie i valori delle loro unità nascoste.

$$
h^{(t)}=f(h^{(t-1)}, x^{(t)}, \theta)
$$

dove $h$ rappresenta lo stato della rete.

Quadno le RRNN sono addestrate ad effettuare un task che richiede la predizione del futuro dal passato, la rete tipicamente aprpender ad usare $h^{(t)}$ come un tipo di LOSSY SYMMARY degli aspetti rielvnati per il task della sequenza passata di input fino a $t$. Questo sommario è in genrarle necessariamente lossy, dal momento che mappa una lunghezza di sequenza arboitraria $(x^{(t)}, x^{(t-1)}, x^{(t-2)}, \ldots, x^{(2)}, x^{(1)}) in un vettore di lunghezza fissata $h^{(t)}$. A seconda del criterio di addestramento, questo sommario può mantenere selettivamente alcuni aspetti della sequenza passata con più precisione di altri aspetti. Ad esempio, se la RNN è usata nello statistical language mdoeling, tipicamente per predire la parola successiva data delle parole precedenti, mermoizzare tutte le informazioni nella sequenza di uinput fino all'istante $t$ potrebbe non essere necessario; memorizzare soltnato infomrazioni sufficienti a predire il resto della frase è sufficiente. La situazione più sfidante è quando chiediamo ad $h^{(t)}$ di essere ricco a sufficienza per permettere di recuperare in maneira approssimativa la sequenza di input, come negli autoencoder. 


