# Classificatori lineari

https://cs231n.github.io/linear-classify/

Sviluppiamo un approccio potente alla classificazione che estenderemo alle reti neurali. L'approccio consta di due componenti principali: una *funzione di scoring* che mappa i dati raw ai punteggi di classe, ed una *loss function* che quantifica il grado di accordo tra i punteggi predetti e le label del ground truth. Il problema sarà quindi un problema di ottimizzazione nel quale minimizzeremo la loss function rispetto ai parametri della score function.

## 

Il primo componente di questo approccio prevede di defeinire la score function che mappa i valori dei pixel di un'immagine ai confidence score per ciascuna classe. Andremo quindi a sviluppare l'approccio con un esempio. Immaginiamo di avere un dataset di trainign di istanze $x_i \in \mathbb{R}^D$ ognuna associata ad una label $y_i$. Qui $i=1, \ldots, N$ e $y_i \in 1, \ldots, K$. Ovvero abbiamo $N$ esempi, ognuno con una dimensionalità $D$, e $K$ diverse categorie. Per esempio, considerando il dataset CIFRA-10 abbiamo un insieme di trainign di $N=50.000$ immagini, ognuna con $D=32 \times 32 \times 3 = 3072$ pixel, e $K=10$, dal momento che ci sono $10$ classi distinte. Definiamo adesso la score function $f: R^D \rightarrow R^K$ che mappa i pixel dell'immagine sui punteggi di classe.

**Linear classifier**

In questo modulo inizieremo con quella che probabilmente è la funzione più semplice possibile, ovvero una mappatura lineare.

$$
f(x_i, W, b) = W_{x_i} + b
$$

Nell'equazione precedente, l'idea è che l'immagine $x_i$ abbia tutti i suoi pixel appiattiti in una singola vettore colnna di dimensioni $D \times 1$. La matrice $W$ di dimensioni $K \times D$ ed il vettore $b$ di dimensioni $K \times 1$ sono i parametri della funzione. Nel caso di CIFAR-10, $x_i$ contiene tutti i pixel nella $i$-ma immagine appiattiti in una singola colonna di dimensioni $3072 \times 1$, $W$ ha dimensioni $10 \times 3072$, e $b$ è $10 \times 1$, per cui ci sono 3072 numeri nella funzione (i valori dei pixel) e $10$ che vanno fuori (i punteggi delle classi). I parametri in $W$ sono spesso chiamati pesi, e $b$ è chiamata *vettore dei bias* perché influenza i pesi in output, ma senza interagire con i dati veri e priori $x_i$. Tuttavia, sentiremo spesso parlare di *pesi* e *parametri* in maniera intercambiabile.

Alcune note:

* per prima cosa, la moltiplicazione $W x_i$ sta valutando 10 classificatori separati in parallelo, uno per classe, dove ogni classificatore è una riga di $W$
* notiamo anche come pensiamo ai dati di input $(x_i, y_i)$ come fissi, ma abbiamo il controllo sui parametri $W$ e $b$. L'obiettivo sarà qello di impostarli in modo che i punteggi calcolati combacino con i label di ground truth nell'intero tarinin set. Intuitivamente, vogliamo che la classe coretta abbia un punteggio che sia più alto di quello delle classi non correte.
* un vantaggio di questo approccio è che i dati di training sono usati per apprendere i parametri $W, b$, ma una volta che l'apprendimento è completto possiamos cartare l'intero trainign set e mantenere solo i parametri appresi. Questo avviene perché una nuova immagine di test può essere semplciemente inviata attraverso la funzione e classificata sulla base dei punteggi calcolati.
* in utliimo, notiamo che classificare l'immagine di test prevede una singola moltiplicazione e somma matriciale, che è singificativamente veloce se comparata ad verificare un'immagine rispetto at tutte le altre immagini.

## interpretare un classificatore lineare

