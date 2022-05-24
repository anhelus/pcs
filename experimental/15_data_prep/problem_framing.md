La prima parte di un problema di Machine learning è lo stabilire il problemma. Questo è il processo dove si analizzaz un problema per isolare gli elementi individuali che devono essere utilizzati per risolverlo. Il probem freaming ci aiuta a determinare la fattibiiltà del problema e foirnoisce uninsieme chiaro di obiettivi e criteri per il soddisfacimento del problema. Quando si considera una solzuione di ML, il problem framing efficace può stabilire se il nostro prodotto ha soccesso o meno.

ad un alto livello, determinare il problema di machine learning avviene in due step distinti:

1. determinare se il machine learning è l'approccio corretto per la risolzuione del problema
2. riformulare il problema in termini di machine learning

## comprensiopne del problema

per copmprendere il problema, dobbiamo effettuare le seguenti task:

1. detemrinare il goal per il prodotto che stiamo sviluppando
2. determianre se il gola può essere risolto al meglio usando il machine learning
3. verificare che si abbiano i dati richiesti per addestrare un modello

## determinare l'obiettivo

Iniziamo determinano il nostro obiettivo in termini di machine learning. L'obiettivo è rispondere alla domanda: "cosa sto cercando di ottenerre".

Ad esempio:

| Applicazione | Obiettivo |
| ------------ | --------- |
| Applicazione meteo | Calcolare le precipitazioni orarie in una determinata zona. |
| Applicazione mail | Individuare lo spam |
| Applicazione bancaria | Identificare transazioni fraudolente |
| Applicazione vidoe | Raccomandare agli utenti dei video |

Alcuni vedono il machine learning come uno strumento "universale", applicabile a tutti i problemi. In realtà, il machien learning è un tool specialistico disponibile solo per determinati problemi. Non vogliamo implementare una soluzione di machine learning complessa quando ve ne è una più semplice che non usa il machine learning ma che funzionerà ugualmente.

## dati

i dati sono alla base del machine learning. per effettuare delle buone predizioni, dobbiamo avere dei dati che contengano feature con potere predittivo. I dati devono essere:

* abbondanti: più esempi rilevanit abbiamo nel dataset, migliroe sarà il nostro prroblema
* consistenti ed affidabili: avere dati collezionati in maneira consistenti ed affidabili produce un modello migliroe. Ad esempio, un modello meteo beneficia dai dati raccolti in molti anni da strumenti affidabili.
* fidati: capiamo da dove vengono i nostri dati. Saranno da sorgenti di cui ci fidiamo e sotto il nostro controllo, oppure da sorgenti su cui non abbiamo molto controllo, come ad esempio  dati provenienti anche da altri sistemi di ML?

* disponibilòitàù:  dobbiamo assicurarci ce tutti gli input siano disponibili nel momento della predizione nel formato corretto. Se sarà difficile ottenere i valori di certe feature nel momento della predizione, queste vanno omesse dal nostro dataset.
* correttezza: in grossi dataset, è inevitabile che alcuni label abbiano i valoiri non corretti, ama se più di una certa percentuale di label sono incorrette, il modello produrràù delle predizioni non ottimali.
* rappresentativi;: il dataset dovrebbe essere quanto più rappreesntativo possibile del modno relael. In altre parole i dataset dovrebbero riflettere accuratamente gli eventi, i comprotamenti utenti ed il fenomeno del mondo reale modlelato. Addestrare un dataset non rappreesntativo può di nuovo inficiare le performacne quando al modello viene chiesto di fare delle predizioni sul mondo reale.

## potere predittivo

per far sì che un modello faccia buone predizioni, le feature nel nostro dataset dovranno avere del potere predittivo. Più una feature è correlata ad una label, più è facile che quest'ultima venga predetta.

Ad esmpio, in un dataset meteo, feature come temperatura e nuvolosità riusciranno a predire meglio la possibilità dio pioggia rispetto al giorno della settimana.

E' importante notare che il potere predittivo di una feature può variare a causa di cambi di contesto o dominio. Ad esempio, in un'app video, una feature come upload_date può essere poco correlata *generalmente* con la label, anche se negli esempi di video su gaming potrebbe essere più correlata.

Determinare quali feature abbiano potere predittivo può essere un processo lungo e dispendioso: potremmo ad esempaio automatizzarlo usando algoritmi di correlazione, che forniscono un valore numerico per analizzare il potere predittivo di una featrure.

## definire l'usicta ideale e l'obiettivo del mdoello

dopo aver verificato che il problema può essere risolto con il MLO, dobbiamo stabilire q    ual è+ l'uscita ideale, ovvero qual è il task esatto che vogliamo efettuare. Ad esempio:

| Applicazione | Obiettivo | Obiettivo del modello |
| - | - | - |
| Applicazione meteo | Calcolare le precipitazioni orarie in una determinata zona. | Predizione delle precipitazione orarie |
| Applicazione mail | Individuare lo spam | Avvertire l'utente di un probabile spam. |
| Applicazione bancaria | Identificare transazioni fraudolente | Meccanismi di protezione in caso di transazioni sospette |
| Applicazione vidoe | Raccomandare agli utenti dei video | Predire se l'utente cliccherà su un video |

## scelta del modello

una voklta individuato l'obiettivo, dovremo scegliere il tipo di modello, tra classificazione (chye predice a quale categoria appartengono i dati), regressione (che predice che valore di output sarà associato ad una determianta combinazione di feature di inpuit), o altro ancora.

Per l'applicazione meteo, la predizione dei mm di pioggia è un chiaro problema di regressione *univariata*, nel senso che date n variabieli iondipendenti cerchiamo di rpedire una variabiel dipendente in uscita. Ovviamente,s e stessimo cercando di predire anche la temperatura, la regressione diventerebbe *multivariata*, in quanto avremmo più di una variabile dipendente da predire.

Per l'applicazione di spam, stiamo cercando di valutare se una mail è o meno fraudolenta, questo rappresenta un tipico esempio di classificazione binaria.

se invece volessimo individuare gli animali in un'immagine, ci troveremmo in un possibile problema di classificazione multiclasse, che potrebbe essere a singola label se dovessimo stabilire un unico tipo dii animale per la figura (ad esempio, quello più presente), o multi-label se ad esempio dovessimo individuare tutti gli animali in una figurea.

in ultimo, dobbiamo definire come valutare il nostro problema. molto spesso, si utilizza l'accuratezza di rpedizione su dati che il modello nmon ha mai visto; in questo modo si valuta la sua capacità di generalizzare, ovvero di non "affezionarsi" troppo ai dati su cui è stato addestrato. All'interno di questo valroe di accuratezza, possiamod efinire empiricamente delle soglie, che variano da applicazione ad applicazione: ad esempio,s e 2 volte su 10 può essere accettabile sbagliare l'animale visualizzato, non lo è sbagliare l'utente in un sistema di autenticazione biometrico.


