# 6.1.2 - Dataset

Nella [lezione precedente](01_intro.md) abbiamo visto come il metodo `fit()` accetti i dati sotto forma di array NumPy. Tuttavia, nel momento in cui si ha a che fare con dataset di grosse dimensioni, potrebbe essere necessario usare oggetti specifici appartenenti alla classe [`Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset).

Per farlo, Keras ci mette a disposizione delle tecniche che ci permettono di creare un `Dataset` a partire dai nostri dati; vediamone alcune. 

## Dataset di immagini

Possiamo creare un dataset a partire da una cartella usando la funzione [`image_dataset_from_directory`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/image_dataset_from_directory).

Supponiamo per prima cosa che la cartella `data_dir` sia organizzata come segue:

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

In pratica, i nostri dati sono organizzati in una cartella "madre", all'interno della quale ci sono tante sottocartelle quante sono le classi del nostro problema, ognuna delle quali conterrà a sua volta tutte le immagini per quella specifica classe.

Usiamo adesso la funzione `image_dataset_from_directory` per creare il nostro dataset:

```py linenums="1"
ds = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    image_size=(32, 32),
    batch_size=32)
```

Nel precedente esempio:

* alla riga 2, specifichiamo la cartella dove sono contenuti i dati;
* alla riga 3, specifichiamo il parametro `image_size` sotto forma di tupla, nella quale il primo elemento è l'altezza dell'immagine, mentre il secondo è la larghezza (nel nostro caso, siamo di fronte ad una $32 \times 32$);
* alla riga 4, specifichiamo il parametro `batch_size`, utile in fase di addestramento del modello.

I più attenti si chiederanno se sia possibile caricare il dataset in modo da suddividere automaticamente i dati in insieme di training e di validazione. Ciò è possibile modificando le precedenti istruzioni come segue:

```py linenums="1"
train_ds = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset='training',
    image_size=(img_height, img_width),
    batch_size=batch_size,
    seed=seed)

val_ds = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset='validation',
    image_size=(img_height, img_width),
    batch_size=batch_size,
    seed=seed)
```

In particolare:

* il parametro `validation_split`, che **deve essere coerente** in entrambi i dataset, indica quanti dati usare per la validazione;
* il parametro `subset` indica se il dataset è indirizzato al training o alla validazione;
* il parametro `seed`, che **deve essere coerente** in entrambi i dataset, fa in modo che i dataset siano generati casualmente in modo consistente.

A questo punto possiamo passare `train_ds` e `val_ds` direttamente al metodo `fit()` del nostro modello usando il parametro `validation_data`:

```py
model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=10)
```

## Dataset di testo

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

Per caricare il nostro dataset possiamo usare una forma analoga a quella usata per il dataset di immagini:

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

##### Preparazione dei dati testuali

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

## Dataset da array NumPy

Nel caso di un array NumPy, occorre utilizzare il metodo [`from_tensor_slices`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#from_tensor_slices):

```py
train = from_tensor_slices((x_train, y_train))
val = from_tensor_slices((x_test, y_test))
```
