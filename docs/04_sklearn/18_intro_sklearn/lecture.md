# 17 - Cosa è Scikit-Learn?

Scikit-Learn è una delle principali librerie per il machine learning disponibili per Python. Il suo ampio utilizzo è legato soprattutto a tre fattori:

* l'ampio supporto ad un gran numero di algoritmi;
* la facilità di utilizzo;
* la perfetta integrazione con NumPy e Pandas.

Vediamo quindi una panoramica ad ampio spettro delle potenzialità di Scikit-Learn.

## 17.1 - Installazione di Scikit-Learn

Come di consueto, la prima cosa da fare è installare la libreria. Per farlo, spostiamoci (eventualmente) nell'ambiente virtuale usato per il corso, ed usiamo il seguente comando:

```sh
pip install scikit-learn
```

## 17.2 - Un po' di terminologia

### Dati e feature

Quando abbiamo parlato di Pandas, abbiamo visto che possiamo immaginare un dataset come una sorta di *matrice*, nella quale le righe sono chiamate *campioni*, mentre le colonne sono chiamate *feature*.

Un dataset serve a modellare un fenomeno sotto osservazione. Nel caso che abbiamo affrontato in precedenza, il dataset Titanic modella il "fenomeno" relativo ai passeggeri della nave; altri dataset possono essere relativi a dati acquisiti da dei sensori, oppure ancora alle immagini in un impianto di videosorveglianza. I fenomeni sono quindi *eterogenei*, e dipendono ovviamente dallo scenario sotto analisi.

!!!note "Nota"
    Normalmente, nella modellazione di un qualsiasi tipo di fenomeno, è bene sfruttare la conoscenza di un *esperto di dominio*.

<!-- TODO: inserire figura 3 slides -->

#### Campioni e sbilanciamento del dataset

I campioni sono le *osservazioni* del fenomeno: nel caso del dataset Titanic, ogni campione è associato ad un passeggero, mentre per dati provenienti da immagini di videosorveglianza, il singolo campione è associato ad ogni immagine acquisita dalle videocamere. 

Ovviamente, è anche possibile che più campioni provengano da meccanismi di generazione dei dati molto simili: ad esempio, potremmo avere due righe che descrivono lo stesso passeggero, o due immagini che riprendono la stessa persona dalla stessa angolazione: in questo caso, occorre valutare se vi è della ridondanza tra i dati, ed eventualmente effettuarne un filtraggio. L'estremizzazione di questo principio porta alla problematica degli *imbalanced data*, ovvero dei dataset *sbilanciati* verso un'unica classe.

<!-- TODO: fare slide -->

#### Feature e feature selection

D'altro canto, le colonne sono le *feature* del nostro dataset. Nel caso del dataset del Titanic, abbiamo a che fare con il nome del passeggero, la cabina, o ad esempio la modalità di imbarco; nel caso di un dataset relativo a dati acquisiti da sensori, potremmo avere le letture di temperatura e di umidità, ad esempio. Per un dataset di immagini, invece, le feature sono, in senso lato, tutte le forme, a differenti livelli di astrazione, che possono essere individuate all'interno dell'immagine.

Così come per i dati, anche le feature possono essere *ridondanti*. Se, ad esempio, notassimo che le letture derivanti dal sensore di ossigeno sono *linearmente proporzionali* rispetto a quelle derivanti dal sensore di temperatura, potremmo decidere di eliminare una delle due letture; lo stesso potremmo fare nel caso individuassimo delle feature a bassa varianza, e che quindi assumono lo stesso valore (o quasi) per tutti i dati.

Questo processo di eliminazione, chiamato *feature selection*, è estremamente importante, soprattutto perché avere troppe feature significa rischiare di incorrere nel fenomeno della *curse of dimensionality*.

<!-- TODO: fare slide -->

##### Curse of dimensionality

Nell'ambito del machine learning, la *curse of dimensionality* indica quel fenomeno che insorge quando il numero di feature è paragonabile a quello dei campioni.

