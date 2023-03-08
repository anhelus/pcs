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
