# 4.4.1 - Metriche di clustering

Diamo un breve cenno a due tra le metriche utilizzate per la valutazione degli algoritmi di clustering, ovvero il *silhouette score* e l'*adjusted rand index*.

##### Adjusted Rand Index

L'ARI può essere calcolato con la funzione [`adjusted_rand_score()`](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_rand_score.html), che funziona esattamente come le metriche usate per la classificazione e la regressione:

```py
from sklearn.metrics import adjusted_rand_score

adusted_rand_score(labels_pred, labels_true)
```

Da notare che, nonostante venga usata per valutare un algoritmo non supervisionato, l'ARI richieda, nei fatti, la conoscenza delle label associate ai campioni utilizzati.

##### Silhouette score

Il silhouette score è calcolato con la funzione [`silhouette_score()`](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html), che determina il silhouette coefficient di *tutti* i campioni presenti nel dataset. Da notare come questa funzione non richieda la conoscenza delle label "vere", permettendo quindi di stimare lo score a partire dai dati iniziali e dalle label predette dall'algoritmo di clustering:

```py
from sklearn.metrics import silhouette_score

silhouette_score(X, labels_pred)
```

!!!tip "La funzione `silhouette_samples`"
    Scikit-Learn ci offre anche la funzione [`silhouette_samples`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_samples.html#sklearn.metrics.silhouette_samples), che permette di calcolare il silhouette coefficient per ogni singolo campione presente nel dataset iniziale.
