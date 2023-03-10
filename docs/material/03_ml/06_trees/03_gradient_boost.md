# Gradient Boosted Decision Trees

Come per il bagging ed il boosting, il gradient boosting è una metodologia applicata su altri algoritmi di mcahine learning.

Informalmente, il gradient boosting coinvolge due tipi di modelli:

* un modello *debole*, che è tipicamente un albero decisionale
* un modello *forte*, che è tipicamente fatto da più modelli deboli

Nel gradient boosting, ad ogni stewp, un nuovo modello debole è addestrato a predire l'errore dell'attuale modello forte (chiamato *pseudo risposta*). Definiremo succesviamente il concetto di *errore*. PEr ora, assumiamo che l'errore sia la differenza tra la predizione ed un valore di regressione. Il modello debole (ovvero l'errore) è quindi aggiunto al modello forte con segno negativo per ridurre l'errore del modello forte.

Il gradient boosting è iterativo. Ogni iterazione invoca la seguente formula:

$$
F_{i+1} = F_i - f_i
$$

dove:

* $F_i$ è il modello forte allo step $i$
* $f_i$ è il modello debole allo step $i$

Questa operazione è ripetuta fino a che non si trova un criterio di arresto, come il numero massimo di iterazione o se il modello forte inizia ad essere in overfitting su un dataset di validazione separato.

Facciamo il gradient boosting su un semplice dataset di regressione. L'obiettivo è quello di predire $y$ a partire da $x$; il modello forte viene inizializzato ad una costante pari a zero: $F_0(x) = 0$.

Vediamo dello pseudocodice per capire il gradient boosting.


```
# Simplified example of regressive gradient boosting.

y = ... # the labels
x = ... # the features

strong_model = []
strong_predictions = np.zeros_like(y) # Initially, the strong model is empty.

for i in range(num_iters):

    # Error of the strong model
    error = strong_predictions - y

    # The weak model is a decision tree (see CART chapter)
    # without pruning and a maximum depth of 3.
    weak_model = tfdf.keras.CartModel(
        task=tfdf.keras.Task.REGRESSION,
        validation_ratio=0.0,
        max_depth=3)
    weak_model.fit(x=x, y=error)

    strong_model.append(weak_model)

    weak_predictions = weak_model.predict(x)[:,0]

    strong_predictions -= weak_predictions
```

Applichiamo questo codice al seguente dataset:

FARE ESEMPIO

Vediamo cosa acade dopo la prima iterazione dell'algoritmo di gradient boosting:

FARE ESEMPIO

Notiamo che:

* il primo plot (a sinsitra) mostra le predizioni del modellop forte, che sono sempre zero
* il secondo plot mostra l'errore, che è il label del modello debole
* il terzo plot mostra il modello debole

