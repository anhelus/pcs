# E28 - TensorFlow & Keras: Tips & Tricks

## E28.1

Scarichiamo il dataset *flowers*. Per farlo, usiamo il seguente codice:

```py
import pathlib
from tensorflow import keras

dataset_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
data_dir = keras.utils.get_file(origin=dataset_url,
                            extract=True)
data_dir = pathlib.Path(data_dir).parent
data_dir = pathlib.Path(data_dir, 'flower_photos')
```

Utilizziamo i metodi di Keras per caricare il dataset in memoria ed addestrare un modello per la classificazione di questo tipo:

```bash
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 rescaling_1 (Rescaling)     (None, 150, 150, 3)       0         
                                                                 
 conv_1 (Conv2D)             (None, 148, 148, 32)      896       
                                                                 
 max_pool_1 (MaxPooling2D)   (None, 74, 74, 32)        0         
                                                                 
 conv_2 (Conv2D)             (None, 72, 72, 32)        9248      
                                                                 
 max_pool_2 (MaxPooling2D)   (None, 36, 36, 32)        0         
                                                                 
 dropout (Dropout)           (None, 36, 36, 32)        0         
                                                                 
 flatten_1 (Flatten)         (None, 41472)             0         
                                                                 
 classification (Dense)      (None, 5)                 207365    
_________________________________________________________________
```

Inferiamo il numero di classi del dataset (ovvero la `X` nel precedente sommario) usando l'attributo `class_names` del dataset ottenuto da `image_dataset_from_directory`.

!!!note "Soluzione"
    La soluzione a questo esercizio è contenuta in [questo notebook](solution_1.ipynb).

## E28.2

Utilizziamo gli opportuni callback per terminare l'addestramento del modello visto nell'esercizio 1 dopo 3 epoche nelle quali l'accuracy di validazione non migliora per più di `0.01`. Visualizziamo inoltre i risultati ottenuti in TensorBoard.

!!!note "Soluzione"
    La soluzione a questo esercizio è contenuta in [questo notebook](solution_1.ipynb).

## E28.3

Scarichiamo il dataset *Stack Overflow* mediante il seguente codice:

```py
import pathlib
from tensorflow import keras

dataset_url = "https://storage.googleapis.com/download.tensorflow.org/data/stack_overflow_16k.tar.gz"
data_dir = keras.utils.get_file(origin=dataset_url,
                            extract=True,
                            cache_subdir='datasets/stack_overflow')

data_dir = pathlib.Path(data_dir).parent
train_dir = pathlib.Path(data_dir, 'train')
test_dir = pathlib.Path(data_dir, 'test')
```

Utilizziamo i metodi di Keras per caricare il dataset in memoria ed addestrare un modello per la classificazione di questo tipo:

```bash
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 dense_1 (Dense)             (None, 64)                64064     
                                                                 
 dense_2 (Dense)             (None, 4)                 260       
                                                                 
_________________________________________________________________
```

Usiamo gli stessi callback utilizzati in precedenza.

Inferiamo il numero di classi del dataset (ovvero la `X` nel precedente sommario) usando l'attributo `class_names` del dataset ottenuto da `text_dataset_from_directory`.

!!!note "Soluzione"
    La soluzione a questo esercizio è contenuta in [questo notebook](solution_2.ipynb).


# E26 - Overfitting e regolarizzazione

## Esercizio E26.1

Proviamo ad utilizzare il dataset IMDB movie da Keras per addestrare una rete neurale con la seguente struttura:

```bash
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 input (Dense)               (None, 8)                 8008      
                                                                 
 dense_1 (Dense)             (None, 8)                 72        
                                                                 
 classification (Dense)      (None, 1)                 9         
                                                                
_________________________________________________________________
```

Proviamo ad aggiungere una regolarizzazione ed un dropout sul secondo layer, e compariamo i risultati ottenuti.

!!!note "Soluzione"
    La soluzione a questo esercizio è contenuta in [questo notebook](solution.ipynb).
