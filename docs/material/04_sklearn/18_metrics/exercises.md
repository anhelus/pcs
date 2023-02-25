# E18 - Metriche

## Esercizio E18.1

Consideriamo il regressore logistico usato nell'[esercizio 17.1](../17_logistic/exercises.md). Valutiamo per prima cosa i risultati ottenuti in termini di accuratezza, precisione e recall usando le apposite funzioni di Scikit Learn. Utilizziamo anche la funzione `classification_report()` per ottenere un report completo dell'esito del classificatore.

## Esercizio E18.2

Proviamo adesso a verificare come variano i valori di accuratezza, precisione e recall per diversi valori della soglia di decisione. In tal senso:

* semplifichiamo il problema riducendolo ad una classificazione binaria, e quindi considerando come label la colonna `time`;
* utilizziamo il metodo `predict_proba(X)` del `LogisticRegressor()`.

## Esercizio E18.3

Consideriamo il regressore lineare usato nell'[esercizio 16.1](../16_lin_reg/exercises.md). Valutiamo i risultati ottenuti in termini di MSE, MAPE ed $R^2$.

!!!note "Soluzione"
    La soluzione a questo esercizio è contenuta in [questo notebook](solution.ipynb).