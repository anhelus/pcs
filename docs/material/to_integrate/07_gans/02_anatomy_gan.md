https://developers.google.com/machine-learning/gan/gan_structure?hl=en

# Struttura di una GAN

Una generative adversarial network (GAN) ha due parti

* il generator apprende a genearere dati plausibili. Le istanze generate diventano degli esempi *negativi*é per il discriminator.
* il *discriminator* apprende a distringuere dai dati falsi del genratore da quelli reali. Penalizza quindi il generatore per produrre dati non plausibioli.

Quando inizia l'addestramento, uil generator produce dei dati ovviamente falsi, e il discriminatro è in grado di stabilire facilmente che non sono veri.

BAD_GAN

Man mano che l'addestramento procede, il genrator migliora il suo output, producendone uno in grado di ingannare il discriminator:

OK_GAN

Se l'addestramento va bene, il discrimnator non è più in grado di dire la differenza tra dato reale e dato falso. Inizia quindi a classificare il dato falso come real, e la sua accuracy diminuisce.

GOOD_GAN

Ecco uno schema del'intero sistema:

GAN_DIAGRAM

Sia il generator sia il discriminator sono delle reti neurali. L'output del generator è connesso direttamente all'input del discriminator. Attraverso la backpropagation, la classificazione del discriminator fornisce un segnale che il generator usa per aggiornare i suoi pesi.

Vediamo i singoli pezzi del sistema in dettaglio.

## Discriminator

Il discriminator in una GAN è semplicemente un classificatore. Prova a distinguere i dati reali dai dati creati dal generator. Può usare una qualsiasi architettrura di rete appropriata al tipo di dati da classificatore.

GAN_DIAGRAM_DISCRIMINATOR

### Dati di training del discriminator

I dati di training del discriminator vengono da due sorgenti:

* istanze di dati reali, come foto vere di persone. Il discriminator usa queste istanze come campioni positivi durante l'addestramento
* istanze di dati falsi, create dal generator. Il discriminatore usa queste istanze come campioni negativi durante l'addestramento

Nella figura precedente, i due box "Sample" rappresentano queste due sorgenti dati che vengono mandate nel discriminator. Durante l'addestramenot del discriminator, il generator non veien addestrato. I suoi pesi rimangono costanti mentre produce esempi per l'addestramento del discriminator.

### AAddestramento del discriminator

Il discriminatro connette due funzioni di costo. Durante l'addestreamnto, viene ignorata la loss del generator, ed utilizzata soltanto quelal del discriminator. Usiamo la generator loss durante l'addestramento del generator.

Duratne l'addestramento del discriminator:

1. il discriminator classifica sia dati reali che falsi dal generator
2. la discriminator loss penalizza il discriminator per aver mal classificato un'istnaza reale come falsa o una falsa come reale
3. il discriminator aggiorna i suoi pesi mediante backpropagation dalla discriminator loss attraverso la discrimiantor network

## Generator

Il generator apprende a creare dei dati falsi incorporando il feedback del discriminator. Apprende a fare in modo che il discriminator classifichi il suo output come "vero".

L'addestramento del generator richiede una integrazione più stretta tra il generator ed il discriminator di quella richiesta dall'addestramento di qquest'ultimo. La porzione del GAN che addestra il generator include:

* input casuale;
* la rete generator, che trasforma l'input casuale in un'istanza dei dati;
* il discriminator, che classifica i dati generati;
* l'output del discriminator;
* la loss del generator, che penalizza il generator per non riuscire ad ingannare il discriminator.

GAN_DIAGRAM_GENERATOR

## Random Input

Le reti neurali hanno bisogno di qualche tipo di input. Normalmente mandiamo in input dei dati con i quali vogliamo fare qualcosa, come un'istanza che vogliamo classificare o predire. Ma cosa usiamo come input per una rete che madnda in output nuove istanze dati?

Nella sua forma più basilare, una GAN prende del rumore casuale come input. Il generator quindi trasforma questo rumore in un output significativo. Introducendo del rumore, possiamof are in modo che la GAN produca un'ampia varietà di dati, scegliendo da diversi posti nella distribuzione obiettivo.

Gli esperimenti suggeriscono che la distribuzione del rumore non conta molto,. per cui possiamo scegleire qualcosa che è di facile campionamento, come una distribuzioen uniforme. Per convenienza, lo spazio dal quale il rumore viene campionato è di soltio di dimensioni più picole dello spazio di output.

