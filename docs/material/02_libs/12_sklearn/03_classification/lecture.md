# Il problema della classificazione

Nella lezione precedente abbiamo brevemente introdotto il problema della *classificazione* che, come il nome stesso suggerisce, prevede che ad ogni dato sia assegnata una *classe*, da intendersi come insieme di proprietà ed attributi che permettono di distinguere oggetti con caratteristiche differenti.

Facciamo un breve esempio. Due immagini, infatti, appartengono alla stessa classe nel caso ritraggono due campioni dello stesso tipo: due gatti, ad esempio, o due auto sportive. Se avessimo a che fare con l'immagine di un cane e quella di un gatto, invece, potremmo ragionevolmente desumere che appartengono a due classi differenti.

Nel caso del Titanic, invece, potremmo classificare i passeggeri come *sopravvissuti* e *non sopravvissuti*, andando quindi a caratterizzare i due gruppi in base alle loro caratteristiche.

!!!note "Note"
    Il concetto di classe è tuttavia correlato al *dominio* che ci troviamo a trattare. Per capirci, qualora stessimo classificando tutti i "quadrupedi", cane e gatto apparterrebbero alla stessa classe.

## Classificazione supervisionata e non supervisioata

La classificazione è spesso approcciata in maniera *supervisionata*. Questo prevede che un *esperto di dominio* "contrassegni", o per meglio dire *etichetti*, una serie di dati mediante la procedura di *labeling*.

Tornando all'esempio delle immagini, l'esperto di dominio dovrebbe assegnare l'etichetta *cane* alle immagini raffiguranti un cane, mentre l'etichetta *gatto* andrebbe assegnata alle immagini contenente un gatto. Per quello che riguarda il dataset del Titanic, l'etichetta sarà assegnata per ogni passeggero in base al fatto che questo sia sopravvissuto o meno.

!!!note "Nota"
    Ovviamente, questi sono casi "semplici" di labeling. Esistono, nella realtà, casi molto più complessi, nei quali l'esperto di dominio deve essere altamente qualificato.

Esiste anche la possibilità di usare un approccio *non supervisionato*, che non prevede la presenza di un esperto di dominio, e che conseguentemente inferisce la struttura dei dati da essi stessi. In questo corso, tratteremo il clustering, che è un approccio totalmente non supervisionato.

## Tipi di classificazione

Oltre alla distinzione tra approcci supervisionati e non, ne esistono delle altre legate al numero di classi e label assegnate ai vari campioni.

### Classificazione binaria

I problemi di *classificazione binaria* prevedono che gli output siano soltanto due, di solito *vero* e *falso*, in ovvia analogia con la logica booleana.

Un tipico esempio di un problema binario è quello del riconoscimento del volto di una persona, nel quale il sistema di machine learning deve restituire *vero* se il volto viene riconosciuto correttamente, e *falso* altrimenti. Altro esempio è quello cui abbiamo accennato in precedenza a riguardo della sopravvivenza dei passeggeri del Titanic.

### Classificazione multi-classe

I problemi che prevedono più di due classi sono detto *multi-classe*.

Tornando all'elaborazione delle immagini, il riconoscimento del tipo di oggetto raffigurato nella foto è un problema tipicamente multi-classe, dato che questo può appartenere ad un elevato numero di classi (ad esempio, auto, smartphone, animali, etc.). Tornando al dataset Titanic, un esempio di problema multi-classe potrebbe prevedere l'esigenza di classificare i passeggeri in base al compartimento nel quale era situata la loro cabina.

### Classificazione multi-task

Parliamo di classificazione *multi-task* quando abbiamo diversi problemi che devono essere risolti contemporaneamente.

Pensiamo, ad esempio, ad un problema che richieda di distinguere un gatto da una tigre, e, contestualmente, di descrivere l'ambiente in cui si trova l'animale. Ovviamente, il problema consta di due aspetti, che però sono tra loro correlati: infatti, è molto probabile che una tigre si trovi in un ambiente di tipo "selvaggio", mentre che la foto del gatto sia all'interno di una casa o comunque di un ambiente più "urbano". In questo caso, si potrebbero addestrare più classificatori, o combinarne diversi in un unico stimatore, per raggiungere il risultato finale.

### Classificazione multi-label

La classificazione *multi-label* è un caso particolare di classificazione multi-task.

Per rimanere nello stesso ambito del caso precedente, potremmo voler considerare un'immagine che abbia al suo interno diversi animali, come ad esempio un gatto, un cane ed una gallina. Il problema multi-label può prevedere, abbastanza banalmente, la descrizione della presenza (o meno) dei diversi animali all'interno della foto; per far questo, il classificatore si pone di suddividere l'immagine in diversi problemi di classificazione binaria, in particolare rispondendo alle domande:

1. Vi è un cane nell'immagine?
2. Vi è un gatto nell'immagine?
3. Vi è una gallina nell'immagine?

## Valutare un algoritmo di classificazione: le metriche

Gli algoritmi di classificazione (e, più in generale, tutti gli algoritmi di machine learning) sono valutati sulla base di una o più *metriche* che, nel caso specifico, mettono in evidenza in che percentuale l'algoritmo è in grado di determinare correttamente l'appartenenza o meno di un campione ad una classe.

