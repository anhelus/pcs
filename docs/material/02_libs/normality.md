https://machinelearningmastery.com/a-gentle-introduction-to-normality-tests-in-python/

# Assunzione di normalità

Una grossa parte del campo della statisitca riguarda i dati che sono estratti da una distribuzione gaussiana.

Se usiamo dei metodi che assumono una distribuzione gaussiana, ed i nostri dati sono stati estrattid a una distribuzione differente, quello che troveremo potrebbe essere fuorviante o, semplicemente, errato.

Vi è un gran numero di tecniche che possiamo usare per controlalre che i nostri campioni siano gaussiani (o simili) per usare tecniche standard, oppure non gaussiani per usare metodi non parmaetrici.

Questo è un punto chiave quando dobbiamo scegliere i metodi statistici per i nostri campioni. In altre parole:

```py
if dati_gaussiani:
    usa_metodi_parametrici()
else:
    usa_metodi_non_parametrici()
```

Vi è anche una terra di nessuno nella quale possiamo presupporre che i dati siano sufficientemente gaussiani per usare i metodi parametrici, o che possiamo usare tecniche di data preprataion per trasformare i dati in modod che siano sufficientemente gaussiani da usare metodi parametrici.

Ci sono tre aree pricnipali dove potremmo dover fare questa valutazione nel machine learning, ovvero:

* dati di ingresso al modello nel caso di fitting;
* valutzione dei risultati del modello in caso di model selection;
* errori dresidui dalle predizioni del modello in caso di regressione.

Vedremo brevemente due classi di tecniche per controllare se un campione di dati è gaussiano, ovvero:

* metodi grafici, che plottano i dati e valutano qualitativamente se sembrano gaussiani;
* test statistici: metodi che calcolano delle statistiche sui dat e quantificano la probabilità che i dati siano statit estratti da una distribzuone gaussiana.

I metodi di quest'ultimo tipo sono sesso chiamati *test di normalità*.