### Usare il discriminator epr addestrare il generator

Per addestrare una rete neurale, alteriamo i pesi della rete per ridurre l'errore sul suo output. Nella nostra GAN, tuttavia, il genratore non è direttamente connesso alla loss che vogliamo modificare. Il generatore manda il suo output al discriminatore, e questo produce l'output che vogliamo influienzare. La loss del generatore penalizza il generatore per produrre un campione che la rete discriminativa classifica come falso.

Questo pezzo extra di rete deve essere incluso nella backpropagation,. La backoproagation modifica ogni peso nella direzione corretta calcolando l'impatto del peso sull'output - come l'ouptut cambia se cambiamo il peso., Ma l'impatto di un peso del generator dipende dall'impatto dei pesi del discriminator. Per cui la backpropagaion iniza con l'output, e va indietro dal discriminator nel genertator.

Allo stesso tempo, non vogliamo che il discriminator cambi durante l'addestreamneto del generator. Provare a colpire un bersaglio in movimento renderebbe il problema ancora più compelsso per il generator.

Di conseguenza, addestriamo il generator con la seguente procedura:

1. campioniamo del rumore casuale
2. produciamo l'output del generatpor dal rumore casuale campionato
3. otteniamo una classificazione "reale" o "falso" per l'output del generator
4. calcoliamo la loss dalla classificazione del discrimiantor
5. effettuiamo la backpropatgation attraverso il discriminator ed il generator per ottenere i graidenti
6. usiamo i gradienti per cambiare solo i pesi del generator

Questa è una singola iterazione dell'addestramento del generator. nella sezione successiva vediamo come mettere insieme il training del generator e del discriminator.

## GAN training

Dato che una GAN contiene due reti addestrate separametne, il suo algoritmo di training deve essere in grado di trattare due complicazioni:

* la GAN deve essere in grado di mettere assieme due tipi diversi di addesteramnto (geneartor e discriminator)
* la convergenza della GAN non è facile da identificare

### Alternare l'addestramento 

Il generaotr ed il discriminator hanno diversi processi di trainign. Come facciamo quindi ad addestrare la GAN in una botta?

L'addestramento di una GAN procede su periodi alternati:

1. il discriminator vioene addestrato per una o più epochje
2. il generator viene addestrato per una o più eopche
3. si ripetopono i passi 1 e 2 per continare ad addestare il gnerator ed il discriminator

Manteniamo il generator costante durante la fase di addestramento del discrimiantor. Man mano che l'addestramento del discrimminator prova a capire come distinguere i dati reali da quelli falsi,. deve comprendere come riconoscere i problemi del generator. Questo è un problema differnete per un generator addestrato rispetto ad un generator non addestrato che produce output casuali.

Inm modo simile, manteniamo il discrimiantor costante durante loa fase di addestramento del generator. Altrimenti il generator proverebbe a colipire un "bersaglio mobile", e potrebbe non convergere mai.

E'm questo andirivieni che permette alle GAN di affrontare dei problemi generativi altrimenti non affronttabili. OTTENIAMO UN TOEHOLD nel difficile rpoblema generativo iniziando con un problema di classificazione molto più semplice. Di converso, se non possiamo addestrare un classificatore a dire la difrenza tra dati reali e generati anche per l'outpu inizializzato casualmente, non possiamo fare in modo che l'addestrramento della GAN possa iniziare.

### Converegenza

Man mano che il genrato migliroa l'addestarmaneot, le performance deld sicrimionator peggiorano percheè il discrimantor non è in garado di dire la differena tra ciò che è vero e falso. Se il generator ha successo al 10=%$, allora il ddiscriminator ha un'accuracy del 50%. Nei fatti, il discrimiantor sta lanciando una moneta per fare le sue predizioni.

Questa progerssione pone un probelma per la convergenza della GAN: il feedback del discriminator diventa meno significativo nel tempo. Se al GAN continua ad addestrarsi oltre al punto in cui il discrimiantor sta dando risposte compeltamente casuali, allora il generator inizia ad addestarsi su feedback spazzatura, e al sua qualità pouò diminiurei.

Per una GAN la convergenza non è quindi mai uno stato stabile.
