# Il problema della regressione

Quello della *regressione* è un problema che si distingue dalla classificazione sotto diversi aspetti, pur conservando alcuni punti in comune con quest'ultima.

La differenza che salta subito all'occhio è infatti che, laddove nella classificazione cerchiamo di caratterizzare la relazione tra una serie di feature in ingresso ed una classe, nella regressione la relazione è tra una serie di *variabili indipendenti* ed una o più *variabili dipendenti*.

!!!note "Nota"
    Per essere precisi, occorre tenere conto anche di un termine di errore, che può essere più o meno rilevante.

Un esempio banale di regressione è quello che ci vede cercare la retta interpolate di una serie di punti in un piano cartesiano

## Regressione lineare

Un modello di regressione lineare predice il target come la somma pesata dlle feature in ingresso. La linearità della relazione appresa rende l'interpretazione del modello semplice. I modelli di regressione lineare sono stati a lungo usati dagli statistici per affrontare problemi di tipo quantitativo.

I modelli lineari possono essere usati per modellare la dipendenza di un obiettivo di regressione $y$ rispetto ad un insieme di feature $X$. Le relazioni apprese sono lineari, e possono essere scritte per una singola istanza $i$ come segue:

$$
y = \beta_0 + \beta_1 x_1 + \ldots + \beta_p x_p + \epsilon
$$

In sostanza, la predizione $y$ sarà data dalla somma pesata delle $p$ feature in ingresso. I valori $\beta_i$ rappresentao i pesi o coefficienti; il primo peso $\beta_0$ è rappreentato dall'intercetta, mentre il valore di $\epsilon$ descrve l'errore, dato dalla differenza tra la predizione $\hat{y}$ e il valore vero e proprio. In particolare si presuppone che questi errori seguano una distribuzione gaussiana, per cui diremo che può assumere valore negativo o positivo, e probabilmente più faremo errori piccoli che grandi.

Diversi metodi possono essere usati per stimare il peso otimale. Il metodo ai minimi quadrati è normalmente usato per indiviuare i pesi che minimizzano la differenza al quadrato tra il valore reale e la stima ottenuta.

il vantaggio principale di un modello di regressione lineare è appunto la linearità: rende la procedura di stima semplice e, ancora più importante, queste equazioni lineari hanno un'interpretazione semplice da capire, data dai pesi. Questo è uno dei motivi principali per cui il modello lineare e tutti quelli simili sono molto diffusi in campi scientifici come medicina, sociologia, psciologia e molti altri campi di ricerca quantitativi. Ad esempio, in campo medico, non solo è importante predire il valore di uscita di un paziente, ma anche quantificare l'influenza della farmaco e allo stesso momento del genere, età, essso, ed altre feature, in modo da interpretare i risultati.

I pesi stimati hanno degli intervalli di confidenza, ovvero dei range che coprono il peso "vero" con un certo grado di confidenza. ad esempio, un intervallodi confidenza del 95% per un peso di due potrebbe essere nei valori che vanno da 1 a 3. L'interpretazione di questo intervallo sarebbe: se ripetiamo la stima 100 volte con dati appena campionati, l'intervallo di confidenza conterrà il valore vero 95 volte su 100, supposto che il modello di regressione lineare sia quello corretto per i dati.

la correttezza del modello dipende sempre da alcuni presupposti. In questo caso particolare, questi sono i seguetni:

* linearità: il modello di regressione lineare fa in modo che le predizioni siano una combinazione lineare di feature, il che rappresenta sia il grande vantaggio che il grande limite di questo modello. La linearità conduce a modelli interpretabili: gli effetti lineari sono facili da quantificare e descrivere. Sono inoltre additivi, per cui è facile separare i singoli effetti. Se sospettivamo interazioni tra le singole feature o associazioni non lineari di una feature con il valore targetm potremmo usare dei modelli non lineari.
* normaltà: si suppone che il risutato date le feature segua una distribuzione di tipo nomale. Se questo assunot viene violato, gli intervalli di confidneza stimati dei pesi delle feature non sono validi.
* omoschedasticità (varianza costante): la varianza del termine di errore deve essere constante nell'intero spazio delle feature. Supponiamo divoler predire il valore di una casa data la metratura. Stimiamo un modello lineare che assume che, indipendentemente dalle dimensioni della casa, l'errore sulla risposta predetta ha sempre la stessa varianza. Questo assunto spesso viene violato nella realtà. nell'esempio delle case, è plausibile che la varianza del termine di errore attorno al prezzo predetto sia più grande per case più grandi, dal momento che i prezzi sono più alti e vi è più spazio per le fluttuazioni di prezzo. Supponiamo un errore medio di 50k euro: se assumiamo l'omoschedatsticità, si dice che questo sia lo stesso per le case che costano un milione e per quelle che costano solo 40k. Questo ovviamente non è ragionevole perché significherebbe che ci aspettiamo prezzi negativi per alcune case.
* indipendenza: si presuppone che ogni istanza sia indipendente dalle altre istanze. se effettuiamo misure ripetute, come ad esempio più test sanguinei per ogni paziente, i data point non sono indipendenti.
* feature fisse: le feature in ingresso sono considerate "fisse", il che significa che sono trattate come costanti e non come variabili statsticihe. Questo implica che sono libere da errori di misurazione. Questo è un assunto non realistico, però se non ci fosse dovremmo fittare dei modelli molto complessi di misura che tengano in conto dell'errore di misura delle feature di input.
* assenza di multicollinearità: non vogliamo delle feature fortemente correlate, in quanto questo rende problematica la stima dei pesi. In una situazione dove due feature sono fortemente correlate, diventa problematico stimare i pesi perché gli effetti delle feature sono additivi, e dienta indeterminabile a quale delle feature correlate attrbuire detti effetti.
