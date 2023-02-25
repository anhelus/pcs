LE reti convoluzionali, conosciute anche come *convolutional neural networks* o CNNs, sono una tipologia specializzata di reti neurali per l'elaborazione dati che ha una topologia basata sul concetto di convoluzione. POssono essere applicati a dati di varia dimensionalità: ad esempio, sono state usate su dati monodimensionali come le serie temproali, o anche su dati immagini, che possono esere pensate come griglie di pixel bidimensionali.

E' alle CNN che si deve il successo avuto negli ultimi anni dal deepè learning, ed alla loro tremenda efficacia nelle applicazioni pratiche. 

La convoluzione è un particolare operazione lineare. Le reti convoluzionali sono semplicemente reti neurali che usano le convoluzioni invece di una moltiplicazione matriciale generica in almeno uno dei loro layer.

Le reti convoluzionali spiccano come esempio dei principi neuroscientifici che influenzano il deep learning. 

## L'opearzione di convoluzione

Nella sua forma più generica, la convoluzione è un'operazione di due funzioni su un argomento a valore reale. Vediamo alcuni esempi di due funzioni che possiamo utilizzare.

Supponiamo di tracciare la posizione di una navicella spaziale con un sensore laser. Il sensore laser fornisce un singolo output $x(t)$, la posizione della navicella al tempo $t$. Sia $x$ sia $t$ sono a valori reali, ovvero possiamo ottenere una diversa lettura da parte del sensore laser ad ogni istante nel tempo.

Supponiamo adesso che il sensore laser sia rumoroso. Per ottnere una stima meno rumorosa della posizione della navicella, vorremmo mediare diverse misure. Naturalmente, le misure più recenti sono quelle più rilevanti,m  per cui vorremo che questa sia una media pesata che dia più peso alle misure recenti. POssiamo farlo con una funzione di pesatura $w(a)$, dove $a$ è l'età della misurazione. Se applichiamo questa operazione di media pesata in ogni istante, otteniamo una nuova funzione $s$ che fornisce una stima "smootherd" della posizione della navicvella:

$$
s(t) = \int x(a) w(t-a) \delta a
$$

Questa operazione è chiamata *convoluzione*. La convoluzione è tipicamente contraddistinta da un asterisco:

$$
s(t) = (x \ast w)(t)
$$

Nell'esempio, $w$ deve essere una funzione densità di probabilità valiuda, o l'output non sarà una media pesata. Inoltre, $w$ deve esere $0$ per tutti gli argomenti negativi, o guarderemmo nel futuro (che, presumibilmente, non è nelle nostre capacità). Questi limit sono specifici per il nostro esempio. In genrale, la convluzione è definita per ogni funzione per la quale l'integrale precedente è definito e può essere usata per altri scopi oltrre a prendere le medie pesate.

Nella terminologia delle CNN, il primo argomento (in questo esempio, la funzione $x$) della convoluzione è definito come *input*, ed il secondo argomento (la funzione $w$) come *kernel*. L'output è chiamato *feature map*.

Nell'esempio, l'0idea di un sensore laser che permetta di fornire misure ad ogni istante non è relaistica. Normalmente, quando lavoriamo con i dati di un computer, il tempo +èm discretizzato, ed il nostro sensore fornisce dati ad intrevalli regolari. Nell'esempio, potrrebbe swessere più realistico assumere che il laser fornisce una misura una volta al secondo. L'indice temporale $t$ può quiindi prendere soltanot valori interi., Se assumiamo che $x$ e $w$ siano deifniti soltanto siugli interi $t$, possiamo definire la convoluzione discreta:

$$
s(t)=(x \ast w)(t)=\sum_{a=-\inf}^{\inf} x(a)w(t-a) 
$$

Nelle applicazioni di machine learning, l'iunput è normalmente un array di dati multidimensioanli, ed il kernel è normalmente un array multidimensioanle di parametri che sono adattati dall'algoritmo di apprendimento. Ci rifieriremo a questi array multidimensioanli come *tensori*. Dato che ogni elmento dell'input ed il kernel devono essere memorizzati esplciitamente in modo separato, normalmente assumiamo che queste funzioni siano zero ovunque tranne che nel finito insieme di punti per i quali memorizziamo i valori. Questo singifica che in pratica possiamo implementare la sommatoria infinita come una sommatoria su un numero finito di elementi di un array.

Infine, spesso suaimo la convoluzione su più di un asse alla volta. Ad esempio, usando un'0immagine bidimensionale $i$ come input, avremo anche un kernel bidioemnsionale $K$:

$$
S(i,j) = (I\ast K)(i, j)=\sum_m \sum_n I(m, n) K(i-m, j-n)
$$

La convoluzione è commutativa, il che significa che possiamo scrivere in maniera equivalente:

$$
S(i,j) = (K\ast I)(i, j)=\sum_m \sum_n I(i-m, j-n) K(i-m, j-n)
$$

