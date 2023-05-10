# 3.6.1 - Metriche di classificazione

Nella [lezione sulla regressione logistica](../03_log_reg/lecture.md) abbiamo visto come l'algoritmo restituisca un valore di probabilità poi convertito in classe mediante una soglia $\mu$, che di default vale $0.5$. Tuttavia, abbiamo sottolineato come questo valore non sia ideale in ogni situazione: chiariamo questo concetto con un semplice esempio.

## Precisione, recall ed accuracy

Partiamo ricordando che, per il nostro esempio, la classe positiva è rappresentata da tutte le mail classificate come spam, mentre quella negativa è data dalle mail legittime. Ciascuna predizione fatta da questo tipo di classificatore, che è indicato come *binario*, in quanto deve scegliere tra due possibili classi, può essere di uno tra i seguenti tipi:

* nel caso in cui il modello classifichi *correttamente* una mail *di spam*, parleremo di *true positive* (*TP*);
* nel caso in cui il modello classifichi *correttamente* una mail *legittima*, parleremo di *true negative* (*TN*);
* nel caso in cui il modello classifichi *erroneamente* una mail *di spam* come legittima, si parlerà di *false negative* (*FN*);
* nel caso in cui il modello classifichi *erroneamente* una mail *legittima* come spam, si parlerà di *false positive* (*FP*).

Generalizzando, abbiamo un *true positive* (o *negative*) quando il modello predice correttamente la classe positiva (o negativa), ed un *false positive* (o *negative*) quando il modello predice erroneamente la classe negativa (o positiva).

Il rapporto tra questi quattro valori permette di definire delle metriche volte a valutare le performance del nostro classificatore. Vediamone in breve alcune.

##### Metrica 1: Accuracy

L'*accuracy* è la principale metrica utilizzata per valutare le performance dei modelli di classificazione. Informalmente, rappresenta la percentuale complessiva di predizioni corrette effettuate dal nostro modello, e può essere definita secondo la seguente formula:

$$
A = \frac{C}{T}
$$

dove $C$ è il numero totale di predizioni corrette, mentre $T$ è il numero totale di predizioni. Nel caso della classificazione binaria, la precedente diventa:

$$
A = \frac{TP + TN}{TP + TN + FP + FN}
$$

Facciamo un esempio numerico. Immaginiamo di aver ricevuto $100$ email, tra cui dieci di spam. Il nostro spam detector individua correttamente cinque messaggi di spam su dieci, per cui $TP=5$, e $FN=5$. Inoltre, dieci messaggi legittimi sono erroneamente indicati come spam, per cui $FP=10$, e $TN=80$. Allora:

$$
A = \frac{TP+TN}{TP+TN+FP+FN}=\frac{5+80}{5+80+10+5}=\frac{85}{100}
$$

L'accuracy del modello è quindi pari a $0.85$: in altri termini, il modello sembra essere in grado di gestire correttamente l'$85\%$ delle mail ricevute.

In realtà, questo risultato è soltanto *apparentemente* buono. Per capire il motivo di questa affermazione, pensiamo al fatto che le mail ricevute non sono egualmente distribuite tra spam e legittime: in grande maggioranza, infatti, abbiamo ricevuto mail legittime (il $90\%$), e soltanto una sparuta minoranza di spam. Ciò implica che il modello è stato in realtà in grado di individuare soltanto il $50\%$ dello spam ricevuto, classificando inoltre circa il $7\%$ delle mail legittime come spam.

Vista sotto questa luce, di conseguenza, l'accuracy assume un aspetto completamente differente, e non è *sempre* efficace nel valutare l'efficacia di un modello. Ciò è soprattutto evidente quando lavoriamo su un dataset molto sbilanciato, nel quale vi è una disparità significativa tra il numero di campioni disponibili per ciascuna classe.

##### Metrica 2: Precisione

Per risolvere alcuni dei problemi dell'accuracy è possibile utilizzare diverse altre metriche. Una di queste è la *precisione*, che valuta la proporzione di campioni positivi identificati correttamente.

Analiticamente, la precisione è espressa come:

$$
P = \frac{TP}{TP+FP}
$$

Tornando all'esempio precedente, la precisione sarà data dal rapporto tra le mail di spam riconosciute come tali ed il totale di mail riconosciute come spam, includendo anche gli errori fatti sulle mail legittime. Nella pratica:

$$
P = \frac{5}{5+5} = 0.5
$$

