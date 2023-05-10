
## 28.2 - Callback

Un *callback* è un'azione che il modello può effettuare durante diverse fasi dell'apprendimento.

Keras ne offre di numerosi, che possono essere utilizzati ad esempio per monitorare le metriche che abbiamo scelto per la valutazione del modello, o salvare lo stesso su disco.

Per usare i callback, dovremo crearne una lista, e passarla al parametro `callbacks` usato dal metodo `fit()` del nostro modello.

Proviamo, ad esempio, a creare un insieme di callback che permetta di salvare i pesi del modello con una certa frequenza, e che termini il training se lo stesso sta andando in overfitting.

Per prima cosa, creiamo un oggetto di tipo [`ModelCheckpoint`](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint), che ci permette di salvare i pesi del modello:

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

Proviamo poi a creare un oggetto di tipo [`EarlyStopping`](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/EarlyStopping), che ci permette di terminare l'addestramento qualora la metrica monitorata non presenti miglioramenti tra un'epoca e l'altra. Ad esempio:

```py
es_callback = keras.callbacks.EarlyStopping(
    monitor='val_acc',
    min_delta=0.1,
    patience=3,
    restore_best_weights=True)
```

Nel codice precedente:

* `monitor` indica la metrica da monitorare;
* `min_delta` indica il valore minimo da considerare migliorativo per la metrica;
* `patience` indica il numero di epoche dopo il quale il training viene interrotto in assenza di miglioramenti;
* `restore_best_weights` indica se ripristinare i valori migliori ottenuti per i parametri dopo il termine dell'addestramento, o se usare gli ultimi.

Aggiungiamo infine un ultimo callback, da utilizzare per permettere di visualizzare i risultati del nostro training su un tool di visualizzazione chiamato TensorBoard.

```py
tb_callback = TensorBoard()
```

Per TensorBoard, possiamo lasciare i parametri al loro valore di default. La reference completa è disponibile sulla [documentazione ufficiale](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TensorBoard).

Possiamo adesso specificare i callback da utilizzare passando le precedenti variabili sotto forma di lista al metodo `fit()` del nostro modello.