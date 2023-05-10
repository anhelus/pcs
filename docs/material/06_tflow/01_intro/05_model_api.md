# 6.1.2 - Le subclassing API

Una delle principali astrazioni offerte da Keras è la classe `Layer`. Questa classe incapsula sia uno stato (i *pesi* del layer) ed una trasformazione dagli input agli output.

Un esempio è il seguente:

```py

class Linear(keras.layers.Layer):
    def __init__(self, units=32, input_dim=32):
        super(Linear, self).__init__()
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

Useremo un layer chiamandolo su alcuni input di forma tensorliae, come una funzione Python:

```py
x = tf.ones((2, 2))
linear_layer = Linear(4, 2)
y = linear_layer(x)
print(x)
```

Notiamo che i pesi `w` ed i bias `b` sono automaticamente tracciati dal layer.

Notiamo anche che abbiamo una scorciatoia per aggiungere dei pesi ad un layer mediante il metodo `add_weight()`:

```py
class Linear(keras.layers.Layer):
    def __init__(self, units=32, input_dim=32):
        super(Linear, self).__init__()
        self.w = self.add_weight(
            shape=(input_dim, units), initializer="random_normal", trainable=True
        )
        self.b = self.add_weight(shape=(units,), initializer="zeros", trainable=True)

    def call(self, inputs):
        return tf.matmul(inputs, self.w) + self.b


x = tf.ones((2, 2))
linear_layer = Linear(4, 2)
y = linear_layer(x)
print(y)
```

I layer possono avere anche dei pesi non addestrabili. Qeusti pesi non vengono considerati durante la backgpropagation:

```py
class ComputeSum(keras.layers.Layer):
    def __init__(self, input_dim):
        super(ComputeSum, self).__init__()
        self.total = tf.Variable(initial_value=tf.zeros((input_dim,)), trainable=False)

    def call(self, inputs):
        self.total.assign_add(tf.reduce_sum(inputs, axis=0))
        return self.total


x = tf.ones((2, 2))
my_sum = ComputeSum(2)
y = my_sum(x)
print(y.numpy())
y = my_sum(x)
print(y.numpy())
```

Possiamo anche evitare di specificare in anticipo la dimensione dei nostri ingressi, in quanto potremmo creare dei pesi in maniera lazy quando questo valore viene conosciuto, dopo aver istanziato il layer. Nell'API di Keras, possiamo creare i pesi nel metodo build(self, inputs_shape):


class Linear(keras.layers.Layer):
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


Il metodo __cal__ del layer chiamerà in automatico il build la prima volta che viene chiamato. Possiamo avere un lazy layer, che di conseguenza è più semplice da usare.

I layer sono cmponibili. Se assegnamo un'istanza di un Layer ad un altro Layer, quello esterno traccerà i pesi creati dal layer interno.

class MLPBlock(keras.layers.Layer):
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


mlp = MLPBlock()
y = mlp(tf.ones(shape=(3, 64)))  # The first call to the `mlp` will create the weights
print("weights:", len(mlp.weights))
print("trainable weights:", len(mlp.trainable_weights))



Quando scriviamo il metodo call() per un layer possiamo crare un tensore di loss che vogliamo usare dopo, quando scriviamo il nostro loop di training. Per farlo, chiamiamo self.add_loss(value):

# A layer that creates an activity regularization loss
class ActivityRegularizationLayer(keras.layers.Layer):
    def __init__(self, rate=1e-2):
        super(ActivityRegularizationLayer, self).__init__()
        self.rate = rate

    def call(self, inputs):
        self.add_loss(self.rate * tf.reduce_sum(inputs))
        return inputs

In modo simile ad add_loss(), un layer può anche avere un metodo add_metric() per tracciare la media mobile di una quantità durante l'addestramento.


## class model

In generale, useremo la classe Layer per definrie dei blocchi di calcolo itnerno, ed useremo la classe Model per definire il modello complessivo dir ete, che sarà quello che addestreremo. Ad esempio, in un mdoello ResNet50, abbiamo diversi blocchi ResNet che fannod elle sottoclassi di Layer, ed un singolo Model che contiene l'intera archietttura di rete.

La classe Model ha la stessa API di Layer, con alcune differenze:

* espone i modelli fit(), evaluate() e predict() per i loop di training, valutazione e predizione, rispettivamente
* espone la lista di layer interni mediante la proprietà models.layers
* espone le API di salvataggio e serializzazione del modello

In efeftti, la classe Layer corrispodne a quello che in letteratura sarebbe un laeyr o blocco (ad esempio, un *Inception block*). D'altro canto, la classe Modle corrispone a quello che è definto come modello o rete.
