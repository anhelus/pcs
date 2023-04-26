# 4.2.3 - Regressione logistica in Scikit-Learn

!!!tip "Notebook di accompagnamento"
	Per questa lezione esiste un *notebook di accompagnamento*, reperibile a [questo indirizzo](https://github.com/anhelus/pcs-exercises/blob/master/02_ml/02_linear_models/03_logistic.ipynb).

La regressione logistica in Scikit-Learn è implementata mediante la classe [`LogisticRegression()`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression), e può essere utilizzata sia in caso di classificazione binaria, sia in caso di classificazione multiclasse.

## Caso binario

Nel caso binario, un oggetto di classe `LogisticRegression()` addestrato su un insieme di dati $X$ restituisce un valore di probabilità $\hat{y}_i$ compreso nell'insieme $[0, 1]$. In particolare, il metodo `predict_proba` predirrà la probabilità della classe positiva $P(\hat{y}_i = 1 | X_i)$ come:

$$
\hat{p}(X_i) = \frac{1}{1 + e^{-X_i w - w_0}}
$$

La funzione obiettivo da minimizzare è data da:

$$
\min_w C \sum_{i=1}^n (-y_i \log(\hat{p}X_i)) - (1-y_i) log (1-\hat{p}(X_i)) + r(w)
$$

con $r(w) termine di regolarizzazione.

## Caso multiclasse

Nel caso multiclasse, invece, il metodo `predict_proba` predice la probabilità per la classe $k$ $P(\hat{y}_i = k | X_i)$ come:

$$
\hat{p}_k(X_i) = \frac{e^{X_i W_k + W_{0,k}}}{\sum_{l=0}^{K-1} e^{X_iW_l + W_{0, l}}}
$$

In questo caso, la funzione obiettivo da minimizzare assume la seguente forma:

$$
\min_W -C \sum_{i=1}^n \sum_{k=0}^{K-1} [y_i = k] \log(\hat{p}_k (X_i)) + r(W)
$$

##### Il parametro `penalty`

Il coefficiente di penalizzazione $r(w)$ può essere uno tra quattro diversi valori specificati al parametro `penalty`, riassunti nella seguente tabella.

| `penalty` | Descrizione | Valore per caso binario | Valore per caso multiclasse |
| --------- | ----------- | ----------------------- | --------------------------- |
| `None` | Non assegna alcuna penalizzazione | $0$ | $0$ |
| `l1_ratio` | Regolarizzazione mediante la norma $l_1$ | $\|w\|_1$ | $\sum_{i=1}^n \sum_{j=1}^K \| W_{i, j}\|$ |
| `l2_ratio` | Regolarizzazione mediante la norma $l_2$ | $\frac{1}{2}\|w\|_2^2 = \frac{1}{2}w^Tw$ | $\frac{1}{2} \|W\|_F^2 = \frac{1}{2} \sum_{i=1}^n\sum_{j=1}^K W_{i,j}^2$ |
| `ElasticNet` | Regolarizzazione mediante una combinazione di norma $l_1$ e norma $l_2$ | $\frac{1-\rho}{2} w^Tw + \rho\|w\|_1$ | $\frac{1-\rho}{2}\|W\|_F^2 + \rho \|W\|_{1,1} |

In particolare, il termine $\rho$ in ElasticNet controlla la forza relativa della regolarizzazione $l_1$ rispetto alla regolarizzazione $l_2$. In pratica, se $\rho=1$, ElasticNet è equivalente ad $l_1$, mentre se $\rho$ è uguale a $0$ allora è equivalente ad $l_2$.

## Esempio di utilizzo

Per utilizzare la regressione logistica dovremo creare uno stimatore di tipo `LogisticRegression()` ed addestrarlo come segue:

```py linenums="1"
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True)
lr = LogisticRegression()
X_train, X_test, y_train, y_test = train_test_split(X, y)
lr.fit(X_train)
y_pred = lr.predict(X_test)
```

In particolare:

* alla riga 5, importiamo il dataset Iris;
* alla riga 6, creiamo il nostro stimatore;
* alla riga 7, suddividiamo i dati in insiemi di training e test;
* alla riga 8, addestriamo il nostro stimatore sull'insieme di training;
* alla riga 9, usiamo lo stimatore addestrato per effettuare le predizioni sui dati di test.
