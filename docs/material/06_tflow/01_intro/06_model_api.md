# 6.1.6 - `Layer` e `Model`: un approfondimento

## La classe `Layer`

L'astrazione fondamentale alla base di Keras è la classe [`Layer`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Layer), che rappresenta lo stato di un layer di una rete neurale (ovvero, i suoi pesi), oltre che i metodi che permettono di mappare l'input del layer verso l'output, questi ultimi contenuti nel metodo `call`. Il seguente snippet illustra un esempio di layer Keras:

```py linenums="1"
class Linear(tf.keras.layersLayer):

    def __init__(
        self,
        units=32,
        input_dim=32):
        super().__init__()
        w_init = tf.random_normal_initializer()
        self.w = tf.Variable(
            initial_value=w_init(shape=(input_dim, units), dtype="float32"),
            trainable=True)
        b_init = tf.zeros_initializer()
        self.b = tf.Variable(
            initial_value=b_init(shape=(units,), dtype="float32"),
            trainable=True)

    def call(self, inputs):
        return tf.matmul(inputs, self.w) + self.b
```

In particolare:

* gli attributi di ogni istanza del layer `Linear` saranno il tensore dei pesi `w` e quello dei bias `b`;
* nel metodo `__init__`, alla riga 8, usiamo il metodo [`random_normal_initializer()`](https://www.tensorflow.org/api_docs/python/tf/random_normal_initializer) di TensorFlow per creare un *inizializzatore* del tensore dei pesi $w$ in modo che detti pesi siano estratti casualmente da una distribuzione normale;
* i pesi sono inizializzati sotto forma di una [`Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable) TensorFlow usando l'inizializzatore definito in precedenza, ed impostando una dimensione `input_dim` $\times$ `units`, con `input_dim` dimensione del vettore di ingresso, ed `units` numero di unità. L'attributo `trainable` assicura infine che sia possibile modificare questi pesi a valle di una procedura di addestramento;
* in modo simile, alla riga 12 creiamo un inizializzatore del tensore degli offset $b$ sfruttando il metodo [`zeros_initializer`](https://www.tensorflow.org/api_docs/python/tf/zeros_initializer), che verrà inizializzato in modo simile al tensore dei pesi $w$;
* alle righe 17-18, infine, definiamo il metodo `call`, che descrive il rapporto tra ingresso ed uscita del layer.

##### Aggiunga dei pesi ad un layer

La procedura vista in precedenza per l'aggiunta dei pesi e del bias al nostro layer può essere notevolmente semplificata mediante il metodo [`add_weight()`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Layer#add_weight):

```py
class Linear(tf.keras.layers.Layer):
    def __init__(self, units=32, input_dim=32):
        super(Linear, self).__init__()
        self.w = self.add_weight(
            shape=(input_dim, units), initializer="random_normal", trainable=True
        )
        self.b = self.add_weight(shape=(units,), initializer="zeros", trainable=True)

    def call(self, inputs):
        return tf.matmul(inputs, self.w) + self.b
```

##### Layer con pesi non addestrabili

Un layer può avere anche dei pesi non addestrabili. In tal senso, si può impostare a `False` il parametro `trainable`.

```py
class ComputeSum(tf.keras.layers.Layer):
    def __init__(self, input_dim):
        super(ComputeSum, self).__init__()
        self.total = tf.Variable(initial_value=tf.zeros((input_dim,)), trainable=False)

    def call(self, inputs):
        self.total.assign_add(tf.reduce_sum(inputs, axis=0))
        return self.total
```

##### Omettere la dimensione dell'input

Keras ci permette di omettere la dimensione dell'input, creandola in maniera *lazy* al momento dell'istanziazione del layer nel nsotro modello. Per farlo, Keras ci mette a disposizione il metodo [`build()`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Layer#build):

```py
class Linear(tf.keras.layers.Layer):
    def __init__(self, units=32):
        super(Linear, self).__init__()
        self.units = units

    def build(self, input_shape):
        self.w = self.add_weight(
            shape=(input_shape[-1], self.units),
            initializer="random_normal",
            trainable=True,
        )
        self.b = self.add_weight(
            shape=(self.units,), initializer="random_normal", trainable=True
        )

    def call(self, inputs):
        return tf.matmul(inputs, self.w) + self.b
```

##### Stack di layer

I layer sono *componibili*; ciò avviene usando un layer come attributo di un altro:

```py
class MLP(keras.layers.Layer):
    def __init__(self):
        super(MLPBlock, self).__init__()
        self.linear_1 = Linear(32)
        self.linear_2 = Linear(32)
        self.linear_3 = Linear(1)

    def call(self, inputs):
        x = self.linear_1(inputs)
        x = tf.nn.relu(x)
        x = self.linear_2(x)
        x = tf.nn.relu(x)
        return self.linear_3(x)
```

## La classe `Model`

In generale, l'uso della classe `Layer` è destinato alla definizione di nuovi layer della rete neurale o, in alternativa, di stack degli stessi. La classe `Model`, invece, viene usata per definire il modello complessivo della rete, che sarà quello che sarà addestrato. Per fare un esempio, in un modello che riproduce una ResNet, avremo diversi blocchi residuali derivanti dalla classe `Layer`, ed un singolo `Model` contenente l'intera architettura di rete.

La classe `Model` usa un'interfaccia molto simile a quella di `Layer` a meno di alcune differenze:

* la classe `Model` espone i metodi `compile()`, `fit()`, `evaluate()` e `predict()` per addestrare, validare ed usare in inferenza la rete;
* un oggetto di classe `Model` espone la lista di layer al suo interno usando l'attributo `layers`;
* un oggetto di classe `Model` ha a sua disposizione le API per il caricamento ed il salvataggio del modello e dei suoi pesi.
