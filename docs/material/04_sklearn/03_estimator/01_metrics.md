# 4.3.1 - Metriche di classificazione

Così come per le [metriche di regressione](../02_linear_models/01_metrics.md) e [di clustering](../04_clustering/01_metrics.md) Scikit-Learn mette a disposizione numerose metriche per la valutazione dei risultati di classificazione. Vediamole brevemente.

##### Metriche binarie e multiclasse

In modo simile alle metriche di regressione, alcune delle metriche di classificazione, come ad esempio quelle che riguardano il calcolo di precisione, recall ed F1-score, sono esplicitamente pensate per la classificazione binaria, e presuppongono che la classe positiva sia etichettata con un `1`.  

Di conseguenza, quando si affronta un problema multiclasse, Scikit-Learn tratta "internamente" il problema come una serie di problemi binari del tipo *one-vs-all*, uno per ciascuna classe. Vi è quindi la necessità di specificare il modo con cui il valore complessivo della metrica dovrà essere calcolato mediante il parametri `average`, che può assumere uno tra i seguenti valori:

| Valore del parametro `average` | Breve spiegazione |
| ------------------------------ | ----------------- |
| `macro` | In questa modalità, viene calcolata la media delle singole metriche, dando egual peso a ciascuna classe |
| `weighted` | Tiene conto di eventuali sbilanciamenti del dataset, usando un peso proporzionale alla presenza nel dataset iniziale per ciascun contributo |
| `micro` | Ad ogni coppia *campione-classe* viene dato egual contributo alla metrica complessiva |
| `samples` | |

!!!tip "Metriche per le singole classi"
    Selezionando `average=None` avremo un array di metriche, una per ogni singola classe.

## Accuracy, precisione, recall, F1 score

##### Accuracy

L'accuratezza delle predizioni effettuate da un classificatore è ottenuta in Scikit-Learn utilizzando il metodo [`accuracy_score()`](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html).

Ad esempio:

```py
from sklearn.metrics import accuracy_score

clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

accuracy_score(y_test, y_pred)
```

!!!tip "Top-k accuracy"
    La funzione [`top_k_accuracy_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.top_k_accuracy_score.html#sklearn.metrics.top_k_accuracy_score) è una generalizzazione dell'`accuracy_score` che considera la predizione corretta se viene individuata nei primi `k` punteggi restituiti dall'algoritmo.

##### Precisione

La precisione delle predizioni effettuate da un classificatore è ottenuta in Scikit-Learn utilizzando il metodo [`precision_score()`](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html).

Ad esempio:

```py
from sklearn.metrics import precision_score

precision_score(y_test, y_pred)
```

Da notare che, nel caso di problemi *multiclasse*, sarà necessario specificare il parametro `average`, che ci consente di assegnare a ciascuna classe un "peso" complessivio all'interno del calcolo della precisione globale.

##### Recall

Ovviamente, anche il recall ha una rappresentazione in Scikit-Learn mediante la funzione [`recall_score()`](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html):

```py
from sklearn.metrics import recall_score

recall_score(y_test, y_pred)
```

Anche in questo caso, i problemi multiclasse prevederanno l'utilizzo del parametro `average`.

##### F1 Score

Finiamo la carrellata con la funzione [`f1_score`](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html) che, prevedibilmente, permette di calcolare l'F1 del modello.

```py
from sklearn.metrics import f1_score

f1_score(y_test, y_pred)
```

Così come per precisione e recall, nei problemi multiclasse dovremo usare il parametro `average`.

## Classification report

E' possibile condensare le metriche precedenti utilizzando un unico comando chiamato [`classification_report`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html):

```py
from sklearn.metrics import classification_report

classification_report(y_test, y_pred)
```

## Matrice di confusione

Ricordiamo che una matrice di confusione è una matrice che, dati i valori "veri" sulle righe, e quelli predetti sulle colonne, associa all'elemento in posizione $(i, j)$ il numero di volte in cui il modello ha associato la classe $j$ all'elemento $i$.

!!!note "Matrice di confusione ideale"
    Idealmente, una matrice di confusione dovrebbe essere diagonale. Nella realtà, ci accontentiamo di matrici "per lo più" diagonali.

Scikit-Learn ci permette di calcolare la matrice di confusione come metrica a sè stante mediante il metodo [`confusion_matrix`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html), che restituisce un array rappresentativo della matrice di confusione:

```py
from sklearn.metrics import confusion_matrix

confusion_matrix(y_test, y_pred)
```

##### Visualizzazione della matrice di confusione

Per visualizzare la matrice di confusione abbiamo due strade:

1. passare l'array restituito da `confusion_matrix` ad una heatmap di Seaborn;
2. utilizzare un oggetto di classe [`ConfusionMatrixDisplay`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html).

Nel secondo caso, potremo sia passare la matrice di confusione come parametro all'inizializzatore dell'oggetto di classe `ConfusionMatrixDisplay`, sia utilizzare i metodi `from_estimator`, che calcola la matrice di confusione a partire da stimatore e dataset, e `from_predictions`, che accetta come parametri `y_true` ed `y_pred`.
