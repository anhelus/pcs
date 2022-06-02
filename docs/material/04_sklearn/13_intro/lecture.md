# 13 - Introduzione a Scikit-Learn

*Scikit-Learn* è una tra le librerie per il machine learning più utilizzate in Python. Ciò avviene principalmente per tre fattori:

* il supporto ad un numero molto elevato di algoritmi di machine learning;
* la semplicità di utilizzo della libreria;
* la perfetta integrazione con NumPy e Pandas.

Partiamo quindi nella nostra discussione sulla libreria da una panoramica ad ampio spettro delle potenzialità della stessa.

Come di consueto, però, la prima cosa da fare è installare la libreria. Per farlo, spostiamoci (eventualmente) nell'ambiente virtuale usato per il corso, ed usiamo il seguente comando:

```sh
pip install scikit-learn
```

## 17.1 - Stimatori e transformer

Scikit Learn si basa su due concetti fondamentali, ovvero quelli di *estimator* (stimatore) e di *transformer* (traducibile maccaronicamente come *trasformatore di dati*).

In particolare, un estimator è l'implementazione di uno specifico algoritmo di machine learning, mentre un transformer è un algoritmo che effettua delle trasformazioni sui dati. Ad esempio, le istanze delle classi [`RandomForestClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html) e [`DBSCAN`](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html) sono degli estimator, mentre quelle della classe [`StandardScaler`](http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html) sono dei transformer.

Questa suddivisione permette di implementare un'interfaccia comune, la quale offre nella maggior parte dei casi i metodi `fit` e `transform` per, rispettivamente, effettuare l'addestramento e la trasformazione dei dati. Tuttavia, è importante notare come ogni stimatore e transformer abbiano parametri specifici e dipendenti dalla natura dell'algoritmo utilizzato; ogni algoritmo, inoltre, andrà verificato secondo delle opportune *metriche*, che permettono di definire, in termini percentuali o assoluti, l'accuratezza dell'algoritmo utilizzato.

## 17.2 - Preprocessing



### Preprocessing

Molto spesso, è necessario effettuare delle operazioni di preprocessing (**mai usare preprocessamento**) sui dati. Questo perché questi possono essere viziati dall'assenza di valori in determinati ambiti, oppure è necessario scalarli. Scikit-Learn offre un intero package dedicato a questo.

Le funzioni che utilizzeremo maggiormente saranno:

* `train_test_split`, per suddividere il dataset in un insieme di training ed uno di test;
* gli *Imputer*, per assegnare eventuali valori mancanti all'interno del dataset;
* i *Transformer*, che ci permettono di modificare il tipo dei dati.

### Pipeline

Accenniamo in ultimo al fatto che, normalmente, è necessario *concatenare* diversi stimatori. Per farlo, Scikit-Learn ci mette a disposizione un'apposita struttura chiamata `Pipeline`, che approfondiremo nelle prossime lezioni.

<!-- TODO: da qui revisione -->

### Train, test e cross-validazione

Apprendere i parametri di uno stimatore e testarlo sugli stessi dati è un errore metodologico: un modello che infatti si limitasse a ripetere le label dei campioni che ha appena visto avrebbe un punteggio perfetto, ma non sarebbe in grado di predire qualcosa di utile su dati non ancora visti. Questa situazione è comunemente chiamata **overfitting**. Per evitare l'overfitting, nei metodi supervisionati, si usa "lasciar fuori" parte dei dati disponibili e chiamarla *set di test*. La funzione principe per questo in scikit learn è train_test_split.

<!-- TODO: questo deve essere spostato in una sezione relativa agli iperparametri -->

Tuttavia, può essere anche possibile che si debbano valutare diversi iperparametri per un singolo stimatore. Il concetto di iperparametro è analogo a quello di configurazione, e non sono chiamati parametri per evitare di generare confusione con i parametri che vengono configurati internamente da uno stimatore durante l'apprendimento.

Quando valutiamo diverse combinazioni di iperparametri, è possibile che vi sia un overfitting verso il test set, perché potremmo voler ritarare i parametri in modo da ottenere delle performance di validazione quanto migliori possibile. In questo modo, è possibile che il meccanismo di generazione dei dati caratteristico del test set possa "fuoriuscire" all'interno del modello, causando conseguentemente un peggioramento delle capacità di generalizzazione. Per risolvere questo problema, ogni parte del dataset può essere messa fuori in quello che viene chiamato *set di validazione*: il training avviene sul set di raining, la cui valutazione avviene sul set di valudazione,e  quando l'esperimento sembra aver successo, la valutazione finale può essere fatta sul set di test.

Ad ogni modo, il partizionamento in questo modo riduce drasticametne il numero di campioni che può essere usato per apprendere il modello, ed i risultati possono dipende da una scelta casuale dalla coppia degli insieme (train, validazione).

Una soluzione di questo problema è una procedura chiamato cross-validazione. Un set test deve essere sempre tenuto da parte per una valutazione finale, ma non è necessario il test di validazione. In questo approccio base, chiamato k-fold CV, il set di training è suddiviso in k set più piccoli. La procedura è la seguente:

* un modello viene addestrato usando $k - 1$ dei fold come training data;
* il modello risultante è validato sulla parte rimanente dei dati (ovvero è usato come test set per calcolare una misura di performacnce come l'accuracy.)

La misura di performance restituita dai k-fold è quindi la media dei valori calcolati nel ciclo.
