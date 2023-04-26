# Esercitazione 4.5

!!!tip "Soluzioni"
	Le soluzioni a questi esercizi sono mostrate nel notebook reperibile a [questo indirizzo](https://github.com/anhelus/pcs-exercises/blob/master/02_ml/05_advanced/exercises.ipynb).

## Esercizio 4.5.1

Creiamo una pipeline di processing che, dati i dati relativi a conto e mance del dataset `tips`, e come label il giorno dello stesso, calcoli l'ARI a valle dell'applicazione di un'operazione di scaling prima dell'algoritmo di clustering. Successivamente, provare a modificare il numero di cluster, ricalcolando l'ARI.

## Esercizio 4.5.2

Usiamo un column transformer per filtrare e pre-elaborare i dati contenuti nel dataset Tips. In particolare:

* assegnamo i dati mancanti;
* scaliamo i dati numerici nel range $[0, 1]$;
* codifichiamo i dati categorici mediante un `OrdinalEncoder()`.

Usiamo il trasformer come step di ingresso ad un multi-layer perceptron, limitandoci a chiamare il metodo `fit()`, e non valutando quindi i risultati.

## Esercizio 4.5.3

Usiamo la grid search per ottimizzare i seguenti parametri del percettrone usato nell'esempio precedente:

* `solver`, tra tutti quelli disponibili;
* `learning_rate_init`, tra $10^{-1}$ e $10^{-5}$, ad ordini di grandezza decrescenti;
* `max_iter`, tra $1000$ e $2000$.

Stampiamo a schermo il miglior punteggio ottenuto, oltre che i parametri del migliore stimatore.

## Esercizio 4.5.4

Integriamo nella pipeline una semplice procedura di feature selection mediante la `VarianceThreshold()`.

## Esercizio 4.5.5

Dato il dataset Diabetes:

1. caricarlo in memoria;
2. visualizzarne e studiarne la struttura mediante un'analisi esplorativa;
3. effettuare un'analisi di correlazione;
4. isolare le $k$ feature più importanti;
5. comparare i risultati in termini di regressione usando un regressore lineare ed un albero decisionale;
6. eseguire una `GridSearchCV` su un albero decisionale, cercando di migliorare le performance in termini di MAPE.

## Esercizio 4.5.6

Dato il dataset Iris:

1. caricarlo in memoria;
2. visualizzarne e studiarne la struttura mediante un'analisi esplorativa;
3. effettuare un'analisi di correlazione;
4. isolare le $k$ feature più importanti;
5. comparare i risultati in termini di regressione usando un regressore logistico ed un albero decisionale;
6. eseguire una `GridSearchCV` su un albero decisionale, cercando di migliorare le performance in termini di accuracy.

## Esercizio 4.5.7

Comparare, per mezzo di due pipeline, i risultati ottenuti effettuando il clustering mediante algoritmo KMeans sui dati di `make_blobs()` con e senza riduzione della dimensionalità.