Di conseguenza, il nostro modello ha una precisione pari al $50\%$. La precisione ci permette quindi di quantificare l'affidabilità del nostro sistema: un alto valore di $P$, infatti, ci assicura che una mail identificata come spam sarà effettivamente tale. Tuttavia, ci manca ancora un fattore: infatti, come quantificare la capacità del modello di caratterizzare *tutto* lo spam ricevuto? Per farlo, ci viene in aiuto la terza metrica.

##### Metrica 3: Recall

Il *recall* è espresso dalla seguente relazione:

$$
R = \frac{TP}{TP+FN}
$$

Nel nostro caso, il recall esprime il rapporto tra le mail correttamente indicate come spam e tutte le mail *effettivamente* di spam. Numericamente:

$$
R = \frac{5}{5+5}
$$

Così come la precisione, il recall è del $50\%$.

##### Metrica 4: F1 score

Come abbiamo potuto vedere, precisione e recall permettono di caratterizzare in maneira adeguata l'affidabilità del nostro modello. Tuttavia, i due valori sono in contrapposizione: come vedremo a breve, migliorare la precisione riduce generalmente il recall, e viceversa. Di conseguenza, è opportuno utilizzare una metrica che sintetizzi le due in un unico valore; questa è chiamata *F1-score*, ed è espressa come segue:

$$
F1 = 2 \frac{P \cdot R}{P + R}
$$

Nel nostro caso:

$$
F1 = 2 \frac{0.5 \cdot 0.5}{0.5 + 0.5} = 0.5
$$

## Tuning della soglia di decisione

Abbiamo detto in precedenza che i valori di precisione  e recall sono inversamente proporzionali: aumentando l'uno, diminuisce l'altro, e viceversa. Proviamo a comprendere empiricamente questo concetto facendo un esempio.

Immaginiamo di avere un dataset per lo spam limitato a $13$ email. Addestriamo il classificatore, ed impostiamo la soglia di decisione $\mu$ a $0.6$. I risultati del primo addestramento sono mostrati in figura 1.

<figure markdown>
  ![results_06](./images/results_06.png)
  <figcaption>Figura 1 - Performance del modello con $\mu=0.6$.</figcaption>
</figure>

I risultati in termini di veri e falsi sono:

$$
\begin{align}
& TP = 4 \\
& TN = 6 \\
& FP = 1 \\
& FN = 2 \\
\end{align}
$$

Di conseguenza:

$$
P = \frac{TP}{TP+FP}=\frac{4}{4+1} = 0.8 \\
R = \frac{TP}{TP+FN}=\frac{4}{4+2} = 0.66
$$

Proviamo adesso ad aumentare il valore di $\mu$, portandolo a $0.75$. I risultati sono mostrati in figura 2.

<figure markdown>
  ![results_075](./images/results_075.png)
  <figcaption>Figura 2 - Performance del modello con $\mu=0.75$.</figcaption>
</figure>

In questo caso:

$$
\begin{align}
& TP = 3 \\
& TN = 7 \\
& FP = 0 \\
& FN = 3 \\
\end{align}
$$

per cui

$$
P = \frac{TP}{TP+FP}=\frac{3}{3} = 1 \\
R = \frac{TP}{TP+FN}=\frac{3}{3+3} = 0.5
$$

Vediamo quindi che la precisione aumenta, portandosi al $100\%$, mentre il recall diminuisce, arrivando al $50\%$.

Proviamo infine a diminuire la soglia di decisione, portandola al $50%$, come mostrato in figura 3.

<figure markdown>
  ![results_05](./images/results_05.png)
  <figcaption>Figura 3 - Performance del modello con $\mu=0.50$.</figcaption>
</figure>

In questo caso:

$$
\begin{align}
& TP = 4 \\
& TN = 4 \\
& FP = 3 \\
& FN = 2 \\
\end{align}
$$

per cui:

$$
P = \frac{TP}{TP+FP}=\frac{4}{4+3} \approx 0.57 \\
R = \frac{TP}{TP+FN}=\frac{4}{4+2} = 0.66
$$

Il recall torna ad aumentare, mentre la precisione diminuisce notevolmente.

Abbiamo quindi visto come la variazione di $\mu$ agisca su $P$ ed $R$, il cui andamento è quasi sempre inversamente proporzionale, a meno che non si abbia a disposizione un modello accurato nel $100\%$ dei casi. Di conseguenza, la detection threshold va scelta a seconda dell'applicazione specifica: nel nostro caso, se non abbiamo paura di perdere mail legittime, potremo tranquillamente abbassare il valore di $\mu$, aumentando il recall; viceversa, se tolleriamo un po' di spam, possiamo aumentare la precisione alzando la soglia decisionale.
