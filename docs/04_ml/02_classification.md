# Il problema della classificazione

Come suggerisce il termine stesso, il problema della *classificazione* viene risolto assegnando ad un determinato campione di una *classe*, da non intendersi (ovviamente!) nel senso prettamente informatico del termine, ma piuttosto come un insieme di proprietà che permette di contraddistinguere dati con caratteristiche differenti. Per questo motivo, la classificazione è (spesso) approcciata in maniera *supervisionata*, facendo sì che un *esperto di dominio* contrassegni un insieme di valori, chiamati *label*, mediante la procedura di *labeling*.

## Tipi di problema

Esistono diversi tipi di approcci alla classificazione, tutti contraddistinguibili in base al numero di classi e label. Diamo un breve sguardo.

### Binaria

Un problema di classificazione *binario* riguarda soltanto due possibili output, che di solito vengono indicati con *vero* o *falso*. Un tipico esempio è quello del riconoscimento dell'identità di una persona dal suo volto, nel quale il sistema di intelligenza artificiale restituisce *vero* se il volto è correttamente riconosciuto, e *falso* altrimenti.

### Multi-classe

Tutti i problemi che prevedono più di due classi sono chiamati *multi-classe*, e sono tra quelli più diffusi in ambiti come la computer vision e l'analisi dei dati. Rimanendo all'interno dell'ambito dell'elaborazione delle immagini, un esempio di problema multi-classe sta nel riconoscimento del tipo di oggetto inquadrato in una foto, che può appartenere ad un numero molto elevato di classi (ad esempio, auto, smartphone, animali, etc.).

### Multi-label

TODO

## Metriche

Di seguito, elencheremo soltanto *alcune* delle metriche che è possibile utilizzare nei problemi di classificazione.

### Accuracy

L'accuracy è definita come una misura dell'errore introdotto dal sistema di classificazione nella corretta identificazione della classe di un campione, valutata sull'intero set di test.

Ad esempio, se il nostro classificatore ha un output di questo tipo:

$$
\hat{y} = [1, 1, 2, 1, 2]
$$

mentre le classi "vere" sono definite dal seguente vettore delle label:

$$
y = [1, 1, 1, 2, 2]
$$

allora l'accuracy è data da:

$$
acc(y, \hat{y}) = \frac{i}{n} \sum_{i=0}^{n-1} 1(\hat{y_i} = y_i)
$$

In altri termini, l'accuracy è data dal rapporto tra la somma del numero di campioni per i quali il predittore è in grado di riconoscere correttamente la classe ed il numero totale dei campioni stessi.

Nell'esempio precedente, appare chiaro come:

$$
acc(y, \hat{y}) = \frac{1}{5} * 3 = \frac{3}{5} = 0.6
$$

Per calcolare l'accuracy dei risultati ottenuti dal nostro predittore, Scikit-Learn ci mette a disposizione un'apposita funzione chiamata `accuracy_score`. Ad esempio:

```py
from sklearn.metrics import accuracy_score
y_true = [1, 1, 1, 2, 2]
y_pred = [1, 1, 2, 1, 2]
accuracy_score(y_true, y_pred)
```

### Recall

Il *recall* è una stima del rapporto tra *veri positivi*, ovvero il numero di campioni che il classificatore è in grado di associare correttamente ad una classe, e *falsi negativi*, ovvero il numero di campioni che il classificatore non associa ad una determinata classe, sbagliando. Analiticamente:

$$
R = \frac{TP}{(TP + FN)}
$$

In altri termini, il recall può essere considerato come una stima dei campioni che il classificatore riesce ad associare correttamente ad una classe rispetto al numero totale di quelli *effettivamente* appartenenti alla stessa.

Ovviamente, il valore del recall sarà tanto più vicino ad uno quanto il valore di $FN$ tenderà a zero, mentre sarà tanto più vicino a $0$ quanto più $TP$ sarà piccolo. Ad esempio:

$$
TP = 10; \\
FN = 5; \\
R = \frac{TP}{(TP + FN)} = \frac{10}{15} ~= 0,67
$$

Anche in questo caso, Scikit-Learn ci mette a disposizione una funzione chiamata `recall_score` mediante la quale calcolare questa metrica.

```py
from sklearn.metrics import recall_score
recall_score(y_true, y_pred)
```

!!!tip "Il parametro `average`"
    La funzione `recall_score` accetta un parametro che, di primo acchitto, potrebbe passare inosservato, ovvero `average`. Questo è in realtà molto importante, in quanto deve essere impsotato in base alle specifiche del problema sotto osservazione. Così, in caso di classificazione binaria, dovremo usare `average='binary'`, specificando anche la classe sulla quale ci interessa calcolare il recall; nel caso di classi non bilanciate, invece, potremmo preferire la modalità `'macro'` alla modalità `'micro'`.

