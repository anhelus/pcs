# 26 - Layer di una rete neurale

Vediamo insieme quali sono alcuni tra i layer più comuni presenti nelle reti neurali, assieme alla loro implementazione in Keras.

## 26.1 - Layer completamente connesso

## 26.2 - Layer convoluzionale

I layer convoluzionali sono alla base del funzionamento di un particolare tipo di rete neurale chiamata *convolutional neurla network*. Questa rete è un tipo di rete specializzato nel lavorare su immagini di tipo bbidimensionale, anche se ci sono applicazioni per segnali monodimensionali e tridimensionali.

Il concetto alla base del layer convoluzionale è quello di un'operazione chiamata *convoluzione*. In questo contesto, è un'operazione di tipo lineare che prevede la moltiplicazione di un insime e di pesi con l'input, proprio come accade in una rete neurale tradizionale. Dato che la tecnica è stata progettata per gli ingressi bidimensionali, la moltiplicazione viene effettuata tra un array di dati in ingresso ed un array bidimensionale di pesi chiamato *filtro* o *kernel*.

Il filtro è più piccolo dei dati in ingresso, ed il tipo di moltiplicazione applicata tra una patch delle dimensioni del filtro dell'input ed il filtro stesso è un prodotto scalare, il che restituisce sempre un singolo valore.

Usare un filtor più piccolo dell'input è intenzionale, in quanto permette allo stesso filtro (insieme di pesi) di essere moltiplicato per l'array di input più volte a diversi punti dell'input. Nello specifico, il filtro viene applicato sistematicamente ad ogni patch dei dati di input, da sinistra a destra, da sopra a sotto, anche sovrapposte.

Questa applicazione sistematica dellos tesso filtro lungo un'immagine è un'idea potente. Se il filtro è progettatto per trovare uno specifico tipo di feature nell'input, all'ora l'applicazione di questo filtro in maniera sistematica lungo l'immagine di input permette al filto di scoprire la feature ovunque nell'immagine. Questa capacit è chaimata *invarianza alla traslazione*.

L'output della moltiplicazione del filtro con l'array di input una volta è un singolo valore. Man mano che il filtro viene applicato sull'intero array, ilr isutlato è un array bidimensionale di valori di output che rappresentano un *filtro* dell'input. Di consegeunza, l'output array bidimensionale è chiamato *feature map*. Una volta che la feature map viene creata, possiamo passare ogni valore nella feature map attravertso una nonlinearità, proprio come faremmo per gli output di un layer completamente connesso.

!!!note "nota"
    Tecnicamente, l'operazione che abbiamo descritto è in realtà uina crosscorrelazione.

Riassumendo, abbiamo un input, come un'immagine, un filtro, che è n insieme di pesi, ed il fitlro è sistematicamente applicato adi dati di input per creare una feature map.

## 26.3 - Layer di pooling

Abbiamo visto che i layer convoluzionali all'interno di una CNN applicano in maniera sistematica i filtri appresi sulle immagini di input per creare delle feature map che riassumono la presenza di queste feature nell'input.

I layer cnvoluzionaoli sono molot efficaci, e concatenarli in architetture deep permette ai layer vicini al'input di apprendere feature a basso livello, mentre a quelli più profondi di apprendere feature più astratti, come forme o oggetti specifici.

Un limite di questa mappatura è che questi registrano la posizione precisa delle feature nell'input. Questo significa che piccoli movimenti nella posizione delle feature dell'immagine di input risulteranno in una diversa feature map. Questo fa sì che la rete sia estremamente sensibile a piccole trasformazioni quali rotazioni, shifting.

Un approccio molto utilizzato per risolvere questo tipo di problema è il sottocampionamento. Qui è dove una versione a bassa risoluzione di un segnale di input viene creata in modo che contenga gli elementi importanti della struttura, senza i piccoli dettagli che potrebbero non essere utili alla task.

Il sottocampionamento può essere ottenuto usando un layer di pooling, Questo è un nuovo layer aggiunto a quello convoluzionale dopo la non linearità.

Il pooling layer opera su ciascuna feature map in maniera separata, creando un nuovo insieme dello stesso numero delle feature map. Il pooling prevede la scelta di un'operazione di pooling, che assomiglia ad un filtro applicato ad una feature map. La dimensione del filtro di pooling è inferiore a quella di una feature map: nello specifico, si tratta di filtri di solito di dimensioni $2 \times 2$ con un passo di $2$ pixel.

Questo significa che il pooling layer riduce la dimensione di ogni feature map di un fattore di $2$, ovvero ogni dimensione risulta essre dimezzata, riducendo il numero di pixel o valori in ogni feature map ad un quarto della dimensione. Ad esmepio, un pooling layer applicato ad una feature map di $6 \times 6$ restiutiàr una feature map in outèut di $3 \times 3$ (9 pixel).

E' importante sottolineare come i filtri di pooling sono specificati a priori. Due funzioni comuni che è possibile usare sono:

* average pooling: calcola la media per ogni feature map
* max pooling: restituisce il valore massimo per ogni patch sulla feature map

Il risultato dell'applicazione di un pooling layer è una versione sottocampionata delle feature individuate dall'input. Queste sono utili in quanto dei piccoli cambiamenti nella posizione delle feature dell'input individuato dai layer convoluzionali risulteranon in una pooled feature map nella stessa posizione. Questa capacità del modello è detta *invarianza del modello a traslazioni locali*.

## 26.4 - Dropout

Il dropout è un metodo di *regolarizzazione* che permette di approssimare l'addestramento di un grosso numero di reti neurali con diverse architetture in parallelo.

Durante l'addestramento, un certo numero (casuale) di layer di output viene ignorato. Questo ha l'effetto di rendere il layer simile ad un layer con un numero diverso di nodi ed una diversa connettività al layer precedente. In pratica, ogni aggiornamento ad un layer durante il training viene effettuato cn una diversa "visione" del layer configurato.

Il dropout ha l'effetto di rendere il processo di apprendimento "rumoroso", forzando i nodi all'interno di un layer a prendersi maggiore eo minore responsabilità per gli input (in maniera probabilistica).

Questa concettualizzazione suggerisce che forse il dropuot rompe le situazioni dove i layer di rete si co-adattano per correggere degli errori dei layer precedenti, rendendo di conseguenza il modello più robusto.

Il dropout simula un'attivazione *sparsa* id un adato layer, il che a sua volta incoraggia la rete ad apprendere una rappresentazione sparsa. 

Inoltre, siccome gli output di un layer sotto dropout sono sottocampionati in maniera casuale, ha l'effetto di ridurre la capacità o rendere piùsottile la rete durante il training. Di conseguenza, quando si usa il dropout potrebbe essere necessario usare una rete più ampia.

Il dropout viene implementato sulla base del singolo layer, e può essere applicato su molti tipi di layer, tra cui quelli completamente connessi e quelli convolutionali.

Il dropout può essere implmeentato su ciascun strato nascosto, così come sul layer di input, ma non sul layer di output.

Per quello che riguarda gli iperparametri usati dal dropout, viene usato un iperparametro che specifica la probabilità con la quale gli outptu del layer sono scartati. Un valore comune di probabilità è 0.5, che pemrette di mantenere l'output di ogni nodo in uno strato nascosto, ed un valroe molto più aulto, pari a circa 0.8, per gli input del layer di input.