Dobbiamo ricordare che il machine learning non fa altro che provare ad "estrarre" una relazione tra i campioni e le feature che li rappresentano: in altre parole, gli algoritmi tentano di capire se, ad esempio, esiste una correlazione tra tutti i passeggeri maschi di età inferiore ai 18 anni, oppure se le donne con età superiore ai 60 anni hanno aderito ad un certo piano tariffario, e via dicendo. Per far questo, è necessario che ci siano abbastanza campioni per descrivere ogni possibile comportamento del fenomeno sotto osservazione: ad esempio, se vi è soltanto una donna che ha pagato il biglietto più di 10 dollari, è plausibile che questa informazione sia *inutile*, ancorché *fuorviante*, mentre se un gran numero di ragazzi è stipato nelle cabine del secondo piano, allora, l'informazione avrà un valore del tutto differente.

La conseguenza immediata di ciò, e che è alla base della curse of dimensionality, risiede quindi nel fatto che quando il numero di feature è circa uguale a quello dei campioni è *molto probabile* che l'algoritmo non sarà in grado di caratterizzare in maniera adeguata il fenomeno sottostante. Le soluzioni a quel punto saranno due: da un lato, potremo provare ad aumentare il numero dei campioni, mentre dall'altro potremo provare a rimuovere le feature poco significative, o anche quelle tra loro correlate, aiutando a mitigare la curse of dimensionality.

<!-- TODO: fare slide -->

### Tipi di dati

Abbiamo finora parlato di campioni e feature. Tuttavia, non abbiamo ancora affrontato un aspetto fondamentale nell'analisi dei dati, ovvero la valutazione del *tipo di dato*, la quale determina, di conseguenza, la scelta dell'algoritmo da utilizzare.

Sostanzialmente, esistono due tipi di dati, ovvero i *dati indipendenti ed identicamente distribuiti* (*IID*) e le *serie temporali*.

#### Dati indipendenti ed identicamente distribuiti

I dati IID sono, come dice il nome stesso, *indipendenti* l'uno dall'altro; inoltre, tutti i dati fanno parte dello stesso meccanismo di generazione dei dati, e quindi si suppone *sottendano alla stessa distribuzione*. In altri termini, ciò significa che il valore di un campione non dipende dal valore di un altro.

Un esempio sono le immagini di diversi oggetti, che possono essere usate per creare un algoritmo di identificazione degli oggetti, oppure gli stessi passeggeri del Titanic.

<!-- TODO: da slide -->

Tipicamente, su questo tipo di dati sono usate tre tipi di algoritmi, ovvero *regressione*, *classificazione* e *clustering*.

##### Classificazione

Le tecniche di classificazione prevedono che ad ogni dato sia assegnata una *classe*, comportando di conseguenza un "raggruppamento" degli stessi in base alle indicazioni sulle classi.

Un esempio sono le classificazioni delle immagini rispetto al tipo di oggetto raffigurato: le immagini relative ad un'auto apparterranno alla classe omonima, mentre le immagini di un cane apparteranno ad un'altra classe, e via dicendo. Altro esempio sono è una possibile classificazione dei passeggeri del Titanic sulla base del fatto che siano sopravvissuti o meno.

<!-- TODO: slide -->

##### Regressione

Le tecniche di regressione cercano invece di trovare una relazione tra le feature di ciascun dato ed un valore numerico (TODO: verificare se continuo o discreto).

Rimanendo ai passeggeri del Titanic, potremmo voler valutare il rapporto esistente tra l'età del passeggero ed il prezzo che questi ha pagato per il biglietto.

<!-- TODO: slide -->

##### Clustering

In ultimo, le tecniche di clustering provano ad inferire dei "raggruppamenti", chiamati formalmente *cluster*, di dati. Ovviamente, i dati appartenenti ad un cluster sono da considerarsi *affini*, mentre i dati appartenenti a cluster differenti sono da considerarsi *differenti*.

Il clustering non prevede la presenza di alcuna classe. Di conseguenza, queste tecniche di apprendimento sono dette *non supervisionate*, in quanto non è necessario l'intervento di un esperto di dominio per definire le classi cui appartengono i dati su cui viene addestrato l'algoritmo.

<!-- TODO: slide -->

#### Serie temporali

A dìfferenza dei dati IID, le serie temporali sono composte da dati tra loro interdipendenti, e "correlati" da vincoli temporali.

Esempi di questo tipo di dati sono i video, composti da *sequenze* di immagini disposte in un ben preciso ordine temporale, oppure ancora le acquisizioni derivate da un sensore.

<!-- TODO: fare slide -->

!!!note "Nota"
	Parleremo più estensivamente delle serie temporali nella lezione su StatsModels.

## Concetti base di Scikit-Learn

### Stimatori

