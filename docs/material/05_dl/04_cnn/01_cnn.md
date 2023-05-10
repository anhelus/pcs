Le *reti convoluzionali*, conosciute anche come *convolutional neural entworks* (CNN), sono un tipo di reti neurali specializzato sull'elabroazione di dati che hanno una topologia a griglia. Esempi includono serie tempiorali, che possono essere pensati come una griglia monodimensionale campionata ad intervalli di tempo regolari, ed immagini, che sono delle grgilie bidimensionali di pixel. Le reti convoluzionali hanno riscosso un enorme successo in applciazioni pratiche. Il nome "cojnvolutional neurla netowrk" indica che la rete impiega un'operazione matematica chiamata *convoluzione*. La convoluzione è uin tipo speciale di operazione lineare. Le reti convoluzzionali sono semplicemnte delle reti neurali che usano delle convoluzioni al posto di una generica moltiplciazione matriciaale in almeno uno degli streati.

Per prima cosa, descriviamo cosa è la convoluzione. QUindi, spieghiamo il motivo dietro l'uso di una convoluzione in una rete neurale. Descriveremo quindi un'operazione chiamata pooling. Usualmente, le operazioni usate in una CNN non corrispondono precisamente alla definizione di convoluzione così come suata in altri campi.

## L'operazione di convoluzione

Nella forma più generale, la convoluzione è un'operazione di due funzioni ad argomenti reali. Per motivare la definizione di convoluzione, iniziamo con campioni di due funzioni che possiamo usare.

Supponiamo che stiamo tracciando la posizione di una navicella spaziale con un sensore laser. Il nostro sensore laser fornisce un output singolo $x(t)$, la posizoine della navicella spaziale al tempo $t$. Sia $x$ e $t$ sono a valori reali, ovvero, possiamo avere una diversa lettura dal sensore laser ad ogni istante del tempo.

Ora supponiamo che il nostro sensore laser sia in qualche modo rumoroso. Per ottenere una stima meno rumorosa della posizione della navicella spaziale, vorremmo misurare diverse misure. Naturalmente, le misure più recenti sono più rilevanti, per cui vorremo che qeusta sia una media pesata che ci dà più peso alle misure recenti. Possiamo farlo con una funzione di peso $w(a)$, dove $a$ è l'età della misura. Se paplicahiamo questa meida pesata ad ogni momento, otteniamo una nuova funzione $s$ forniscono una media della posizione della navicella spaziale:

$$
s(t) = \int x(a) w(t-a) \delta a
$$

Questa operazione è chiamata  *convoluzione*. L'operazione convoluzione è tipicamente denotata con un asterisco:

$$
s(t)  = (x * w)(t)
$$

Nel nostro esempio, $w$ ha bnisogno di avere una funzione di densità di probabiòlità valida, o l'output non sarà una media pesata. Inoltre, $w$ deve essere $0$ per tutti gli argomenti negativi., o guarderà al futuro, che presumiobilmente è oltre le nostre capacità. Queste limtiazioni sono specifiche per il nostro esempio, comujnque. In generale, la convoluzione è definita per una qualsiasi funzione per la quael l'integrale precedente è definito e può essere usato per altro scopi oltre a prender le medie pesate.

Nella terminologia delle reti convoluzionali, il priomo argomento (ovvero la funzione $x$) alla convoluzione è spesso chiamato il suo *input*, mentre il secondo argomento (in qeusto esempio la funzione $w$) è il *kernel*. L'output è alle volte chiamato *feature map*.

Nel nostro campione, l'idea di un sensore laser che può fornire la misura ad ogni istante non è erealistica. Normalmente, quando laviramo con i dati su un computer, il tempo sarà discretizzato, ed il nostro sensore ci fornirà dati ad invervalli regolari. Nel nostro esempio, può essere più realistico presumere che il nostro laser fornisca una misurazione una volta al secondo. L'indice di tempo $t$ può quindi prendere soltanto valori interi. Se presumiamo che $x$ e $w$ siano definite soltanto sull'intero $t$, possiamo definire la convoluzione discreta come:

$$
s(t) = (x * w)(t) = \sum_{a=-\infty}^{\infty} x(a) w(t-a)
$$

Nelle applicazioni di machine learning, l'input è di solito un array di dati multidimesnsioanli, ed il kernel è di solito un array multidimensiopnael di parametri che sono adattati dall'algoritmo di apprendimento. Dato che ogni elemtno dell'input e del ckernel deve essere esplicitamente emmorizzato separatamente, normalmente ipotiziamo che queste funzioni siano zero onvuqne tranne nell'ìoinsieme di punti finito per i quali memorizziamo i valori. Questo singifica che nella pratica possiamo implmeentare al sommatoria infinita come una somma su un numero finito di eloemnetoi.

Infine, possiamo usare le convoluzioni su più di un asse per volta. Per esempio, se usiamo un'imamgine bidimensionale $I$ come input,. probabilmente vorremo usare un kernel bidimensionale $K$:

$$
S(i,j) = (I * K)(i, j) = \sum_m \sum_n I(m,n)K(i-m, j-n)
$$

La convoluzione è commutativa, il che significa che possiamo scrivere in maneir aequivalente:

$$
S(i,j) = (K*I)(i,j) = \sum_m \sum_n I(i-m, j-n) K(m,n)
$$

La proprietàò commutativa della convoluzione nasce dal fatto che abbiamo *inveritop* il kernel rispetto all'iunput,. nel senso che man mano che $m$ aumenta, l'indice nell'ingresso aumenta, ma l'indice nel kernel decrementa. Mentre la proprrioetà commutativa è utile per scirvere teorimi, non è normalmente una proprietà importante dell'0implementazione di una rete neurale. Invece, molte librerie di reti neurali implementano una funzioen correlata chiamata *cross-correlazione*é, che è identica alla convoluzione ma senza rovesciare il kernel:

$$
S(i,j) = (K * I)(i,j) = \sum_m \sum_n I(i+m, j+n) K(m,n)
$$

Molte libreire di machine learning implemnentano la cross-correlazione chiamadnoal convoluzoione.
