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

DA QUI

Questa suddivisione permette di implementare un'interfaccia comune, la quale offre nella maggior parte dei casi i metodi `fit` e `transform` per, rispettivamente, effettuare l'addestramento e la trasformazione dei dati. Tuttavia, è importante notare come ogni stimatore e transformer abbiano parametri specifici e dipendenti dalla natura dell'algoritmo utilizzato; ogni algoritmo, inoltre, andrà verificato secondo delle opportune *metriche*, che permettono di definire, in termini percentuali o assoluti, l'accuratezza dell'algoritmo utilizzato.

## 15.2 - Preprocessing

Abbiamo visto come spesso sia necessario effettuare delle operazioni di preprocessing sui dati. In tal senso, gli strumenti che utilizzeremo maggiormente saranno tre:

* la funzione [`train_test_split`](http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html), utile a suddividere il dataset in un insieme di training ed uno di test;
* gli *imputer* come [`SimpleImputer()`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html) transformer che ci permettono di assegnare eventuali valori mancanti all'interno del dataset;
* i transformer veri e propri per le operazioni di categorizzazione e normalizzazione.
