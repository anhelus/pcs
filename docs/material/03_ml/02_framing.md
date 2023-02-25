# 13 - Definire un problema di machine learning

Il primo passo nella risoluzione di un problema di machine learning è, per l'apponto, *definirlo*. In pratica, dovremo analizzare il problema, isolando gli elementi essenziali da utilizzare per la sua risoluzione: determineremo la fattibilità del problema, fornendo un insieme chiaro di *obiettivi* e *criteri* per la sua risoluzione. 

## 13.1 - Determinare l'obiettivo

Partiamo nella definizione del problema determinando il nostro obiettivo, ovvero definendo ciò che si vuole ottenere a valle della risoluzione del problema.

Ad esempio, potremmo voler calcolare le precipitazioni orarie in una determinata zona, oppure vorremmo definire un modo di individuare automaticamente lo spam in un'applicazione email, o ancora identificare delle transazioni fraudolente in applicazioni di tipo bancario.

Questo passo è fondamentale per un motivo: infatti, a volte il machine learning è visto come uno strumento "universale", in grado di risolvere qualsiasi problema a cui viene applicato. In realtà, questo non è vero, ed il machine learning è applicabile solo a determinati problemi, i quali alle volte possono essere anche risolti mediante approcci meno complessi.

Una volta verificato che il problema può essere risolto mediante approcci di machine learning, dovremo stabilire quale sia l'esatta natura del task che vogliamo portare avanti. Mantenendoci al caso precedente:

| Applicazione | Obiettivo del problema | Output del modello |
| ------------ | ---------------------- | ------------------ |
| Previsioni meteo | Calcolare le precipitazioni orarie in una determinata zona | Predizione delle precipitazione orarie |
| Spam detector | Individuare lo spam | Alert per un possibile spam |
| Prevenzione bancaria | Identificare transazioni fraudolente | Blocco transazioni sospette |

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