Disolito la seconda formulazione è più semplice da implementare all'interno di una libreria per il machine learning, perché vi è una minore variazione nel range di valori validi di $m$ ed $n$.

La proprietà commutativa della convoluzione deriva dal fatto che abbiamo FLIPPATO il kernel rispetto all'input, nel senso che man mano che $m$ aumenta l'indice dell'input aumenta ma l'indice nel kernel decresce. L'unica ragione per rovesciare il kernel è ottenere la proprietà commutativa. ANche se la proprietà commutativa è utile per scrivere dei teoriemi, non è normalmente imporante nel contesto dell'implementazione di una rete neruael. Invece, molte librerie implemnetano una funzione simile chiamata *cross-correlazione*, che è la stessa della convoluzione senza però invertire il kernel:

$$
S(i,j) = (K \ast I)(i, j) = \sum_{m} \sum_{n} I(i+m, j+n)K(m,n)
$$

Molte librerie di machien learning implementano la cross correlazione chiamandola però convoluzione. Nel contesto del machine learning, l'algoritmo di apprendiemnto apprenderà i valori appropriati del kernel nello spazio appropriato, per cui un algoritmo basato sulla convoluzione con il kernel invertito apprenderà un kernel che è invertito relativamente al kernel appreso da un algoritmo che non ha effettuato l'inversione. E' anche raro che la convoluzione sia usata da sola nel machine learning; invece, la convoluzione è usata simultaneamente con altre funzioni, e la combinazione di queste funzioni non cambia indipendnetmente dal fatto che l'operazione di convoluzione inverte il suo kernel o meno.

## 9.2 motivazioni

La convoluzione sfrutta tre idee importanti che possono aiutare a migliroare un sistema di machine learning: *sparse interactions*, *parameter sharing* ed *equivariant represntation*. Inolter, la convoluzione fornisce un mezzo per lavorare ocn ingressi di dimensioni variabili.

I layer tradizionali di una rete neurale usano lamoltiplicazione matriciale con una matrice di parametri con un parametro separato che descrive l'interazione tra ogni unità di input ed ogni unità di output. Questo significa che ogni unità di output interagisce con ogni untià di input. Le reti convoluzionali, tuttavia, hanno tipicamente delle *interazioni sparse* (*sparse connectivity*). Questo è ottenuto rendendo il kernel più piccolo dell'input. Per esempio, quanod si elabora un'immagine, l'immagine di input può avere migliaia, o milioni, di pixel, ma possiamo dinviduare delle piccole, significative featurem, come degli edge,. con dei kernel che occupano soltnato decine o centinaia di pixel. Questo singifica che dobbiamo memorizzare meno parmaetir, riducendo i requisiti in memoria del modello, e miglirandone l'efficienza statistica. Significa anche che calcolare l'output richiede meno operazioni. Questi miglioramenti in termini di efficienza sono di solito notevoli. Se vi sono $m$ input ed $n$ output, la moltiplicazione matriciale richiede $m \times n$ parametri, e gli algoritmi usati nella pratica hanno un $O(m \times n)$ a runtime per ciascun esempio.

SE limitiamo il numero di connessione che può avere ogni output a $k$, allora l'approccio sparsamente connesso richiede solo $k \times n$ parametri ed un $O(k \times n)$ a runtime. Per molte applicazioni pratiche, è possibile ottenere delle buone performance sui task di machine learning tenendo $k$ diversi ordini di grandezza più piccolo di $m$. 

TODO: FIGURE SU SPARSE CONNECTIIVTY



Il **parameters sharing** si rifersice all'utilizzo dello stesso parametro per più di una funzione in un modello. In una rete neurale tradizionale, ogni elemento della matrice dei pesi è usato esattamente una volta quando si calcola l'output di un layer. E' moltiplicato epr un elemento dell'input, e non più riutilizzato. Come sinonimo per il parameter sharing, si può dire che la rete abbia dei **tied weights**, perché il valore del peso applicato ad un input è legato al valore el peso applicato altrove. In uan CNN, ognimembro del kernel è usato ad ongi posizione dell'input (ad eccezione forse dei pixel di contorno, a seconda della decisione di design che riguarda il contorno). Il parameter sharing usato dall'operazione di convoluzoione indica che piuttosto che apprendere un insieme separato di parametri per ogni posizione, apprenderemo slo un insiem. QUesto non influenza il tempo necessario alla forward propagation (è sempre un $O(k \times n$)) ma riduce ulteriormente i requisiti di memoria del modello in $k$ parametri. Ricordiamo che $k$ è nomalmente diversi ordini di grandezza più piccolo di $m$. Dal momento che $m$ ed $n$ sono normalmente approssimativamente della stessa dimensione, $k$ è praticamente trascurabile se comparato ad $m \times n$. La convoluzione è quindi estremamente molto più efficiente della moltiplicazione di matrici dense in termini di reqiusiti di memoria ed efficienza statistica.

TODO PARAMETER SHARING
