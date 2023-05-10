# 6.2.1 - Simple autoencoder

Per definire un autoencoder in Keras, possiamo usare due layer di tipo `Dense`, rappresentativi rispettivamente di un encoder ed un decoder.

Per defionire il nostro modello, possiamo usare le API di Keras per creare un model (Keras Model Subclassing API).



In

```py
class Autoencoder(Model):

    def __init__(self, latent_dim):
        super(Autoencoder, self).__init__()
        self.latent_dim = latent_dim
        self.encoder = tf.keras.Sequential([
            layers.Flatten(),
            layers.Dense(latent_dim, activation='relu')
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
```

Chiamiamo poii i metodi fit e compile.

## Denoising autoencoder

## Anomaly detection

## Variational autoencoder
