# XX - Le Generative Adversarial Networks

Le *Generative Adversarial Networks* (*GAN*) rappresentano una delle più interessanti tra le recenti innovazioni in ambito deep learning. Le GAN sono un modello di tipo *generativo*: creano, infatti, nuovi dati che "ricordano" quelli usati per l'addestramento della rete. Ad esempio, una GAN può essere addestrata a creare dei volti che, in realtà, non appartengono ad una persona reale.

TODO: ESEMPIO VOLTI GAN

Una GAN è in grado di ottenere questo livello di realismo facendo "lavorare in parallelo" un *generatore*, che impara a produrre gli output richiesti, ed un *discriminatore*, il cui compito è discernere i dati "veri" da quelli mandati in output dal generatore. La GAN sarà ritenuta addestrata con successo quando il generatore sarà in grado di ingannare il discriminatore.

## XX.1 - I modelli generativi

Facciamo un passo indietro. Cosa si intende per *modello generativo*?

In breve, un modello generativo è un modello statistico in grado di generare nuove istanze appartenenti ad un certo dataset. Di contro, i *modelli discriminativi* (che abbiamo usato finora) permettono di discriminare tra diverse classi di dati.

!!!note "Cani e gatti"
    Immaginiamo un dataset fatto di foto di cani e gatti. Un modello discriminativo ci permette di capire se la foto rappresenta un cane o un gatto; un modello generativo ci permette di generare la foto di un cane o, in alternativa, quella di un gatto.

Più formalmente, supponiamo di avere una coppia di insiemi $(X, Y)$, dove $X$ sono le istanze del nostro dataset, ed $Y$ le label ad esse assegnate. Allora:

!!!quote "Modelli generativi"
    I modelli generativi descrivono la probabilità congiunta $P(X, Y)$ o, nel caso di dati non etichettati, la probabilità $P(X)$.

!!!quote "Modelli discriminativi"
    I modelli discriminativi descrivono la probabilità condizionale $P(Y|X)$.

Appare chiaro come i modelli generativi descrivano la distribuzione dei dati, e ci dicano quanto sia probabile un dato esempio. Ad esempio, un modello che predice la parola successiva in una certa frase è tipicamente generativo, perché assegna una probabilità ad una certa sequenza di parole. Di converso, un modello discriminativo ci dice solo quanto è probabile che una certa label sia applicata ad una data istanza.

Un modello discriminativo ignora la questione di se una data istanza è probabile, e ci dice solo quanto probabile è che una label sia applicata ad un'istanza.

Notiamo che questo è una definizione molto generale. Ci sono molti tipi diversi di modelli generativi. Le GAN sono soltanto uno.

## Modellare le probabilità

Non tutti i tipi di modelli devono restituire un numero che rappresenta una probabilità. Possiamo modellare la distribuzione dei dati che immita quella distribuzione.

Ad esempio, un classificatore discriminativo come un albero decisionale può etichettare un'istanza senza assegnare una probabilità a quella label. Un classificatore di questo tipo sarebbe sempre un modello perché la distribuzione di tutti i label predetti modellerebbero la distribuzione reale delle label nei dati.

In modo simile, un modello generativo può modellare una distribuzione producendo dei falsi convincenti che sembrano essere estratti da quella stessa distribuzione.

## I modelli generativi sono difficili

I modelli generativi affrontano un task più difficile di quello gestito dai modelli discriminativi analoghi. I modelli generativi devono modellare infatti più dati.

Un modello generativo per le immagini può catturare le correlazioni come come "cose che sembrano navi dovrebbero probabilmente apparire vicino a cose che sembrano acqua" e "gli occhi probabilmente non saranno sulla fronte". Queste sono distribuzioni complicate.

In contrasto, un modello discriminativo può apprendere la differenza tra "nave" e "non nave" guardando soltanto pochi pattern. Può ignorare molte delle correlazioni che il modello generativo deve invece tenere in conto.

I modelli discriminativi provano a disegnare dei confini nello spazio dei dati, mentre i modelli generativi provano a modellare come i dati sono disposti nello spazio. Ad esempio, il seguente diagramma mostra i modell discriminativi e generativi per le cifre scritte a mano:

TODO: DIAGRAMMA

Il modello discriminativo prova ad individuare la diferenza tra gli 0 e gli 1 scritti a mano tracciando una riga nello spazio dei dati. Se fa le giuste assunzioni sulla linea, può distinguere gli 0 dagli 1 senza doiver modellare dove le istanze sono piazzate nello spazio dei dati su ogni lato della linea.

