Il vincitore della competizione ImageNet nel 2015 è stato ResNet152, ovvero una variante della rete residua con 152 livelli. In questo post, tratteremo il concetto di ResNet50, che può essere generalizzato a qualsiasi altra variante di ResNet. Prima di spiegare la rete residua profonda, vorrei parlare delle semplici reti profonde (reti che hanno un maggior numero di livelli di convoluzione, pooling e attivazione sovrapposti gli uni agli altri). A partire dal 2013, la comunità di Deep Learning ha iniziato a costruire reti più profonde perché erano in grado di raggiungere valori di precisione elevati. Inoltre, le reti più profonde possono rappresentare caratteristiche più complesse, quindi è possibile aumentare la robustezza e le prestazioni del modello. Tuttavia, aggiungere più livelli non ha funzionato per i ricercatori. Durante l'addestramento di reti più profonde, si è osservato il problema della degradazione della precisione. In altre parole, l'aggiunta di più livelli alla rete ha fatto sì che il valore di precisione si saturasse o diminuisse bruscamente. Il colpevole della degradazione della precisione è l'effetto del gradiente che svanisce, che può essere osservato solo nelle reti più profonde.

Durante la fase di retropropagazione, viene calcolato l'errore e vengono determinati i valori del gradiente. I gradienti vengono inviati indietro alle hidden layer e i pesi vengono aggiornati di conseguenza. Il processo di determinazione del gradiente e l'invio verso la successiva hidden layer continua fino a raggiungere il layer di input. Il gradiente diventa sempre più piccolo man mano che raggiunge il fondo della rete. Di conseguenza, i pesi dei layer iniziali si aggiorneranno molto lentamente o rimarranno gli stessi. In altre parole, i layer iniziali della rete non impareranno in modo efficace. Pertanto, l'addestramento di una rete profonda non convergerà e la precisione inizierà a degradare o a saturarsi a un valore particolare. Nonostante il problema del gradiente che svanisce sia stato affrontato utilizzando l'inizializzazione normalizzata dei pesi, la precisione della rete più profonda non aumentava ancora.

Cos'è Deep Residual Network?
Deep Residual Network è quasi simile alle reti che hanno livelli di convoluzione, pooling, attivazione e completamente connessi sovrapposti uno sopra l'altro. L'unica differenza nella costruzione della rete semplice per trasformarla in una rete residua è la connessione di identità tra i livelli. Lo screenshot qui sotto mostra il blocco residuo utilizzato nella rete. Puoi vedere la connessione di identità come la freccia curva che parte dall'input e si dirige alla fine del blocco residuo.

Rappresentazione del blocco residuo
Un blocco residuo di una Deep Residual Network

Qual è l'intuizione dietro il blocco residuo?
Come abbiamo appreso in precedenza, l'aumento del numero di livelli nella rete degrada bruscamente la precisione. La comunità del deep learning voleva un'architettura di rete più profonda che potesse eseguire bene o almeno allo stesso modo delle reti meno profonde. Ora, cerca di immaginare una rete profonda con livelli di convoluzione, pooling, ecc. sovrapposti uno sopra l'altro. Supponiamo che la funzione effettiva che stiamo cercando di apprendere dopo ogni livello sia data da Ai(x), dove A è la funzione di output del i-esimo livello per l'input dato x. Puoi fare riferimento allo screenshot successivo per comprendere il contesto. Puoi vedere che le funzioni di output dopo ogni livello sono A1, A2, A3, .... An.

CNN profonda ipotizzata
Assunta rete neurale convoluzionale profonda

In questo modo di apprendimento, la rete sta cercando direttamente di apprendere queste funzioni di output, cioè senza alcun supporto aggiuntivo. In pratica, non è possibile per la rete apprendere queste funzioni ideali (A1, A2, A3, .... An). La rete può solo apprendere le funzioni, diciamo B1, B2, B3, .... Bn, che sono più vicine ad A1, A2, A3, .... An. Tuttavia, la nostra rete profonda ipotizzata è così scarsa che non riesce nemmeno ad apprendere B1, B2, B3, .... Bn che sarebbero più vicine ad A1, A2, A3, .... An a causa dell'effetto del gradiente che svanisce e anche a causa del modo non supportato di addestramento.

Il supporto per l'addestramento sarà dato dall'aggiunta della mappatura di identità all'output residuo. Innanzitutto, vediamo cosa si intende per mappatura di identità? In poche parole, applicare la mappatura di identità all'input restituirà l'output che è uguale all'input (AI = A: dove A è una matrice di input e I è la mappatura di identità).

Le reti tradizionali come AlexNet, VGG-16, ecc. cercano di apprendere direttamente A1, A2, A3, .... An come mostrato nel diagramma della rete profonda semplice. Nel passaggio in avanti, l

'input (immagine) viene passato alla rete per ottenere l'output. Viene calcolato l'errore, si determinano i gradienti e la retropropagazione aiuta la rete a stimare le funzioni A1, A2, A3, .... An nella forma di B1, B2, B3, .... Bn. Gli autori di ResNet hanno pensato che:

"SE I LIVELLI NON LINEARI MULTIPLI POSSONO APPROSSIMARE ASINTOTICAMENTE FUNZIONI COMPLICATE, ALLORA È EQUIVALENTE SUPPORRE CHE POSSANO APPROSSIMARE ASINTOTICAMENTE LA FUNZIONE RESIDUALE".
Dopo aver letto l'affermazione, la prima domanda che ci viene in mente è la seguente:

