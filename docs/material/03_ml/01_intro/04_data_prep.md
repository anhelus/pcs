# 3.1.3 - Preparazione dei dati

Nella [lezione precedente](./02_framing.md) abbiamo evidenziato come uno dei passi fondamentali nella definizione di un algoritmo di machine learning sia la definizione dei dati sui quali il modello deve essere addestrato. Infatti, per ottenere delle buone predizioni, dovremo opportunamente costruire un dataset; questa operazione avviene in due step, ovvero *campionamento* e *preparazione* dei dati.

## Campionamento del dataset

Il primo problema da affrontare è quello relativo al *campionamento*, ovvero alla raccolta dei dati che andranno a comporre il nostro dataset. In particolare, dovremo tenere conto di due aspetti, ovvero il numero dei dati e la loro qualità.

##### Dimensione del dataset

Il primo aspetto di cui tenere conto riguarda il numero dei dati da raccogliere, che influenza direttamente la *dimensione* del dataset. In tal senso, non esiste una regola vera e propria per deteterminare il quantitativo di dati sufficiente ad addestrare un modello in modo adeguato; in generale, tuttavia, potremo dire che questa quantità deve essere almeno un ordine di grandezza superiore rispetto al numero dei parametri utilizzati dal modello. A scopo puramente esemplificativo, usare una rete neurale con $100$ neuroni implicherà la presenza di almeno $100$ pesi e $100$ bias, per cui dovremo avere indicativamente almeno $2000$ campioni a disposizione.

##### Qualità del dataset

Parafrasando una vecchia pubblicità degli anni '90, *la quantità (potenza) è niente senza qualità (controllo)*. In altri termini, avere a disposizione grandi quantità di dati non basta se questi non sono anche *significativi* nella caratterizzazione del fenomeno sotto osservazione.

Per comprendere questo concetto, cerchiamo di usare un approccio empirico. Riprendiamo il nostro modello di predizione delle precipitazioni, ed immaginiamo di doverlo addestrare scegliendo tra due dataset. In particolare:

* il dataset **A** contiene un dato relativo ai valori di temperatura e pressione campionato ogni $15$ minuti negli ultimi $100$ anni *esclusivamente per il mese di luglio*;
* il dataset **B** contiene un unico dato giornaliero per i valori di temperatura e pressione per ciascun giorno degli ultimi $100$ anni.

Possiamo quindi facilmente verificare che il dataset **A** contiene $297.600$ campioni (pari a $4 \cdot 24 \cdot 31 \cdot 100$, ovvero il numero di campioni per ora moltiplicati per il numero di ore e per il numero di giorni presenti a luglio), mentre il dataset **B** contiene solo $365 \cdot 100 = 36.500$ campioni.

Tuttavia, la qualità del dataset **B** risulta essere migliore rispetto a quella del dataset **A**: infatti, nonostante quest'ultimo abbia quasi dieci volte più campioni del primo, non potrà essere utilizzato per stimare le precipitazioni in mesi differenti da luglio.

## Preparazione dei dati

Una volta acquisito in maniera appropriata il dataset, dovremo preparare i dati in esso contenuto. 

!!!warning "Anonimizzazione dei dati"
    Lo step "zero" della preparazione del dataset è quello legato all'anonimizzazione dei dati, che assume fondamentale importanza in taluni contesti, come ad esempio quello medico o finanziario. Presupporremo, nel prosieguo, che questo passo venga effettuato di default.

Questa preparazione prevede gli step riassunti nel prosieguo.

##### Step 1: Data cleaning

Abbiamo visto come la qualità ed affidabilità del dataset siano essenziali per garantire adeguate performance del modello addestrato. In tal senso, è necessario determinare diversi fattori, ad esempio:

* **presenza di errori nel labelling**: il lavoro svolto dall'esperto di dominio nel labeling può, alle volte, essere subottimale, e presentare errori grossolani ed evidenti. In questo caso, potrebbe essere necessario effettuare un'ulteriore procedura di etichettatura;
* **presenza di rumore**: è importante valutare se i dati sono affetti da rumore o da trend evidenti. Per esempio, potremmo notare che tutte le letture di un sensore sono affette da un certo punto in avanti da un certo offset, legato magari ad una staratura dello stesso;
* **assenza di dati**: immaginando che un sensore risulti danneggiato, potrebbe verificarsi la situazione per cui le letture per lo stesso non siano disponibili da un certo istante in avanti. Questo fenomeno, che abbiamo già analizzato quando abbiamo parlato [della manipolazione dei DataFrame in Pandas](../../02_libs/03_pandas/04_functions.md), va adeguatamente affrontato;
* **valori contrastanti o duplicati**: data la dinamicità delle campagne di acquisizione, specialmente se lunghe, potrebbero esserci delle incoerenze nei dati campionati. Ad esempio, lungo l'arco della campagna, un sensore di temperatura non funzionante potrebbe essere stato sostituito con un altro che, però, a differenza del primo effettua le letture in gradi Kelvin.

