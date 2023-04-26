# 4.2.2 - Regressione in Scikit-Learn

!!!tip "Notebook di accompagnamento"
	Per questa lezione esiste un *notebook di accompagnamento*, reperibile a [questo indirizzo](https://github.com/anhelus/pcs-exercises/blob/master/02_ml/02_linear_models/02_regression.ipynb).

La forma più semplice di regressione in Scikit-Learn è implementata grazie ad una serie di stimatori contenuti nel package `linear_model` della libreria.

Esaminiamone brevemente alcuni, ovvero quello [lineare](#regressione-lineare), [robusto](#regressione-in-caso-di-rumore) e [polinomiale](#regressione-polinomiale).

## Regressione lineare

Gli stimatori di classe [`LinearRegression()`](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html) permettono di effettuare una regressione lineare basandosi sul metodo dei minimi quadrati.

Il funzionamento base di un oggetto di tipo `LinearRegression` è il seguente:

```py linenums="1"
import numpy as np
from sklearn.linear_model import LinearRegression

reg = LinearRegression()
X = np.array([[0, 1, 2]])
y = np.array([[0, 1, 2]])
reg.fit(X, y)
```

In particolare:

* alla riga 4, creiamo un oggetto di classe `LinearRegression()`;
* alle righe 5-6, creiamo due array chiamati `X` ed `y` che saranno usati rispettivamente come variabili *indipendente* e *dipendente*;
* alla riga 7 addestriamo il regressore sugli array creati in precedenza.

Una volta addestrato, il regressore sarà pronto ad effettuare le opportune predizioni mediante il metodo `predict()`:

```py
reg.predict([[5]])
```

##### Accesso ai parametri dello stimatore

Una volta addestrato, un regressore lineare ci offre l'accesso a due parametri, ovvero coefficiente angolare ed intercetta. Questi sono accessibili mediante gli attributi `coef_` ed `intercept_`; ad esempio:

```py
print(f'Coefficiente: {reg.coef_}')
print(f'Intercetta: {reg.incercept_}')
```

!!!tip "Dimensionalità di coefficiente ed intercetta"
    Come ovvio, la dimensionalità di coefficiente ed intercetta dipende dal numero di variabili indipendenti considerate. In altre parole, la regressione lineare non restituisce necessariamente una retta, ma piuttosto un piano interpolante ad $n$ dimensioni, con $n$ numero di variabili indipendenti.

##### Coefficiente di regressione

La classe `LinearRegression()` ci mette a disposizione anche il metodo `score()`, che ci permette di ottenere il coefficiente $R^2$ ottenuto dal modello di regressione. Questo è pari a:

$$
R^2 = (1 - \frac{u}{v})
$$

dove:

* $u$ è pari alla sommatoria dei quadrati dei *residui*, ovvero $\sum (y - y')^2$;
* $v$ è pari alla sommatoria della differenza tra i valori veri ed il valor medio, ovvero $\sum (y - \mu(y))^2$.

Conoscere il valore di $R^2$ è importante per avere un'idea della bontà del modello. Nel caso ideale, infatti, questo valore è $1$, mentre valori inferiori (o addirittura negativi) rappresentano delle possibili criticità del modello.

!!!note "Intervalli di confidenza"
    Scikit-Learn non fornisce un intervallo di confidenza per le predizioni ottenute; più informazioni su questa scelta di design [qui](https://github.com/scikit-learn/scikit-learn/issues/6773). Tuttavia, è possibile implementare questa funzionalità usando NumPy, come descritto [qui](https://datascience.stackexchange.com/questions/41934/obtaining-a-confidence-interval-for-the-prediction-of-a-linear-regression), o in alternativa usare il package Statsmodels.

## Regressione robusta

Nel caso in cui i nostri dati siano "sporchi", può essere utile utilizzare un regressore in grado di minimizzare l'influenza di questi effetti. In particolare, questi algoritmi ci permettono di isolare gli **inlier** dagli **outlier**: i primi, infatti, sono i campioni che afferiscono alla distribuzione "vera" del dato, mentre i secondi sono campioni "esterni" alla stessa.

!!!tip "Esempio pratico"
    Facciamo un banale esempio pratico: in un dataset di cani pastore, la presenza di un chihuahua sarà da considerarsi come un outlier.

Scikit-Learn offre tre tipi di regressore, ovvero il [RANSAC](https://scikit-learn.org/stable/modules/linear_model.html#ransac-regression), il [Theil Sen](https://scikit-learn.org/stable/modules/linear_model.html#theil-sen-regression), e l'[HuberRegressor](https://scikit-learn.org/stable/modules/linear_model.html#huber-regression).

Tra questi, il più utilizzato è certamente il *RANSAC*, crasi di *RANdom SAmple Consensus*. Vediamolo in breve.

##### RANSAC

L'algoritmo RANSAC prevede che il modello sia calcolato a partire da un insieme di inlier casualmente estratti a partire dal dataset iniziale. Il risultato sarà, per l'appunto, un modello lineare che si adatta *esclusivamente* agli inlier, i quali possono essere soggetti a rumore bianco, scartando gli outlier, che si suppone provengano da distribuzioni dei dati differenti.

A differenza di regressori più semplici, come quello lineare, il RANSAC produce risultati non deterministici: in altre parole, il modello garantisce soltanto una certa "percentuale" di efficacia, strettamente dipendente dal numero di iterazioni considerate.

Il RANSAC è un algoritmo puramente iterativo, in cui ogni ciclo si articola in quattro step:

1. Al primo step della $i$-ma iterazione, viene selezionato un certo numero di campioni casuali dal dataset originario, chiamato $S_i$. In Scikit-Learn, questo numero è determinato con il parametro `min_samples`.
2. Al secondo step, si addestra un modello lineare $M_i$ sui dati $S_i$.
3. Al terzo step, si utilizza $M_i$ per calcolare le predizioni su tutti i campioni $S_i$. Se il residuo su ciascuna predizione (ovvero, la differenza tra dato predetto e dato vero) è al di sotto di un certo valore di soglia, il campione è classificato come inlier. In Scikit-Learn, il valore di soglia è determinato dal parametro `residual_threshold`.
4. Il modello $M_i$ viene considerato come "miglior modello" se ha un numero di inlier superiore a quello del modello migliore ottenuto fino a quel momento, che viene quindi aggiornato con $M_i$.

Il numero di iterazioni massime ammesse sul RANSAC è determinato dal parametro `max_trials`. Tuttavia, è possibile anche iterare l'algoritmo soltanto fino a quando non viene rispettato un certo criterio, come il numero di inliers considerati (`stop_n_inliers`) o il punteggio $R^2$ ottenuto (`stop_score`).
