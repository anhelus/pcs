# 4.5.4 - Feature selection

Le tecniche di *feature selection* ci permettono di "isolare" le feature maggiormente significative tra quelle presenti all'interno del nostro dataset, scartando contestualmente le altre.

Il motivo principale per il quale è necessario operare la feature selection è quello di *ridurre la dimensionalità del dataset*, evitando così l'insorgenza di fenomeni indesiderati come quelli correlati alla *curse of dimensionality*.

Scikit-Learn offre diverse tecniche per la feature selection, contenute nel [modulo omologo](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.feature_selection). Vediamone alcune.

## Scartare le feature a bassa varianza

Una prima, semplice tecnica per la feature selection prevede la rimozione delle feature che hanno una bassa varianza. Il motivo di questa scelta è abbastanza facile da intuire: infatti, una feature che assume un valore costante ed uguale per ogni campione non darà alcun contributo ad un modello che provi a discriminare tra una coppia degli stessi.

A tal scopo, Scikit-Learn ci offre i trasformer di classe [`VarianceThreshold`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.VarianceThreshold.html#sklearn.feature_selection.VarianceThreshold), che rimuovono tutte le feature la cui varianza è al di sotto di un valore di soglia determinato dal parametro `threshold`:

```py
from sklearn.feature_selection import VarianceThreshold

sel = VarianceThreshold(threshold=.2)
sel.fit_transform(X)
```

In questo caso, il trasformer eliminerà eventuali feature (colonne) la cui varianza è inferiore alla soglia specificata.

## Feature selection univariata

Le tecniche di feature selection univariata offerte da Scikit-Learn permettono di scegliere le feature da mantenere sulla base di un determinato test statistico. Un esempio di questo trasformer è [`SelectKBest`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html#sklearn.feature_selection.SelectKBest) che, sulla base di un determinato test statistico, restituisce soltanto le $k$ migliori feature.

Ad esempio:

```py linenums="1"
from sklearn.feature_selection import SelectKBest, f_classif

select = SelectKBest(f_classif, k=10)
select.fit_transform(X)
```

In poche parole, il trasformer inizializzato alla riga 3 accetta come test statistico [`f_classif`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.f_classif.html#sklearn.feature_selection.f_classif) (che, in pratica, restituisce l'F-value calcolato secondo un ANOVA), andando a restituire soltanto le migliori $10$ feature.

Esistono anche altri trasformer che implementano feature selection basata su test univariati: un esempio è [`SelectPercentile`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectPercentile.html#sklearn.feature_selection.SelectPercentile), che seleziona soltanto le feature con le performance migliori in base al valore minimo di percentile scelto dall'utente, o classi come [`SelectFpr`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFpr.html#sklearn.feature_selection.SelectFpr), [`SelectFdr`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFdr.html#sklearn.feature_selection.SelectFdr) e [`SelectFwe`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFwe.html#sklearn.feature_selection.SelectFwe). Il funzionamento di ognuno di questi test è praticamente sempre lo stesso; ciò che cambia è il modo in cui vengono selezionate le migliori feature.

## Recursive feature elimination

La tecnica chiamata *recursive feature elimination* (RFE) permette la selezione ricorsiva delle feature più importanti. In pratica, dato uno stimatore che assegna un determinato peso alle sue feature (come ad esempio la regressione logistica o il percettrone), la RFE prevede che lo stesso venga addestrato sull'intero insieme delle feature. Una volta completato l'addestramento, l'importanza di ciascuna feature viene stimata secondo un determinato criterio, e quella a più bassa importanza viene rimossa. A questo punto, lo stimatore viene addestrato sul dataset "ridotto", e la procedura viene reiterata fino a che non si raggiunge il numero desiderato di feature da mantenere.

Scikit-Learn ci offre la classe [`RFE`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html#sklearn.feature_selection.RFE), che accetta come argomenti l'istanza di uno stimatore, oltre che il numero di feature da selezionare, ed il criterio con il quale valutarne l'importanza. Ad esempio:

```py linenums="1"
from sklearn.feature_selection import RFE

select = RFE(
    estimator,
    n_features_to_select=10,
    importance_getter='auto')
```

In particolare, l'attributo `n_features_to_select` definisce il numero di feature da mantenere, mentre `importance_getter` specifica la modalità con cui valutare l'importanza delle singole feature. Se impostato ad `auto`, il trasformer proverà ad inferire automaticamente questo metodo, usando eventuali attributi `coef_` o `feature_importances_` dello stimatore; in alternativa, potrà essere una funzione specificata dall'utente, oppure una stringa che specifica il nome dell'attributo da utilizzare.

!!!tip "`RFE` e `Pipeline`"
    Se usato per effettuare la RFE su di una pipeline, l'attributo `importance_getter` può essere una stringa nella forma `pipeline.clf.feature_importances_`, con `pipeline` nome della pipeline, e `clf` nome dello step di cui recuperare l'attributo `feature_importances_`.
