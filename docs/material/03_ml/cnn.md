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