In contrasto,il modello generativo prova a produrre degli 1 e degli 0 convinceenti generando dei numeri che cadono vicino alle controparti vene nello spazio dei dati. Deve modellare la distribuzione attraverso lo spazio dei dati.

Le GAN offrono un modo efficace di addestrare questi modelli ricchi che ricordano una distribuzione reale. Per capire comue funzionano dobbiamo capire la struttura base di una GAN.

## Test

Abbiamo il test della QI per 1000 persone. Modelliamo la distribuzione dei punteggi dei QI mediante la seguente procedura:

1. lanciamo tre dadi a sei facce
* moltiplichiamo il risultato per una costante w
3. ripetiamo 100 volte e prendiamo la media dei risultati

Proviamo diversi valori per w fino a che il risultato della procedura è uguale alla media dei punteggi QI reali. Il modello è genrativo o discriminativo?

Not enough information to tell.
This model does indeed fit the definition of one of our two kinds of models.
Try again.
Discriminative model
Incorrect: an analogous discriminative model would try to discriminate between different kinds of IQ scores. For example, a discriminative model might try to classify an IQ as fake or real.
Try again.
Generative model
Correct: with every roll you are effectively generating the IQ of an imaginary person. Furthermore, your generative model captures the fact that IQ scores are distributed normally (that is, on a bell curve).
Correct answer.

Un modello restituisce una probabilità quando gli diamo un'istanza dei dati. E' generativo o discriminativo?

