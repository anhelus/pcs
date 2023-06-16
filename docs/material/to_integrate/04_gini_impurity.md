# TODO

# Cosa è la Gini Impurity

La gini impurity è una misura usata per costruire gli alberi decisionali che determina come le feature di un dataset devono suddividere i nodi nella formazione dell'albero. Più di preciso, la gini impurity di un datase tè un numero che varia tra 0 e 0.5, che indica la probabilità che, assegnando una label casuale estratta seguendo la distribuzione delle classi nel dataset, un dato sia mal classificato.

Per esempio, diciamo che vogliamo costruire un classificatore che determian se qualcuno andrà in default sulla propria carta di credito. Abbiamo alcuni dati etichettati con delle feature, come età, introito, rating di credito, e se la persona è o meno uno studente. Per trovare la miglior feature per la prima suddivisione dell'albero (ovvero il nodo radice) possiamo calcolare quanto "male" ogni feature ha diviso i dati nella classe corretta, ovvero va in default (sì) o non va in default (no). Questo calcolo misura l'*impurità* della suddivisione, e la feature con l'impurità più bassa determina la miglior feature per suddividere il nodo attuale. Questo processo continuerà per ogni nodo successivo usando le feature rimanenti.

nell'esempio precedente (COPIARE IMMAGINE ) la variabilie età ha la gini impurity minima, per cui è scelta come radice nell'albero decisionale.



https://www.learndatasci.com/glossary/gini-impurity/

##Definizione matematica

Consideriamo un dataset $D$ che contiene campioni da $k$ classi. La probabilità che i campioni appartengano ad una classe $i$ ad un dato nodo può essere scritta come $p_i$. La gini impurity di $D$ è definita come:

$$
Gini(D) = 1 - \sum_{i=1}^k p_i^2
$$

Il nodo con la distribuzione di classe uniforme ha quindi l'impurità più alta, mentre quella minima è ottenuta quando tutti i record appartengono alla stessa classe. Ad esempio:

| Nodo | $n_1$ | $n_2$ | $p_1$ | $p_2$ | Gini impurity |
| -    | -     | -     | ----- | ----- | ------------- |
| A | 0 | 10 | 0 | 1 | 1 - 0x0 - 1x1 = 0 |
| B | 3 | 7 | 0.3 | 0.7 | 1 - 0.3x0.3 - 0.7x0.7 = 0.42 |
| C | 5 | 5 | 0.5 | 0.5 | 1 - 0.5x0.5 - 0.5x0.5 = 0.5 | 

Un attributo con la più piccola gini impurity viene scelto per suddividere il nodo.

Se un dataset $D$ è suddiviso su un attributo $A$ in due sottoinsiemi $D_1$ e $D_2$ con dimensioni $n_1$ ed $n_2$, rispettivamente, la Gini Impurity può essere definita come:

$$
Gini_A (D) = \frac{n_1}{n} Gini (D_1) + \frac{n_2}{n} Gini (D_2)
$$

Quando si addestra un albero decisionale, l'attributo che fornisce il valore minore di $Gini_A (D)$ è quello scelto per suddividere il nodo.

PEr ottenere l'information gain per un attributo, le impurità pesate dei branch vengono sottratte dall'impurity originaria. Il milgior split può anche essere ottenuto massimizzando il Gini gain. Il gini gain è calcolato come:

$$
\Delta Gini (A) = Gini(D) - Gini_A (D)
$$


