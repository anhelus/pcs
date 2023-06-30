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

Cerchiamo di essere più precisi. Ricordiamo che per l'$i$-mo campione abbiamo i pixel dell'immagine $x_i$ e le label $y_i$ che specificano l'indice della clase corretta. La funzione di score prende i pixel e calcola i vettori $f(x_i, W)$ dei punteggi di classe, che abbreviamo in $s$. Per esempio, lo score per la $J$-ma classe è il $j$-mo elemento $s_j=f(x, W)_j$. La Multiclass SVM loss per l'$i$-mo esempio è quindi formalizzato come segue:

$$
L_i = \sum_{j \neq y_i} \max(0, s_j - s_{y_i} + \Delta)
$$

**Esempio** Proviamo a vedere come funziona il tutto con un esempio. Supponiamo di avere tre classi che ricevono i punteggi $s = [13, -7, 11]$, e che la prima classe sia quella vera (ovvero $y_i=0$). Supponiamo inoltre che $\Delta$ (un iperparametro di cui parleremo più a breve) sia pari a $10$. L'espressione somma tutte le classi non correte ($j \neq y_i$), per cui abbiamo due termini:

$$
L_i = \max(0, -7-13+10)+max(0, 11 - 13 + 10)
$$

Possiamo vedere che il primo termine ci dà zero dal momento che la somma è negativa, che viene quindi sogliata a zero con la funzione $\max(0, -)$. Otteniamo una loss pari a zero per questa coppia perché il punteggio di classe corretto (13) è stato più grande di quello non corretto almeno per un margine pari a $10$. Infatti la differnza era di $20$, che è molto più grande di $10$ ma la SVM si interessa solo del fatot che la differenza sia almeno 10; una qualsiasi altra differenza oltre il margine viene mandata a zero grazie all'operazione $\max$. Il secondo termine calcola $[11-13+10]$ che dà $8$. Ovvero, anche se la classe corretta ha un punteggio più alto di quella non corretta $(13 > 11)$, non era più grande del margine desiderato di $10$. La differenza era solo di $2$, il che ci dice perché la loss diventa $8$ (ovvero, quanto dovrebbe essere grande la differnza per essere in gado di rispettare il margine autoimposto). In pratica, la SVM loss function vuole che il punteggio della classe corertta $y_i$ sia più grande di $\Delta$. Se ciò non accade, accumuleremo una loss.

Notiamoc he in questo particolare modulo stiamo lavorando con un score lineare $f(x_i; W)=Wx_i$, per cui possiamo riscrvere l'intera funzione di costo in qeusta forma equivalente:

$$
L_i = \sum_{j \neq y_i} \max(0, w_j^T x_i - w_{y_i}^T x_i + \Delta)
$$

dove $w_j$ è la $j$-ma riga di $W$ rimdoellata come una colonna. Comunque, questo non sarà necessariamente il caso quando iniziamo a considerare le forme più complesse della funzione di score $f$.

Un ultimo punto di terminologia che menzioneremo prima di finire questa sezione è che funzione $\max(0,-)$ è chiamata *hinge loss*.

**Regolarizzazione**

Vi è un bug con la loss function di prima. Supponiamo che abbiamo un dataset ed un insieme di prametri $W$ che classificano correttamente ogni campione (ovvero tutti i punteggi sono fatti in modo che tutti i margini siano rispettati, ed $L_i=0 \forall i$). Il problema è che questo insieme di $W$ non è necessariamente univoco: ci potrebbero essere molti $W$ simili che classificano corretttamente i campioni. Un modo semplice di vederlo è che se alcuni parametri $W$ classifica correttaemtne tutti i campioni (per cui la loss è zero per ogni esempio), quindi ogni multiplo di questi parametri $\lambda W$ dove $\lambda > 1$ ci darà una loss di zero perché questa trasformazione streatcha uniformaemente tutti i punteggi di magnitudine e quindi anche le loro differenze assolute. Ad esempio, se la differenza negli score tra una classe corretta e quella incorretta più vicina era 15, quindi multiplicare tutti gli elementi di $W$ di 2 renderebbe la nuova differenza 30.

In altre paroli, vogliamo codificare alcune preferenze per un certo insieme di pesi $W$ su altri per rimuovere questa ambiguità. Possiamo farlo estendendo la loss function con una *penalità di regolarizzaizone* R(W). La più comune regolarizzazione è la norma $L2$ che soraggia dei grossi pesi attraverso una penalità elemento per elemento su tutti i parametri:

$$
R(W) = \sum_k \sum_l W_{k, l}^2
$$

