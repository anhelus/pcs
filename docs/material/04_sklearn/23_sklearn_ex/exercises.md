# Esercitazione 23

## E23.1

Caricare i dataset Diabetes (a scopo di regressione) ed Iris (a scopo di classificazione). Visualizzarne rapidamente la struttura.

## E23.2

Studiare le feature e la distribuzione delle stesse del dataset Diabetes.

## E23.3

Effettuare un'analisi delle cross-correlazioni presenti tra le feature del dataset Diabetes. Utilizzare il $\tau$ di Kendall.

## E23.4

Isolare le $k$ feature più importanti del dataset Diabetes. Per farlo, utilizzare un oggetto di classe `SelectKBest()` scegliendo la metrica più appropriata tra `mutual_info_regression` e `mutual_info_classif`.

## E23.5

Comparare i risultati di regressione ottenuti da un regressore lineare e da un albero decisionale in termini di MAPE.

## E23.6

Provare ad eseguire una `GridSearchCV` sull'albero decisionale, e valutare se i risultati in termini di MAPE migliorano.

## E23.7

Ripetere gli stessi step degli esercizi precedenti per il dataset Iris.

## E23.8

Comparare, per mezzo di due pipeline, i risultati ottenuti effettuando il clustering mediante algoritmo KMeans sui dati di Iris con e senza feature selection.

!!!note "Soluzione"
    La soluzione a questo esercizio è contenuta in [questo notebook](solution.ipynb).
