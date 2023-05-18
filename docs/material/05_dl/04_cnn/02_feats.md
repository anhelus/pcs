# 5.4.2 - Principi alla base delle CNN

Allo scopo di massimizzare le performance in termini di classificazione, le CNN sfruttano tre importanti principi, ovvero le **interazioni sparse**, la **condivisione (sharing) dei parametri** e la **rappresentazione equivariante**. Vediamoli nel dettaglio

## Interazioni sparse

Le classiche reti neurali feedforward sfruttano la moltiplicazione (matriciale) per una matrice di parametri nella quale ogni parametro descrive l'interazione tra una singola unità di input ed una singola unità di output; se la matrice dei parametri non ha alcun valore pari a zero, ciò significa che ogni unità di input interagisce con ogni unità di output, e viceversa.

Le CNN, invece, sono caratterizzate da delle **interazioni sparse**, anche conosciute come **connettività sparsa** (*sparse connectivity*): in altre parole, *non tutte* le unità di input interagiscono con ogni unità di output, e viceversa. Per ottenere questo scopo, basta utilizzare in fase di convoluzione un kernel più piccolo dell'input. Immaginiamo ad esempio di elaborare un'immagine: questa può avere migliaia, o anche milioni, di pixel; tuttavia, per individuare le feature di interesse, si possono utilizzare dei kernel di piccola dimensione, attorno alle decine di pixel; ciò permette di memorizzare un numero inferiore di parametri, il che da un lato migliora l'efficienza statistica del modello, riducendo al contempo i requisiti in termini di memoria e tempo necessario per l'addestramento.

In particolare, il miglioramento in termini di efficienza apportato dalla connettività sparsa è decisamente rilevante. Supponendo che vi siano $m$ input ed $n$ output ad un dato layer, una moltiplicazione matriciale completa richiederebbe $m \times n$ parametri, con una complessità pari ad $O(m \times n)$ *per singola osservazione*. Limitando invece le possibili connessioni di ciascun output a $k$, avremo la necessità di utilizzare soltanto $k \times n$ parametri, con un $O(k \times n)$.

!!!tip "Il valore di $k$"
    Per la maggior parte delle applicazioni, il valore di $k$ può essere scelto di diversi ordini di grandezza inferiore ad $n$, mantenendo comunque delle buone performance.

## Parameters sharing

In una classica rete feedforward, il calcolo dell'uscita di un layer prevede che ogni elemento della matrice dei parametri venga usato solo e soltanto una volta. Ciò non è tuttavia vero in una CNN, in quanto il paradigma del **parameters sharing** prevede che un singolo parametro sia usato da più di una funzione. In altre parole, una CNN ha dei parametri strettamente correlati (*strictly tied parameters*), dato che il peso applicato a due o più input può essere lo stesso; ciò avviene perché nelle CNN il kernel viene fatto scorrere sull'interezza dell'input (a possibile eccezione di alcuni pixel di contorno).

Il paradigma del parameter sharing fa quindi in modo che, invece di apprendere un insieme di parametri specifico per ogni posizione dell'input, la rete apprenda un parametro per ciascun *intorno*. Questo non influenza la complessità della rete, che rimane sempre $O(k \times n)$; tuttavia, i requisiti di memoria del modello a $k$ parametri risultano essere ulteriormente ridotti.

Il parameter sharing usato dall'operazione di convoluzoien indica che piuttosto che apprendere un insieme di parameteri separato per oigni posizione, apprendiamo soltanto un insieme. Questo non influenza il runtime della forward propagation (è sempre $O(k \times n)$), ma riduce ulteriormente i requisiti di memoria dle modello a $k$ parametri. Ricordiamo che $k$ è normalemnte diversi ordini di grandezza più piccola di $M$. Dal momento che $m$ ed $n$ soino normalmente della stesso rordine, $k$ è praticamente trascurabile se comparato ad $m \times n$. La convoluzione è qunidion molto più efficiente della moltiplicazione matriciale densa in termini dei requisiti di memoria e dell'efficienza statistica.

## Rappresentazione equivariante

Il parameter sharing di una CNN ha come consequenza l'**equivarianza** di un layer convoluzionale alla transazione; in altri termini, l'output del layer cambierà nello stesso modo in cui viene modificato l'input.

Formalmente, uan funzione $f(x)$ è equivariante ad una funzione $g(x)$ se $f(g(x)) = g(f(x))$. Immaginiamo ad esempio che la funzione $I(\cdot)$ sia quella che restituisce la luminosità di un'immagine. Sia $g$ una funzione che trasli l'ouptut di un pixel a destra in modo che:

$$
I^{'} = g(I) \rightarrow g(x, y) = I^{'}(x, y) = I(x-1, y)
$$

Applicando la trasformazione $g(I)$, e successivamente convolvendo il risultato, avremo lo stesso effetto dell'applicazione diretta della convoluzione ad $I^{'}$, applicando di conseguenza la trasformazione $g$ all'output di convoluzione.

Ciò implica l'insorgenza di un fenomeno interessante. Applicare la convoluzione a dati monodimensionali ci restituisce una sorta di "timeline", la quale ci mostra quando appaiono specifiche feature nell'input. Grazie alla proprietà di equivarianza, qualora spostassimo un determinato evento nell'input, avremmo che la rappresentazione di tale evento nell'output traslerebbe in maniera equivalente. Lo stesso avviene per una rappresentazione bidimensionale: la convoluzione crea una *feature map* che rappresenta la posizione in cui appaiono alcune feature all'interno dell'immagine di ingresso. Se questa viene manipolata spostando un oggetto, la rapprentazione a valle della convoluzione sarà contestualmente spostata allo stesso modo.

!!!warning "Equivarianza"
    La convoluzione è equivariante esclusivamente alla traslazione. Nel caso di altre trasformazioni, come ad esempio rescaling o rotazioni, l'equivarianza non è garantita.
