# Cosa sono le foreste decisionali?

Una foresta decisionale è un termine genrico per descrivere i modelli fatti di più alberi decsionali. La predizione in uscita da una foresta decisioanle è data dall'insieme delle predizione dei sui alberi decisionali.

L'implementazione di questa agtgregazione dipende dall'algortimo usato per addestrare la foresta decisionale. Ad esempio, in una random forest cmulticlasse, ogni albero vota per una singola classe, e la predizione della random forest è la classe più rappresentata. In un binary classification gradient boosted tree (un altroi tipo di decision forest), ogni albero manda in uscita un *logit* (ovvero, un valore floating point), ed il gradient boosted tree manda una predizione che è la somma di questi valori, seguita da una funzione di attivazione (ad esempio, una signomidale).

## Random Forest

Nel 1906, [venne tenuta in Inghilterra](https://www.nature.com/articles/075450a0.pdf) una competizione per stabilire il peso di un bue tra 787 partecipanti. L'errore mediano delle predizioni di ciascuno era di circa 37 libre, ovvero 17 kg, pari al 3.1%. Tuttavia, la *mediana delle predizioni* era di sole 9 libbre (4 kg) distante dal risultato vero, con un errore di circa lo 0.7%.

Questo aneddoto permette di illustrare il cosiddetto principio della [*saggezza della folla*](https://it.wikipedia.org/wiki/Saggezza_della_folla): in certe situazioni, le opinioni collettive forniscono un giudizio estramemnte preciso.

Matematicamente, la saggezza della folla può essere modellata con il [teorema centrale del limite](https://it.wikipedia.org/wiki/Teoremi_centrali_del_limite): informalmente, l'errore quadratico medio tra un valroe e la media di $N$ stime rumorose di questo valore tende a zero con un fattore pari ad $\frac{1}{n}$. Tuttavia, se le variabili non sono indpendente, la variazna è più grande.

Nel machine learning, un ensemblke è un insieme di modelli le cui predizioni sono mediate (o aggregate in qualche maniera). Se i modelli nell'ensemble sono abbastanza differenti senza essere pessimi se presi da soli, la qualità dell'ensemble è generalmente più alta che la qualità di ognuno dei modelli individuali. Un ensemble richiede maggior tempo di addestramento ed inferenza rispetto ad un singolo modello. Dopotutto, dobbiamo effettuare il trainign e l'inferenza di più modelli invece di un singolo modello.

Informalmente, affinché un ensemble lavori al meglio, i modelli dinivudali dovrebbero essere indipendenti. Per esempio, un esnseble composto di 10 modelli identici (ovvero, non indipendenti tra loro) non sarà meglio del modello idnividuale. D'altro canto, forzare i modelli affinché siano indipendenti può renderli peggiori. Un ensemblingf efficace richiede l'indivioduazione del bilancio tra l'ndiepenze del modello e la qualità dei suoi sotto-modelli.

## Randomn forest

Un random forest è un insieme di alberi decisionali nei quali ogni albero decisioanle è addestrato con un certo rumore casuale. Le random forest sono la fforma più popolare di ensemble di alberi decisionali. Vediamo alcuen tecniche per creare degli alebri decisionali indipendenti per migliorare le cahnce di creare una random forest efficace.

### Bagging

La tecnica del bagging (bootstrap aggregating) fa in modo che ogni albero decisionale sia addestrato su un sottoinsieme casuale dei campioni nell'insieme di training. In altre parole, ogni albero decisionale nelle random forest è addestrato su un sottoinsieme differente di campioni.

Il bagging è peculiare. Ogni albero decisionale è addestrato sullo stesso numero di campioni dell'insieme di addestramento originario. Per esempio, se l'insieme di training originario contiene 60 campioni, allora ogni albero decisionale è addestrato su 60 campioni. Tuttavia, il bagging addestra soltanto ogni decision tre su un sottoinsieme (tipicamente, il 67%) di questi esempi. Per cui, alcuni di questi 40 campioni nel sottoinsieme saranno riutilizzati quando si addestra un dato albero decisionale. Questo riutilizzo è chiamato *addestramentp con rimpiazzo*.

Facciamo un esempio. Nella tabella successiva, vediamo come il bagging può distribuire sei campioni su tre alberi decisionaloi. Notiamo che:

* ogni albero decisionale è addestrato su un totale di sei campioni
* ogni albero cdecisioanle +è addestrato su un insieme diverso di campioni
* ogni albero decisionale riutilizza certi campioni. Ad esempio, il campione 4 è usato due volte nell'albero decisionale 1, quindi, i pesi appresi da parte del campion 4 è effettivamente duplicato nel primo albero decisionale.

<table>
<thead>
  <tr>
    <th></th>
    <th colspan="6">Campioni di training</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td></td>
    <td>1</td>
    <td>2</td>
    <td>3</td>
    <td>4</td>
    <td>5</td>
    <td>6</td>
  </tr>
  <tr>
    <td>dataset originario</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>albero decisionale 1</td>
    <td>1</td>
    <td>0</td>
    <td>2</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>albero decisionale 2</td>
    <td>3</td>
    <td>2</td>
    <td>0</td>
    <td>1</td>
    <td>0</td>
    <td>1</td>
  </tr>
  <tr>
    <td>albero decisionale 3</td>
    <td>2</td>
    <td>1</td>
    <td>3</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
  </tr>
</tbody>
</table>

Nel bagging, ogni albero decisionale è quasi sempre addestarto sul numero ttoale di campioni nell'insieme di training originale. L'addestramento di ogni albero decisionale su un numero maggiore o inferiore di campioni può degradare la qualità del randomn forest.

Anche se non presente nel [paper originale](https://www.stat.berkeley.edu/~breiman/randomforest2001.pdf), il campionamento dei campioni alle volte è svolto *senza rimpiazzo*; in altri termini, un campione di training non può essere presente più di una volta nell'insieme di addestramento di un albeor decisionale. Ad esempio, nella tabella precedente, tutti i valori sarebbero 0 o 1.

## Attribute sampling

L'attribute sampling indica che invece di guardare alla migliore condizione rispetto a *tutte* le feature disponibili, soltanto un sottoinsieme casuale di feature sono testate ad ogni nodo. L'insieme di feature testate è campionato casualmente ad ogni nodo dell'albero decisionale.

Il seguente albero decisionale illustra l'attribute sampling. Qui, un albero decisionale è addestrato su 5 feature (f1-f5). I nodi in blu rappresentano le feature testate, mentre quelli in bianco non sono testati. La condizione è costruita a parteire dalle feature meglio testate (rappresentate con un contorno rosso).

TODO: FARE FIGURA

Il rapporto dell'attribute sampling è un importante iperparametro per la regolarizzazione. La figura precednete usa un rapporto di 3/5. Molte implemnentazioni di random forest testano, di default, 1/3 delkle feature in fase di regressione, e la radice quadrata del numero dif eature epr la classificazione.

In TF-DF, i seugenti iperparametri controllano l'attribute sampling:

* num_candidate_attributes
* num_candidate_attributes_ratio

Per esempio, se num_candidate_attributes_ratio=0.5, metà delle featrure saranno testate ad ogni nodo.

## Disabiliatre la regoalrizzazione degli alberi decisionali

Gli alberi decisionali in una foresta casuale sono addestrati senza il pruning. La mancanza di pruning aumenta singificativamente la varianbza, riducendo singificativamente il bias legato al singolo albero decisionale. In altre parole, l'albero individuale può andare in overfitting, ma la random forest no.

Ci aspettiamo che le accuracy di trainign e di test di una random forest siano differenti. L'accuracy di training di una random forest è, generalmente, molto alta (alle volte pari al 100%). Tuttavia, un'accuracy di training molto alta in una random forest èp normale, e non indica che la random forest sia in overfitting.

Le due sorgenti di casualità (il baggin e l'attribute sampling) si assicurano che vi sia indipendenza relativa tra gli alberi decisionali. Questa indipendenza corregege l'overfitting dei singoli alberi decisionali. Di conseguenza, l'ensemble non è in overfitting. Vedremo questo effetto (controintuitivo) nella seguente unità.

Le random forest *pure* sono addestrate senza una profondità massima o un numero minimo di osservazioni per foglia. Nella praica, limitare la profondità massima ed il minimo numero di osservazioni per foglia è un beneficio. Di default, molte random forest usano i sengeunti valori di default.

* massima profondità di circa 16
* minimo numero di osservaizoni per foglia di circa 5



## Chiarezza del rumore

Perché il rumore casuale migliora la qualità del random forest? Per illustrare i benefici delò rumore casuale, vediamo le rpedizioni di un albero decisionale classico e di una random forest addestrata su alcuni campioni di un semplice problema ellittico.

I pattern ellittici sono notoriamente complessi per gli alberi decisionali e. notiamo come l'albero decisionale dopo il pruning non riesce ad ottenre la stessa qualità di predizione delle random forest.

TODO: IMMAGINE CON RIFERIMENTO

Vediamo anche le predizioni dei primi tre alberi decisionali senza pruning nel random forest; ovvero, gli alberi decisionali sono tutti addestrati con una combinazione di bagging, attribute sampling e senza pruning.

Le rpedizioni individuali di questi tre alberi sono *peggiori* delle predizioni dell'albero decisionale con pruning nella precedente figura. TUttavia, dal momento che gli errori degli alberi decisionali individuali sono soltanto correlati debolmente, i tre alberi decisionali combinano in un ensemble per creare delle predizioni efficace.

Dato che gli alberi decisionali di una random forest non sono prunati, il training di una random forest non richiede un dataset di validazione. Nella pratica, e specialmente su piccoli dataset, i modelli dovrebbero essere addestrati su tutti i dati disponibili.

Quando si addestra una random forest, man mano che più alberi decisionali sono aggiunti, l'errore quasi sempre diminuisce; ciò singific ache la qualitàd el modello quasi sempre aumenbta. Aggiungere più alberi decisionali quasi sempre *riduce* l'errore della random forest. In altre parole, aggiungere più alberi decisionali non può causare l'overfit della random forest. Ad un certo punto, il modello semplicemente smette diu migliorare.

Ad esempio, il seguente plot mostra la valutazione di una random forest man mano che vengono aggiunti più alberi decisionali. L'accuracy migliropa rapidamente fino a che non si ferma attorno al valòore di TODO: ESPERIMENTO. Tuttavia, aggiungere più alberi decisionali non fa diminuire l'accuracyt; in altre parole, il modello non va in overfittng. QUestro comportamento è quasi sempre vero ed indipendente dagli iperparametri.

## Out-of-bag evaluation

Le random forest non richiedono un dataset di validazione. La maggior parte delle random forest usa una tecnica chaimata *out-of-bag evaluation* (OOB) per valutare la qualità del modello. La OOB evaluation tratta il set di training come se fosse il set di test di una cross-validazione.

COme spiegato in precedenza, ogni albero decisionale in una random forest è tipicamente addestrato su circa il 67%% degli esempi di training. Di conseguenza, ogni albero decisionale non vede circa il 33% degli esempi di training. L'idea alla base della OOB-evaluation è la seguente:

* valutare la randomn forest sull'insieme di training
* per ogni campione, usiamo solo l'albero decisionale che non vede il campione durante il training

La seugente tabella illustra la valutazione OOB di una random forest con 3 alberi decisionali addestrati su 6 campioni (COPIARE QUELLA DI PRIMA). La tabella mostra quale albero decisionale è usato con quale esempio nella valutazione OOB.


<table>
<thead>
  <tr>
    <th></th>
    <th colspan="6">Campioni di training</th>
    <th>Campioni per la valutazione OOB</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td></td>
    <td>1</td>
    <td>2</td>
    <td>3</td>
    <td>4</td>
    <td>5</td>
    <td>6</td>
    <td></td>
  </tr>
  <tr>
    <td>dataset originario</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td></td>
  </tr>
  <tr>
    <td>albero decisionale 1</td>
    <td>1</td>
    <td>0</td>
    <td>2</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>3</td>
  </tr>
  <tr>
    <td>albero decisionale 2</td>
    <td>3</td>
    <td>2</td>
    <td>0</td>
    <td>1</td>
    <td>0</td>
    <td>1</td>
    <td>2, 4</td>
  </tr>
  <tr>
    <td>albero decisionale 3</td>
    <td>2</td>
    <td>1</td>
    <td>3</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1, 5, 6</td>
  </tr>
</tbody>
</table>

Nell'esempio mostrato nella precedente tabella, le predizioni OOB per l'esempio di training 1 saranno calcolate con l'albero decisionale 3 (dal momento che gli alberi decisionali 1 e 2 usano questo campione per il training). Nella pratica, su unb dataset con dimensioni ragionevoli con alcuni alberi decisionali, tutti gli esempi hanno una predizione OOB.

La valutaizone OOB è efficace anche per calcolare l'importanza delle variabili nei modelli random forest. Ricordiamo che questa importanza misura l'importanza di una variabile misurando la caduta dell a qualità del modello quando questa variabile viene "mescolata". In caso di OOB epr un random forest, l'importanza è calcolata usando la valutazione OOB.

## Altri topic

## interpretazione dei random forest

I random forest sono più compèlessi da interpretare degfliu alberei decisionali. Le random forest contengono degli alberi decisionali addestrati con rumore casuale. Quindi, diviene difficile dare un giudizio suilla struttura dell'albero decisionale. Tuttavia, possiamo interpretare i modelli del random forest in due diversi modi.

Un approccio è quello di limitarsi ad addestrare ed interpretare un albero decisionale con l'algortimo CART. Siccome sia le random forest che il cCART sono addestrati con lo stessdo algoritmo alla base, "condividono la stessa visione globale" sul datasaet. Qeusta opzione funziona al meglio epr dataset semplici e per comprendere l'interpretazione compelssiva del modello.

L'importanza delle variabili è un altro approccio all'intepretabilità.

Un altro tipo di metodo per la spiegazione è quello di suare algoritmi agnostici, come lo SHAP (SHapley Additive exPlanations). 

Vantaggi:

* come gli alberi defcisionali, i random forest supportano natgivamente feature categoriche e numeriche e non richiedono il preprocessing delle stesse
* dato che gli alberi decisionali sono indipendenti, i random forest possono essere addestrati in parallelo, e quindi più velocemente
* le random forest hannod ei aprametri di default che danno ottimi risutlati. il tuning di questi parametri ha spesso poche conseguenze sul modello

Svantaggi:

* siccome gli alberi decisionali non sono soggetti a pruning, possono essere grandi, con modelli con anche un milione di nodi. La dimensione delle random forest può quindi essere un problema
* le random forest non possono apprendere e riutilizzare delle rappresentazioni interne. Ogni albero decisionale (ed ogni ramo di ogni albero decisionale) deve apprendere nuovamente il pattern del datset. Ina lcuni dataset (specie quelli non tabellari) questo fa sì che le random forst abbiano risutlati peggiori daltrri metodi.
