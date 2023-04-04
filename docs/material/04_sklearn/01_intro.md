# 1 - Una breve introduzione a Scikit Learn

!!!tip "Notebook di accompagnamento"
	Per questa lezione esiste un *notebook di accompagnamento*, reperibile a [questo indirizzo](https://github.com/anhelus/pcs-exercises/blob/master/02_ml/01_intro.ipynb).

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
    Gli stimatori derivano tutti da una classe base comune, chiamata [`BaseEstimator`](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html). Questa scelta garantisce l'interfaccia comune accennata in precedenza e, conseguentemente, il rispetto dei principi di [incapsulamento e polimorfismo](../01_python/02_syntax/05_classes.md). Anche i transformer offrono un'interfaccia comune, basata tuttavia sull'uso del [`TransformerMixin`](https://scikit-learn.org/stable/modules/generated/sklearn.base.TransformerMixin.html), ovvero di un particolare tipo di classe (detta, per l'appunto, *mixin*) che permette di implementare meccanismi di ereditarietà multipla. 

## Preprocessing

Quando abbiamo [introdotto i concetti alla base del machine learning](../03_ml/03_data_prep.md), abbiamo visto come sia spesso necessario effettuare una serie di operazioni di preprocessing sui dati. Scikit-Learn offre un gran numero di strumenti per farlo; tra questi, vale la pena ricordarne tre in particolare, ovvero:

* la funzione [`train_test_split`](http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html), utile a suddividere il dataset in un insieme di training ed uno di test;
* gli *imputer* come [`SimpleImputer()`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html) transformer che ci permettono di assegnare eventuali valori mancanti all'interno del dataset;
* i transformer, come il già citato `StandardScaler()`, che permettono di categorizzare e normalizzare i dati.

## Convenzioni

Gli stimatori in Scikit Learn seguono alcune regole; elenchiamone alcune tra le più rilevanti.

##### Type casting

Quando possibile, Scikit Learn fa in modo che i dati di ingresso mantengano il loro tipo; in caso contrario, saranno convertiti in `float64`. Ad esempio:

```py
import numpy as np
from sklearn import kernel_approximation

rng = np.random.RandomState(0)
X = rng.rand(0, 100)
X = np.array(X, dtype='float32')

transformer = kernel_approximation.RBFSampler()
X_new = transformer.fit_transform(X)
X_new.dtype

print(X.dtype)              # Il risultato sarà dtype('float32')
print(X_new.dtype)          # Anche qui, il risultato sarà dtype('float32')
```

In questo esempio, il formato di `X` è `float32`, e possiamo verificare come non cambi dopo la chiamata a `fit_transform(X)`.

!!!tip "Tipo di dati e prestazioni"
    L'uso di dati `float32` è spesso più efficiente rispetto all'uso del formato `float64`, in quanto permette di ridurre i requisiti sia spaziali, sia temporali. Tuttavia, ci potrebbero essere degli errori di troncamento che causando problemi di stabilità numerica.

!!!note "Nota"
    Esistono anche degli stimatori (soprattutto regressori) che lavorano esclusivamente con dati in formato `float64`.

##### Refitting ed aggiornamento dei parametri

