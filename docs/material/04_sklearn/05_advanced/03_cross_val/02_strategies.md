# 4.5.3.2 - Strategie di cross-validazione

Abbiamo accennato al fatto che esistono diverse strategie di cross-validazione. In tal senso, Scikit-Learn offre delle utility per ciascuna di queste strategie; vediamole brevemente.

## K-Fold

La K-Fold cross-validation suddivide i campioni in $k$ gruppi di dimensione uguale (laddove possibile). Il modello viene quindi addestrato su $k-1$ gruppi, ed il restante è usato come test. Scikit-Learn usa la classe [`KFold()`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html#sklearn.model_selection.KFold) per questa strategia di cross-validazione:

```py
from sklearn.model_selection import KFold

kf = KFold(n_splits=2)
kf.split(X)
```

## Repeated K-Fold

Come suggerisce il nome stesso, questa strategia ripete la K-Fold classica per un certo numero di volte, con diverse suddivisioni ad ogni ripetizione. In tal senso, Scikit-Learn offre la classe [`RepeatedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RepeatedKFold.html#sklearn.model_selection.RepeatedKFold):

```py
from sklearn.model_selection import RepeatedKFold

rkf = RepeatedKFold(n_splits=2, n_repeats=2)
rkf.split(X)
```

## Stratified K-Fold

La K-Fold classica opera in maniera *indipendente* dalle classi: in pratica, non tiene conto della distribuzione delle label nel dataset iniziale. La *stratified* K-Fold, invece, restituisce degli insiemi nei quali è contenuta approssimativamente la stessa percentuale di campioni di ogni classe target del set completo. Anche in questo caso, viene offerta una funzione apposita da Scikit-Learn, chiamata [`StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html#sklearn.model_selection.StratifiedKFold):

```py
from sklearn.model_selection import StratifiedKFold

skf = StratifiedKFold(n_splits=2)
skf.split(X)
```
