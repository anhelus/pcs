# 4.5.1 - Processing pipeline

Finora abbiamo spesso visto i singoli algoritmi di machine learning come blocchi *monolitici* ed a sè stanti. Tuttavia, questo non è quello che accade nella realtà.

Immaginiamo, ad esempio, di dover effettuare un clustering usando il K-Means: come [abbiamo avuto modo di vedere](../04_clustering/02_clustering.md#k-means), l'algoritmo ha dei forti prerequisiti, tra cui la gaussianità dei dati, che ne pregiudicano il funzionamento qualora non rispettati. Potremmo voler quindi utilizzare uno `StandardScaler` per effettuare un'operazione di normalizzazione del nostro dataset, riportandolo a varianza unitaria e media nulla, ed applicando il K-Means ai dati già trasformati.

Portando questo concetto alle sue naturali conseguenze, è abbastanza semplice vedere come non si parla più di algoritmo, ma di *pipeline* di processing, intesa come *insieme di transformer e stimatori da applicare in maniera sequenziale sui dati* per ottenere il risultato atteso. In tal senso, Scikit-Learn ci mette a disposizione un'apposita classe chiamata [`Pipeline()`](http://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html), la quale ci permette per l'appunto di concatenere più algoritmi, senza dover gestire manualmente i risultati intermedi.

Facciamo un esempio. Riprendiamo gli algoritmi di clustering trattati in precedenza, con particolare riferimento al K-Means, per il quale abbiamo illustrato le difficoltà nell'utilizzo in caso di dati non normalizzati. Volendo quindi applicare una standardizzazione ai dati sotto analisi, possiamo usare in cascata un trasformer di classe `StandardScaler` ed un oggetto di tipo `KMeans`:

```py linenums="1"
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

X, y = make_blobs()
scaler = StandardScaler()
X_new = scaler.fit_transform(X)
kmeans = KMeans()
kmeans.fit_predict(X_new)
```

In particolare:

* alla riga 6, l'oggetto `scaler` creato alla riga 5 viene utilizzato per trasformare `X` in `X_new`;
* alla riga 8, l'oggetto `kmeans` viene addestrato su `X_new`.

Ovviamente, questa sintassi è molto prolissa, e può essere facilmente suscettibile ad errori. Usando un oggetto di tipo `Pipeline`, invece, il codice precedente diventa:

```py linenums="1"
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

X, y = make_blobs()

pipe = Pipeline(steps=[
    ('scaler', StandardScaler()),
    ('kmeans', KMeans())
])
pipe.fit_predict(X)
```

Alla riga 8 viene quindi creato un oggetto di tipo `Pipeline` cui vengono passati i singoli algoritmi che lo compongono sotto forma di tuple, ognuna delle quali è a sua volta composta da un identificativo univoco (ad esempio, `scaler` o `kmeans`), oltre che dallo stimatore o trasformer stesso. Conseguentemente, alla riga 12, vediamo un esempio di come è possibile usare una pipeline: molto semplicemente, basta invocare i metodi opportuni (che sono una combinazione tra `fit`, `predict` e `trasform`) sui dati originari.

## Accesso e modifica dei parametri degli stimatori

Sottolineamo come sia possibile accedere ai parametri di ciascuno degli stimatori e dei trasformer presenti all'interno della pipeline al momento della sua creazione. Ad esempio:

```py linenums="1"
pipe = Pipeline(steps=[
    ('scaler', MinMaxScaler(range=(0, 2))),
    ('kmeans', KMeans(n_clusters=3))
])
```

In questo caso, alla riga 2 stiamo creando un `MinMaxScaler` il cui range varia tra $0$ e $2$, mentre alla riga 3 creiamo uno stimatore per il K-Means con `3` cluster.

Possiamo anche modificare successivamente tali parametri a patto di conoscere l'identificativo assegnato all'elemento della pipeline, ed utilizzando congiuntamente il comando `set_params` e la notazione `elemento__parametro`. Ad esempio, per portare il numero di cluster a `4`:

```py
pipe.set_params(kmeans__n_clusters=4)
```

Infine, notiamo che possiamo anche accedere al singolo elemento di una pipeline trattandola come se fosse un dizionario:

```py
pipe['kmeans']
```

e modificarne di conseguenza i parametri.
