# 15 - Introduzione a Scikit-Learn

*Scikit-Learn* è una tra le librerie per il machine learning più utilizzate in Python. Ciò avviene principalmente per tre fattori:

* il supporto ad un numero molto elevato di algoritmi di machine learning;
* la semplicità di utilizzo della libreria;
* la perfetta integrazione con NumPy e Pandas.

Partiamo quindi nella nostra discussione sulla libreria da una panoramica ad ampio spettro delle potenzialità della stessa.

Come di consueto, però, la prima cosa da fare è installare la libreria. Per farlo, spostiamoci (eventualmente) nell'ambiente virtuale usato per il corso, ed usiamo il seguente comando:

```sh
pip install scikit-learn
```

## 15.1 - Stimatori e transformer

Scikit Learn si basa su due concetti fondamentali, ovvero quelli di *estimator* (stimatore) e di *transformer* (traducibile maccaronicamente come *trasformatore di dati*).

In particolare, un estimator è l'implementazione di uno specifico algoritmo di machine learning, mentre un transformer è un algoritmo che effettua delle trasformazioni sui dati. Ad esempio, le istanze delle classi [`RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html) e [`DBSCAN`](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html) sono degli estimator, mentre quelle della classe [`StandardScaler`](http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html) sono dei transformer.

Questa suddivisione permette di implementare un'interfaccia comune, la quale offre nella maggior parte dei casi i metodi `fit` e `transform` per, rispettivamente, effettuare l'addestramento e la trasformazione dei dati. Tuttavia, è importante notare come ogni stimatore e transformer abbiano parametri specifici e dipendenti dalla natura dell'algoritmo utilizzato; ogni algoritmo, inoltre, andrà verificato secondo delle opportune *metriche*, che permettono di definire, in termini percentuali o assoluti, l'accuratezza dell'algoritmo utilizzato.

## 17.2 - Preprocessing

Abbiamo visto come spesso sia necessario effettuare delle operazioni di preprocessing sui dati. In tal senso, gli strumenti che utilizzeremo maggiormente saranno tre:

* la funzione [`train_test_split`](http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html), utile a suddividere il dataset in un insieme di training ed uno di test;
* gli *imputer*, transformer che ci permettono di assegnare eventuali valori mancanti all'interno del dataset;
* i transformer veri e propri per le operazioni di categorizzazione e normalizzazione.
