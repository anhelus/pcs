# Esercitazione 4.2

!!!tip "Soluzioni"
	Per questi esercizi esiste un *notebook di accompagnamento*, reperibile a [questo indirizzo](https://github.com/anhelus/pcs-exercises/blob/master/02_ml/02_linear_models/exercises.ipynb).

## Esercizio 4.2.1

Proviamo ad operare sul dataset Tips di Seaborn, effettuando una regressione lineare che riguardi le mance ed il conto totale. Per farlo, usiamo un oggetto di classe `LinearRegression()` messo a disposizione dal package `linear_model` di Scikit-Learn.

Valutiamo lo score $R^2$ ottenuto, e mostriamo a schermo i risultati dell'interpolazione, assieme al coefficiente angolare ed all'intercetta ottenuti.

## Esercizio 4.2.2

Proviamo ad effettuare poi un'interpolazione mediante un oggetto di classe `RANSACRegression()`, e confrontiamo i risultati ottenuti in precedenza in tre modi:

* tramite un plot;
* valutando lo score;
* valutando i valori di coefficiente ed intercetta del modello usato.

Proviamo infine ad eseguire due volte il RANSAC, e verifichiamo che i risultati ottenuti siano differenti.

## Esercizio 4.2.3

Continuiamo ad operare sul dataset Tips di Seaborn. In particolare, scegliamo come label il *giorno*, e come feature sulle quali operare il *conto totale*, la *mancia* e la *dimensione del tavolo*. Addestriamo un classificatore a determinare qual è il giorno più probabile sulla base delle feature selezionate.

## Esercizio 4.2.4

Proviamo adesso a verificare come variano i valori di accuratezza, precisione e recall per diversi valori della soglia di decisione. In tal senso:

* semplifichiamo il problema riducendolo ad una classificazione binaria, e quindi considerando come label la colonna `time`;
* utilizziamo il metodo `predict_proba(X)` del `LogisticRegressor()`.

## Esercizio 4.2.5

Consideriamo il regressore lineare usato nell'esercizio 4.2.1. Valutiamo i risultati ottenuti in termini di MSE, MAPE ed $R^2$.
