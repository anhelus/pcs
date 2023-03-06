# 3 - Preparazione dei dati

Nella [lezione precedente](./02_framing.md)

TODO


 abbiamo evidenziato come uno dei passi fondamentali per il machine learning sia quello di determinare i dati sui quali il modello deve essere addestrato: per ottenere buone predizioni, dovremo *costruire un dataset*, ed eventualmente effettuare delle opportune *trasformazioni* sui dati. Queste operazioni sono normalmente riassumibili nei concetti di *campionamento* e *preparazione dei dati*.

## 14.1 - Il campionamento

Il primo problema da affrontare è la raccolta dei dati, che servirà ovviamente a generare il nostro dataset. In questa fase, dovremo partire affrontando due aspetti: la *dimensione* e la *qualità* dei dati che abbiamo raccolto.

### 14.1.1 - Dimensione del dataset

Non vi è una regola vera e propria per determinare il quantitativo di dati *sufficiente* per addestrare adeguatamente un modello. In generale, tuttavia, potremmo dire che il modello deve essere addestrato su un quantitativo di dati che sia maggiore di almeno un ordine di grandezza rispetto al numero dei parametri dello stesso. A scopo puramente esemplificativo, usando una rete neurale con $100$ neuroni dovremmo indicativamente avere almeno $1000$ campioni a disposizione.

### 14.1.2 - Qualità del dataset

Parafrasando un vecchio adagio, *la quantità è niente senza qualità*. Nell'ambito della data science, ciò implica che avere a disposizione grandi quantità di dati non basta se questi non sono anche *significativi* nella caratterizzazione del fenomeno sotto osservazione.

Per comprendere questo concetto, possiamo usare un approccio empirico. Immaginiamo di voler creare il nostro solito modello di predizione delle precipitazioni, e di dover scegliere per addestrarlo tra due dataset. Il dataset A contiene i campionamenti ogni $15$ minuti dei valori di temperatura e di pressione degli ultimi $100$ anni, ma soltanto per il mese di luglio, mentre il dataset B contiene un unico valore giornaliero, ma preso per tutti i mesi dell'anno. E' facile calcolare che il numero di campioni del dataset A è pari a $4 \cdot 24 \cdot 31 \cdot 100 = 297.600$ valori, mentre quello per il dataset B è pari a $365 \cdot 100 = 36.500$. Tuttavia, la qualità del dataset B è migliore rispetto a quella del dataset A: infatti, nonostante quest'ultimo abbia quasi il decuplo dei dati, sarà praticamente inutile per la stima delle precipitazioni in inverno, primavera o autunno.

## 14.2 - Preparazione dei dati

Una volta completata la procedura di campionamento, dovremo passare ad effettuare la preparazione dei dati. Il primo step è in molti casi trascurato, ma è di vitale importanza nel caso si stiano utilizzando delle informazioni in qualche modo sensibili, come ad esempio informazioni legate alle condizioni sanitarie di diversi pazienti. In questi casi, infatti, è strettamente necessario provvedere all'*anonimizzazione* dei dati, rimuovendo tutte le informazioni definite come *personally identifiable* (*PII*).

Una volta completato questo passaggio, potremo passare alle azioni maggiormente rilevanti dal punto di vista scientifico.

### 14.2.1 - Pulizia dei dati

Abbiamo in precedenza sottolineato come l'affidabilità del dataset sia essenziale a garantire performance ottimali del modello addestrato. In tal senso, occorre determinare diversi fattori, tra cui:

* **errori nel labelling**: bisogna valutare a grandi linee se il lavoro svolto dall'essere umano nell'etichettatura è accettabile, o se questa procedura è stata soggetta ad errori di natura grossolana;
* **rumorosità del dataset**: è importante valutare se i dati sono affetti da rumore. Ad esempio, le letture di un sensore potrebbero essere tutte quante affette da offset o bias o, nel caso peggiore, essere causate da lettori non più tarati e quindi inutilizzabili;
* **dati mancanti**: potrebbe darsi che i valori di alcune feature non siano disponibili per alcuni campioni;
* **valori contrastanti o duplicati**: ad esempio, ci potrebbero essere parti di dataset in cui una lettura di temperatura avviene in gradi Kelvin, ed altre in cui la lettura avviene in gradi centigradi, oppure ancora ci potrebbero essere valori duplicati a causa di errori nell'I/O del sensore.

In tutti questi casi, va scelta una strategia di pulizia: in certe situazioni potrebbe essere sufficiente eliminare un campione, oppure effettuare un'operazione di *filling* a partire dalla restante parte del dataset, o ancora, in casi estremi, si potrebbe eliminare *completamente* la feature interessata da rumore.

### 14.2.2 - Sbilanciamento del dataset

