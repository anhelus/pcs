# 28 - TensorFlow & Keras: Tips & Tricks

## 28.1 - Dataset

I dati che abbiamo utilizzato finora erano organizzati sotto forma di array NumPy. Tuttavia, per dataset di grosse dimensioni, potrebbe essere necessario utilizzare degli oggetti di tipo [`Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset). In tal senso, Keras ci mette a disposizione diverse tecniche; vediamone alcuni.

### 28.1.1 - Immagini

Per caricare un dataset di immagini a partire da una cartella, possiamo usare la funzione [`image_dataset_from_directory`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/image_dataset_from_directory), che ha una sintassi di questo tipo:

```py
train = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset='training',
    image_size=(img_height, img_width),
    batch_size=batch_size,
    seed=seed)

val = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset='validation',
    image_size=(img_height, img_width),
    batch_size=batch_size,
    seed=seed)
```

Nel precedente esempio:

* `data_dir` è la cartella dove sono presenti i dati;
* `validation_split` indica quanti dati usare per la validazione. Il valore deve essere coerente tra il dataset di train e quello di validazione;
* `subset` indica se il dataset è indirizzato al training o alla validazione;
* `image_size` rappresenta la dimensione (in pixel) dell'immagine;
* `batch_size` rappresenta la dimensione del batch di dati da usare;
* `seed` è un parametro che ci assicura la coerenza tra le immagini scelte per il training e quelle scelte per il test.

La cartella `data_dir` deve essere organizzata come segue:

```bash
data_dir/
...class1/
......1.png
......2.png
...class2/
......1.png
......2.png
......3.png
```

A questo punto possiamo passare `train` e `val` direttamente al metodo `fit` del nostro modello.

```py
model.fit(
    train,
    validation_data=val,
    epochs=10)
```

!!!note "Nota"
    Un accorgimento utile a migliorare le prestazioni della nostra rete è quello di inserire un layer di *rescaling* qualora si abbia a che fare con immagini a colori. Infatti, i canali RGB possono assumere valori all'interno del range $[0, 255]$, mentre è consigliabile usare per una rete neurale valori compresi nell'intervallo $[0, 1]$. Keras ci mette a disposizione un apposito layer:
    > ```py
    tf.keras.layers.Rescaling(1./255)
    ```

### 28.1.2 - Testo

Keras offre un metodo simile per creare un dataset a partire da un insieme di file di testo, utilizzando il metodo [`text_dataset_from_directory`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/text_dataset_from_directory).

Analogamente al metodo usato per le immagini, `text_dataset_from_directory` si aspetta una cartella in una certa forma:

```bash
data_dir/
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
train = text_dataset_from_direcotry(
    data_dir,
    batch_size=batch_size,
    validation_split=0.2,
    subset='training',
    seed=seed)

val = text_dataset_from_directory(
    data_dir,
    batch_size=batch_size,
    validation_split=0.2,
    subset='validation',
    seed=seed)
```

I parametri sono esattamente gli stessi, a meno dell'assenza del parametro `image_size`.

#### 28.1.2.1 - preparazione dati testuali per il trainng

Rispetto alle immagini, i dati testuali richiedono tre ulteriori operazioni, ovvero:

* *standardizzazione*: si tratta di una procedura di preprocessing sul testo, che consiste tipicamente nella rimozione della punteggiatura. Di default, questa operazione converte l'intero testo in minuscolo e rimuove la punteggiatura;
* *tokenizzazione*: si tratta di una procedura di suddivisione delle stringhe in *token*. Ad esempio, si può suddividere una frase nelle singole parole. Di default, questa operazione suddivide i token in base allo spazio;
* *vettorizzazione*: si tratta della procedura di conversione dei token in valori numerici trattabili da un modello di rete neurale. Di default, il metodo di vettorizzazione è `int`.

Questi tre step sono gestiti in automatico da un layer chiamato [`TextVectorization`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TextVectorization).

Procediamo quindi a creare un layer di TextVectorization utilizzando una vettorizzazione *binaria*:

```py
vectorize_layer = TextVectorization(
    max_tokens=VOCAB_SIZE,
    output_mode='binary')
```

In particolare, `max_tokens` permette di stabilire il numero massimo di vocaboli consentiti, mentre l'`output_mode` indica la modalità con cui sarà gestita la sequenza vettorizzat.

A questo punto, occorre creare il dataset che sarà effettivamente passato al primo layer della rete neurale. In tal senso, dobbiamo tenere conto che i dataset che abbiamo creato mediante `text_dataset_from_directory` non sono ancora stati vettorizzati, ed inoltre le singole coppie campione/label *non* sono accessibili mediante le tecniche standard di indicizzazione. Ciò è legato al fatto che le funzioni `*_dataset_from_directory` creano un oggetto di tipo `BatchDataset`, usato da TensorFlow per *ottimizzare* il caricamento in memoria di dataset di grosse dimensioni.

Di conseguenza, dovremo innanzitutto estrarre il testo *senza considerare le singole label*. Per farlo, possiamo usare la funzione `map()` del nostro dataset:

```py
train_text = train.map(lambda text, labels: text)
```

La funzione `map()` non fa altro che applicare all'intero iterabile la funzione passata come argomento. In tal senso, il parametro passato altro non è se non una *lambda function*, ovvero una funzione anonima che assume una forma sintattica del tipo:

```py
lambda args : expression
```

e quindi applica l'espressione a valle dei `:` agli argomenti passati. In questo caso, stiamo semplicemente facendo in modo che tutte le coppie testo/label siano "mappate" sul semplice testo.

Una volta estratto il testo, dovremo chiamare il metodo [`adapt`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/TextVectorization#adapt) del layer di vettorizzazione in modo tale da creare il vocabolario che associ un determinato token numerico a ciascuna stringa.

```py
vectorize_layer.adapt(train_text)
```

Potremo quindi procedere ad integrare il layer di vettorizzazione all'interno del nostro modello.

In tal senso, dovremo assicurarci che il modello abbia un input di forma `(1,)` e tipo stringa, facendo in modo che la rete abbia un'unica stringa in input per ciascun batch:

```py
model.add(
    keras.Input(shape=(1,),
    dtype=tf.string))
```

### 28.1.3 - Array NumPy

Nel caso di un array NumPy, occorre utilizzare il metodo [`from_tensor_slices`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#from_tensor_slices):

```py
train = from_tensor_slices((x_train, y_train))
val = from_tensor_slices((x_test, y_test))
```