Notiamo che un classificaotre lineare calcola il punteggio di una calsse come somma pesata di tutti i suoi valori di pixel lungo i 3 canali. A seconda di quali valori impostiamo per questi pesi, la funzione ha la capacità di farsi piacere o meno (a seconda dal segno di ogni peso) certi colori a certe posizioni nell'immagine. Per esempio, si può immaginare che la classe "Nave" potrebbe avere più probabilità di verificarsi quando vi è molto più blu ai lati di un'immagine (che potrebbe probabilmente essere acqua). Possiamo pensare che la classificazione "nave" avrà molti pesi positivi lungo i suoi pesi del canale blu (presenza di blu aumenta il punteggio di nave), e pesi negativi nei canali rossi/verdi (presenza di rosso/verde decrementa il punteggio della nave).

Analogia delle immagini come punti ad alta dimensionalità. Dal momento che le immagini sono vettori colonna ad alta dimensioanlità, possiamo interpretare ogni immagine come un solo punto in questo spazio (ad esempio, ogni immagine in CIFAR-10 è un punto in uno spazio a $3072$ dimensioni con uno spazio a $32\times32\time3$ pixel). Analogamente, l'intero dataset è un insieme etichettato di punti.

Dal momento che abbiamo definito il punteggio di ogni classe come somma pesata di tutti i pixel delle immagini, ogni punteggio di classe è una funzione lineare in questo spazio. Non possiamo visualizzare uno spazio a $3072$ dimensioni, ma se immaginiamo di comprimere queste dimensioni in due dimensioni, potremmo provare a visualizzare quello che fa il classificatore.

Come abbiamo detto, ogni riga di $W$ è un classificatore per una delle classi. L'interpratazione geometrica di quesit numeri è che man mano che cambiano una delle righe di $W$, la linea corrispondente nello spazio dei pixel ruota in differenti direzioni. I bias $b$ d'altro canto permettono al nostro classificatore di traslare le linee. IN particolare, notiamo che senza il termine di bias, mandando $x_i=0$ avremmo sempre un punteggio pari a zero indipendentemente dai pesi, per cui tutte le righe sarebbero forzate ad attraversare l'origine.

### Interpretazione dei classificatori lineari con il template matching

Un'altra interpetezione per i pesi $W$ è che ogni riga di $W$ corrisponde ad un *template*, alle volte chiamata *prototipo*, per una delle classi. Il punteggio di ogni classe per un'immagine è quindi ottenuto comparando ogni template con l'immagine usando un prodotto scalare uno ad uno per trovare quello che "combacia" ("fit") meglio. Con questa terminologia, il classificatore lineare sta effettuando il template matching, dove i template vengono appresi. Un altro modo di pensarlo è che stiamo effettivamente effettuando il nearest neighbor, ma invece di avere migliaia di immagini di training stiamo usando soltanto un'immagine per classe (anche se la apprenderemo, e non deve essere necessariamente una delle immagini nel training set), e usiamo il prodotto interno negativo come la distanza invece della distanza L1 o L2.

Inoltre, notiamo che il template di un cavallo sembra contenere un cavallo a due teste, che è legato al fatto che ci sono nel dataset sia cavalli rivolti a destra, sia a sinistra. Il classificatori lineare fonde queste due modalità di rappresentare i cavalli nei dati in un singolo template. In modo simile, il classificatore per una auto sembra aver unito insieme diversi modi in una singoal template che deve identificare le auto da ogni lato, e di tutti i colori. In particoalre, questo template è rosso, il che indica che ci sono più auto nel dataset CIFAR-10 rispetto a quelle di tutti gli atlri colori. Il classificaotre lineare è troppo debole per considerare auto di diversi colori, anche se questo non accade con le reti neurali che ci permettono dif arlo. Guardando nel futuro, una rete neurale sarà in grado di sviluppare neuroni intermedi nei suoi strati nascosti che possono individuare diversi tipi di auto (ad esempio, auto verde che guarda a sinistra, auto blu che guarda a destra), e neuroni sui layer successivi possono combinare questi in un punteggio più accurato attraverso una somma pesata dei singoli car detector.

