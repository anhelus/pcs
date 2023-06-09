# TODO

# Cosa è la Gini Impurity

La gini impurity è una misura usata per costruire gli alberi decisionali che determina come le feature di un dataset devono suddividere i nodi nella formazione dell'albero. Più di preciso, la gini impurity di un datase tè un numero che varia tra 0 e 0.5, che indica la probabilità che, assegnando una label casuale estratta seguendo la distribuzione delle classi nel dataset, un dato sia mal classificato.

Per esempio, diciamo che vogliamo costruire un classificatore che determian se qualcuno andrà in default sulla propria carta di credito. Abbiamo alcuni dati etichettati con delle feature, come età, introito, rating di credito, e se la persona è o meno uno studente. Per trovare la miglior feature per la prima suddivisione dell'albero (ovvero il nodo radice) possiamo calcolare quanto "male" ogni feature ha diviso i dati nella classe corretta, ovvero va in default (sì) o non va in default (no). Questo calcolo misura l'*impurità* della suddivisione, e la feature con l'impurità più bassa determina la miglior feature per suddividere il nodo attuale. Questo processo continuerà per ogni nodo successivo usando le feature rimanenti.

nell'esempio precedente (COPIARE IMMAGINE ) la variabilie età ha la gini impurity minima, per cui è scelta come radice nell'albero decisionale.



https://www.learndatasci.com/glossary/gini-impurity/