Not enough information to tell.
Both generative and discriminative models can estimate probabilities (but they don't have to).
Correct answer.
Generative model
A generative model can estimate the probability of the instance, and also the probability of a class label.
Try again.
Discriminative model
A discriminative model can estimate the probability that an instance belongs to a class.
Try again.


## Anatomia di una GAN

Una GAN ha due parti:

* il generatore, che apprende a generare dati plausibili. Le istanze generate divetano degli esempi negativi per il discriminatore
* il discriminatore che apprende a distinguere i dati falsi del genratore dai dati reali. il discriminatore penalizza il genaeratore che produce risultati poco plausibili.

Quando inizia il training, il generatore produce ovviamente dati falsi, ed il discriminatore impara rapidamente a dire che è falso:

TODO: ESEMPIO

Man mano che l'addestramento procede, il generatore produce degli oiutput che possono man mano sempre più ingannare il discriminatore:

TODO IMMAGINE

Infine, se l'addestramento del generatore va a buon fine, il discriminatore non riesce a dire la differenza tra reale e falso. Inizia a classificare i dati falsi come reali, e l'accuracy diminuisce.

TODO IMMAGINE

Ecco uno schema dell'intero sistema

https://developers.google.com/machine-learning/gan/gan_structure?hl=en

Sia il generatore sia il discriminaotre sono reti neurali. L'output del generatore è connesso direttamente all'input del discriminatore. Attraverso la backpropagation, la classificazione del discriminatore fornisce un segnale che il generatore usa per aggiornare i suoi pesi.

## Il discriminatore

Il discriminatore in una GAN è semplicemente un classificatore. Prova a distinguere i dati reali dai dati creati dal generatore. Può usare una qualsiasi archiettura di rete appropriata al tipo di dati da classificare.

## Dati di training per il discriminatore

I dati di training per il discriminatore provengono da due sorgenti:

* istanze di dati reali, come vere immagini di persone. Il discriminatore usa queste istanze come campioni positivi durante il training.
* istanze di dati falsi creati dal generatore. Il discriminatore usa queste istazne come campioni negativi durante il training.

Nella figura precedente, le due box "Samples" rappresentano quesete due sorgenti dati chee vengono inviate al discriminatore. Durante l'addestramento del discriminatore, il generatore non viene addestrato. I suoi pesi rimangono costanti, mentre produce i campioni su cui il discrimniatore verrà addestrato.

## Addestramento del discriminatore

Il discriminatore si connette a due funzioni di costo. Durante l'addestreamento del discrimiantore, questo ignora la loss del generatore e usa soltanto la sua. Usiamo la loss del generatore durante l'adestramento del generatore.

Durante il trainign del discriminatore:

1. il discriminaotre classifica sia i dati reali sia quelli falsi dal generatore
2. la loss del discrimiantore penalizza il discriminatore per classificare male un'istanza vera come falsa o una falsa come vera
3. il discriminaotre aggiorna i suoi pesi mediante la backgpropagation dalla loss del discrimiantore attraverso la rete dello stesso

## il generatore

la parte del generatore di una GAN apprende a creare dei dati falsi incororando il feedback dal discriminatore. Apprende a fare in modo che il discriminatore classifichi il suo output come reale.

L'addestramento del generatore richiede un'integrazione più strateta tra il genratore ed il discriminatore rispetto a quella raggiunta durante il training del discriminatore. La porzione della GAN che addestra il generatore include:

* inpuyt casuale
* rete generatrice, che trasforma l'input random in un'istanza dei dati
* rete discriminatorice, che classifica i dati generati
* output del discriminatore
* loss del generatore, che penalizza il generatore se questo non riesce ad imbrogliare il discriminatore

## input casuale

le reti neurali hanno bisogno di un qualche tipo di input. Normalmente daimo in input dati con i quali vogliamo fare qualcosa, come un'istanza che vogliaomo classificare o su cui vogliamo effettuare una predizione. Ma cosa usiamo come input per una rete che manda in output delle nuove istanze dati?

Nella sua forma base, una GAN prende del rumore casuale come input. Il generatore quindi trasforma questo rumore in un output significativo. introduciendo rumore, possiamo fare in modo che la GAN produca un'ampia quantità di dati, campionati da diversi posti nella distribuzione obiettivo.

GLi espeirmenti suggeriscono che la distribuzione del rumore non conti molto, per cui possiamo scegliere qualcosa da cui sia facile campionare, come una distribuzione unifoirme. Per convenienza, lo spazio dal quale il rumore viene campionato è spesso di dimensioni più piccole rispetto alla dimensionalità dello spazio in output.

## usare il discriminatore per addestrare il generatore

Per addestrare una rete neurale, atleriamo i pesi dellar ete per ridurre l'errore o la perdita del suo output. Nella nostra GAN, tuttavia, il generatore non è direttamente connesso alla loss che stiamo provando ad influenzare. La loss del generatore penalizza il generatore per produrre unc ampione che la rete discriminativa classifica come falso.

Questo pezzo extra di rete deve essere incluso nella backpropagation. La backpropagation modifica ogni peso nella direzione giusta calcolando l'impatto del peso sull'output - come l'output cambierebbe se cambiamo il peso. Ma l'impatto del peso di un generatore dipende dall'impatto dei pesi del discriminatore nel quale va ad inseririsi. Per cui la backpropagation inizia all'usicta e va indietro attraverso il discriminatore nel generatore.

Allo stesso tempo, non vogliamo che il discrimiantore cambi durante l'addestramento del generatore. Provare a colpire un target in movimento renderebbe un problema duro ancora più duro per il generatore.

Per cui addestriamo il generatore ocn la seguente procedura:

1. campioniamo rumore casuale
2. produciamo l'output del generatore da rumore campionato casualmente
3. otteneiamo delle classificazioni reali o false per l'output del generatore
4. calcoliamo la loss dalla classificazione del discriminatore
5. effettuiamo la backpropagation attraverso il discriminatore ed il generatore per ottenere i gradienti
6. usiamo i gardienti per cambiare soltanto i pesi del generatore

Questa è un'iterazione del training del generatore. Nella prossima sezione vedremo come unire il training del generatore e del discrimiantore.

## GAN Training

Dato che una GAN contiene due reti addestrate separatamente, i suoi algoritmi di training devono risolvere due complicazioni:

* le GAN devono tenere in conto due diversi tipi di training (generatore e discriminatore)
* la convergenza della GAN è difficile da identificare

## Alternare i training

Il generatore ed il discrimanatore hanno diversi processi di training. Per cui come addestriamo la GAN?

L'addestramento della GAN avviene a fasi alterne:

1. il discriminatore si addestra per una o più epoche
2. il generaotre si addestra per una o più epoche
3. ripetiamo gli step 1 e 2 per continuare ad addestrare le reti di generazione e discriminazione

Manteniamo il generatore costante durante la fase di disriminazione. Man manco che il training del discriminatore prova a capire come distinguere i dati reali da quelli falsi, deve apprendere a come riconsocere le "colpe" del generatore. Questo è un problema differente per un genereatore addestrato piuttosto di uno non addestrato che produce output casuale.

In modo simile, dobbiamo mantenere il discrimninatore costante durante la fase di training del generatore. Altrimenti il generatore proverà a colpire un bersaglio in movimento, e potrebbe non convergere.

E' questo andiriviene che permetete alle GAN di affrontare dei problemi altreimneit intrattabili. Possiamo entrare nel problema complesso di genrazione iniziando con un problema di classificazione molto più semplice. Di converso, se non possiamo addestrare un classificatore a dire la differenza tra dati reali e generati anche per dati generati casualmente, non possiamo iniziare il training della GAN.

## convergenza

Man mano che il generatore migliora l'addestramento, le performance del discriminatore migliora perché il discrimnaotre non può facilmente dire la differenza tra reale e falso. Se il generatore ha un successo "perfetto"; allora il discriminatreo ha un'accuracy del 50%. Nei fatti, il discriminatore lancia una moneta per fare la sua predizione.

Questa progressione pone un problema per la convvergenza dell'intera GAN: il feedback del discriminaotre diventa meno sigificativo nel tempo. Se la GAN continua ad addestrarsioltre il punto dove il discriminaotre sta dando dei feedback completamente casuali, allora il generatore inizia ad addestrarsi su feedback non buoni, e la sua qualità può collassare.

Per una GAN, la convergenza è spesso un valore "mobile", non stabile.

## Loss functions

Le GAN provano a replicare una distribuzione di probabilità. Dovrebber quindi usare una loss function che riflette la distanza tra la distribuzione dei dati generati dalla GAN e la distribzuione dei dati reali.

Come catturare la differnezaa tra due distribuzioni nelle funzioni di costo della GAN? Questa question è un'area di ricerca attiva, e molti approcci sono stati proposti. Vedremo due funzioni di costo comuni per le GAN, entrambe le quali sono implementate in TF-GAN:

* minimax loss: la funzione di costo usata nel paper che ha introdotto le GAN (https://arxiv.org/abs/1406.2661)
* loss di Wasserstein: la funzione di costo di defautl per TF-GAN descritta in un paper del 2017 (https://arxiv.org/abs/1701.07875)

TF-GAN implementa molte altre funzioni di costo.

## UNa o due funzioni di costo?

Una GAN può avere due funzioni di costo: una per l'addestramento del generator ed uno per il training del discriminator. Come possono le due funzioni di costo lavorare insieme per riflettere una misura di distanza tra distribuzioni di probabilità?

Nello schema delle loss che vedremo qui, le loss del generator e del descriminator derivano da una singola misura didistanza tra le distribuzioni di probabilità. In entrambi questi schemi, comunque, il generator può influenzare un solo termine nella misura di distanza: il termine che riflette la distribuzione dei dati falsi. Per cui durante il training  del generator lasciamo l'altro termine, che rfilette la distribuzione dei dati reali.

Le loss del generator e del discriminator appaiono differenti alla fine, anche se derivano da una singola formula.

## Minimax loss

Nel paper che ha introdtto il GAN, il generatore prova a minimizzare la seguente funzione, mentre il discriminatore prova a massimizzarla:

$$
E_x \[log(D(x))\] + E_z [log(1-D(G(z)))]
$$

In questa funzione:

* $D(x)$ è la stima del discriminatore sulla probabilità che l'istanza dei dati reali $x$ sia vera.
* $E_x$ è il valore atteso di tutte le istanze dei dati reali.
* $G(z)$ è l'output del generatore ad un dato rumore $z$.
* $D(G(z))$ è la stima del discriminatore della probabilità che un'istanza falsa sia reale.
* $E_z$ è il valore atteso su tutti gli input casuali del generatore (in effetti, i vaore atteso di tutte le istanze fake generate $G(z)$).
* La formula deriva dalla cross-entropia tra le distribuzioni reali e generate.

Il generatore non può direttamente influenzare ilt ermine $log(D(x))$ nella funzione, per cui, per il genratore, minimizzare la loss è equivalente a minimizzare $log(1 - D(G(z)))$.

## Modified Minimax Loss

Il paper originale del GAN nota che la funzione di costo precedente può far sì che le GAN rimangano ferme nei primi stage dell'addestramento, qunado il compito del discirminatore è molto semplice. Il paper quindi suggerisce di modificare la loss del generatore in modo che questi provi a massimizzare $log(D(G(z)))$.

## Wasserstein Loss

Di default, TF-GAN usa la loss di Wasserstein.

Questa funzione di costo dipende da una modifca dello schema della GAN (chiamato "Wasserstein GAN" o "WGAN") nel quale il discriminatore non classifca in effett delle istanze. Per ogni istanza dà invece un numero. Questo numero non deve essere inferiore ad 1 o più grande di ', per cui non possiamo usare 0.5 come soglia per decidere se un'istanza è vera o falsa. Il training del discriminator prova a rendere l'output più grande per istanze reali che per istanze fake.

Siccome non può realmente discriminare tra real e fake, il discriminatore WGAn è in effetti chiamato "critica" invece di "discriminatore". Questa distinzione ha importanza teorica, ma per gli scopi pratici possiamo trattarlo come un acknowledgement che gli input alla funzione di costo non devono essere delle probabilità.

La funzione di costo stessa è molto semplice:

**Critic Loss**: $D(x) - D(G(z))$

Il discrimnatore prova a massimizzare questa funzione. In altre parole, prova a massimizzare la differenza tra i suoi output su istanze reale ed il suo output su istanze false.

**Generator Loss**: $D(G(z))$

Il generatore prova a massimizzare questa funzione. In altre parole, prova a massimizzare l'output del discrimnatroe per le sue istanze false.

In queste funzioni:

* $D(x)$ sono l'output della critica per una istanza vera.
* $G(z)$ è l'output del generatore quando c'è un dato rumore $z$.
* $D(G(z))$ è l'output della critica per un'istanza fake.
* L'output della critica $D$ deve NON essere tra 1 e 0.
* Le formule derivano dalla *earth mover distance* tra le distribuzioni reali e generate.

## Requisiti

La giustificazione teorica per la WGAN richiede che i pesi attraverso la GAN possano essere tagliati in modo che rimangano all'interno di un range vincolato.

## Benefit

Le WGAN sono meno vulnerabili a rimanere ferme piuttosto che le GAN minimax-based, ed evitare problemi con i vanisghin gradients. L'earth mover distance ha anche il vantaggio di essere una vera metrica: una misura di distanza in uno spazio di distribuzioni di probabilità. La cross-entropy non è in tal senso una metrica.

Earth Mover Distance: https://en.wikipedia.org/wiki/Earth_mover's_distance

## Problemi comuni

Le GAN hanno un certo numero di fallimenti comuni. Tutti questi problemi comuni sono aree di ricerca attiva. Mentre nessuno di questi problemi è stato completamente risolto, vedremo alcune cose che le persone hanno già provato.

### Vanishing Gradients

La ricerca (https://arxiv.org/pdf/1701.04862.pdf) ha suggerito che se il discriminatore è troppo bbuono, allora il training del generatore può fallire a causa del vanishing gradients (https://wikipedia.org/wiki/Vanishing_gradient_problem). In effetti, un discriminatore ottimale non fornisce abbastanza informazioni per far fare progressi al generatore.

## Prove a rimediare

* Wasserstein loss: la Wasserstein loss è progettata per prvenire i vanishing gradients anche quando addestriamo il discriminatore all'ottimalità.
* Modified minimax loss: il paper originalke propone una modifica alla minimax loss per affrontare i vanishign gradients.

## MOde Collapse

Normalmente vogliamo che il GAN produca un'ampia varietà di output. Vogliamo, ad esempio, un diverso volto per ogni input al nostro generatore di volti.

Tuttavia, se un generatore prduce un outptu specialmente plausibile, il generatore può apprendere a produrre solo quell'output. Infatti, il generatore sta sempre provando a trovare l'output che sembra essere più plausibile al discriminatore.

Se il generaotre inizia a produrre lo stesso output (o un piccolo insieme di output) ancora ed ancora, la miglior strategia del discriminatore è apprendere a respingere sempre quell'output. Ma se la prossiam generazione del discriminatore rimane fermo in un minimo locale e non trova la miglior starategia, allora è più facile per l'iterazione successiva del generatore per trovare l'output più plausibile per il discriminatore attuale.

Ogni iterazione del generatore sovra-ottimizza per un certo discriminatore, ed il dsicrimiantore non riesce mai ad apprendere il suo percorso al di fuori della trappola. Come risultato il generatore ruota attraverso un piccolo insieme di tipi di output. Questa forma di fallimento del GAN è chiamato mode collapse.

### Tentativi di rimediare

I seguenti approcci provano a forzare il generatore ad ampliare il suo ambito prevenendo l'ottimizzazione di un singoli discriminatore prefissato:

* Wasserstein loss: la Wasserstein loss allevia il mode collapse permettendoci di trainare il discriminatore all'ottimalità senza preoccuparsi dei vanishing gradients. Se il discriminator non si ferma in un minimo locale, apprende a respingere gli outptu su cui si stabilizza il generatore. Per cui il generatore deve imparare qualcosa di nuovo.
* Unrolled GANs: le unrolled GANs (https://arxiv.org/pdf/1611.02163.pdf) usano una funzione di costo per il generatore che icnorpora non solo l'attuale classificazione del discrimiantor, ma anche l'output delle versioni future del discriminaotre. Per cui il genratore non può sovraottimizzarsi su un singolo discriminator.

## Mancata convergenza

Le GAN spesso onon convergono.

### PRove a rimediare

I ricercatori hanno provato ad usare varie forme di regolarizzazione per migliroare la convergenza delle GAN, inclusi:

* aggiungere rumore agli input del discriminator (https://arxiv.org/pdf/1701.04862.pdf)
* penalizzare i pesi dei discriminatori (https://arxiv.org/pdf/1705.09367.pdf)

## Variazioni tra GAN

I ricercatori continuano a trovare delle tecniche GAN migliroate e nuovi usi per le GAN. Ecco un esempio di alcune delle variazioni per darci un'idea delle possibilità.

### Progressive GANs

In una progressive GAN, i primi layer del genrator producono immagini a risoluzione molto bassa, ed i conseguenti layer aggiungono dei dettagli. Questa tec ica permette alle GAN per addestrare più velocemente rispetto alle GAN non progressive, e produce delle immagini a risoluzione più alte. https://arxiv.org/abs/1710.10196

### Conditional GANs

Le GAN condizionali addestrate su und ataset etichettato e ci permette di specificare le label per ogni istanza generata. Per esempio, una MNIST GAN non condizionale produrrebbe cifre casuali, mentre una MNIST GAN condizionale ci permetterebbe di specificare quale cifra la GAN deve generare.

Invece di modellare la probabilità confiunta $P(X,Y)$ la GAN condizionale modella la probabilità condizionale $P(X|Y)$. https://arxiv.org/abs/1411.1784

### Image-to-Image Translation

Le GAN che si occupano di Image-to-Image translation prendono un'immagine in input e la mappano ad un'immagine generata in output con proprietà difefrenti. Ad esempio, possiamo prendere una maschera con dei blob di colore nella forma di un'auto, e la GAN può riempire la forma con dei dettagli fotorealistici di un'auto.

In modo simile, possiamo addestrare una GAN image-to-image a prendere degli schizzi di bagagli e tradurli in immagini fotorealistiche di bagagli.

In questi casi, la loss è una combinazione pesata della solita loss basata sul discriminatore e di una loss pixel-wise che penalizza il generatore per discorstarsi dall'immagine sorgente.

Isola et al 2016

## CycleGAn

La CycleGAN apprende a trasformare immagini da un insieme in immagini che possono plausibilmente appartenere ad un altro insieme.


I dati di addestramento per una CycleGAN sono semplicemente due insiemi di immagini. Il sistema non richiede alcuna label o corrispondenze a coppie tra immagini. Zhu et al., 2017

## Text-to_image Synthesis

Le Text-to_image GAN prendono il testo come input e producono delle immagini che sono plausibili e descritte dal testo. Zhang et al, 2016.

## Super-resolution

Le super-resolution GAN aumentano la risoluzione delle immagini, aggiungendo dettagli dove necessario per riempire le aree sfocate. Ledig et al, 2017.

## Face Inpainting

Le GAN sono usate per il task di *image inpainitng* semantico, nel quale parti delle immagini sono oscurate, ed il sistema prova a riempire le parti mancanti. Yeh et al, 2017

## Text-to-Speech

Non tutte le GAN producono immagini. Ad esempio, alcuni ricercatori hanno anche usato delle GAN per produrre parlato sintetizzato dall'input testuale. Yang et al., 2017

## Conclusioni

Dovremmo essere in grado di:

* comprendere la differenza tra modelli generativi e discriminativi
* identificare i problemi che le GAN possono risolvere
+ comprendere il ruolo del generatore e del discriminaotre in una GAN
* comprendere i vantaggi e svantaggi delle funzioni di costo in comune delle GAN
* identificare psosibili soluzioni a problemi comuni con l'addestamento delle GAN
* usare la libreria TF GAN per creare una GAN
