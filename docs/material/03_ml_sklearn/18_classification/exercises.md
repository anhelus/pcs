# E18 - Accuratezza, precisione e recall

## Esercizio E18.1

Consideriamo il regressore logistico usato nell'[esercizio 17.1](../17_logistic/exercises.md). Valutiamo per prima cosa i risultati ottenuti in termini di accuratezza, precisione e recall usando le apposite funzioni di Scikit Learn. Utilizziamo anche la funzione `classification_report()` per ottenere un report completo dell'esito del classificatore.

Proviamo poi a verificare l'andamento dei valori di accuratezza, precisione e recall per diversi valori della soglia di decisione. In tal senso, utilizziamo il metodo `predict_proba(X)` del `LogisticRegressor()`.

!!!note "Soluzione"
    La soluzione a questo esercizio è contenuta in [questo notebook](solution.ipynb).