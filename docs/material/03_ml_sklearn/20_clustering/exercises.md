# E20 - Il clustering

## Esercizio E20.1

Il dataset Iris contiene i dati riguardanti lunghezza ed ampiezza di steli e petali per tre classi di fiori, ed è uno dei dataset "standard" per l'analisi dei dati nel machine learning. In tal senso, usiamo il metodo `load_iris` del package `datasets` di Scikit Learn per caricarlo. Una volta caricato in memoria, proviamo ad effettuare un primo clustering usando l'algoritmo k-means con 3 cluster.

## Esercizio E20.2

Verifichiamo l'andamento di magnitudine e cardinalità nell'esercizio precedente.

## Esercizio E20.3

Valutiamo il valore migliore per il numero di cluster da utilizzare per il K-means utilizzando il dataset Iris e l'approccio empirico discusso a lezione. Usiamo valori per il clustering compresi tra 2 e 4.

## Esercizio E20.4

Il K-Means parte da alcune ipotesi sulla natura dei diversi cluster in cui sono organizzati i dati, ovvero che questi siano *isotropi*, *ad egual varianza* ed aventi un numero di campioni uniforme. Verifichiamo questi assunti su dati generati dal metodo [`make_blobs()`](http://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html).

!!!note "Nota"
    Questo esercizio si "ispira" ad un tutorial analogo proposto da Scikit Learn.

## Esercizio E20.5

TODO: uso di DBSCAN

!!!note "Soluzione"
    Le soluzioni a questi esercizi sono contenute in [questo notebook](solution.ipynb).
