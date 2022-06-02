# 

## thresholding

La regressione logistica restituisce una probabilità, che però viene automaticamente convertita in un valore binario o multiclasse.

Immaginiamo il caso binario per semplicità. Un modello di regressione logistica che restituisce 0.9995 per un dato messaggio di email sta predicendo che è molto probabile che sia spam. Di converso, se un altro messaggio ha una probabilità di 0.003 è molto improbabile che isa spam. Che succede però nel caso di un messaggio email con un punteggio di predizione di 0.6? Per arrivare dalla probabilità alla classificazione abbiamo bisogno di definire una *soglia di decisione*. Un valore oltre questa soglia indica "spam", uno al di sotto di questa soglia indica "assenza di spam". La tentazione potrebbe essere quella di presupporre che la soglia di decisione sia sempre 0.5, ma in realtà questa dipende dal problema, e quindi è un valore che bisogna adattare sulla base della situazione.

Vediamo adesso le metriche che possiamo usare per valutare le predizioni di un classificatore, così come l'impatto delle modifiche della soglia di decisione su queste predizioni.

## true false positive negative

Prima di procedere, è il caso di introdurre il concetto di *classe positiva* e classe negativa.

TODO: ESEMPIO

Un true positive è un'uscita dove il modello predice corretatamnte la classe positiva. In modo simile, un true negative è un'uscita vero il modello predice correttamente la classe negativa.

Un falso positivo è un'uscita dove il modello predice in maniera non corretta la classe positiva. Ed un falso negativo è un'uscita dove il modello predice in maneira non corretta laclasse negativa.

## accuracy

L'accuratezza è una metrica per valutare i modelli di classificazione. Informalmente, l'accuratezza è la frazione delle predizioni che i nostri modelli hanno preso. Formalmente l'accuratezza ha la seguente definzione:

$$
AC = \frac{C}{T}
$$

dove $C$ è il numero totale di predizioni corrette, mentre $T$ è il numero totale di predizioni. Per la classificazione binaria, l'accuratezza può essere calcolata in termini di positivi e negativi come segue:

$$
AC = \frac{TP + TN}{TP + TN + FP + FN}
$$

dove $TP$ è il numero di veri positivi, $TN$ il numero di veri negativi, $FP$ il numero di falsi positivi e $FN$ il numero di falsi negativi.

Ad esempio:



L'accuracy è pari a:

$$
AC = \frac{TP+TN}{TP+TN+FP+FN}=\frac{1+90}{1+90+1+8}
$$

L'accuratezza è pari a $0.91$, o del $91\%$, il che significa che ci sono $91$ predizioni corrette su $100$ campioni totali. Questo significa che il nostro classificatore sta facendo un buon lavoro, giusto?

Vediamo più da vicino l'analisi dei positivi e dei negativi per avere più indizi sulle performance del modello. Dei nostri $100$ esempi, $91$ sono benigni (90 $TN$ e 1 $FP$), mentre $9$ sono maligni (1 TP e 8 FN). Questo singifica che dei 9 tumori maligni il modello è stao in grado di identificare soltanto uno come maligno, un'uscita terribile, in quanto 8 di 9 maligni non sono stati diagnosticati.

In questo caso specifico, il nostro modello non è essenzialmente migliore di uno che abbia un'abilità di predizione nulla in grado di distinguere i tumori maligni da quelli benigni.

L'accuratezza non ci dice quindi la storia vera quando stiamo lavorando su un dataset sbilanciato come questo, dove vi è una dispartià significantetra il numero delle etichette positive e negative.

### precisione

La precisione prova a rispondere a questa questione, ovvero:

* quale proporzioni di identificazione positiva è corretta?

La precisione è definita come segue:

$$
PR = \frac{TP}{TP+FP}
$$

Proviamo a calcolare la precisione del modello ML che abbiamo visto prima:


$$
PR = \frac{TP}{TP+FP} = \frac{1}{1+1} = 0.5
$$

Il modello ha quindi una precisione di $0.5$, ovvero, quando predice un tumore maligno, è corretto il $50\%$ delle volte.

### recall

Il recall prova a rispondere alla seguente questine:

* quale proporzione dei positivi veri è stata identificata correttamente?

Matematicamente, il recall è stato definito come segue:

$$
R = \frac{TP}{TP+FN}
$$

Calcoliamo ilr ecall per il nostro classificatore:

$$
R = \frac{TP}{TP+FN}=\frac{1}{1+8}=0.11
$$

Il modello ha un recall $0.11$, in altre parole, identifica correttamente l'$11\%$ dei tumori maligni.

per valutare l'efficacia del modello, occcorre esaminare sia la precisione sia il recall. Purtroppo, la precisione ed il recall sono spesso l'uno contrapposto all'altro. Questo significa che migliorare la precisione tipicamente riduce il recall e viceversa. Per capire questo cocnettovediamo quest'immagine. Le mail a destra del classification threshold sono classificate come spam, mentre quelle a sinistra sono classificate come non spam.

Calcoliamo la precisione e il recall in questo caso.

La precisione misura le percentuali di email segnalate come spam classificati correttamente, ovvero la perctenuale di èunti a destra della soglia che sono verdi nella figura 1.

$$
P = \frac{TP}{TP+FP}=\frac{8}{8+2} = 0.8
$$

Il recall misura la percentuale di email di spam che sono state correttamente classificate - ovvero, la percentuale di puntini verdi che sono alla destra della soglia:

$$
R = \frac{TP}{TP+FN} = \frac{8}{8+3} = 0.73
$$

Se aumentassimo la detection trheshold, il numero di falsi positivi diminuirebbe, aumentando tuttavia quello di falsi negativi. Come risultato, la precisione aumenta, ma il recall diminuisce. Al contrario, diminuendo la classification threshold, la precisione diminuisce ed il recall aumenta.

TODO: rivedere 