I parametri di uno stimatore vengono fissati passando gli opportuni argomenti al costruttore. Tuttavia, questi possono essere successivamente modificati utilizzando il metodo [`set_params()`](https://scikit-learn.org/stable/modules/generated/sklearn.base.BaseEstimator.html#sklearn.base.BaseEstimator.set_params). Tuttavia, per vedere gli effetti dei nuovi valori dei parametri, dovremo provvedere a ri-addestrare il modello. Ad esempio:

```py linenums="1"
X, y = load_iris(return_X_y=True)
clf = SVC()
clf.set_params(kernel='linear').fit(X, y)
clf.predict(X[:10])
clf.set_params(kernel='rbf').fit(X, y)
clf.predict(X[:10])
```

Nel codice precedente:

* alla riga 1, carichiamo il dataset Iris;
* alla riga 2, creiamo uno stimatore di classe [`SVC`](http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html);
* alla riga 3, impostiamo il parametro `kernel` del nostro stimatore a `linear`, e lo addestriamo sui dati a nostra disposizione;
* alla riga 4, effettuiamo la predizione sui primi dieci campioni con i parametri impostati in precedenza;
* alla riga 5, modifichiamo il parametro `kernel`, riaddestrando il modello con il nuovo valore impostato;
* alla riga 6, infine, effettuiamo un'altra predizione, usando il modello appena riaddestrato.

##### Problemi multiclasse vs. problemi multilabel

Un problema si definisce *multiclasse* quando ad ogni campione è possibile associare *una ed una sola* classe tra molte disponibili. Un problema è invece definito come *multilabel* quando ad ogni campione è possibile associare *più di una* tra le classi disponibili.

Ad esempio, classificare un film in base al numero di stelle ricevute può essere interpretato come un problema multiclasse:

| Film | Numero di stelle |
| ---- | ---------------- |
| Jumanji | 5 |
| Il Grinch | 2 |
| La fabbrica di cioccolato | 4 |

Se invece considerassimo il genere a cui ciascun film appartiene, potremmo trovarci di fronte ad una situazione di questo tipo:

| Film | Avventura | Commedia | Fantasy | Crime | Per bambini |
| ---- | --------- | -------- | ------- | ----- | ----------- |
| Jumanji | Vero | Falso | Vero | Falso | Vero |
| Il Grinch | Falso | Vero | Vero | Falso | Vero |
| La fabbrica di cioccolato | Vero | Falso | Vero | Falso | Vero |

In questo caso, avremmo diverse etichette "vere" per ciascun campione, per cui il problema può essere impostato come un multilabel.

Nel caso si voglia affrontare un problema multiclasse, l'apprendimento e la predizione dipendono dal formato dei dati di output:


Quando usiamo un classificatore multiclasse, il task di learning e predizione che viene effettuato è dipendente dal formato dei dati target. Proviamo con un array monodimensionale:

```py
X = [[1, 2], [2, 4], [4, 5], [3, 2], [3, 1]]
y = [0, 0, 1, 1, 2]

clf = OneVsRestClassifier(estimator=SVC(random_state=0))
clf.fit(X, y).predict(X)
```

Il risultato sarà:

```py
array([0, 0, 1, 1, 2])
```

Notiamo quindi come il metodo `predict()` fornisca un array a singola dimensione, nel quale l'$i$-mo elemento è associato alla classe predetta per l'$i$-mo campione. Se invece volessimo effettuare il fitting su un array bidimensionale, dovremmo trasformare `y`, ad esempio mediante un'operazione di *one-hot encoding*:

```py
y = LabelBinarizer().fit_transform(y)
clf.fit(X, y).predict(X)
```

In questo caso, il risultato sarà:

```py
array([[1, 0, 0],
       [1, 0, 0],
       [0, 1, 0],
       [0, 0, 0],
       [0, 0, 0]])
```

Notiamo quindi come `predict()` restituisca un array bidimensionale, nel quale ad ogni riga è associato un campione, con il valore `1` assegnato alla classe predetta, e `0` altrimenti. In altre parole, per il primo campione, il predittore associerà la classe $0$, per il secondo sempre la classe $0$, per il terzo la classe $1$, e via dicendo.

In caso di problema multilabel dovremo usare un [`MultiLabelBinarizer`](http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html):

Notiamo che la quarta e quinta istanza restituiscono tutti zero, il che indica che non combaciano con nessuna delle tre label su cui sono state addestrate. Con gli output multilable, è simile per un'istanza ad avere label multiple:

```py
y = [[0, 1], [0, 2], [1, 3], [0, 2, 3], [2, 4]]
y = MultiLabelBinarizer().fit_transform(y)
clf.fit(X, y).predict(X)
```

Il risultato sarà:

```py
array([[1, 1, 0, 0, 0],
       [1, 0, 1, 0, 0],
       [0, 1, 0, 1, 0],
       [1, 0, 1, 0, 0],
       [1, 0, 1, 0, 0]])
```

Come è possibile vedere, l'array bidimensionale restituito ha diverse label per ogni singola istanza.
