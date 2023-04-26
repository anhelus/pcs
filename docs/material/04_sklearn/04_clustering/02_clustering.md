# 4.4.2 - Clustering in Scikit-Learn

!!!tip "Notebook di accompagnamento"
	Per questa lezione esiste un *notebook di accompagnamento*, reperibile a [questo indirizzo](https://github.com/anhelus/pcs-exercises/blob/master/02_ml/04_clustering/02_clustering.ipynb).

## K-Means

Il più semplice algoritmo di clustering disponibile in Scikit-Learn è il K-Means, implementato mediante l'omonima classe [`KMeans()`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html). Essendo degli stimatori, gli oggetti di questa classe usano i soliti metodi `fit()` e `predict()`:

```py
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

X, y = make_blobs()
clusterer = KMeans()
clusterer.fit(X)
y_pred = clusterer.predict(X)
```

E' possibile settare diversi parametri per il K-Means, tuttavia il più importante è sicuramente `n_clusters`, che indica il valore di $k$ da considerare:

```py
clusterer = KMeans(n_clusters=8)
```

Uno degli attributi più interessanti è sicuramente `labels_`, che restituisce un array indicativo delle label di ciascun campione.

```py
clusterer.labels_
```

!!!note "Mini-batch K-Means"
    Scikit-Learn offre una variante del K-Means che opera su piccoli insiemi di dati, implementata nella classe [`MiniBatchKMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html#sklearn.cluster.MiniBatchKMeans). Il funzionamento di un oggetto di questa classe è concettualmente analogo a quello di oggetti di classe `KMeans()`; tuttavia, in alcuni casi, l'uso dei mini batch può essere utile a ridurre la complessità computazionale, a patto di accettare un lieve calo in termini di performance.

## Clustering gerarchico

In una delle [lezioni precedenti](../../03_ml/07_clustering/lecture.md) abbiamo visto che gli algoritmi di clustering gerarchico vanno a definire un "albero" di cluster annidati, suddividendo cluster all'$i$-mo livello in più cluster al livello $i+1$-mo o, al contrario, agglomerando più cluster all'$i+1$-mo livello in un singolo cluster al livello $i$-mo.

Il clustering gerarchico è implementato in Scikit-Learn mediante la classe [`AgglomerativeClustering`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering). Il funzionamento è concettualmente identico a quello degli altri stimatori; tuttavia, ci sono alcuni parametri di interesse, ovvero:

* `n_clusters`: in questo caso, il parametro `n_clusters` indica il numero di cluster che desideriamo che l'algoritmo individui.
* `compute_full_tree`: questo parametro indica se calcolare o meno l'intera gerarchia di cluster.
* `linkage`: indica la strategia utilizzata per definire se due campioni appartengono ad uno stesso cluster.

In particolare, il criterio di linkage può essere uno tra i seguenti:

* `ward`: questo criterio minimizza la somma dei quadrati delle distanze nei campioni del cluster, in modo simile al criterio di inerzia del K-Means;
* `complete`: questo criterio, chiamato *complete linkage*, definisce un cluster minimizzando la distanza massima tra le osservazioni che lo compongono;
* `average`: questo criterio, chiamato *average linkage*, definisce un cluster minimizzando la distanza media tra le osservazioni che lo compongono;
* `single`: questo criterio, chiamato *single linkage*, definisce un cluster minimizzando la distanza tra le osservazioni più vicine in un cluster.

!!!tip "Costo computazionale"
    Il clustering gerarchico è particolarmente costoso nel caso non vi siano dei particolari vincoli di connettività tra campioni, in quanto deve considerare, ad ogni step, tutte le diverse combinazioni di cluster. Per ridurre questo problema, è possibile usare la variante [`FeatureAgglomeration`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html#sklearn.cluster.FeatureAgglomeration), che raggruppa tra loro feature di valore simile, riducendo il costo computazionale complessivo.

!!!tip "Visualizzazione della gerarchia di cluster"
    E' possibile visualizzare la gerarchia dei cluster definiti da un metodo agglomerativo usando la funzione [`dendrogram`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.dendrogram.html#scipy.cluster.hierarchy.dendrogram) del package SciPy.

## DBSCAN

Anche il DBSCAN ha ovviamente un'implementazione in Scikit-Learn grazie alla classe [`DBSCAN`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN). Da notare come l'algoritmo restituisce anche label di valore `-1`, che contraddistinguono i campioni contrassegnati come *rumorosi* o, per meglio dire, *outlier*.
