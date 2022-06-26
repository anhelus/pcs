# 28 - TensorFlow & Keras: Tips & Tricks

## 28.1 - Creazione di un dataset

Per dati di grosse dimensioni, TensorFlow potrebbe richiedere l'uso di un oggetto di tipo `Dataset`.

### 28.1.1 - Immagini

Finora ci siamo limitati ad utilizzare dati

### 28.1.2 - Testo

Così come per le immagini, Keras offre un modo per creare un dataset testuale a partire da una cartella. Per farlo, occorre usare il metodo [`text_dataset_from_directory`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/text_dataset_from_directory).

Analogamente al metodo usato per le immagini, `text_dataset_from_directory` si aspetta una cartella in una certa forma:

```bash
data/
...class1/
......1.txt
......2.txt
...class2/
......1.txt
......2.txt
......3.txt
```

Per caricare il nostro dataset possiamo usare una forma analoga a quella delle immagini:

```py
# Dataset di training
train_ds = text_dataset_from_direcotry(
    data_dir,
    batch_size=batch_size,
    validation_split=0.2,
    subset='training',
    seed=seed)

# Dataset di validazione
val_ds = text_dataset_from_directory(
    data_dir,
    batch_size=batch_size,
    validation_split=0.2,
    subset='validation',
    seed=seed)
```

#### preparazione dati testuali per il trainng

Una volta scaricati i dati, effettueremo la standarizzaione, tokenizzazione e vettorizzazione usando il layer [`TextVectorization`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TextVectorization). I tre passi si riferiscono a:

* standardizzazione è una procedura di preprocessing del testo, ripicamente rimozione di punteggiatura o elementi HTML per semplificare il daset
* la tokenizzazione si riferisce alla suddivisione di stringhe in token (per esempio, suddividere una frase in parole individuali)
* la vettoprizzazione prevede che i token siano convertiti in numeri per poter poi essere passati ad una rete neurale

Notiamo che:

* la standardizzazione di default converte il testo in minuscolo e rimuove la punteggiatura
* il tokenizer di default suddivide i token in base allo spazio
* il modo di vettorizzazione di default è int, ovvero dà degli indici interi (uno per token)

Ad esempio:

```py
int_vectorize_layer = TextVectorization(
    max_tokens=VOCAB_SIZE,
    output_mode='int',
    output_sequence_length=MAX_SEQUENCE_LENGTH)
```
Qui specifichiamo VOCAB_SIZE come numero massimo di vocaboli consentiti, ed un valore massimo da considerare per la frase mediante il parametro `output_sequence_length`.

A questo punto, provvederemo a chiamaere il mtodo adapt di TextVectgorization per efettuare il fitting dello stato del layer di preprocessing al dataset e convertire il dataset.

int_vectorize_layer.adapt(train_text)

Come passo finale, applichiamo il layer di TextVectorization ai test di training, validazione e test.

int_train_ds = raw_train_ds.map(int_vectorize_text)
int_val_ds = raw_val_ds.map(int_vectorize_text)
int_test_ds = raw_test_ds.map(int_vectorize_text)

### 28.1.3 - Array NumPy

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


# 27

## Callback modello

Un *callback* è un oggetto che può effettuare un'azione durante diversi stage del training.

Si può usare un callback epr:

* scrivere i log di tensorboard dopo ogni batch di training per monitorare le nostre metriche
* salvare periodicamente il modello su disco
* fare l'early stopping
* avere una vista sugli stati e statistiche interne di un modello durante il training

Per usarli, possiamo passare una lista di callback al parametro callbacks al metodo fit() di un modello.

### ModelCheckpoint

Questo callback ci permette di salvare un modello Keras o i suoi pesi con una certa frequenza, in modo che il modello o i pesi possano essere caricati successivamente per continuare il training dallo stato raggiunto.

Alcune opzioni importnati del ModelCheckpoint sono le seguenti:



## Visualizzazione su TensorBoard

## Transfer learning e fine tuning

Il transfer learning consiste nel prendre dellef eature apprese su un problema e sfruttarle per risolvere un nuovo (e simile) problema. Ad esempio, le feature che sono state apprese per apprendere la razza di un felino possono essere usate epr apprendere la razza di un canide.

Il transfer learning è spesso effettuato per i task dove il dataset ha pochi dati per permettere un addestramento da zero del nostro modello.

L'incarnazione più conosciuta in tal senso del workflow da seguire è la seguetne:

1. prendiamo i layer da un modello precedentemente addestrato;
2. congeliamo detti layer, in modo da evitare di distruggere l'informazione che contengono durante futuri round di addestramento;
3. aggiungiamo alcuni layer addestrabili sull'ultimo dei layer freezati. Questi impareranno quindi a modificare le vecchie feature in predizioni sul nuovo dataset.
4. addestriamo i nuovi layer del nostro dataset

Un ultimo step opzionale è il fine tuning, che prevede di "sbloccare" l'intero modello ottenuto in precedenza (o parte di esso) e riaddestrarlo sui nuovi dati con un learning rate molto blando. Questo può potenzialmente ottenre dei miglioramenti significativi adattando in maniera incrementale le feature precedentemente ottenute ai nuovi dati.
