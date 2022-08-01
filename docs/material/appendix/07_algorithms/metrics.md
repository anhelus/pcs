Top-k: metrica che calcola il numero di volte dove la label corretta è tra le prime $k$ label predette, ordinate secondo gli score di predizione.

Average precision:

la AP riassume la curva precision-recall come media pesata delle precisioni ottenute al variare della soglia, con un aumento nel recall dalla precedente soglia usato come peso:

$$
AP = \sum_{n} (R_n - R_{n-1}) P_n
$$

dove $P_n$ ed $R_n$ sono la precisione ed il recall alla $n$-ma soglia. Questa implementazione non è interpolata, ed è diversa dal calcolare l'area nella curva precision-recall con la regola trapeziodale, che usa l'interpolazione lineare e può essere eccessivamente ottimista.

ROC AUC

Una ROC è un plot grafico che illustra le performance di un sistema di classificazione binaria al variare della soglia di discriminazione. Viene creata plottando la frazione di true positive rispetto ai positivi (TPR = true positive rate) rispetto alla frazione di falsi positivi sui negativi (FPR = false positive rate) a diverse impostazioni di soglia. La TPR è anche chiamata *sensitivity*, mentre la FPR è+ 1 meno la specificity (ovvero il true negative rate).

Possiamo clacolare l'area sotto la curva ROC, che è chiamata AUC o AUROC. Calcolando l'AUC, la curva viene riassunta in un unico numero.

F1 score

L'F1 score può essere interpretato come la media armonica di precisione e recall, dove un F1 score raggiunge il suo valore migliore ad 1 e peggiore a 0. Il contributo relativo di precisione e recall all'F1 score sono uguali.
