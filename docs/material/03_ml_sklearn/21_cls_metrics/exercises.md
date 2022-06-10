# E21 - Metriche di clustering

## Esercizio E21.1

Ricreiamo le condizioni sperimentali degli esercizi [E20.4](../20_clustering/exercises.md#esercizio-e204) ed [E20.5](../20_clustering/exercises.md#esercizio-e205). Stavolta, però, valutiamo le performance di ogni algoritmo utilizzando l'ARI ed il silhouette score.

Inoltre, proviamo a vedere cosa accade per i seguenti parametri:

* per il K-Means, facciamo variare il numero di cluster tra `2` e `5`;
* per il DBSCAN, assegnamo ad $\epsilon$ i valori `0.5` o `1.0`, ed a `min_samples` i valori `5` e `10`.

Per ognuno dei due algoritmi, infine, riportiamo a schermo solo i valori dei parametri per i quali le metriche assumono valore massimo.

!!!note "Soluzione"
    La soluziona a questo esercizio è contenuta in [questo notebook](solution.ipynb).