### Bia trick

Prima di andare avanti vogliamo menzionare un trucco semlice per rappresentare i due parametri $W, b$ come uno solo. Ricordiamo che abbiamod efinito al funzione di score come:

$$
f(x_i, W, b) = Wx_i + b
$$

Man mano che procediamo attraverso il materiale è difficiel tener traccia di due insiemi di aprametri (i bias $b$ ed i pesi $W$) separatamente. Un trucco suato spesso è combinare i due insiemi di parametri in una singola matrice che li contiene entrambi estendendo il vettore $x_i$, con una dimensione ulteriorie che conteine sempre la costante $1$ - una dimensione del bias di defautl. Con la dimensione extra, una nuova funzione di score più semplice è la seguente:

$$
f(x_i, W) = W x_i
$$

In CIFAR, $x_i$ è adesso 3073 x 1 invece di 3072 x 1 - con la dimensione extra che contiene una costante 1, e W è 10 x 3073 invece di 10 x 3072. L'ulteirioe colonna che $W$ ha corrisponde al bias $b$.

TODO FARE IMMAGINE 

#### image data preprocessing

nell'esempio precedente abbiamo suatoo i valori grezzi dei pixel, che vanno da 0 a 255. Nel machine learning è spesso una buona pratica fare la normalizzazione delle nostre feature di input (nel caso di immagini, ogni pixel è pensato come una feature). In particolare, è imporattne per centrare i nostri dati sottraendo la media da ogni feature. Nel caso di immagini, questo corrispodne a calcolare una immagine media lungo le immagini di training, sottraendola da ogni immagine per ottenree delle immagini dove i valori dei pixel spaziano approssimativamente tra $[-127, \ldots, 127]$. Altro preprocessing comune è quello di scalare ogni feature di input in modo che i suoi valori spazino tra -1 ed 1. Di qeusti, lo zero mean centering è più importante, ma dovremo aspettare per la sua giufisticazione fino a che non capiamo le dinamiche della discesa di gradiente,.

## Funzioni di costo

Nella sezione rpecedente abbiamo definito una funzione che va dai valori dei pixel ai punteggi di classi, che sono parametrizzati da un insieme di pesi $W$. Inoltre, abbiamo visto che non abbiamo controllo sui dati $(x_i, y_i)$, ma abbiamo controllo su questi pesi e vogliamo impostarli in modo che i punteggi di classe predetti siano consistenti con le label di ground truth nei dati di training.

Per esempio, andando indietro all'immagine di esempio di un gato ed i suoi punteggi per le classi "gatto", Cane e nave, abbiamov isto che il particoalre insieme di pesi in quegli esempi non era per niente buono: abbiamo dato i pixel che mostrano un gatto, ma il punteggio relativo al gatto era molto piccolo (-96,8) se comparato alle altre classi (437.9 per il cane e 61.95 per la nave). Dobbiamo misurare il nostro disappunto con i risultati con una loss function (chiamata anche cost funciton o  obiettivo. Intuitivamente, il costo sarà alto se stiamo facendo un lavoro non buono nel classificare i dati di addestramento, e sarà buono se stiamo facendo bene.)

### Mutliclass SVM loss

Ci sono molti modi per definire i detatagli di una loss funciton. Come primo esempio svilupperemo una loss comunemente chiamata Multiclass Support Vector Machine (SVM) loss. La SVM loss è impostata in modo che la SVM voglia la classe corretta per ogni immagine per avere un punteggio più alto che le classi incorrette di un certo margine $\Delta$. Notiamo che alle volte è utile umanizzare la funzione di costo come abbiamof atto prima: la SVM vuoel una certa uscita nel senso che l'uscita mandi una loss più bassa (il che è un bene).
