# Introduzione agli autoencoder

In questa lezione, vedremo tre esempi di utilizzo degli autoencoder.

Un autoencoder è uno speciale tipo di rete neurale che viene addestrata a copiare il suo input sul suo output. Ad esempio, data un'immagine di una cifra scritta a mano, un autoencoder per prima cosa codifica l'immagine in una rappresentazione a bassa dimensionalità, quindi decodifica questa rappresentazione restituendo l'immagine originaria. Per far questo, l'autoencoder apprende a comprimere i dati minimizzando contestualmente l'errore di ricostruzione.

## Definizione

FOrmalmente, un autoencoder ha un layer nascosto $h$ che descrive un codice usato per rappresentare l'input.

Un autoencoder può essere visto come composto di due parti: una funzione di codifica $h = f(x)$ (chiamata, per l'appunto, encoder), ed una funzione di *ricostruzione* chiamata $r = g(h)$, chiamata decoder.

TODO FIGURA AUTOENCODER

Se un autoencoder è in grado semplicemente di impostare $g(f(x)) = h$, allora non sarebbe utile. Invece, gli autoencoder sono progettati nin modo tale da non essere in grado di apprendere a copiare perfettamente il dato. Normalmente sono ristretti in modi che permettono di copiare i dati soltanto in maniera approssimativa, e copiare soltanto gli input che assomigliano ai dati di addestramento. Dato che il modello viene forzato a prioritizzare quali aspetti dell'ingresso dovrebbero essere copiati, spesso è in grado di apprendere delle proprietà utili sui dati.

Gli autoencoder moderni hanno genralizzato l'idea della coppia encoder/decoder oltre alle funzioni deterministiche, producendo dei mapping stocastici di tipo $p_{encoder}(h | x)$ e $p_{decoder}(x | h)$.

L'idea di autoencoder è stata parte del paesaggio delle reti neurali per decadi. Tradizionalmente, gli autoencoder erano suati per la riduzione della dimensionalità, o l'estrazione di feature. Di recente, nuove connessioni teoriche tra gli autencoder ed i modelli a variabili latenti hanno portato gli autoencoder nel mondo dei modelli generativi. Gli autoencoder possono essere pensati come un caso speciale di reti feedforward, e possono essere adestrati con le stesse tecniche, tipicamente il gradient deshent che segue i gradienti calcolati mediante back-propagataion. A differenza delle reti feedforward generiche, gli autoencoder possono anche essere addestrati usando tecniche come la *recirculation* (HINTON MCCLELLAND 1988), un algoritmod i apprendimento basato sulla comparazione delle attivazioni della rete sull'input originario con le attivazioni sull'input ricostruito. La recirculation è consdierata maggiormente plausibile dal punto di vista biologico rispetto alla back-propagation, ma viene raramente usata per applicazioni di machine learning.

## Autoencoder sottocompleti

Copiare l'input all'output potrebbe suonare inutili, ma tipicamente non siamo interessati nell'output del decoder. Invece, speriamo che addestrare l'autoencoder ad effettuare il task di copia dell'input risulterà nel fatto che $h$ assuma delle proprietà utili.

Un modo per ottenere feature utili dall'autoencoder è vincolare $h$ ad avere una dimensione inferiore ad $x$. Un autoencoder la cui dimensione del codice è inferiore alla dimensione dell'ingresso è chiamato *sottocompleto*. Apprendere una rappresentazione sottocompleta forza l'autoencoder a catturare le feature maggiormente significative dei dati di training.

Per questo tipo di autoencoder, il processo di apprendimento può essere definito come la minimizzazione di una funzione di costro:

$$
L(x,g(f(x)))
$$

dove $L$ è la funzione i costo che penalizza $g(f(x))$ dall'essere dissimile da $x$, come l'MSE.

Quando il decoder è lineare ed $L$ è l'errore quadratico medio, un autoencoder sottocompleto apprende lo stesso sottospazio della PCA. In questo caso, un autoencoder addestrato ad effettuare il task di copying ha appreso il sottospazio principale dei dati di addestramento come effetto collaterale.

Gli autoencoder con le funzioni non lineari di encoding $f$ e decoding $g$ possono quindi apprendere una generalizzazione non lineare più potente della PCA. Sfortunatamente, se l'encoder ed il decoder hanno eccessiva capacità, l'autoencoder può apprendere a d effettuare il task di copia senza estrarre informazioni utili sulla distribuzione dei dati. Teoricamente, si può immaginare che un autoencoder con un codice monodimensionale ma con un encoder non lineare molto potente può apprendere a rappresentare ogni campione di training $x^(i)$ con il codice $i$. Il decoder può apprendere a mappare questi indici interi ai valori degli specifici campioni di training. Questo specifico scenario non avviene nella pratica, ma illustra chiaramente che un autoencoder addestrato ad effettuare il task di copying può fallire ad apprendere qualcosa di utile nel dataset se la capacitàd dell'autoencoder può diventare eccessivamente grande.


## Esempio

Per prima cosa, importiamo le librerie necessarie.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf

from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from tensorflow.keras import layers, losses
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.models import Model

A questo punto, carichiamo il dataset usando MNIST.

(x_train, _), (x_test, _) = fashion_mnist.load_data()

x_train = x_train.astype('float32') / 255.
x_test = x_test.astype('float32') / 255.

print (x_train.shape)
print (x_test.shape)

## Primo esempio: autoencoder base

Per il primo esempio, definiremo un autoencoder con due layer densi: un encoder, che comprime l'immagine in un vettore a 64 dimensioni, ed un decoder, ceh ricostruisce l'immagine originale dallo spazio latente. Per definire il modello, useremo l'API Model di Keras:


latent_dim = 64 

class Autoencoder(Model):
  def __init__(self, latent_dim):
    super(Autoencoder, self).__init__()
    self.latent_dim = latent_dim   
    self.encoder = tf.keras.Sequential([
      layers.Flatten(),
      layers.Dense(latent_dim, activation='relu'),
    ])
    self.decoder = tf.keras.Sequential([
      layers.Dense(784, activation='sigmoid'),
      layers.Reshape((28, 28))
    ])

  def call(self, x):
    encoded = self.encoder(x)
    decoded = self.decoder(encoded)
    return decoded

autoencoder = Autoencoder(latent_dim)


autoencoder.compile(optimizer='adam', loss=losses.MeanSquaredError())


Addestriamo adesso il modello usando `x_train` sia come input, sia come target. L'encoder apprenderà a comprimere il dataset da 784 dimensioni (28x28) allo spazio latente, mentre il decoder apprenderà a ricostruire le immagini originarie.

autoencoder.fit(x_train, x_train,
                epochs=10,
                shuffle=True,
                validation_data=(x_test, x_test))


Una volta addestrato il modello, testiamolo codificando e decodificando delle immagini dal set di test.

encoded_imgs = autoencoder.encoder(x_test).numpy()
decoded_imgs = autoencoder.decoder(encoded_imgs).numpy()

n = 10
plt.figure(figsize=(20, 4))
for i in range(n):
  # display original
  ax = plt.subplot(2, n, i + 1)
  plt.imshow(x_test[i])
  plt.title("original")
  plt.gray()
  ax.get_xaxis().set_visible(False)
  ax.get_yaxis().set_visible(False)

  # display reconstruction
  ax = plt.subplot(2, n, i + 1 + n)
  plt.imshow(decoded_imgs[i])
  plt.title("reconstructed")
  plt.gray()
  ax.get_xaxis().set_visible(False)
  ax.get_yaxis().set_visible(False)
plt.show()


## Regolarized autoencoders

Gli autoencoder sottocompleti, con le dimensioni del codice inferiori alle dimensioni di input, possono apprendere le feature maggiormente importanti della distribuzione dei dati. Abbiamo visto che questi autoencoder falliscono ad apprendere delle informazioni utili se all'encoder ed al decoder è data una capacità eccessiva.

Un problema simile avviene se il codice può avere una dimensione uguale all'ingresso, e nel caso *sovracompleto*, nel quale il codice ha dimensioni superiori a quelle dell'input. IN questi casi, anche un encoder lineare ed un decoder lineare può apprendere a copiare l'input all'output senza dover apprendere delle informazioni sulla distribuzione dei dati.

Idealmente, si può addestrare una qualsiasi archietttura di autoencoder con successo, scegliendo la dimensione del codice e la capacità di encoder e decoder sulla base della complessità della distribuzione da modellare. Gli autoencoder regolarizzati forniscono la capacità di far questo. Pitutosto che limitare la capacità del moello mantenendo l'encoder ed il decoder poco profondi con ridotta dimensione del codice, gli autoencoder regolarizzati usano una funzione di costo che incoraggia il modello ad avere altre proprietà oltre alla capacità di copiare i suoi input ai suoi output. Queste altre prorpietà includono la sparsezza della rappresentazione, al riduzione elle derivate della rappresentazione, e la robustezza al rumore o agli input mancanti. Un autoencoder regolarizzato può essere non lineare ed overcompleto, ed apprendere comunque qualcosa di utile sulla distribuzione dei dati, anches e la capacità del modello è abbastanza grande per apprendere una banale funzione di identità. Oltre ai metodi descritti qui, che sono interpretati come autoencoder regolarizzati, praticamente ogni modello generativo con variabili latenti ed equipaggiato con una procedura di inferenza per calcolare delle rappresentazioni latenti dato un certo input può essere visto come una forma particolare di autoencoder. 

Un primo esempio di autoencoder regolarizzato è lo sparse autoencoder. Questo è semplicemente un autoencoder i cui criteri di addestramento coinvolgono la presenza di una penalità di sparsità $\Omega(h)$ sul code layer $h$, otlre all'errore di ricostruzione. La funzione diventa quindi:

$$
L(x, g(f(x))) + \Omega(h)
$$

dove $g(h)$ è l'output del decoder, e tipicamente abbiamo $h=f(x)$, l'outpu dell'encoder. Gli sparse autoencoder sono tipicamente usati per apprendere feature per altri task, come quelli di classificazione. Un autoencoder che è stato regolarizzato per essere sparso deve rispondere a feature statistiche univoche per il dataset su cui è stato addestrato, piuttosto che agire semplicemente come funzione identità. In questo modo, addestrare ad effettuare il task di copia con una penalità di sparsità può potrare ad un modello che ha appreso delle feature utili.

Possiamo pensare alla penalità $\Omega(h)$ come al termine di regolaizzazione aggiunto ad una rete feedforward il cui task primario è quello di copiare l'input all'output (obiettivo di apprendimento non supervisionato) ed effettuare possibilmente anche dei task 


https://www.deeplearningbook.org/contents/autoencoders.html -> Denoising autoencoder

## Image denoising

Un autoencoder può anche essere addestrato a rimuovere del rumore dalle immagini. In questo esempio, creeremo una versione rumorosa del dataset MNIST andando ad applicare del rumore casuale ad ogni immagine. Addestreremo quindi un autoencoder usando l'immagine rumorosa come input, e l'immagine originaria come target.

Aggiungiamo rumore casuale alle immagini

noise_factor = 0.2
x_train_noisy = x_train + noise_factor * tf.random.normal(shape=x_train.shape) 
x_test_noisy = x_test + noise_factor * tf.random.normal(shape=x_test.shape) 

x_train_noisy = tf.clip_by_value(x_train_noisy, clip_value_min=0., clip_value_max=1.)
x_test_noisy = tf.clip_by_value(x_test_noisy, clip_value_min=0., clip_value_max=1.)

Plottiamo le immagini rumorose.

n = 10
plt.figure(figsize=(20, 2))
for i in range(n):
    ax = plt.subplot(1, n, i + 1)
    plt.title("original + noise")
    plt.imshow(tf.squeeze(x_test_noisy[i]))
    plt.gray()
plt.show()

## definiamo un convolutional autoencoder
