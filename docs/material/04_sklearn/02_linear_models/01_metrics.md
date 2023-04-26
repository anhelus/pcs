# 4.2.1 - Metriche di regressione

Il modulo [`metrics`](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics) offre numerose metriche per la valutazione delle performance di regressione, alcune delle quali possono gestire la regressione multivariata.

In particolare, le metriche che offrono il parametro `multioutput` permettono di specificare il modo in cui mediare i contributi associati alle diverse variabili dipendenti. Il valore di default di questo parametro è `uniform_average`, che fa in modo che sia utilizzata una media pesata. In alternativa, è possibile passare un array di pesi, oppure utilizzare il valore `raw_values`, che fa in modo che nel computo complessivo della metrica siano utilizzati i punteggi non mediati.

## Errore di regressione

##### Mean Squared Error (MSE)

Il valore di MSE è ottenuto usando la funzione [`mean_squared_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error). Ad esempio:

Il loro utilizzo è sempre del tipo:

```py
from sklearn.metrics import mean_squared_error

# ...

mse = mean_squared_error(y_true, y_pred)
```

##### Mean Absolute Error (MAE)

Il MAE può essere ottenuto usando la funzione [`mean_absolute_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html#sklearn.metrics.mean_absolute_error):

```py
from sklearn.metrics import mean_absolute_error

# ...

mae = mean_absolute_error(y, y_pred)
```

##### Mean Absolute Percentage Error (MAPE)

Il valore del MAPE può essere ottenuto usando la funzione [`mean_absolute_percentage_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_percentage_error.html):

```py
from sklearn.metrics import mean_absolute_error

# ...

mape = mean_absolute_error(y, y_pred)
```

## Metriche statistiche

##### Coefficiente di determinazione $R^2$

Abbiamo visto che una delle metriche più utilizzate è il coefficiente di determinazione $R^2$, che può variare tra $- \infty$, in quanto il modello può commettere errori potenzialmente "infiniti", ed $1$, ottenuto quando il modello aderisce perfettamente ai dati.

Per quantificare il coefficiente di determinazione, Scikit-Learn offre la funzione [`r2_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score). Questa funzione è utilizzabile come segue:

```py
from sklearn.metrics import r2_score

# Caricamento di modello e dati...
rgr.fit(X_true, y_true)
y_pred = rgr.predict(X_true)

r2 = r2_score(y_true, y_pred)
```

!!!note "Regressione multivariata"
    La funzione `r2_score` può essere usata anche in caso di regressione multivariata. In questo caso, oltre ai possibili valori indicati in precedenza, il parametro `multioutput` accetta anche il valore `variance_weighted`, che pesa ciascun punteggio per la varianza della corrispondente variabile target. In pratica, utilizzare questa modalità fa sì che le variabili a maggiore varianza abbiamo maggiore importanza nella quantificazione della metrica.

##### Varianza spiegata

In modo del tutto analogo alle altre metriche, la varianza spiegata è calcolata usando la funzione [`explained_variance_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.explained_variance_score.html):

```py
from sklearn.metrics import explained_variance_score

# ...
ev = explained_variance_score(y_true, y_pred)
```