Cos'è una funzione residua?
La risposta semplice a questa domanda è che la funzione residua (nota anche come mappatura residua) è la differenza tra l'input e l'output del blocco residuo in questione. In altre parole, la mappatura residua è il valore che verrà aggiunto all'input per approssimare la funzione finale (A1, A2, A3, .... An) del blocco. Puoi anche supporre che la mappatura residua sia la quantità di errore che può essere aggiunta all'input per raggiungere la destinazione finale, ovvero approssimare la funzione finale. Puoi visualizzare la mappatura residua come mostrato nella figura successiva. Puoi vedere che la mappatura residua agisce come un ponte tra l'input e l'output del blocco. Nota che i livelli di peso e la funzione di attivazione non sono mostrati nel diagramma, ma sono effettivamente presenti nella rete.

Modo semplice di rappresentare la mappatura residua
Rappresentazione intuitiva della funzione residua

Cambiando le nostre convenzioni di denominazione per rendere questo post compatibile con il paper di ResNet, la figura 1 mostra il blocco residuo. La funzione che dovrebbe essere appresa come risultato finale del blocco è rappresentata come H(x). L'input al blocco è x e la mappatura residua

Perché la funzione residua funzionerà?
Gli autori di ResNet hanno di nuovo pensato come recita l'affermazione:

"INVECE DI ASPETTARSI CHE I LIVELLI SOVRAPPONENTI POSSANO APPROSSIMARE H(x), GLI AUTORI LI LASCINO APPROSSIMARE UNA FUNZIONE RESIDUALE, OVVERO F(x) = H(x) - x".
L'affermazione precedente spiega che durante l'addestramento della rete residua profonda, l'obiettivo principale è apprendere la funzione residua F(x). Quindi, se la rete riuscirà in qualche modo a imparare la differenza (F(x)) tra l'input e l'output, allora la precisione complessiva può essere aumentata. In altre parole, il valore residuo dovrebbe essere appreso in modo tale da avvicinarsi a zero, rendendo così la mappatura di identità ottimale. In questo modo, tutti i livelli della rete produrranno sempre le mappe di caratteristiche

 ottimali, ovvero la mappa delle caratteristiche migliore dopo le operazioni di convoluzione, pooling e attivazione. La mappa delle caratteristiche ottimali contiene tutte le caratteristiche pertinenti che possono classificare perfettamente l'immagine nella sua classe di verità fondamentale.

Perché la mappatura di identità funzionerà? In che modo la connessione di identità influisce sulle prestazioni della rete?
Durante la retropropagazione, ci sono due percorsi per i gradienti che transitano fino al livello di input mentre attraversano un blocco residuo. Nel diagramma successivo, puoi vedere che ci sono due percorsi: il percorso 1 è il percorso di mappatura di identità e il percorso 2 è il percorso di mappatura residua.

Percorsi di gradiente in ResNet
Percorsi di gradiente in ResNet

Abbiamo già discusso il problema dei gradienti che svaniscono nella semplice rete profonda. Ora cercheremo di spiegare la soluzione per lo stesso tenendo presente la connessione di identità. Innanzitutto, vedremo come rappresentare matematicamente il blocco residuo F(x)?

y = F(x, {Wi}) + x
dove y è la funzione di output, x è l'input al blocco residuo e F(x, {Wi}) è il blocco residuo. Nota che il blocco residuo contiene livelli di peso rappresentati come Wi, dove 1 ≤ i ≤ numero di livelli in un blocco residuo. Inoltre, il termine F(x, {Wi}) per 2 livelli di peso in un blocco residuo può essere semplificato e scritto come segue:

 F(x, {Wi}) = W2 𝛔(W1x)
dove 𝛔 è la funzione di attivazione ReLU e la seconda non linearità viene aggiunta dopo l'addizione con la mappatura di identità, ovvero H(x) = 𝛔( y ).

Quando i gradienti calcolati passano attraverso il Percorso di Gradiente-2, si incontrano due livelli di peso che sono W1 e W2 nella nostra funzione residua F(x). I pesi o i kernel nei livelli di peso W1 e W2 vengono aggiornati e vengono calcolati nuovi valori di gradiente. Nel caso dei livelli iniziali, i nuovi valori calcolati diventeranno piccoli o svaniranno. Per salvare i valori dei gradienti dallo svanire, entrerà in gioco la connessione shortcut (mappatura di identità). I gradienti possono passare direttamente attraverso il Percorso di Gradiente-1 mostrato nel diagramma precedente. Nel Percorso di Gradiente-1, i gradienti non devono incontrare alcun livello di peso, quindi non ci sarà alcuna variazione nel valore dei gradienti calcolati. Il blocco residuo verrà saltato in una sola volta e i gradienti possono raggiungere i livelli iniziali che li aiuteranno ad apprendere i pesi corretti. Inoltre, ResNet versione 1 ha una funzione ReLU dopo l'operazione di addizione, quindi i valori dei gradienti verranno modificati

 solo se sono negativi.

In questo modo, l'aggiunta della connessione di identità migliora il flusso dei gradienti, prevenendo l'effetto di svanimento del gradiente. La connessione di identità agisce come un percorso diretto per i gradienti, permettendo loro di raggiungere facilmente i livelli iniziali. Ciò aiuta la rete a imparare i pesi corretti e a migliorare le prestazioni complessive.

In sintesi, l'intuizione di base di ResNet è che l'apprendimento delle funzioni residue è più facile rispetto all'apprendimento delle funzioni dirette. L'aggiunta della connessione di identità e il flusso diretto dei gradienti attraverso di essa aiutano a risolvere il problema del degrado delle prestazioni delle reti profonde. Questa è la ragione per cui le reti residuali come ResNet hanno ottenuto risultati eccezionali in molte sfide di visione artificiale.