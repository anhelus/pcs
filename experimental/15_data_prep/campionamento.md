## Cosa è il campionamento?

Uno dei problemi principali riguarda il collezionare un quantitativo di dati sufficiente. Alle voltre, però, vi sono *troppi* dati, e dobbiamo scegliere un sottoinsieme di campioni per l'addestramento.

Come scegliamo il sottoinsieme? Ad esempio, immaginiamo di fare una ricerca su Google. A quale granularità campioneremmo i quantiativi di dati? Useremo delle query random? 

In ultimo, la risposta dipende dal problema: cosa vogliamo predire, e quali feature vogliamo?

## filtrare le infromazioni PII (Personally Identifiable Information)

Se i dati includono delle informazioni personali, dovremo filtrarli a partire dai nostri dati. Una politica può richiederci di rimuovere feature infrequenti, per esempio.

Questo filtraggio ovviamente andrà ad influenzare la nostra distribuzione, perderemo delle informazioni, che di solito sono all'interno della coda della distribuzione.

Questo filtraggio è utile perché delle feature non molto frequenti sono difficili da apprendere. Ma è anche importante realizzare che il dataset sarà biasato verso i dati più frequenti.

## dati non bilanciati

un datast di classificazioni con diverse proporizioni dei dati è chiamato non bilanciato. LE classi che fanno parte delle grosse proprozioni dei dati sono chiamate classi maggioritarie. Quelle che coprono una parte minore sono chiamate classi minoritarie.

Cosa conta con "sbilanciato"? La risposta può essere da leggera ad estrema:

| Grado di sblianciamento | Proporzione di classi minoritarie |
| ----------------------- | --------------------------------- |
| Leggero | 20-40 % del datset |
| moderato | 1-20 % del dataset |
| Estremo | < 1% del dataset |

Perché guardiamo ai dati non bilanciati? potremmo dover applicare una certa tecnica di campionamento se abbiamo un task di classificazione con un dataset sblilanciato.

Immaginiamo ad esempio di avere un dataset che individua lo spam. Abbiamo ricevuto 50 mail di spam, e 950 non di spam, per cui il 0.5% dei dati sarà positivo, mentre 950 negativo.

Questo è un problema, perché con così pochi positivi, il modello di training spenderà la maggior parte del tempo su campioni negativi, e non apprenderà a riconoscere gli esmpi positivi. Per esempio, se il batch size è 128, molti batch non avranno campioni positivi, per cui il gradiente sarà meno informativo.

Se abbiamo un dataset sbilanciato, per prima cosa proviamo ad efeettare il trainign sulla distribuzione vera. Se il modello funziona ed è in grado di generalizzare, siamo a posto; altrimenti, dovremo usare una tecnica di bilanciamento.

### downsampling ed upweighting

Un modo efficace potrebbe gestire dati non bilanciati è quello di sottocampionare (downsampling) e dare un peso maggiore (upweighting) alla classe maggioritaria. Iniziamo definendo questi due nuovi termini:

* il downsampling significa effettuare il training su un sottoinsieme della classe maggioritaria
* l'upweighting significa aggiungere un 

per esempio, se sottocampioniamo di 2 gli esempi negativi, e quindi scegliamo casualmente la metà dei campioni negativi, avremo 475 campioni negativi, aumentando l'incidenza della classe maggioritaria a circa il 10%, passando ad un dataset *moderatamente* sbilanciato.

Successivamente, potremmo dare maggior peso ai campioni estratti a valle dal downsampling, in un fattore pari a quello che abbiamo usato per il sottocampionamento. In pratica, nel nostro caso, ogni campione della classe sottocampionata avrà un peso doppio rispetto a quello che avrebbe avuto se si fosse utilizzato il campione iniziale.



I benefici legati al downsampling ed all'upweighting sono vari:

* convergenza più rapida: dato che vediamo più spesso la classe minoritaria, avremo il modello a convergenza più rapida;
* spazio su disco: consolidare la classe maggioritaria in minori campioni con pesi più ampi, spenderemmo meno per memorizzarlo. Questo risparmio ci permette di avere più spazio su disco  per la classe minoritaria, ma possiamo collegare un numero più grande ed un range più ampio di campioni da quella classe.
* calibrazione: l'upweighting assicura che il modello sia ancora calibrata; l'output può essere interpretato come probabilità.

## split dei dati

nomralmente si effettua la suddivisione casuali dei dati.

Normalmente, quello che avivene è che l'intero set di dati viene suddiviso per il 70% in dati per l'addestramento, ed il 30% per i dati per la validazione dei risultati ottenuti.

Esistono particolari casi in cui ci sono diverse dimensioni di splitting, che possono causare eventualmente degli skew nei dati.

Immaginiamo ad esempio di avere un dataset di email, che vanno naturalmente ad organizzarsi secondo tipo di mittente ed orario di ricezione. Potremmo scegliere due dimensioni quindi di splitting, ovvero tipo di mittente ed orario di ricezione, o anche un'altra, che non tiene presente di nessuna delle due cose, ed effettua una suddivisione completamente casuale.