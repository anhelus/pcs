# 3.8.2 - Metriche di regressione

La valutazione di un modello di regressione avviene utilizzando delle metriche differenti rispetto a [quelle usate per un modello di classificazione](01_classification.md). Vediamone brevemente alcune.

## Errore di regressione

##### Mean Squared Error

L'*errore quadratico medio*, o *mean squared error* (MSE), è una metrica comunemente utilizzata per la valutazione delle performance di regressione, ed è definito come:

$$
MSE = \frac{1}{n} \sum_{i=1}^n (y_i-\hat{y}_i)^2
$$

L'MSE permette di eliminare l'influenza del segno dell'errore, valutandone esclusivamente il modulo. Tuttavia, è estremamente sensibile all'entità dello stesso: infatti, un errore dell'$1\%$ su un valore $y=100$ sarà più influente di un errore del $50\%$ su un valore $y=1$.

Ovviamente, tanto minore è l'MSE, tanto è migliore il modello considerato.

##### Mean Absolute Error

L'*errore assoluto medio*, o *mean absolute error* (MAE) rappresenta il valore atteso dell'errore assoluto o, equivalentemente, della norma $l1$.

Se $\hat{y}_i$ è il valore predtto per l'$i$-mo campione, ed $y_i$ è il corrispondente valore "vero", allora il MAE calcolato su $N$ campioni è dato da:

$$
MAE(y, \hat{y}) = \frac{1}{N} \sum_{i=0}^{N-1} | y_i - \hat{y}_i |
$$

##### Mean Absolute Percentage Error

Il *mean absolute percentage error* (MAPE) viene calcolato a partire dal rapporto tra il valore assoluto della differenza tra i valori veri e quelli predetti dal regressore e i valori veri stessi. Tale rapporto viene quindi mediato sull'insieme dei campioni, e ne viene dedotta la percentuale. La formula è la seguente:

$$
MAPE = \frac{1}{n} \sum_{i=1}^n \frac{|y_i - \hat{y}_i|}{max (\epsilon, y_i)} \%
$$

Anche nel caso del MAPE, l'utilizzo del valore assoluto elimina gli annullamenti non desiderati derivanti da errori di segno opposto. Inoltre, la presenza del valore vero a denominatore fa in modo che la metrica sia sensibile all'entità relativa dell'errore.

Anche in questo caso, un valore di MAPE basso indica un'ottima approssimazione.

## Metriche statistiche

##### Coefficiente di determinazione

Il valore $R^2$ determina la proporzione della varianza del valore vero che viene spiegata dal modello. In pratica, ci permette di definire quanta della variabilità del fenomeno (ovvero, del modo in cui il fenomeno combina le $n$ variabili indipendenti per ottenere le $m$ variabili dipendenti) viene correttamente caratterizzata attraverso il modello considerato.

Il valore di $R^2$ può oscillare tra $1$ e $- \infty$, ovvero tra la modellazione completa dell'intera variabilità del fenomeno ed un modello totalmente incorrelato allo stesso. Analiticamente, $R^2$ è definito come:

$$
R^2 = 1 - \frac{\sum_{i=1}^n (y_i - \hat{y_i})^2}{\sum_{i=1}^n (y_i-avg(y_i))}
$$

con:

$$
avg(y_i) = \frac{1}{n} \sum_{i=1}^n y_i
$$

##### Varianza spiegata

La *varianza spiegata* è definita come segue:

$$
EV(y, \hat{y}) = 1 - \frac{\sigma \{y - \hat{y}\}}{\sigma \{y\}}
$$

dove $\hat{y}$ è il valore predetto per la variabile indipendente, $y$ è il valore vero, e $\sigma$ è la varianza.

##### Differenze tra $R^2$ e varianza spiegata

La differenza tra $R^2$ e la varianza spiegata sta nel fatto che quest'ultima non tiene conto di errori sistematici presenti nelle predizioni; di conseguenza, è preferibile usare $R^2$ ove possibile. Inoltre, nel caso in cui la variabile indipendente sia costante, il valore numerico della varianza spiegata non è un valore reale: può essere infatti `NaN`, in caso di predizioni perfette, o $- \infty$, in caso di predizioni imperfette.

!!!note "Varianza spiegata in Scikit-Learn"
    A causa dell'ultimo fattore, in Scikit-Learn la varianza spiegata assume valore compreso tra $1$ e $0$ proprio per evitare l'insorgenza di problematiche durante la validazione delle performance.