E' possibile che un dataset abbia diverse proporzioni nei raggruppamenti dei dati. Anche se questo fenomeno può interessare ogni insieme di dati, è maggiormente evidente nei problemi di classificazione, nei quali abbiamo un feedback immediato sulle differenti proporzioni grazie proprio alla presenza delle label per le classi.

In particolare, avremo due tipi di "suddivisioni": le *classi maggioritarie* saranno quelle con il maggior numero di campioni, mentre quelle *minoritarie* saranno prevedibilmente quelle con a disposizione un numero limitato di dati. Un dataset in cui sussiste questa ineguaglianza è detto *sbilanciato*.

E' possibile quantificare approssimativamente lo sbilanciamento del dataset. In tal senso, possiamo rifarci alla seguente tabella:ì

| Grado di sblianciamento | $\%$ di campioni di classi minoritarie |
| ----------------------- | --------------------------------- |
| Leggero | 20-40 $\%$ del datset |
| moderato | 1-20 $\%$ del dataset |
| Estremo | < 1 $\%$ del dataset |

#### 14.2.2.1 - Influenza dello sbilanciamento

Per capire qual è il problema legato allo sbilanciamento del dataset, immaginiamo di dover creare un modello che individui una mail di spam. Per farlo, usiamo un dataset con la seguente proporzione:

| | Mail non spam | Mail spam |
| - | - | - |
| Numero di immagini | $5$ | $995$ |
| Percentuale | $0.5 \%$ | $99.5 \%$

Il problema sta nel fatto che un numero così esiguo di mail di spam farà sì che il modello spenda la maggior parte dell'addestramento su mail normali, non imparando quindi a riconoscere i casi di spam. Per fare un parallelismo con il nostro cervello, se vedessimo 995 immagini di penne, e solo 5 di matite, è probabile che non saremmo in grado di distinguere una matita da una penna perché, semplicemente, *non sapremmo come è fatta una matita*.

#### 14.2.2.2 - Downsampling ed upweighting

Un modo efficace per gestire situazioni in cui il dataset è sbilanciato è quello di utilizzare tecniche di *data balancing*. Ne esistono di diverse, più o meno efficaci; tuttavia, la più semplice è quella di rimuovere un certo numero di campioni di classe maggioritaria (*downsampling*), dando agli esempi sottocampionati un peso maggiore nell'addestramento (*upweighting*).

In pratica, se scegliessimo di mantenere soltanto il $10 \%$ delle mail non-spam, avremmo circa $99$ campioni. Ciò porterà il rapporto tra le mail di spam e quelle non di spam a circa il $5 \%$, passando da una situazione di sbilanciamento estremo ad una di sbilanciamento moderato.

A valle di questa operazione, dovremmo dare maggior peso ai campioni delle mail non-spam, usando un fattore tendenzialmente pari a quello che abbiamo usato in fase di downsampling. Nella pratica, ogni mail non-spam avrà un peso dieci volte superiore a quello che avrebbe avuto se si fosse utilizzato il dataset iniziale.

### 14.2.3 - Trasformazione dei dati

Il passo successivo nella preparazione dei dati è quello di *trasformare* alcuni valori. In tal senso, possiamo operare per due ragioni principali.

La prima è che siano necessarie delle trasformazioni obbligatorie volte a garantire la compatibilità dei dati, come ad esempio:

* **convertire feature non numeriche in numeriche**: in pratica, non possiamo effettuare operazioni sensate tra interi e stringhe, per cui dovremmo trovarci ad individuare un modo per favorire il confronto;
* **ridimensionare gli input ad una dimensione fissa**: alcuni modelli, come ad esempio le reti neurali, prevedono un numero fisso di nodi di input, per cui i dati in ingresso devono avere sempre la stessa dimensione.

La seconda è legata invece a delle trasformazioni opzionali, che ottimizzano l'addestramento del modello. Ad esempio, potremmo dover effettuare la *normalizzazione* dei dati numerici, ovvero portarli tutti all'interno di una stessa scala di valori, normalmente compresa tra $0$ ed $1$ o tra $-1$ ed $1$. Vediamo più nel dettaglio alcune possibilità.

#### 14.2.3.1 - Trasformazione dei dati numerici

Abbiamo detto in precedenza che potremmo voler applicare delle *normalizzazioni* a dei dati numerici per migliorare le performance del nostro modello.

Per comprenderne il motivo, immaginiamo di avere un dataset che comprende feature per età (che possiamo presupporre assuma valori da $0$ a $100$) e stipendio (che possiamo presupporre assuma valori da $10.000$ a $100.000$ €). Quando andiamo ad utilizzare questi valori in algoritmi che effettuano delle operazioni tra feature, l'età diventerà presto trascurabile rispetto allo stipendio, che è di due o tre ordini di grandezza superiore, per cui il modello si troverà a prediligere quest'ultimo in fase di analisi. Ciò implica quindi la necessità di arrivare ad una "base comune" a partire dalla quale operare.

