# 6.1.1 - Introduzione a TensorFlow

TensorFlow è una delle librerie più utilizzate per l'addestramento di modelli di reti neurali.

TensorFlow basa il suo funzionamento sul concetto di tensore, che ricordiamo essere un concetto imputabile ad ogni generico array ad $N$ dimensioni. Visto sotto questo punto di vista, TensorFlow sembra essere molto simile a NumPy; tuttavia, ci sono tre differenze fondamentali tra le librerie.

La prima è che, a differenza di NumPy, TensorFlow è intrinsecamente orientato al calcolo parallelo, per cui trae grande beneficio dalla presenza di GPU (Graphic Processing Unit) o TPU (Tensor Processing Unit).

!!!note "TensorFlow, GPU e TPU"
    Allo stato attuale, con la versione 2.12.x di TensorFlow, le schede grafiche supportate (a meno di non utilizzare degli artifici) sono le NVIDIA, che mettono a disposizione CUDA e, nelle versioni più recenti, anche delle TPU specifiche per l'elaborazione dei tensori.

TensorFlow è inoltre pensato per il calcolo differenziale su tensori, e può scalare su un gran numero di dispositivi. 

In generale, quindi, TensorFLow è una libreria pensata per la programmazione differenziale su tensori ad un numero arbitrario di dimensioni.

## TensorFlow e Keras

Messa così, è possibile programmare TensorFlow per effettuare delle operazioni su tensori (array, matrici, ed anche immagini) e simulare quindi l'utilizzo di una rete neurale. Tuttavia, allo scopo di ridurre la complessità di dover implementare da zero un'intera rete neurale, a partire dalla versione 2.0 di TensorFlow è stata integrata al suo interno la libreria Keras, che precedentemente era una libreria accessoria, il cui scopo è quella di fornire un'interfaccia di programmazione (detta anche API, Application Programming Interface) ad alto livello in grado di fornire tutti i mezzi per creare delle architetture orientate al deep learning in ogni possibile applicazione.

L'astrazione fondamentale alla base di Keras è quella legata alla classe Layer, che contiene al suo interno una rappresentazione dello stato di un layer di una rete neurale (ovvero, i suoi pesi) e dei metodi di processing che mappano l'inptu verso l'output, questi ultimi contenuti all'interno del metodo call. Ad esmpio:

```py
class Linear(keras.layers.Layer):
    """y = w.x + b"""

    def __init__(self, units=32, input_dim=32):
        super().__init__()
        w_init = tf.random_normal_initializer()
        self.w = tf.Variable(
            initial_value=w_init(shape=(input_dim, units), dtype="float32"),
            trainable=True,
        )
        b_init = tf.zeros_initializer()
        self.b = tf.Variable(
            initial_value=b_init(shape=(units,), dtype="float32"), trainable=True
        )

    def call(self, inputs):
        return tf.matmul(inputs, self.w) + self.b
```

TODO: DESCRIVERE QUESTA CLASSE

In questo corso, non creeremo direttamente dei nuovi layer, per cui non andremo a vedere alcune delle caratteristiche di questa classe.

## Keras API: Sequential e Functional

Keras offre due modalità per 




Laddove la Sequential API è orientata agli oggetti, la Fucntional API è una modalità di creazione del modello orientata all'applicazione dei concetti di programmazione funzionale. Ad esempio:


# We use an `Input` object to describe the shape and dtype of the inputs.
# This is the deep learning equivalent of *declaring a type*.
# The shape argument is per-sample; it does not include the batch size.
# The functional API focused on defining per-sample transformations.
# The model we create will automatically batch the per-sample transformations,
# so that it can be called on batches of data.
inputs = tf.keras.Input(shape=(16,), dtype="float32")

# We call layers on these "type" objects
# and they return updated types (new shapes/dtypes).
x = Linear(32)(inputs)  # We are reusing the Linear layer we defined earlier.
x = Dropout(0.5)(x)  # We are reusing the Dropout layer we defined earlier.
outputs = Linear(10)(x)

# A functional `Model` can be defined by specifying inputs and outputs.
# A model is itself a layer like any other.
model = tf.keras.Model(inputs, outputs)

# A functional model already has weights, before being called on any data.
# That's because we defined its input shape in advance (in `Input`).
assert len(model.weights) == 4

# Let's call our model on some data, for fun.
y = model(tf.ones((2, 16)))
assert y.shape == (2, 10)

# You can pass a `training` argument in `__call__`
# (it will get passed down to the Dropout layer).
y = model(tf.ones((2, 16)), training=True)


Rispetto alla Sequential API, la Functional API tende ad essere più sintetica, e ci permette di creare un *grafo* di layer, piuttosto che uan sequenza degli stessi.


## Model training API

##### Il metodo `compile()`

Per addestrare un modello, dobbiamo utilizzare le API specifiche. In primis, dovremo chiamare il metodo `compile()`, che configura un modello per il training. Ad esempio:

```py linenums="1"
model.compile(
    optimizer=keras.optimizers.SGD(),
    loss=keras.losses.BinaryCrossentropy(),
    metrics=[
        keras.metrics.BinaryAccuracy(),
        keras.metrics.Precision(),
        keras.metrics.Recall()
    ]
)
```

In particolare: BREVE DESCRIZIONE

##### Il metodo `fit()`

Su

## Caricamento dei dati

Esempio su image_dataset_from_directory()
