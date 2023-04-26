# 3.2 - Definizione del problema

La *definizione di un problema* è, come prevedibile, il primo passo per la sua risoluzione. Pensiamoci un attimo: se non abbiamo una chiara idea del problema da affrontare, *come possiamo pensare di risolverlo*?

Il primo step per affrontare il problema è quindi analizzarlo, isolando gli elementi essenziali da utilizzare nella sua risoluzione: andrà fatto uno *studio di fattibilità*, determinando se il problema è risolvibile o meno; saranno poi forniti un chiaro insieme di *obiettivi*, assieme ai *criteri* ed ai *vincoli* da rispettare nella risoluzione. Approfondiamo questi aspetti.

## Analisi del problema

Partiamo analizzando il problema, definendo quindi sia i dati in ingresso, sia quello che vogliamo ottenere a valle della risoluzione. Facciamo un paio di esempi concreti:

* **Predittore di precipitazioni**: il nostro primo problema prevede la predizione delle precipitazioni orarie. In questo caso, l'obiettivo è quello di creare un software/hardware che, data la collezione storica delle precipitazioni, sia in grado di predire l'entità delle stesse, a partire dalla zona e dal periodo dell'anno, con un buon grado di confidenza.
* **Spam detector**: il nostro secondo problema ci chiede di capire se una mail è di spam. L'obiettivo sarà quindi la creazione di un software che, una volta ricevuta una mail, sia in grado di estrapolarne le informazioni che permettano di classificarla come legittima (o meno).

Una possibile schematizzazione è nella seguente tabella.

| Applicazione | Obiettivo del problema | Output atteso | Input |
| ------------ | ---------------------- | ------------- | ----- |
| Previsioni meteo | Calcolare le precipitazioni orarie in una determinata zona | Predizione delle precipitazione orarie | Storico delle precipitazioni, località, situazione attuale |
| Spam detector | Individuare lo spam | Alert per un possibile spam | Mail sotto analisi, esempi di mail di spam e legittime |

Una volta individuati obiettivo, input ed output, dovremo verificare che il problema sia risolvibile mediante un algoritmo di machine learning. In particolare, dovremo verificare la presenza di un'adeguata quantità di dati rappresentativi del fenomeno osservato, e decidere quale approccio utilizzare tra classificazione, regressione e clustering. In questa nostra analisi, inoltre, dovremo tenere conto del cosiddetto [*rasoio di Occam*](https://it.wikipedia.org/wiki/Rasoio_di_Occam): infatti, alle volte, potrebbe *non* essere necessario utilizzare un algoritmo di machine learning per risolvere il problema sotto analisi.

!!!note "Machine learning? No, grazie!"
    Ad eempio, nonostante un semplice sistema massa - molla - smorzatore possa essere modellato tramite il machine learning, è decisamente più produttivo usare delle semplici relazioni fisiche.

Una volta analizzato il problema, e verificata la necessità (e possibilità) di usare il machine learning, dovremo passare alla fase successiva, che prevede l'analisi e lo studio dei dati a nostra disposizione.

## Comprensione dei dati

La disponibilità di un'adeguata quantità di dati caratterizzanti il fenomeno sotto analisi sono alla base del corretto funzionamento degli algoritmi di machine learning. Per effettuare delle predizioni efficaci, infatti, abbiamo bisogno di usare dati di *quantità* e *qualità* adeguate, in grado quindi di garantire un elevato potere predittivo. In particolare, i nostri dati dovranno essere:

* **abbondanti**: più esempi rilevanti abbiamo a disposizione, maggiori saranno gli aspetti che potremo caratterizzare e, di conseguenza, migliore sarà il potere risolutivo del nostro modello;
* **consistenti**: raccogliere dati usando criteri e strumenti ben determinati e coerenti permetterà una migliore campagna di acquisizione. Ad esempio, il modello meteorologico ottenuto usando dati raccolti ogni giorno per cento anni sarà più preciso di quello ottenuto raccogliendo dati una volta l'anno per lo stesso periodo di tempo;
* **affidabili**: la sorgente dei nostri dati dovrà essere affidabile. Ad esempio, l'igrometro ed il barometro dovranno essere ben tarati ed accessibili, mentre l'insieme di email usate per caratterizzare lo spam dovrà essere acquisita da utenti verificati;
* **disponibili**: dovremo verificare che non vi siano parti del nostro dataset completamente omesse e, qualora queste siano presenti, che non riguardino aspetti fondamentali e non trascurabili del fenomeno sotto analisi. Ad esempio, un dataset nel quale i valori di temperatura, umidità e pressione sono presi soltanto nei giorni soleggiati avrà ben poca utilità nella predizione delle precipitazioni;
* **corretti**: i dati andrebbero verificati in termini sia di valori delle feature, che potrebbero essere errati a causa di starature o malfunzionamenti dei sensori, oppure ancora in caso di perdita di dettagli del testo analizzato, sia di label assegnate. In quest'ultimo caso, infatti, un esperto di dominio potrebbe erroneamente contrassegnare come spam una mail legittima, o viceversa, e ciò andrebbe ovviamente ad inficiare le performance del nostro modello;
* **rappresentativi**: il dataset dovrebbe descrivere in maniera completa il fenomeno sottostante, riflettendone accuratamente aspetti e caratteristiche. Utilizzare un dataset non rappresentativo inficierà negativamente le performance predittive del modello.

## Scelta del modello

L'ultimo step è la scelta del tipo di modello da utilizzare, valutando ad esempio tra classificatore, regressore ed algoritmo di clustering.

Per la nostra applicazione meteo, ad esempio, predire il quantitativo di pioggia che cadrà in un determinato luogo è un chiaro problema di regressione, nel senso che date $n$ variabili indipendenti cercheremo di predire una variabile dipendente in uscita.

!!!note "Regressione univariata e multivariata"
    In questo caso, la regressione si dice *univariata* a causa del fatto che si sta predicendo un'unica variabile dipendente. Se provassimo a predire (ad esempio) anche la temperatura, avremmo a che fare con una regressione *multivariata*.

Nel caso dell'applicazione mail, dato che stiamo cercando di valutare se un messaggio è classificabile o meno come spam, avremo a che fare con un problema di classificazione binaria.

Una volta determinato il tipo di problema, dovremo scegliere l'algoritmo da utilizzare sulla base dei dati, oltre che la metrica con la quale valutare i risultati ottenuti (in accordo al modello scelto). In particolare, la metrica, ed il valore da essa assunto, dipendono strettamente dall'ambito applicativo: se, ad esempio, un errore del $10\%$ potrebbe non essere estremamente importante nell'applicazione mail, questo diventerebbe estremamente rilevante (e potenzialmente pericoloso) nella stima dei millimetri di pioggia che cadranno in una certa zona.

## Problemi multiclasse e multioutput

Esistono diverse tipologie di problemi sulla base dell'ordine sia dei nostri dati, sia delle nostre label. In particolare, distinguiamo i seguenti.

##### Classificazione multiclasse

In questo task di classificazione, i dati possono appartenere ad *una ed una sola* tra più di due classi. Un esempio è un classificatore che identifica il tipo di frutta mostrato in un'immagine, discernendo tra mele, pere ed uva.

##### Classificazione multioutput

In questo tipo di classificazione, ogni campione è associato ad $m$ label prese da $n$ diverse classi, con $0 < m \leq n$. Un esempio può essere la predizione dei topic di riferimento di un documento, presi tra *scienza*, *tecnologia*, *cultura* e *religione*: possono esserci infatti documenti che parlano sia di cultura che di religione, o anche di religione e scienza, e così via.

##### Classificazione multiclasse/multioutput

In questo tipo di classificazione, nota anche come *multitask classification*, ad ogni campione è associato un insieme di proprietà, per ciascuna delle quali sarà possibile scegliere tra più di due classi. Per fare un esempio, immaginiamo di voler associare i parametri *specie* e *razza* ad una serie di immagini di grandi felini: la specie potrà variare tra *leone*, *leopardo*, *tigre*, e così via, mentre la *razza* varierà per ciascuna specie, ad esempio, *leone senegalese* e *leone indiano* per i leoni, *tigre siberiana* e *tigre cinese meridionale* per le tigri, e via dicendo.