Le principali tecniche di normalizzazione disponibili sono quattro.

##### 14.2.3.1.1 - Scaling

Lo **scaling** prevede la conversione dei valori assunti da una feature in un range che va di solito tra $[0, 1]$ o $[-1, 1]$. La formula dello scaling è la seguente:

$$
y = \frac{(x - x_{min})}{(x_{max} - x_{min})}
$$

##### 14.2.3.1.2 - Clipping

Può capitare che il dataset contenga degli *outlier*, ovvero dei campioni che divergono notevolmente dalle caratteristiche statistiche del dataset. In questo caso, potremmo limitarci a rimuovere completamente tali valori mediante soglie statistiche, come i range interquartili in caso di distribuzione parametrica, o i classici $3 \sigma$ in caso di distribuzione normale.

##### 14.2.3.1.3 - Trasformazione logaritmica

Un'altra possibilità è quella di convertire i nostri valori in scala logaritmica, comprimendo un range ampio in uno più piccolo usando la funzione logaritmo:

$$
y = Log(x)
$$

##### 14.2.3.1.4 - Z-score

Un ultimo tipo di trasformazione prevede l'uso dello *z-score*, che prevede una riformulazione dei valori assunti dalla feature per fare in modo che questi aderiscano ad una distribuzione a media nulla e deviazione tandard unitaria. Per calcolarlo, si usa la seguente formula:

$$
y = \frac{x - \mu}{\sigma}
$$

dove $\mu$ è la media della distribuzione dei nostri dati, mentre $\sigma$ ne è chiaramente la varianza.

#### 14.2.3.2 - Trasformazione dei dati categorici

Alcune delle nostre feature possono assumere esclusivamente valori *discreti*. Ad esempio, le nostre immagini potrebbero raffigurare diverse razze di cani, oppure il campo "località" potrebbe riportare il codice postale. Queste feature sono conosciute come feature *categoriche*, ed i valori ad esse associate possono essere sia stringhe sia numeri.

!!!note "Le feature categoriche di tipo numerico"
    Spesso, dobbiamo trattare feature categoriche che contengono valori numerici. Per fare un esempio, consideriamo il codice postale, che è un numero. Se lo si rappresentasse come una feature di tipo numerico, il nostro modello potrebbe interpretare la distanza tra Bari (70126) e Taranto (74121) come pari a $3.995$, il che non avrebbe ovviamente alcun senso.

Per essere trattate, comunque, le feature categoriche hanno rappresentazioni di tipo numerico, *mantenendo il riferimento al significato categorico e discreto*. Per comprendere le implicazioni di questo concetto, immaginiamo i giorni della settimana. Il modo più semplice per passare da una rappresentazione puramente categorica ad una numerica è quella di usare un numero:

| Giorno | Rappresentazione |
| ------ | ---------------- |
| Lunedì | 1 |
| Martedì | 2 |
| Mercoledì | 3 |
| Giovedì | 4 |
| Venerdì | 5 |
| Sabato | 6 |
| Domenica | 7 |

In questa maniera creeremo un "dizionario", nel quale potremo accedere ad una chiave (la rappresentazione) che rappresenterà un determinato valore (il giorno).

!!!warning "Sulle feature categoriche trasformate"
    A valle di questa trasformazione, la differenza aritmetica tra domenica e sabato continua ad avere un senso alquanto limitato, e comunque relativo ad un generico concetto di *distanza*.

Un altro modo di rappresentare le feature categoriche è mediante una *rappresentazione sparsa*, detta anche *one-hot encoding*, nella quale ogni valore è rappresentato da un vettore $V$ di lunghezza $m$, con $m$ numero di categorie possibili. In questo caso, tutti i valori di $V$ saranno pari a $0$, tranne quello rappresentativo del valore attualmente assunto dalla feature, che sarà pari ad $1$. Ad esempio, la rappresentazione sparsa del lunedì è data da:

```py
lunedi = np.array([1 0 0 0 0 0 0])
```

mentre quella del giovedì:

```py
giovedi = np.array([0 0 0 1 0 0 0])
```

### 14.2.4 - Suddivisione dei dati

L'ultimo passo nella preparazione del dataset è quello della suddivisione dei dati. In particolare, si destinano un certo quantitativo di dati per l'addestramento del modello, delegando la restante parte alla validazione dei risultati ottenuti; ciò è legato alla volontà di verificare la capacità di *generalizzazione* del modello, ovvero a quanto è in grado di "funzionare" il nostro algoritmo in caso di analisi di dati su cui non è stato addestrato.

Un rapporto molto usato in tal senso è quello che prevede che il $70\%$ dei dati sia usato per l'addestramento, mentre il restante $30\%$ per la validazione dei risultati ottenuti.
