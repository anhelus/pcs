# Esercitazione 4.4

!!!tip "Soluzioni"
	Le soluzioni a questi esercizi sono mostrate nel notebook reperibile a [questo indirizzo](https://github.com/anhelus/pcs-exercises/blob/master/02_ml/04_clustering/exercises.ipynb).

## Esercizio 4.4.1

Il dataset Iris contiene i dati riguardanti lunghezza ed ampiezza di steli e petali per tre classi di fiori, ed è uno dei dataset "standard" per l'analisi dei dati nel machine learning. In tal senso, usiamo il metodo `load_iris` del package `datasets` di Scikit-Learn per caricarlo. Una volta caricato in memoria, proviamo ad effettuare un primo clustering usando l'algoritmo k-means con 3 cluster.

## Esercizio 4.4.2

Verificare il valore di magnitudine e cardinalità per i cluster identificati nell'esercizio precedente.

## Esercizio 4.4.3

Valutiamo il valore migliore per il numero di cluster da utilizzare per il K-means utilizzando il dataset Iris e l'approccio empirico discusso a lezione. Usiamo valori per il clustering compresi tra 2 e 4.

## Esercizio 4.4.4

Ricreiamo le condizioni sperimentali degli esempi visti nel [notebook che accompagna la lezione](https://github.com/anhelus/pcs-exercises/blob/master/02_ml/04_clustering/02_clustering.ipynb). Stavolta, però, valutiamo le performance di ogni algoritmo utilizzando l'ARI ed il silhouette score.

Inoltre, proviamo a vedere cosa accade per i seguenti parametri:

* per il K-Means, facciamo variare il numero di cluster tra `2` e `5`;
* per il DBSCAN, assegnamo ad $\epsilon$ i valori `0.5` o `1.0`, ed a `min_samples` i valori `5` e `10`.

Per ognuno dei due algoritmi, infine, riportiamo a schermo solo i valori dei parametri per i quali le metriche assumono valore massimo.