Se si presenta una di queste occorrenza, è necessario valutare una strategia di data cleaning. Ne abbiamo brevemente parlato in precedenza analizzando le funzioni `dropna()` e `fillna()`; ne vedremo delle altre nel proseguo.

##### Step 2: Bilanciamento del dataset

Quando si affronta un problema di classificazione, esiste la (tutt'altro che remota) possibilità che il dataset acquisito presenti diverse proporzioni nel raggruppamento delle classi. In altre parole, supponendo la presenza di due classi $X$ ed $Y$, potremmo avere il $70\%$ di campioni appartenenti alla classe $X$, ed il restante $30\%$ appartenenti alla classe $Y$.

Ciò comporta che avremo una *classe maggioritaria*, ovvero $X$, che avrà un maggior numero di campioni rispetto alla *minoritaria* $Y$, la quale, prevedibilmente, sarà rappresentata da un numero limitato di campioni. Un dataset in cui si verifica questo fenomeno è detto *sbilanciato*.

Possiamo quantificare, in maniera approssimativa, l'entità dello sbilanciamento del dataset, rifacendoci alla seguente tabella.

| Grado di sbilanciamento | $\%$ di campioni di classi minoritarie |
| ----------------------- | --------------------------------- |
| Leggero | 20-40 $\%$ del datset |
| Moderato | 1-20 $\%$ del dataset |
| Estremo | < 1 $\%$ del dataset |

Per comprendere a fondo quali siano gli effetti dello sbilanciamento del dataset, possiamo tornare al nostro spam detector. Per addestrarlo, usiamo un dataset di qeusto tipo:

| | Mail non spam | Mail spam |
| - | - | - |
| Numero di mail | $5$ | $995$ |
| Percentuale | $0.5 \%$ | $99.5 \%$

Notiamo subito che abbiamo un numero molto limitato di mail di spam. Di conseguenza, l'addestramento avverrà per la maggior parte su mail "normali"; inoltre, un numero così esiguo di mail di spam non potrà descrivere adeguatamente tutti i casi in cui ci si trova di fronte a questo fenomeno.

##### Data balancing

Una maniera efficace per trattare situazioni di questo tipo è quella di adottare una tecnica di *data balancing* (ovvero, bilanciamento dei dati). Ne esistono diverse, più o meno efficaci; tra queste, la più semplice riguarda la rimozione di un certo numero di campioni della classe maggioritaria (*downsampling*), dando agli esempi sottocampionati un peso maggiore nell'addestramento (*upweighting*).

Facciamo un esempio. Scegliendo di mantenere soltanto il $10 \%$ delle mail non-spam, avremmo circa $99$ campioni. Ciò porterà il rapporto tra le mail di spam e quelle non di spam a circa il $5 \%$, passando da una situazione di sbilanciamento estremo ad una di sbilanciamento moderato.

A valle di questa operazione, dovremo dare maggior peso ai campioni delle mail non-spam, usando un fattore tendenzialmente pari a quello che abbiamo usato in fase di downsampling. Nella pratica, ogni mail non-spam avrà un peso dieci volte superiore a quello che avrebbe avuto se si fosse utilizzato il dataset iniziale.

## Trasformazione dei dati

Il passo successivo nella preparazione dei dati è quello di *trasformare* un insieme (o la totalità) dei valori. Ciò avviene principalmente per due motivi.

Il primo è legato alla necessità di trasformazioni obbligatorie volte a garantire la compatibilità dei dati. Alcuni esempi:

* **conversione di feature non numeriche in numeriche**: in pratica, non possiamo effettuare operazioni sensate tra interi e stringhe, per cui dovremmo trovarci ad individuare un modo per permettere tale confronto;
* **ridimensionamento degli input ad una dimensione fissa**: alcuni modelli, come ad esempio le reti neurali, prevedono un numero fisso di nodi di input, per cui i dati in ingresso devono avere sempre la stessa dimensione.

Il secondo motivo è legato a delle trasformazioni opzionali che ottimizzino i risultati ottenuti durante l'addestramento. Ad esempio, potremmo dover portarli tutti i valori numerici all'interno di una stessa scala di valori (*rescaling*), oppure trasformarli in modo tale che ricordino una distribuzione normale (*normalizzazione*).

Per comprendere al meglio il motivo alla base di questa necessità, immaginiamo di avere un dataset che comprende due feature: l'età (che assume valori da $0$ a $100$) e reddito annuo (che supponiamo assuma valori da $10.000$ a $100.000$ €). Dando in pasto queste feature ad algoritmi che le combinano in qualche modo, l'età diventerà presto trascurabile rispetto al reddito, dato che quest'ultimo risulta essere di due o tre ordini di grandezza superiore. Di conseguenza, il modello trascurerà l'età in fase di analisi, utilizzando esclusivamente lo stipendio.

Da questa considerazione appare evidente come sia necessario portare tutti i dati ad una "base comune" prima di effettuare un addestramento. Per farlo, abbiamo a disposizione quattro tipi di trasformazione.

##### Scaling

Lo **scaling** prevede la conversione dei valori assunti da una feature in un range che va di solito tra $[0, 1]$ o $[-1, 1]$. La formula dello scaling è la seguente:

$$
y = \frac{(x - x_{min})}{(x_{max} - x_{min})}
$$

##### Clipping

La tecnica del **clipping** viene usata quando il dataset contiene degli *outlier*, ovvero alcuni campioni che divergono notevolmente dalle caratteristiche statistiche del resto dei dati. In questo caso, potremmo limitarci a rimuovere completamente tali valori mediante soglie statistiche, come i range interquartili in caso di distribuzione parametrica, o i classici $3 \sigma$ in caso di distribuzione normale.

##### Trasformazione logaritmica

Un'altra possibilità è quella di convertire i nostri valori in scala logaritmica, comprimendo un range ampio in uno più piccolo usando la funzione logaritmo:

$$
y = Log(x)
$$

##### Z-score

Un ultimo tipo di trasformazione prevede l'uso dello *z-score*, che prevede una riformulazione dei valori assunti dalla feature per fare in modo che questi aderiscano ad una distribuzione a media nulla e deviazione tandard unitaria. Per calcolarlo, si usa la seguente formula:

$$
y = \frac{x - \mu}{\sigma}
$$

dove $\mu$ è la media della distribuzione dei nostri dati, mentre $\sigma$ ne è chiaramente la varianza.

## Trasformazione dei dati categorici

Alcune delle nostre feature possono assumere esclusivamente valori *discreti*. Ad esempio, la feature "località" associato alle precipitazioni potrebbe riportare il CAP, mentre la feature "spam" nel nostro dataset di email potrebbe avere al suo interno un booleano. Queste feature sono dette *categoriche*, ed i valori ad esse associate possono essere sia stringhe sia numeri.

!!!note "Le feature categoriche di tipo numerico"
    Spesso, dobbiamo trattare feature categoriche che contengono valori numerici. Consideriamo ad esempio il CAP: rappresentandolo come un tipo numerico, il nostro modello potrebbe interpretare la distanza tra Bari ($70126$) e Taranto ($74121$) come pari a $3.995$, il che non avrebbe ovviamente senso.

Le feature categoriche devono però essere *convertite* in valori numerici, *mantenendo contestualmente il riferimento al significato originario*. Immaginiamo ad esempio di avere a che fare con una feature categorica che descrive il giorno della settimana. Il modo più semplice per passare da una rappresentazione puramente categorica ad una numerica è quella di usare un numero:

| Giorno | Rappresentazione numerica |
| ------ | ---------------- |
| Lunedì | 1 |
| Martedì | 2 |
| Mercoledì | 3 |
| Giovedì | 4 |
| Venerdì | 5 |
| Sabato | 6 |
| Domenica | 7 |

In questa maniera creeremo un dizionario, nel quale potremo accedere ad una chiave (*la rappresentazione numerica*) che rappresenterà un determinato valore (*il giorno*).

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

## Dati di training, test e validazione

L'ultimo passo nella preparazione del dataset è quello della *suddivisione* dei dati. In particolare, si destinano un certo quantitativo di dati per l'addestramento del modello, delegando la restante parte alla validazione dei risultati ottenuti; ciò è legato alla volontà di verificare la capacità di *generalizzazione* del modello, ovvero a quanto è in grado di "funzionare" il nostro algoritmo in caso di analisi di dati su cui non è stato addestrato.

Un rapporto molto usato in tal senso è quello che prevede che il $60\%$ dei dati sia usato per l'addestramento, un altro $20\%$ per il test del modello, ed il restante $20\%$ per la validazione dei risultati ottenuti.