Il primo modello debole sta apprendendo una rappresentazione grossolana della label e si focalizza sulla parte sinistra dello spazio delle feature (la parte con la maggiore variazione, e quindi l'errore maggiore per il modello costantemente errato).

A seguire gli stessi plot per un'altra iterazione dell'algoritmo:

ALTRA FIGURA

A questo punto:

* il modello forte contiene le predizioni del modello debolerispetto alla precdente iterazione
* il nuoivo errore del modello forte è ifneriroe
* la nuova predizione del modello debole è focalizzata sulla parte destra dello spazio della feature

Se eseguiamo ulteriormente il modello:

FARE FIGURA

Noptiamo che, dopo alcune iterazioni, la predizione del modello forte inizia a ricordare il plot del dataset  originario.

Qeuste figure illustriano l'algoritmo di gradient boosting che usa gli alberi decisionali come mdoelli deboli. Questa combinazione è chiamata *gradient boosting decision trees*.

Le operazioni, tuttavia, mancano di due operazioni che sono svolte nel modno relae, ovvero shrinkage ed ottimizzazione.

### Shrinkage

Il modello debole $f_i$ è moltiplicato per un valore piccolo $\epsilon$ priam di esere aggiunto al modello forte $F_i$. Questo piccolo valroe è chiamatop *shrinkage* (FARE TRADUZIONE). In altre parole,. invece di usare ad ogni iterazione la formula:

$$
F_{i+1} = F_i - f_i
$$

usiamo:

$$
F_{i+1} = F_i - \ni f_i
$$

Lo shirnkage nel gradient boosting è analogo al learning rate nelle reti neurali. Lo shringkage controlla quanto veloce il modello forte sta apprendendo, il che aiuta a limitare l'overfitting. In altre parole, un valore di shrinkage vicino allo 0' riduce l'overfitting di più rispetto ad un valore vicino ad 1.


shrinkage = 0.1   # 0.1 is a common shrinkage value.
strong_predictions -= shrinkage * weak_predictions


## L'0algoritmo di Gradient boosting

Nei problemi di regressione, ha senso definire l'errore con segno come la differenza tra la predizione ed il label. Tuttavia, in altri tipi di problemi, questa strategia spesso conduce a risultati scadenti.  Una miogliore strategia usata nel gradient boosting è quella di:

* definire una funzoine di costo simile a quella usata nelle reti neurali (ad esempio, l'entropia per un problema di classificazione)
* addestrare il modello debole a predire il *gradiente del costo* in accordo all'output del modello forte

Formalmente, data una funzione di costo $L(y, p)$, dove $y$ è una albel e $p$ una predizione, la pseudo-risposta $z_i$ uisata per addestrare il modello debole allo step $i$ è:

$$
z_i = \frac{\delta L(y, F_i)}{\delta F_i}
$$

dove:

* $F_i$ è la predizione del modello forte

L'esempio precedente era un problema di regressione: l'obiettivo è predire un valore numerico. Nel caso della regressione, l'errore quadratico è una normale funcione di costo:

$$
L(y,p)=(y-p)^2
$$

In questo caso, il gradiente è:

$$
z =  \frac{\delta L(y, F_i)}{\delta F_i} = \frac{\delta (y-p)^2}{\delta p} = 2(y-p) = 2 * e_p
$$

dove $e_p$ è l'errore di predizione MSE (Mean Signed Error) NOTA: NON E' MEDIO. In pratica, il gradiente è il doppio dell'errore di predizione. Notiamo chei fattori costanti non contano a causa dello shrinkage. Questa equivalenza è inoltre vera soltanto per prpobnlemi di regressione con costo correlato all'errore quadratico. Per altri tipi di problema di apprendimento supervisionato (ad esempio, classificaizone, ranking, regressione con altre funzioni di costo) non vi è equivalenza tra il gradiente e l'errore di predizione.

## Foglieed ottimizzazione della struttura con il metodo di Newton

Il metodo di Neuwton è un metodo di ottimizzazione come quello a discesa di gradiente. Tuttavia, a differenza della discesa di gradiente che usa soltanto il gradiente della funzione da ottimizzazre, il metodo di Newton usa sia il gradiente (derivata prima) che la derivata seconda della funzione.

Uno step dell'algoritmo a discesa di gradiente è dato dalla seguente:

$$
x_{i+1} = x_i - \frac{\delta f}{\delta x}(x_i) = x_i - f^'(x_i)
$$

mentre per il metodo di Newton abbiamo:

$$
x_{i+1} = x_i - \frac{\frac{\delta f}{\delta x}(x_i)}{\frac{\delta^2 f}{\delta^2 x}(x_i)} = x_i - \frac{f^'(x_i)}{f^{''}(x_i)}
$$

Opzionalmente, il metodo di Newton può essere integrato nell'addestramento dei GBT in due modi:

1. una volta che un albero viene addestrato, un passo del meotod di Newton è applciato su ogni foglia, andando a sovrscrivere il suo valore. La struttura ad albero è lasciata intatta; soltanto i valori foglia cambiano.
2. durante l'accrescimento dell'albero, sono scelte delle condizioni secondo un punteggio che include una componente della formula di Newton. La struttura dell'albero è alterata.


## Overfitting, regolarizzazione ed early stopping

A differenza delle random forest, i GBT possono andare in overfitting. Quindi, come per la rete neurale, si può applicare la regolarizzazione e l'early stopping usando un dataset di validazione.

Dei tipici parametri di regolarizzazione per i GBT includono:

* massima profondità ell'albero
* tasso di shrinkage
* rapporto degli attributi testati ad ogni nodo
* coefficienti L1 ed L2 sulla loss

Notiamo che gli alberi decisionali generalmente sono molto meno profondi dei modelli random forest. Di defautl, i GBT in TF-DF cresdcono fino alla profondità di 6. Siccome gli alberi sono poco profondi, il numero minimo di campioni epr foglia ha un piccolo impatto, e di solito non viene TUNED.

La necessità di un dataset di validazione è un problema quando il numero di campioni di esempio è piccolo. Quindi, è comune addestrae i GBT all'interno di un loop di cross-validazione, o disabilitare l'early stopping quando il modello si è sicuri non vada in overfitting.

## Esempi di utilizzo

model = tfdf.keras.GradientBoostedTreesModel()

# Part of the training dataset will be used as validation (and removed
# from training).
model.fit(tf_train_dataset)

# The user provides the validation dataset.
model.fit(tf_train_dataset, validation_data=tf_valid_dataset)

# Disable early stopping and the validation dataset. All the examples are
# used for training.
model.fit(
   tf_train_dataset,
   validation_ratio=0.0,
   early_stopping="NONE")
# Note: When "validation_ratio=0", early stopping is automatically disabled,
# so early_stopping="NONE" is redundant here.

## Vantaggi

I GBT hanno i seguenti vantaggi.

* come gli alberi decisionali, supportano nativamente lef eature numeriche e categoriche e spesso non hanno bisogno del preprocessing delle feature
* i GBT hanno degli iperparametri di default che spesso danno ottimi risultati. Tuttavia, il tunign di questi iperparametri può singificativamente miglikorare il modello
* i GBT sono di solito piccoli (come numero di nodi ed in memoria) e veloci da eseguire (di solito solo uno o pochi microsecondi per campione)

## Svantaggi

* gli alberi decisionalid evono essere addestrati in maniera sequenziale, che può rallentare consierevolmente il training. Tuttavia, il rallentamento nell'0addestramento è in qualche modo compensato dalle piccole dimensioni dell'albero
* così come le random forest, i GBT non possono apprendere e riutilzizare rappresentazioni interne. Ogni albero decisionale (ed ogni ramo di ogni albero decisionale) deve apprendere nuovamente il pattern del dataset. In alcuni dataset, specie quelli con dati non strutturati (ad esempio, immagini e testo) possono fare in modo che i GBT abbaino risultati peggiori rispetto ad altri metodi.

ULTIMA: https://developers.google.com/machine-learning/decision-forests/overfitting-gbdt?hl=en
