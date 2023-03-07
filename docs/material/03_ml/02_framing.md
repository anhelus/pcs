# 3.2 - Problem framing

La *definizione* di un problema è, come prevedibile, il primo passo per la sua risoluzione. Pensiamoci un attimo: se non abbiamo una chiara idea del problema da affrontare, *come possiamo pensare di risolverlo*?

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


DA QUI

## 13.2 - Comprendere i dati

La disponibilità di dati per l'analisi è alla base del machine learning. Per effettuare delle predizioni efficaci, infatti, abbiamo bisogno di usare dati dotati di un certo potere predittivo. In particolare, i dati devono essere:

* **abbondanti**: più esempi rilevanti abbiamo a disposizione, migliore sarà il nostro algoritmo risolutivo;
* **consistenti**: i dati devono essere raccolti usando criteri e strumenti ben determinati e coerenti. Ad esempio, un algoritmo meteo beneficierà di dati raccolti ogni mese per cento anni, piuttosto che di dati raccolti lungo lo stesso arco di tempo ma soltanto nel mese di luglio;
* **affidabili**: occorre valutare la sorgente dei nostri dati: siamo in grado di comprenderla e ritenerla affidabile, oppure è soltanto parzialmente sotto il nostro controllo?
* **disponibili**: dobbiamo assicurarci che i dati siano disponibili e completamente accessibili. Infatti, qualora ci siano delle parti del dataset parzialmente omesse, potrebbe essere preferibile trascurarle completamente in fase di analisi;
* **corretti**: molto spesso vi è una percentuale di dati con feature o label non corrette. Per quanto possibile, questi dati andrebbero isolati e rimossi in fase di preprocessing;
* **rappresentativi**: il dataset dovrebbe rappresentare in maniera completa il fenomeno sottostante, riflettendone accuratamente aspetti e caratteristiche. Utilizzare un dataset non rappresentativo inficierà negativamente le performance predittive del modello.

## 13.3 - Scegliere il modello

L'ultimo step è la scelta del tipo di modello da utilizzare, valutando ad esempio tra classificazione, regressione e clustering.

Per la nostra applicazione meteo, ad esempio, predire il quantitativo di pioggia che cadrà in un determinato luogo è un chiaro problema di regressione, nel senso che date $n$ variabili indipendenti cercheremo di predire una variabile dipendente in uscita.

!!!note "Regressione univariata e multivariata"
    In questo caso, la regressione si dice *univariata* a causa del fatto che si sta predicendo un'unica variabile dipendente. Se provassimo a predire (ad esempio) anche la temperatura, avremmo a che fare con una regressione *multivariata*.

Nel caso dell'applicazione mail, dato che stiamo cercando di valutare se un messaggio è classificabile o meno come spam, avremo a che fare con un problema di classificazione binaria.

Una volta determinato il tipo di problema, dovremo scegliere l'algoritmo da utilizzare e, in ultimo, la metrica con cui valutare i risultati. In particolare, quest'ultimo valore dipende molto dall'ambito applicativo: se, ad esempio, un errore del 10% potrebbe non essere estremamente importante nell'applicazione mail, questo diventerebbe estremamente rilevante e potenzialmente disastroso nell'individuazione di transazioni fraudolente.
