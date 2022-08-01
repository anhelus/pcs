# 27 - Convolutional Neural Networks in TensorFlow e Keras

Una delle applicazioni più diffuse del deep learning riguarda il riconoscimento degli oggetti presenti all'interno di un'immagine. In tal senso, è necessario introdurre due ulteriori layer, che rappresentano la base per le cosiddette **convolutional neural network**.

Queste reti (che chiameremo per brevità CNN) sono specializzate nel lavorare su immagini, ma possono anche essere usate per segnali monodimensionali (come la voce) o tridimensionali (come le nuvole di punti).

Le CNN assumono una rilevanza fondamentale nel moderno deep learning: è grazie a loro se il campo del deep learning è diventato *mainstream* nel mondo della ricerca, il che ha portato ad un interesse e, conseguentemente, ad avanzamenti impensabili in un ridottissimo lasso di tempo di soli dieci anni. Oggigiorno, le CNN vengono utilizzate in ogni ambito che preveda l'elaborazione di dati bidimensionali, dal riconoscimento facciale all'individuazione e caratterizzazione delle targhe degli autoveicoli in transito; conoscerle, quindi, è imprescindibile.

## 27.1 - Layer convoluzionale

I layer **convoluzionali** sono alla base del funzionamento delle CNN.

Il concetto alla base di questo tipo di layer è la *convoluzione* che, nel contesto del deep learning, è un'operazione lineare che prevede la moltiplicazione di un insieme di pesi, chiamato *filtro*, con una piccola porzione (o *finestra*) dell'immagine considerata, seguita ovviamente da una funzione di attivazione. Questo processo è analogo a quello che avviene in una tradizionale rete neurale.

Il filtro ha dimensioni volutamente inferiori rispetto a quelle dell'immagine da convolvere, tipicamente nell'ordine di $3 \times 3$ o $5 \times 5$ pixel; la convoluzione del filtro per ogni finestra dell'immagine è inoltre assimilabile ad un prodotto scalare, per cui viene restituito sempre un unico valore per ogni finestra convoluta. In tal senso, il filtro viene "fatto scorrere" dall'alto in basso, da sinistra verso destra, anche su finestre sovrapposte, che scorrono quindi a passo di un pixel.

!!!tip "Nota"
    Tecnicamente, quindi, l'operazione definita come "convoluzione" è in realtà una cross-correlazione.

Applicare sistematicamente lo stesso filtro su tutte le finestre possibili dell'immagine, anche sovrapposte, è un'idea alquanto potente: infatti, un filtro viene opportunamente tarato per riconoscere uno specifico tipo di feature, come un bordo o una forma, che potrà essere trovata ovunque nell'immagine grazie allo scorrimento, ottenendo la cosiddetta *invarianza alla traslazione*.

Abbiamo accennato al fatto che l'output dell'applicazione di un filtro su di una finestra dell'immagine è un prodotto scalare. Di conseguenza, man mano cheil filtro scorre, viene creato un array bidimensionale di valori, che viene indicato come *mappa delle feature*, o *feature map*. Sarà proprio questa, e non l'immagine iniziale, ad essere passata al layer successivo.

## 27.2 - Layer di pooling

Abbiamo visto come i layer convoluzionali creino delle feature map che "sintetizzano" la presenza di determinate feature all'interno di un input. Un limite di queste mappature sta però nel fatto che registrano la posizione *precisa* della feature individuata all'interno dell'input: ciò significa quindi che anche *piccole* variazioni nella posizione di una feature risulterà in una feature map completamente differente, il che comporta un'estrema sensibilità della rete neurale a piccole trasformazioni dell'immagine di input.

Per risolvere questo problema, si utilizza un approccio chiamato *sottocampionamento*: in pratica, si ricava una versione a più bassa risoluzione del segnale di ingresso, evidenziando di conseguenza gli elementi più importanti, e scartando i piccoli dettagli non rilevanti nel task di classificazione. Per far questo, viene utilizzato un layer di **pooling**, applicato a cascata rispetto a quello convoluzionale.

Il layer di pooling non fa altro che applicare un filtro, di solito di dimensioni $2 \times 2$ e con un passo di $2$ pixel (quindi senza sovrapposizioni), che applica una funzione di sottocampionamento, scegliendo quindi un unico pixel tra quelli presenti nel filtro. Due funzioni di pooling molto comuni sono le seguenti:

* *average pooling*: questo filtro associa ad ogni finestra dell'immagine in input il valore medio presente nella finestra;
* *max pooling*: questo filtro associa ad ogni finestra dell'immagine in input il valore massimo presente nella finestra.

Ottenendo quindi una versione "sottocampionata" dell'input, si raggiunge la cosiddetta *invarianza a traslazioni locali*, ovvero una sorta di "insensibilità" del modello a traslazioni o rotazioni di entità minima.

## 27.3 - Creazione di una semplice rete neurale per l'elaborazione delle immagini

Iniziamo creando una semplice rete neurale per l'elaborazione delle immagini digitali. Per farlo, useremo l'API `Sequential` di Keras, andando a creare una "pila" di layer. Ad esempio:

```py
from tensorflow import keras

model = keras.Sequential(
    [
        keras.Input(shape=(28, 28, 1)),
        keras.layers.Conv2D(
            32,
            (3, 3),
            activation='relu',
            name='first_conv_layer'),
        keras.layers.Conv2D(
            32,
            (3, 3),
            activation='relu',
            name='second_conv_layer'),
        keras.layers.Flatten(name='flatten_layer'),
        keras.layers.Dense(
            10,
            activation='softmax',
            name='layer_class')
    ]
)
```

Nel modello precedente:

* creiamo un'architettura con due layer convoluzionali bidimensionali istanziando due oggetti di classe `Conv2D`;
* ognuno di questi oggetti accetta come attributi:
  * il **numero di filtri** da usare nel banco convoluzionale (in particolare, 32);
  * la dimensione di ciascun filtro, in pixel ($3 \times 3$);
  * la funzione di attivazione da usare (`activation = 'relu'`);
  * opzionalmente, un nome.

Dopo i due layer convoluzionali notiamo la presenza di un layer di vettorizzazione delle feature estratte, ottenuto tramite un oggetto di classe  `Flatten`, ed un layer completamente connesso con un numero di neuroni pari al numero di classi coinvolte nel nostro problema (in questo caso, dieci) ed attivazione `softmax`.
