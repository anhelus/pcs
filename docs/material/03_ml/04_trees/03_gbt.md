# 3.4.3 Gradient boosted trees

Il *gradient boosting* è un altro approccio che può essere utilizzato per l'addestramento di alberi decisionali. Informalmente, il gradient boosting coinvolge due modelli:

* il primo è un modello *debole*, tipicamente un albero decisionale;
* il secondo è un modello *forte*, composto da più modelli deboli.

Il gradient boosting lavora in maniera iterativa. Ad ogni step, un nuovo modello debole viene addestrato per caratterizzare l'errore, o *pseudo riposta*, del modello forte, che assumiamo essere la differenza tra il valore vero $y$ ed il valore predetto $\hat{y}$. Conseguentemente, il modello debole sarà "sottratto" al modello forte, in modo tale da ridurre l'entità dell'errore complessivo. Analiticamente, ad ogni iterazione avviene la seguente:

$$
F_{i+1} = F_i - f_i
$$

dove:

* $F_i$ è il modello forte all'$i$-mo step;
* $f_i$ è il modello debole all'$i$-mo step.

Le iterazioni sono ripetute sino al raggiungimento di un determinato criterio di arresto, come ad esempio un numero massimo di iterazioni, o anche il fatto che il modello forte inizia ad andare in overfitting. Ovviamente, se i modelli deboli utilizzati sono degli alberi decisionali, siamo di fronte a dei *gradient boosting decision trees* (GBT).

Esistono diverse tecniche per migliorare le performance del gradient boosting, evitando che il modello vada in overfitting. Un esempio di queste tecniche è lo *shrinkage*.

##### Shrinkage

Lo *shrinkage* prevede che il modello debole $f_i$ sia moltiplicato per un $\epsilon$ molto piccolo, chiamato appunto shrinkage, prima di essere aggiunto al modello forte. In altre parole, il gradient boosting diventa:

$$
F_{i+1} = F_i - \epsilon \cdot f_i
$$

Lo shrinkage permette di controllare la "forza" dell'apprendimento del modello forte, limitando quindi l'entità dell'overfitting.

!!!tip "Shrinkage e learning rate"
    Lo shrinkage è concettualmente analogo al learning rate nelle reti neurali.

## Vantaggi e svantaggi

I GBT hanno diversi vantaggi:

* come gli alberi decisionali, supportano nativamente feature numeriche e categoriche e spesso non hanno bisogno di preprocessing delle feature;
* i valori di default degli iperparametri possono essere utilizzati dando ottimi risultati;
* sono poco costosi sia dal punto di vista spaziale, sia da quello temporale.

Tuttavia, presentano anche alcuni limiti:

* a differenza delle random forest, i singoli modelli deboli devono essere addestrati in maniera sequenziale, il che può rallentare la velocità di esecuzione dell'algoritmo;
* ogni albero deve essere addestrato da zero sull'intero dataset. Specialmente in caso di dati non strutturati, ciò fa in modo che i GBT abbiano performance peggiori rispetto ad altri metodi.