Vediamo in tal senso alcune delle metriche maggiormente usate.

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

Per calcolare l'accuracy dei risultati ottenuti dal nostro predittore, Scikit-Learn ci mette a disposizione un'apposita funzione chiamata `accuracy_score`.

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

!!!tip "Il parametro `average`"
    La funzione `recall_score` accetta un parametro che, di primo acchitto, potrebbe passare inosservato, ovvero `average`. Questo è in realtà molto importante, in quanto deve essere impsotato in base alle specifiche del problema sotto osservazione. Così, in caso di classificazione binaria, dovremo usare `average='binary'`, specificando anche la classe sulla quale ci interessa calcolare il recall; nel caso di classi non bilanciate, invece, potremmo preferire la modalità `'macro'` alla modalità `'micro'`.

### Precision

Simile al recall è la *precision*, calcolata questa volta usando la seguente formula:

$$
R = \frac{TP}{(TP + FP)}
$$

dove $FP$ è il numero di *falsi positivi*, ovvero dei campioni che il classificatore reputa erroneamente appartenenti ad una certa classe. La precision può quindi essere descritta come la capacità del classificatore di non assegnare una certa classe a campioni appartenenti ad un'altra.

Per la precision valgono esattamente le stesse considerazioni fatte per il recall; l'unica differenza sostanziale, oltre quella "semantica", sta nel fatto che viene calcolata usando la funzione `precision_score`.

### Matrice di confusione

Un altro modo di rappresentare i risultati ottenuti da un classificatore è quello di usare una *matrice di confusione*.

La definizione di una matrice di confusione $C$ è tale che $C_{i,j}$ sia uguale al numero di osservazioni che sono nel gruppo $i$, ma che vengono predette dal classificatore nel gruppo $j$.

## Algoritmi di classificazione

Scikit-Learn offre un gran numero di metodi di classificazione. In questo corso, ci limiteremo a descrivere brevemente un paio di algoritmi, ovvero le SVM e gli alberi decisionali. Al solito, però, è importante sottolineare come Scikit-Learn offra un'interfaccia in tutto e per tutto *omogenea* tra i diversi algoritmi, il che ci permette quindi di modificare il nostro approccio riscrivendo solo piccole parti del nostro codice.

### Un primo esempio: gli alberi decisionali

Gli *alberi decisionali* sono tra gli algoritmi più semplici che possiamo utilizzare per classificare dei dati.

Un albero decisionale agisce sulle singole feature, impostando delle "regole" sulla base delle quali si stabilisce un outcome certo outcome. Partiamo da un esempio illustrato nella figura successiva.

Un classificatore basato su albero decisionale prevede una struttura di questo tipo.

![decision_tree](./images/decision_tree.jpg){: .center}

Comprendere il funzionamento di un albero decisionale è abbastanza semplice. L'obiettivo di un albero decisionale è quello di creare un modello che predica il valore di una variabile obiettivo imparando delle semplici regole decisionali apprese a partire dalle feature dei dati. In pratica, possiamo pensare ad un albero come ad un percorso "a step", nel quale ad ogni step vi è un'approssimazione successiva verso il risultato finale.

Questo esempio mostra le possibilità di sopravvivenza individuate tra i passeggeri del Titanic, assieme alle percentuali di questi sul totale. La suddivisione che viene subito all'occhio è la seguente:

* il 36% dei passaggeri era donna;
* il 60% uomo di età superiore ai 9 anni e 6 mesi;
* il 4% uomo di età inferiore ai 9 anni e 6 mesi.

L'albero invece ci dice che sono sopravvissuti:

* il 73% delle donne;
* il 17% degli uomini con più di 9 anni e 6 mesi;
* il 2% degli uomini con meno di 9 anni e 6 mesi, con *più* di tre fratelli;
* l'89% degli uomini con meno di 9 anni e 6 mesi, con *meno* di tre fratelli.

### Le Support Vector Machine

Le *Support Vector Machine* (*SVM*) operano sulla disposizione dei dati nell'iperspazio delle feature, cercando di individuare un iperpiano ottimale che ne consenta la migliore separazione possibile. Questo tipo di algoritmo prende il nome dai dati più vicini all'iperpiano, che sono chiamati *Support Vector*.

Nella figura successiva, presa da WikiMedia e creata da [Zack Weinberg](https://commons.wikimedia.org/w/index.php?curid=22877598), vediamo un esempio in un piano a due dimensioni.

![svm_plane](./images/svm_plane.png){: .center}

Le SVM calcolano la distanza tra i campioni mediante un'apposita funzione, chiamata *kernel*. Ve ne sono di diversi tipi, ognuno dei quali permette di ottenere risultati più o meno validi a seconda delle diverse situazioni.

!!!note "Nota"
	Le SVM, per loro natura, sono utili principalmente in caso di classificazione binaria. In realtà, però, gli algoritmi offerti da Scikit Learn permettono di implementare in maniera automatica *anche* la classificazione multi-classe, sfruttando un approccio chiamato *one-to-one*, che scompone il problema in una serie di problemi binari, sulla stregua della classificazione multi-label.
