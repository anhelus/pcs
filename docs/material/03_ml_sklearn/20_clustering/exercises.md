# E20 - Il clustering

## Esercizio E20.1

Il dataset Iris contiene i dati riguardanti lunghezza ed ampiezza di steli e petali per tre classi di fiori, ed è uno dei dataset "standard" per l'analisi dei dati nel machine learning. In tal senso, usiamo il metodo `load_iris` del package `datasets` di Scikit Learn per caricarlo. Una volta caricato in memoria, proviamo ad effettuare un primo clustering usando l'algoritmo k-means con 3 cluster.

## Esercizio E20.2

Verificare il valore di magnitudine e cardinalità per i cluster identificati nell'esercizio precedente.

## Esercizio E20.3

Valutiamo il valore migliore per il numero di cluster da utilizzare per il K-means utilizzando il dataset Iris e l'approccio empirico discusso a lezione. Usiamo valori per il clustering compresi tra 2 e 4.

## Esercizio E20.4

Il K-Means parte da alcune ipotesi sulla natura dei diversi cluster in cui sono organizzati i dati, ovvero che questi siano:

1. *isotropi*, e quindi che abbiano una forma "identica" in tutte le direzioni;
2. *ad eguale varianza*, e quindi che non vi siano dei cluster di varianza sensibilmente superiore o inferiore alla varianza media dell'insieme degli stessi;
3. *ad eguale cardinalità*, e quindi che il numero di campioni per i diversi cluster sia all'incirca costante.

Verifichiamo questi assunti su dati generati dal metodo [`make_blobs()`](http://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html).

!!!note "Note"
    1. Per ottenere l'anisotropia, potete applicare una rotazione all'insieme dei dati. Questa può essere definita in questo modo:
    > ```py
      t = np.tan(np.radians(60))
      rot = np.array([[1, t], [0, 1]])
      X_an = X.dot(rot)
      ```
    2. Per ottenere dei cluster a diversa cardinalità, proviamo a selezionare diversi sottoinsiemi dei dati originari in base al loro valore di `y`.

## Esercizio E20.5

Proviamo ad utilizzare l'algoritmo DBSCAN, implementato mediante la classe [`DBSCAN()`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html) del package `cluster`, nelle tre diverse situazioni ispirate dall'esercizio precedente.

!!!note "Soluzione"
    Le soluzioni a questi esercizi sono contenute in [questo notebook](solution.ipynb).