Nell'espressione rpecedente stiamo sommando gli elementi quadratici di $W$. Notiamo che la funzione di regolarizzazione non è una funzione dei dati, è solo basata sui pesi, inclusa la penalità di regolarizzazione che completa la loss mutlicass SVM, che è fatta di due componenti: la data loss (che è la loss media $L_i$ su tutti gli esempi) e la regularization loss:

$$
L = \frac{1}{N} \sum_i L_i + \lambda R(W)
$$

che espansa è:

$$
L = \frac{1}{N} \sum_i \sum_{j \neq y_i} [\max(0, f(x_i;W)_j)-f(x_i;W)_{y_i}+\Delta] + \lambda \sum_k \sum_l W_{k,l}^2
$$

dove $N$ è il numero di campioni di training. Come possiamo vedere, aggiungiamo la penalità di regolarizzazione all'obiettivo della loss, pesato per un iperparametro $\lambda$. Non vi è un modo semplice di impostare questo iperparametro ed è normalmente determinato dalla cross-validazione.

Oltre alla motivazione fornta precedente ci sono molte proprietà desiderabili da includere nella penalty di regolarizzazione, molti dei quali riprenderemo successivamente.

La proprietà più interesasnte è che penalizzare i grossi pesi tende a migliorare la generalizzazione, perché significa che non vi sono delle dimensioni di input che possono avere una grossa influeza sui punteggi da sole. Supponiamo ad esempio che abbiamo alcuni vettori di input $x=[1,1,1,1]$ e due vettori dei pesi $w_1=[1,0,0,0]$, $w_2=[0.25, 0.25, 0.25, 0.25]$. Quindi $w_1^Tx=w_2^Tx=1$ per cui entrambi i vettori dei pesi conducono allo stesso prodotto scalare, ma la penalità di $w_1$ è $1$ mentre la penalità L2 di $w_2$ è solo 0.5. Quindi, accordare alla penalità L2 il vettore dei pesi $w_2$ sarebbe preferibile perché ottiene una regularization loss più bassa. Inviece, questo è perché i pesi in $_2$ sono più piccoli e più diffusi. Dal momento che la penalità L2 preferisce vettori dei pesi più piccoli e diffuso, il classificaotre finali è incoraggiato a prendere in considerazione tutte le dimensioni di input verso piccoli quantitativi piuttosto che poche dimensioni di input molto forti. 

Notiamo che i bias non hanno lo stesso effetto dal momento che, a differenza dei pesi, non controllano la forza dell'influenza di una dimensione di input. Quindi, è facile regolarizzare solo i pesi $W$ ma non i bias $b$. Tuttaiva, nella pratica questo spesso ha un effetto trascurabile. In ultimo, notiamo che grazie alla penalità di regolarizzazione non possiamo mai avere una loss di esattamente 0 su tutti gli esempi, perché questo sarebbe possibile solo nel setting $W=0$.

### Considerazioni pratiche

**Valore di delta**

Notiamo che abbiamo parlato poco di $\Delta$ e di come impostarlo. Quale valore dovremmo associargli, e come dovremmo determinarlo? In realtà, questo iperparametro può essere tranquillamente impostaot a $\Delta=1.0$ in tutti i casi. Gli iperparametri $\Delta$ e $\lambda$ sembrano essere differenti, ma nei fatti controllano lo stesso compromesso. Il compromesso è quello tra la data loss e la regularization loss nella funzione obiettivo. La chiave per comprender ciò è che la magnitudine dei pesi $W$ ha deffetti diretti sugli score (e quindi anche le loro difererenze): man mano che SHRINK tutti i valori dentro $W$ le differenze di score diventeranno più piccole, e man mano che aumentiamo i pesi le differenze tra gli score diventeranno più grandi. Quindi, il valore esatto del margine tra i punteggi (e.g., $\Delta=1$ o $\Delta=100$) è in qualche modo senza significato perché i pesi possono restringere o allargare in maniera arbitraria le differenze. Quindi, l'unico vero e proprio compromesso è quanto possiamo permettere ai pesi di crescere attraverso la forza di regolarizzazione $\lambda$.

**Relazione con le bianry SVM**

La loss delle binary SVM può essere scritta per l'$i$_mo caompione come:

$$
L_i = C \max(0, 1-y_iw^Tx_i) + R(W)
$$

dove $C$ è un iperparametro e $y_i \in {-1, 1}$. Potremmo convincerci che la formulaizone presentata in questa sezione contiene la SVM binaria come caso speciale quando ci sono solo due classi. Ovvero, se abbiamo soltanto due classi allora la loss si riduce alla SVM binaria mostrata in precedenza. Inoltre, $C$ in questa formulazione e $\lambda$ nella nostra formulazione controllano lo stesso rapporto e sono inversamente propozionali.

## Softmax

La SVM è solo uno dei classificatori comuni. L'altra sceta
