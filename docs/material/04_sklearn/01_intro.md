# 1 - Una breve introduzione a Scikit LEarn

[Scikit Learn](https://scikit-learn.org/) è una delle librerie per il machine learning tra le più utilizzate in Python. Questo avviene principalmente a causa di tre fattori:

* un esteso supporto ad una grande varietà di algoritmi di machine learning;
* la semplicità di utilizzo della libreria;
* la perfetta integrazione con NumPy e Pandas.

Per iniziare, quindi, diamo una panoramica ad ampio spettro sulle potenzialità della libreria.

!!!note "Installazione di Scikit Learn"
    Ovviamente, prima di inizizare, installiamo la libraria:
    > ```sh
      pip install scikit-learn
      ```

## Stimatori e transformer

Scikit Learn si basa su due concetti fondamentali, ovvero quelli di *stimatore* (*estimator*) e *transformer*.

In particolare, uno stimatore è un oggetto che implementa uno specifico algoritmo di machine learning, mentre un trasformer permette di effettuare delle trasformazioni sui dati. Per esempio, un'istanza della classe [`RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html) è uno stimatore, mentre un'istanza della classe [`StandardScaler`](http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html) è un transformer.

Gli stimatori ed i transformer offrono un'interfaccia comune, la quale offre (nella maggior parte dei casi) i metodi `fit` e `transform` per, rispettivamente, addestrare l'algoritmo (`fit`) ed effettuare le predizioni (`transform`). Tuttavia, è importante notare come ogni stimatore e transformer abbiano parametri specifici e dipendenti dalla natura dell'algoritmo utilizzato; ogni algoritmo, inoltre, andrà verificato secondo delle opportune *metriche*, che permettono di definire, in termini percentuali o assoluti, l'accuratezza dell'algoritmo utilizzato.

!!!tip "OOP in NumPy"
    Gli stimatori derivano tutti da una classe base comune, chiamata [`BaseEstimator`](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html). Questa scelta garantisce l'interfaccia comune accennata in precedenza e, conseguentemente, il rispetto dei principi di [incapsulamento e polimorfismo](../../01_python/02_syntax/05_classes.md). Anche i transformer offrono un'interfaccia comune, basata tuttavia sull'uso del [`TransformerMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.TransformerMixin.html), ovvero di un particolare tipo di classe (detta, per l'appunto, *mixin*) che permette di implementare meccanismi di ereditarietà multipla. 

## Preprocessing

Quando abbiamo [introdotto i concetti alla base del machine learning](../../03_ml/03_data_prep.md), abbiamo visto come sia spesso necessario effettuare una serie di operazioni di preprocessing sui dati. Scikit-Learn offre un gran numero di strumenti per farlo; tra questi, vale la pena ricordarne tre in particolare, ovvero:

* la funzione [`train_test_split`](http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html), utile a suddividere il dataset in un insieme di training ed uno di test;
* gli *imputer* come [`SimpleImputer()`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html) transformer che ci permettono di assegnare eventuali valori mancanti all'interno del dataset;
* i transformer, come il già citato `StandardScaler()`, che permettono di categorizzare e normalizzare i dati.
