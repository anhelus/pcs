# 21 - Metriche di clustering

Così come per la regressione e la classificazione, esistono delle metriche appositamente progettate per valutare la qualità dei risultati ottenuti da un algoritmo di clustering. Nello specifico, valuteremo l'*adjusted rand index* ed il *silhouette score*.

## 21.1 - Adjusted Rand Index

Sia $C$ l'insieme dei cluster "veri" assegnati ad un certo dataset, e $K$ l'insieme dei cluster assegnati a valle dell'applicazione di un algoritmo di clustering. Allora definiamo l'indice di Rand come:

$$
RI = \frac{a + b}{C_2^n}
$$

dove:

* $a$ è il numero di coppie di campioni che appartengono allo stesso cluster sia in $C$ sia a valle dell'assegnazione $K$;
* $b$ è il numero di coppie di campioni che *non* appartengono allo stesso cluster sia in $C$ sia a valle dell'assegnazione $K$;
* $C_2^n$ è il numero totale di coppie di campioni presenti nel dataset.

In pratica, se:

$$
s = [s_1, s_2, s_3, s_4, s_5] \\
C = [s_1, s_2], [s_3, s_4, s_5] \\
K = [s_1, s_2, s_3], [s_4, s_5] \\
$$

allora:

$$
a = |(s_1, s_2), (s_4, s_5)| = 2 \\
b = |(s_1, s_4), (s_1, s_5), (s_4, s_2), (s_5, s_2)| = 4 \\
C_2^n = \frac{|s|*|s-1|}{2} = 5 * 2 = 10
$$

Di conseguenza, $RI=\frac{6}{10}=0.6$.

Si può dimostrare non è garantito che l'indice di Rand assuma valore vicino allo zero a seguito di un'assegnazione completamente casuale dei cluster da parte dell'algoritmo.

Possiamo quindi tenere conto dell'aspettazione $E[RI]$ di ottenere un'assegnazione casuale mediante l'*indice di Rand modificato*:

$$
ARI = \frac{RI - E[RI]}{max(RI) - E[RI]}
$$

In Scikit Learn, l'indice di Rand modificato è ottenuto usando la funzione [`adjusted_rand_score()`](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_rand_score.html) del package `metrics`.

Il valore ottimale dell'ARI è pari proprio ad 1, caso in cui il clustering è riuscito a predire correttamente tutte le classi dei singoli campioni. Valori prossimi allo zero o negativi (fino a -1) contraddistinguono invece labeling non corretti.

Una metrica di questo tipo ha l'ovvio vantaggio di essere facilmente interpretabile, oltre che di non essere collegata ad uno specifico algoritmo di clustering. Tuttavia, vi è una criticità indotta dalla necessità di conoscere *a priori* il labeling esatto dei campioni (il che, quindi, potrebbe farci propendere per l'uso di un algoritmo di classificazione).

## 21.2 - Silhouette Score

A differenza dell'ARI, il *silhouette score* non richiede la conoscenza aprioristica delle label vere; per valutare la qualità del clustering, invece, questa metrica si affida a valutazioni sulla separazione dei cluster, ottenendo un valore tanto più alto quanto questi sono tra di loro ben separati e definiti.

In particolare, il silhouete score per un singolo campione è definito come:

$$
s = \frac{b-a}{max(a, b)}
$$

dove:

* $a$ è la distanza media tra un campione e tutti gli altri campioni appartenenti allo stesso cluster;
* $b$ è la distanza media tra un campione e tutti gli altri campioni appartenenti al cluster più vicino.

Questa metrica, implementata grazie alla funzione [`silhouette_score()`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html#sklearn.metrics.silhouette_score) del package `metrics`, è anch'essa di facile interpretazione, in quanto può assumere valori compresi nell'intervallo $[-1, 1]$, con:

* valori prossimi a $-1$ che indicano un clustering non corretto;
* valori prossimi allo $0$ che indicano cluster sovrapposti;
* valori prossimi a $+1$ che indicano cluster densi e ben suddivisi.

Uno svantaggio del silhouette score è che, in generale, può variare in base all'algoritmo utilizzato.
