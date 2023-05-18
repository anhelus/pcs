# 6.1.3 - Callbacks

Un **callback** è una specifica azione che il modello può effettuare durante il training. Keras ne offre di numerosi, utilizzati (ad esempio) per monitorare le metriche che abbiamo scelto per la valutazione del modello, o salvare lo stesso su disco.

Per usare uno o più callback, dovremo creare un'apposita lista da passare al parametro omonimo (`callbacks`) nel metodo `fit()` del nostro modello.

## Salvataggio dei pesi del modello

Come primo esempio, creiamo un callback che salvi i pesi del modello con una certa frequenza. Per farlo, useremo un oggetto di tipo [`ModelCheckpoint`](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint):

```py
mc_callback = keras.callbacks.ModelCheckpoint(
    filepath=path_to_checkpoints,
    save_weights_only=True,
    monitor='val_acc',
    save_best_only=True)
```

In particolare:

* `filepath` indica il percorso del file nel quale salveremo i checkpoint;
* `save_weights_only` istruisce Keras a salvare soltanto i pesi del modello, riducendo lo spazio occupato in memoria;
* `monitor` indica la metrica da monitorare;
* `save_best_only` istruisce Keras a salvare soltanto il modello "migliore", trascurando quelli ottenuti durante le altre iterazioni.

## Evitare l'overfitting

Un altro callback interessante è quello che permette di interrompere l'addestramento della rete quando una o più metriche non migliorano per un certo intervallo di epoche. Per farlo, useremo un oggetto di tipo [`EarlyStopping`](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/EarlyStopping), che ci permette di terminare l'addestramento qualora la metrica monitorata non presenti miglioramenti tra un'epoca e l'altra. Ad esempio:

```py
es_callback = keras.callbacks.EarlyStopping(
    monitor='val_acc',
    min_delta=0.1,
    patience=3,
    restore_best_weights=True)
```

In particolare:

* `monitor` indica la metrica da monitorare;
* `min_delta` indica il valore minimo da considerare migliorativo per la metrica;
* `patience` indica il numero di epoche dopo il quale il training viene interrotto in assenza di miglioramenti;
* `restore_best_weights` indica se ripristinare i valori migliori ottenuti per i parametri dopo il termine dell'addestramento, o se usare gli ultimi.

## Visualizzazione dei risultati dell'addestramento

Aggiungiamo infine un ultimo callback, da utilizzare per permettere di visualizzare i risultati del nostro training su un tool di visualizzazione chiamato **TensorBoard**.

```py
tb_callback = TensorBoard()
```

Per TensorBoard, possiamo lasciare i parametri al loro valore di default. La reference completa è comunque disponibile sulla [documentazione ufficiale](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TensorBoard).

## Mettiamo i pezzi insieme...

Possiamo adesso specificare i callback da utilizzare passando le precedenti variabili sotto forma di lista al metodo `fit()` del nostro modello.

```py
callbacks = [mc_callback, es_callback, tb_callback]

model.fit(
    train_ds,
    validation_data=val_ds,
    callbacks=callbacks)
```
