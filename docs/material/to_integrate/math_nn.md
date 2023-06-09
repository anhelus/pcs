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
