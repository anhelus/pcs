# E22 - Scikit Learn: Tips & Tricks

## Esercizio E22.1

Creiamo una pipeline di processing che, dati i dati relativi a conto e mance del dataset `tips`, e come label il giorno dello stesso, calcoli l'ARI a valle dell'applicazione di un'operazione di scaling prima dell'algoritmo di clustering. Successivamente, provare a modificare il numero di cluster, ricalcolando l'ARI.

## Esercizio E22.2

Usiamo un column transformer per filtrare e pre-elaborare i dati contenuti nel dataset Titanic. In particolare, selezioniamo i dati relativi all'età ed alla tariffa dei passeggeri, riempiendo eventuali dati mancanti e scalandoli nel range `[0, 1]`, e codifichiamo i dati relativi alla sopravvivenza, classe, genere e porta di imbarcazione del passeggero mediante un `OrdinalEncoder()` seguito da un imputer. Una volta completato il transformer, usiamolo in una pipeline di clustering.

## Esercizio E22.3

Utilizziamo la tecnica della grid search per automatizzare le prove effettuate in precedenza al variare dei parametri.

## Esercizio E22.4

Utilizziamo la tecnica di feature selection più semplice offerta da Scikit Learn, ovvero [`VarianceThreshold()`](http://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.VarianceThreshold.html), per effettuare una procedura di feature selection sul dataset Titanic. Filtriamo in tal senso tutte le feature con varianza inferiore a 0.5.

!!!note "Soluzione"
    La soluzione a questo esercizio è contenuta in [questo notebook](solution.ipynb).