Scikit-Learn definisce gli algoritmi di machine learning come *stimatori*: in tal senso, sia gli algoritmi di clustering, sia quelli di regressione, sia quelli di classificazione sono trattati, per l'appunto, come stimatori.

!!!note "Nota"
	Come vedremo, questa caratterizzazione permette a Scikit-Learn di offrire un'interfaccia comune per la maggior parte degli algoritmi.

#### Parametri dello stimatore

Molto importanti sono i *parametri* con cui regolare il funzionamento dello stimatore. Ad esempio, per l'algoritmo `KMeans`, un possibile parametro è il numero di cluster in cui i dati sono suddivisi.

Vedremo come modificare questi parametri può cambiare *enormemente* le performance di un algoritmo. Performance che, ovviamente, sono valutate secondo apposite *metriche*.

#### Metriche

Ogni algoritmo viene valutato secondo una metrica, che di solito permette di definire, in termini percentuali o assoluti, l'accuratezza dell'algoritmo.

### Preprocessing

Molto spesso, è necessario effettuare delle operazioni di preprocessing (**mai usare preprocessamento**) sui dati. Questo perché questi possono essere viziati dall'assenza di valori in determinati ambiti, oppure è necessario scalarli. Scikit-Learn offre un intero package dedicato a questo.

Le funzioni che utilizzeremo maggiormente saranno:

* `train_test_split`, per suddividere il dataset in un insieme di training ed uno di test;
* gli *Imputer*, per assegnare eventuali valori mancanti all'interno del dataset;
* i *Transformer*, che ci permettono di modificare il tipo dei dati.

### Pipeline

Accenniamo in ultimo al fatto che, normalmente, è necessario *concatenare* diversi stimatori. Per farlo, Scikit-Learn ci mette a disposizione un'apposita struttura chiamata `Pipeline`, che approfondiremo nelle prossime lezioni.

<!-- TODO: da qui revisione -->

### Train, test e cross-validazione

Apprendere i parametri di uno stimatore e testarlo sugli stessi dati è un errore metodologico: un modello che infatti si limitasse a ripetere le label dei campioni che ha appena visto avrebbe un punteggio perfetto, ma non sarebbe in grado di predire qualcosa di utile su dati non ancora visti. Questa situazione è comunemente chiamata **overfitting**. Per evitare l'overfitting, nei metodi supervisionati, si usa "lasciar fuori" parte dei dati disponibili e chiamarla *set di test*. La funzione principe per questo in scikit learn è train_test_split.

<!-- TODO: questo deve essere spostato in una sezione relativa agli iperparametri -->

Tuttavia, può essere anche possibile che si debbano valutare diversi iperparametri per un singolo stimatore. Il concetto di iperparametro è analogo a quello di configurazione, e non sono chiamati parametri per evitare di generare confusione con i parametri che vengono configurati internamente da uno stimatore durante l'apprendimento.

Quando valutiamo diverse combinazioni di iperparametri, è possibile che vi sia un overfitting verso il test set, perché potremmo voler ritarare i parametri in modo da ottenere delle performance di validazione quanto migliori possibile. In questo modo, è possibile che il meccanismo di generazione dei dati caratteristico del test set possa "fuoriuscire" all'interno del modello, causando conseguentemente un peggioramento delle capacità di generalizzazione. Per risolvere questo problema, ogni parte del dataset può essere messa fuori in quello che viene chiamato *set di validazione*: il training avviene sul set di raining, la cui valutazione avviene sul set di valudazione,e  quando l'esperimento sembra aver successo, la valutazione finale può essere fatta sul set di test.

Ad ogni modo, il partizionamento in questo modo riduce drasticametne il numero di campioni che può essere usato per apprendere il modello, ed i risultati possono dipende da una scelta casuale dalla coppia degli insieme (train, validazione).

Una soluzione di questo problema è una procedura chiamato cross-validazione. Un set test deve essere sempre tenuto da parte per una valutazione finale, ma non è necessario il test di validazione. In questo approccio base, chiamato k-fold CV, il set di training è suddiviso in k set più piccoli. La procedura è la seguente:

* un modello viene addestrato usando $k - 1$ dei fold come training data;
* il modello risultante è validato sulla parte rimanente dei dati (ovvero è usato come test set per calcolare una misura di performacnce come l'accuracy.)

La misura di performance restituita dai k-fold è quindi la media dei valori calcolati nel ciclo.
