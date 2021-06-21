# Il problema della classificazione

Nella lezione precedente abbiamo brevemente introdotto il problema della *classificazione*. Questo, come suggerisce il nome stesso, prevede che sia assegnata ad ogni campione una *classe*, da intendersi come un "insieme" di proprietà ed attributi che permette di distinguere oggetti con caratteristiche differenti.

Per fare un esempio, due immagini appartengono alla stessa classe se ritraggono due "oggetti" dello stesso tipo: due auto rosse, due gatti, o due persone vestite allo stesso modo. Se avessimo a che fare con un'immagine di un cane ed una di un gatto, invece, potremmo ragionevolmente desumere che appartengono a due classi differenti.

Nel caso del Titanic, invece, potremmo classificare i passeggeri come *sopravvissuti* e *non sopravvissuti*, andando quindi a caratterizzare i due gruppi in base alle loro caratteristiche.

!!!note "Note"
    Il concetto di classe è tuttavia correlato al *dominio* che ci troviamo a trattare. Per capirci, qualora stessimo classificando tutti i "quadrupedi", cane e gatto apparterrebbero alla stessa classe.

## Classificazione supervisionata e non supervisioata

La classificazione è spesso approcciata in maniera *supervisionata*. Questo prevede che un *esperto di dominio* "contrassegni", o per meglio dire *etichetti*, una serie di dati mediante la procedura di *labeling*.

Tornando all'esempio delle immagini, l'esperto di dominio dovrebbe assegnare l'etichetta *cane* alle immagini raffiguranti un cane, mentre l'etichetta *gatto* andrebbe assegnata alle immagini contenente un gatto. Per quello che riguarda il dataset del Titanic, l'etichetta sarà assegnata per ogni passeggero in base al fatto che questo sia sopravvissuto o meno.

!!!note "Nota"
    Ovviamente, questi sono casi "semplici" di labeling. Esistono, nella realtà, casi molto più complessi, nei quali l'esperto di dominio deve essere altamente qualificato.

Esiste anche la possibilità di usare un approccio *non supervisionato*, che non prevede la presenza di un esperto di dominio, e che conseguentemente inferisce la struttura dei dati da essi stessi. In questo corso, non tratteremo questi approcci per ciò che riguarda la classificazione vera e propria; vedremo però il clustering, che è, per antonomasia, non supervisionato.

## La classificazione e la sua tipologia

Oltre alla distinzione tra approcci supervisionati e non, esistono altre distinzioni, derivanti dal numero di classi e label assegnate ai vari campioni.

### Classificazione binaria

I problemi di *classificazione binaria* prevedono che l'output possibile siano soltanto due, di solito *vero* e *falso*, in ovvia analogia con la logica booleana.

Un tipico esempio di un problema binario è quello del riconoscimento del volto di una persona, nel quale il sistema di machine learning deve restituire *vero* se il volto viene riconosciuto correttamente, e *falso* altrimenti. Altro esempio è quello cui abbiamo accennato in precedenza a riguardo della sopravvivenza dei passeggeri del Titanic.

### Classificazione multi-classe

I problemi che prevedono più di due classi sono detto *multi-classe*, e sono anche tra i più diffusi.

Tornando all'elaborazioen delle immagini, il riconoscimento del tipo di oggetto raffigurato nella foto è un problema tipicamente multi-classe, dato che questo può appartenere ad un elevato numero di classi (ad esempio, auto, smartphone, animali, etc.). Tornando al dataset Titanic, un esempio di problema multi-classe potrebbe prevedere l'esigenza di classificare i passeggeri in base al compartimento nel quale era situata la loro cabina.

### Classificazione multi-label

<!-- TODO -->

La classificazione *multi-label* prevede che ogni campione sia etichettato con $m$ label provenienti dall'insieme di $N$ classi, con $0 \leq m \leq N$. In altre parole, potremmo pensare ad un problema multi-label come ad un problema che predice le proprietà *non mutualmente esclusive* di ogni campione.

Per esempio, potremmo pensare di definire, oltre alla label *sopravvissuto*, anche la label *genere*, e valutare le due congiuntamente, in quanto supposte non mutualmente esclusive.

!!!note "Nota"
    In realtà, il genere potrebbe, e dovrebbe, aver avuto una relazione con le possibilità di sopravvivenza del passeggero, in quanto potrebbero essere state favorite le donne nel momento del salvataggio.

Questo tipo di problema è concettualmente riconducibile all'uso "concatenato" di una serie di classificatori binari in cascata, uno per ciascuna delle label disponibili.

### Classificazione multi-output

La classificazione *multi-output*, conosciuta anche come *multi-task*, è un approccio alla classificazione nel quale ogni campione viene etichettato mediante una serie di proprietà non binarie, in numero strettamente maggiore di 2. Ovviamente, stiamo parlando di una generalizzazione dei problemi che abbiamo visto finora, in particolare dei multi-label (che prevedono solo label binarie) e dei multi-classe.

Per esempio, avremmo un problema multi-task quando, oltre ad andare ad individuare il tipo di oggetto, vogliamo definirne anche il colore: il fatto di vedere un'auto, ad esempio, non influirà (in linea teorica) il colore della stessa. 

## Metriche

<!-- TODO da qui -->

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