### Precision

Simile al recall è la *precision*, calcolata questa volta usando la seguente formula:

$$
R = \frac{TP}{(TP + FP)}
$$

dove $FP$ è il numero di *falsi positivi*, ovvero dei campioni che il classificatore reputa erroneamente appartenenti ad una certa classe. La precision può quindi essere descritta come la capacità del classificatore di non assegnare una certa classe a campioni appartenenti ad un'altra.

Per la precision valgono esattamente le stesse considerazioni fatte per il recall; l'unica differenza sostanziale, oltre quella "semantica", sta nel fatto che viene calcolata usando la funzione `precision_score`:

```py
from sklearn.metrics import precision_score
precision_score(y_true, y_pred)
```

### Matrice di confusione

Un altro modo di rappresentare i risultati ottenuti da un classificatore è quello di usare una *matrice di confusione*.

La definizione di una matrice di confusione $C$ è tale che $C_{i,j}$ sia uguale al numero di osservazioni che sono nel gruppo $i$, ma che vengono predette dal classificatore nel gruppo $j$.

```py
from sklearn.metrics import confusion_matrix
confusion_matrix(y_true, y_pred)
```

Possiamo visualizzare a schermo la matrice di confusione usando una heatmap di Seaborn.

## Algoritmi di classificazione

Scikit-Learn offre un gran numero di metodi di classificazione. Nel seguito, ne descriviamo alcuni, non in ordine di importanza, né di utilità.

### Alberi decisionali

Comprendere il funzionamento di un albero decisionale è abbastanza semplice. L'obiettivo di un albero decisionale è quello di creare un modello che predica il valore di una variabile obiettivo imparando delle semplici regole decisionali apprese a partire dalle feature dei dati. In pratica, possiamo pensare ad un albero come ad un percorso "a step", nel quale ad ogni step vi è un'approssimazione successiva verso il risultato finale.

Vediamo un esempio grafico.

![decision_tree](../assets/images/04_ml/0x_classification/decision_tree.jpg)

Questo esempio mostra le possibilità di sopravvivenza individuate tra i passeggeri del Titanic, assieme alle percentuali di questi sul totale. La suddivisione che viene subito all'occhio è la seguente:

* il 36% dei passaggeri era donna;
* il 60% uomo di età superiore ai 9 anni e 6 mesi;
* il 4% uomo di età inferiore ai 9 anni e 6 mesi.

L'albero invece ci dice che sono sopravvissuti:

* il 73% delle donne;
* il 17% degli uomini con più di 9 anni e 6 mesi;
* il 2% degli uomini con meno di 9 anni e 6 mesi, con *più* di tre fratelli;
* l'89% degli uomini con meno di 9 anni e 6 mesi, con *meno* di tre fratelli.

!!!tip "Suggerimento"
    Qualora troviate una Delorean con la data puntata al 15 aprile 1912, assicuratevi di essere donna o di essere figli unici con meno di nove anni.

Gli alberi decisionali possono essere usati sia come classificatori, sia come regressori; in questa lezione, ci concentreremo sull'uso come classificatori.

```py
from sklearn.tree import DecisionTreeClassifier
x = np.random.random_integers(0, 10, size=(100, 1))
y = np.random.random_integers(0, 2, size=(100))

clf = DecisionTreeClassifier()
clf = clf.fit(x, y)

clf.predict(np.random.random_integers(0, 2, size=(100)))
```

Una volta terminato l'addestramento, possiamo visualizzare l'albero mediante la funzione `plot_tree`:

```py
from sklearn import tree

tree.plot_tree(clf)
```

Il risultato sarà simile a quello mostrato in figura:

TODO: FIGURA

## Metodi ensemble

L'obiettivo dei metodi ensemble è combinare le predizioni di diversi stimatori di base con un dato algoritmo di apprendimento per migliorare la generalizzabilità / robustezza di un singolo stimatore.

Due famiglie di metodi ensemble sono normalmente idnividuati:

* nei metodi averaging, il principio guida è quello di costruei diversi stimatori indipendenti e quindi mediare le loro predizioni. In media, gli stimatori combinati sono di solito migliori di uno qualsiasi dei singoli stimatori base perché ne viene ridotta la varianza.

* di contrasto, nei metodi di boosting, gli stimatori di base sono costruiti in maniera sequenziale, a cascata, e si prova a ridurre il bias degli stimatori combinati. La motivaizone è combinare diversi modelli "deboli", per produrre un ensemble migliore.

Vediamo un esponente di entrambi.

### Random forest

Il random forest è un metodo averaging. In pratica, viene costruito un insieme

### AdaBoost

L'algoritmo AdaBoost è un metodo boosting.

## Reti neurali

### Multi-Layer Perceptron
