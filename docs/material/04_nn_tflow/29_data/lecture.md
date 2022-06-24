https://www.tensorflow.org/tutorials/load_data/images?hl=en

# 28 - Preprocessing dei dati

## Immagini

Esistono diversi modi per caricare ed effettuare il preprocessing di un dataset di immagini. In questo caso, vedremo delle utility di preprocessing di Keras, così come dei layer per leggere le immagini su disco.

Per prima cosa, possiamo usare la funzione `image_dataset_from_directory` del package `utils` di Keras. Questa ci permette di caricare direttamente le immagini dalla cartella, ed ha una sintassi di questo tipo:

```py
train = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset='training',
    image_size=(img_height, img_width),
    batch_size=batch_size
)
val = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset='validation',
    image_size=(img_height, img_width),
    batch_size=batch_size
)
```

Possiamo passare questi valiori direttamente ad un dataset; infatti, in pratica si tratta di una lista di *batch* dalla dimensione (batch, height, width, channel):

```py
model.fit(
    train,
    validation_data=val,
    epochs=10
)
```

Da notare che è bene inserire un layer di rescaling qualora si tratti di un'immagine RGB. Infatti, i canali RGB hanno valori all'interno del range [0, 255], il che non è ideale per una rete neurale, che funziona meglio con valori compresi tra [0, 1]. In tal senso, possiamo usare un layer di Rescaling:

```py
tf.keras.layers.Rescaling(1./255)
```

## Array

https://www.tensorflow.org/tutorials/load_data/numpy?hl=en

## Dataframe

https://www.tensorflow.org/tutorials/load_data/pandas_dataframe?hl=en
