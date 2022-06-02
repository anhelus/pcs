# E16 - Apprendimento supervisionato e regressione lineare

## Esercizio E16.1

Proviamo ad operare sul dataset Tips di Seaborn, effettuando una regressione lineare che riguardi le mance ed il conto totale. Per farlo, usiamo un oggetto di classe `LinearRegression()` messo a disposizione dal package `linear_model` di Scikit Learn.

Valutiamo lo score $R^2$ ottenuto, e mostriamo a schermo i risultati dell'interpolazione, assieme al coefficiente angolare ed all'intercetta ottenuti.

## Esercizio E16.2

L'algoritmo RANSAC (RANdom SAmple Consensus) permette di effettuare una regressione in quattro step.

1. Per prima cosa, viene scelto un sottoinsieme dei dati iniziali.
2. Viene stimato un modello a partire dal sottoinsieme considerato nel punto 1.
3. Tutti i dati sono classificati come inlier o outlier sulla base di un valore di soglia.
4. Se il modello ha un numero di outlier *inferiore* a quello estrapolato dal modello all'iterazione precedente, viene aggiornato il "modello migliore", e si passa all'iterazione successiva.

Proviamo ad effettuare poi un'interpolazione mediante un oggetto di classe `RANSACRegression()`, e confrontiamo i risultati ottenuti in precedenza in tre modi:

* tramite un plot;
* valutando lo score;
* valutando i valori di coefficiente ed intercetta del modello usato.

Proviamo infine ad eseguire due volte il RANSAC, e verifichiamo che i risultati ottenuti siano differenti.

!!!note "Soluzione"
    La soluzione a questo esercizio è contenuta in [questo notebook](solution.ipynb).
