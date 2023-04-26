# Esercitazione 4.3

!!!tip "Soluzioni"
	Le soluzioni a questi esercizi sono mostrate nel notebook reperibile a [questo indirizzo](https://github.com/anhelus/pcs-exercises/blob/master/02_ml/03_estimator/exercises.ipynb).

## Esercizio 4.3.1

Operiamo sul problema visto nell'[esercizio 4.2.1](../02_linear_models/exercises.md#esercizio-421) usando un albero decisionale, un random forest ed un multilayer perceptron. Compariamo i risultati in termini di errore quadratico medio usando la funzione [`mean_squared_error`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html) del package `sklearn.metrics`.

## Esercizio 4.3.2

Operiamo sul problema visto nell'[esercizio 4.2.3](../02_linear_models/exercises.md#esercizio-423) usando un albero decisionale, un random forest ed un multilayer perceptron. Compariamo i risultati usando un `classification_report`.

## Esercizio 4.3.3

Esploriamo i risultati ottenuti dall'albero decisionale nell'[esercizio 4.3.2](#esercizio-432). Per farlo, usiamo il metodo [`plot_tree`](https://scikit-learn.org/stable/modules/generated/sklearn.tree.plot_tree.html?highlight=plot_tree#sklearn.tree.plot_tree) del package `sklearn.tree`.

## Esercizio 4.3.4

Proviamo a variare leggermente alcuni parametri per i classificatori ed i regressori usati negli esercizi precedenti. Confrontiamo i risultati ottenuti nei termini delle metriche viste in precedenza.
