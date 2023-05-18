# 6.1.1 - Introduzione a TensorFlow

[**TensorFlow**](https://www.tensorflow.org/) è una delle librerie più utilizzate per l'addestramento di modelli di reti neurali.

TensorFlow basa il suo funzionamento sul concetto di *tensore*, che ricordiamo essere un concetto imputabile ad ogni generico array ad $n$ dimensioni. Visto sotto questo punto di vista, TensorFlow potrebbe apparire simile a NumPy che, come ricordiamo, si occupa proprio di array $n$-dimensionali. Tuttavia, tra le librerie esistono diverse differenze: ad esempio, TensorFlow è pensato esplicitamente per il calcolo differenziale, è scalabile su architetture distribuite, ed è intrinsecamente orientato al calcolo parallelo, traendo grande beneficio dalla presenza di *GPU* (*Graphic Processing Unit*) e *TPU* (*Tensor Processing Unit*).

!!!note "TensorFlow, GPU e TPU"
    Allo stato attuale, con la versione 2.12.x di TensorFlow, le schede grafiche supportate (a meno di non utilizzare degli artifici) sono le NVIDIA, che mettono a disposizione i cosiddetti CUDA core e, nelle versioni più recenti, anche delle TPU specifiche per l'elaborazione dei tensori.

## TensorFlow e Keras

TensorFlow può essere usato per operazioni su tensori di ogni tipo sui tensori: di conseguenza, è possibile sfruttarlo anche per creare una rete neurale. Tuttavia, utilizzare direttamente TensorFlow può risultare abbastanza ostico; di conseguenza, a partire dalla versione 2.0 del framework, è stata integrata al suo interno la libreria **Keras**, il cui scopo è quello di fornire un'*interfaccia di programmazione* (in inglese *Application Programming Interface*, o *API*) ad alto livello, che semplifica notevolmente la creazione di architetture per il deep learning. Vediamone alcune tra le più importanti.

## Keras API: Sequential e Functional

Keras ci mette a disposizione due modi per creare un'architettura di rete neurale, definiti rispettivamente dalle API [`Sequential`](https://www.tensorflow.org/api_docs/python/tf/keras/Sequential) e [`Functional`](https://www.tensorflow.org/guide/keras/functional?hl=en).

La differenza tra le due API è facilmente riassumibile: 

* l'API `Sequential` offre un approccio interamente *object-oriented* alla creazione di architetture *puramente* sequenziali, il che la rente semplice da usare, ma limitata;
* l'API `Functional` offre un approccio puramente *funzionale* alla creazione dell'architettura, intrinsecamente più complesso, ma anche in grado di offrire una maggiore flessibilità, e non limitato ad architetture puramente sequenziali, in quanto ci permette di creare architetture rappresentabili secondo un *grafo* più o meno complesso.

Nel seguente snippet, possiamo vedere le due modalità a confronto.

=== "Sequential"
    ``` py
    model = Sequential()
    model.add(Input(shape=(16), dtype="float32"))
    model.add(RegLin(32))
    model.add(Dropout(0.5))
    model.add(RegLin(10))
    ```
=== "Functional"
    ``` py
    inputs = Input(shape=(16,), dtype="float32")
    x = RegLin(32)(inputs)
    x = Dropout(0.5)(x)
    outputs = RegLin(10)(x)
    model = Model(inputs, outputs)
    ```

In particolare:

* nell'approccio funzionale usiamo un oggetto di tipo [`Input`](https://www.tensorflow.org/api_docs/python/tf/keras/Input) che crea un tensore per descrivere la forma ed il tipo degli ingressi;
* nell'approccio sequenziale usiamo invece un `InputLayer` per aggiungere un layer di ingresso al modello;
* l'API `Sequential` utilizza il metodo `add()` parametrizzato con un layer per concatenare (agendo quindi in modo strettamente sequenziale) uno stack di layer;
* l'API `Functional` utilizza invece sfrutta la programmazione funzionale per "chiamare" i layer sullo stack precedente: ad esempio, l'istruzione `x = Dropout(0.5)(x)` "chiama" la classe `Dropout` sullo stack di layer costruito in precedenza;
* il modello funzionale deve essere definito usando la classe [`Model`](https://www.tensorflow.org/api_docs/python/tf/keras/Model) e specificandone input ed output.

## Model training API

L'addestramento di un modello con Keras prevede l'utilizzo di due metodi definiti dalla *model training API*. Vediamoli insieme.

##### Il metodo `compile()`

Il primo metodo da utilizzare è [`compile()`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#compile), che configura il modello con i parametri specificati. Ad esempio:

```py linenums="1"
model.compile(
    optimizer=SGD(),
    loss=BinaryCrossentropy(),
    metrics=[
        BinaryAccuracy(),
        Precision(),
        Recall()
    ])
```

I tre parametri che è importante passare al metodo `compile()` sono:

* `optimizer`, che specifica l'algoritmo di ottimizzazione da utilizzare per l'addestramento del modello;
* `loss`, che specifica la funzione di costo usata per valutare le performance del modello;
* `metrics`, che specifica quali metriche saranno mostrate nella valutazione del modello.

Nel caso precedente, utilizziamo l'algoritmo SGD per l'ottimizzazione, la cross-entropy binaria come funzione di costo, e precisione, recall ed accuracy binaria come metriche da mostrare all'utente.

##### Il metodo `fit()`

Il metodo `compile()` **non addestra la rete**, limitandosi a configurarla. Per effettuare l'addestramento, dobbiamo usare il metodo [`fit()`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit). Ad esempio:

```py linenums="1"
history = model.fit(
    x=X,
    y=y,
    batch_size=8,
    epochs=10,
    validation_split=0.3)
```

In particolare, i parametri che stiamo usando sono:

* `X` ed `y`, rappresentativi della matrice di design e del vettore delle label, che possono essere (tra gli altri) degli array NumPy;
* `batch_size`, che indica quanti campioni verranno elaborati ad ogni singolo passaggio dal modello;
* `epochs`, che indica quante iterazioni di addestramento dovranno essere effettuate dalla rete;
* `validation_split`, che indica la percentuale dei dati che saranno usati per la validazione.

!!!note "Callback e dati"
    Il metodo `fit()` offre molti altri interessanti parametri, alcuni dei quali approfondiremo nelle lezioni successive.
