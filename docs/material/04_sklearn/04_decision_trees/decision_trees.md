# X.X - Gli alberi decisionali

Gli *alberi decisionali* sono una tra le famiglie di modelli maggiormente utilizzate per l'apprendimento supervisionato, sia in fase di classificazione, sia in fase di regressione. Offrono alcuni benefici rispetto agli altri modelli, tra cui:

* una maggiore semplicità di configurazione rispetto alle reti neurali, legata alla presenza di meno iperparametri, il cui tuning, tra l'altro, risulta essere meno influente per le prestazioni finali (in pratica, è possibile utilizzare tranquillamente i valori di default);
* la capacità di gestire feature di diverso tipo (ad esempio, numeriche, categoriche, o anche mancanti), il che comporta la possibilità di effettuare meno preprocessing rispetto ad altri modelli;
* la possibilità di essere usati su dataset di piccole dimensioni con una maggiore efficienza rispetto a modelli più complessi come le rete neurali.

Da non sottovalutare, inoltre, il fatto che gli alberi decisionali forniscono spesso buoni risultati, sono robusti al rumore, ed hanno dei risultati che sono facilmente interpretabile.

## X.X. - Dataset per gli alberi decisionali

Gli alberi decisionali risultano essere molto efficaci quando si ha a che fare con dataset di tipo tabulare, come file CSV o tabelle di un database. Un esempio è, ovviamente, il dataset Titanic. Inoltre, non abbiamo la necessità di effettuare operazioni di preprocessing, come normalizzazioni, one-hot encoding, o data imputation.

Tuttavia, gli alberi decisionali non sono assolutamente adatti ad essere utilizzati su dati non tabulari (anche detti *non strutturati*), come ad esempio immagini o testo. 

## Performance

Gli alberi decisionali possono essere addestrati con efficacia su piccoli dataset, o su dataset sui quali comunque il rapporto tra feature e numero di campioni non è di molto superiore ad 1.

!!!note "Efficacia degli alberi"
    Anche se gli alberi decisionali sono efficaci in caso di rapporto quasi unitario tra feature e numero di campioni (*sample efficiency*), il funzionamento migliora quando sono disponibili molti dati, così come tutti gli algoritmi di machine learning.

## Funzionamento degli alberi decisionali

Vediamo un esempio di funzionamento degli alberi decisionali.

Un albero decisionale non è altro se non un modello composto da un insieme di *domande*, o per meglio dire *condizioni*, organizzate in maniera gerarchica sotto forma di albero. Ognuno dei nodi *non* foglia dell'albero descrive una condizione, mentre ogni nodo foglia contiene una predizione. Nella seguente figura vediamo un esempio di albero decisionale:

```mermaid
flowchart TB
  A[Gambe>2] -->|No| B[Occhi>2]
  A -->|Sì| C(Cane)
  B -->|Sì| D(Ragno)
  B -->|No| E(Gallina)
```

L'inferenza dell'albero decisionale viene quindi calcolata eseguendo il routing di un campione dalla radice fino ad una delle foglie, a seconda dei valori assunti dalle feature; il valore della foglia raggiunta rappresenta la predizione raggiunta dall'albero, mentre l'insieme dei nodi visitati è detto *percorso di inferenza*. 

Cerchiamo di capire cosa sta succedendo nel nostro esempio. Nel nodo radice, viene descritta la condizione relativa al fatto che il nostro campione abbia più o meno di due gambe. Nel nodo B, che non è un nodo foglia, viene valutata la presenza di un numero di occhi maggiore o minore di due. Nei tre nodi foglia, ovvero C, D ed E, abbiamo la *decisione* presa dall'albero (rispettivamente, cane, ragno o gallina). Ad esempio, consideriamo un campione avente due gambe e due occhi. Allora, partendo dalla radice ed arrivando alla foglia, avremo il seguente percorso di inferenza:

```mermaid
flowchart TB
  A[Gambe>2] -->|No| B[Occhi>2]
  A -->|Sì| C(Cane)
  B -->|Sì| D(Ragno)
  B -->|No| E(Gallina)
  linkStyle 1,3 stroke-width:2px,fill:none,stroke:red;
``` 

In modo simile, è possibile fare in modo che un albero decisionale effettui una predizione di regressione su dei valori numerici. Ad esempio, possiamo predire l'indice di tenerezza di un animale:

```mermaid
flowchart TB
  A[Pelosità>medio] -->|Si| B[Carineria>medio]
  A -->|No| C(1)
  B -->|Sì| D(3)
  B -->|No| E(2)
```

!!!tip "Risultati della regressione"
    Dall'esempio precedente, è evidente come cani, gatti e pulcini siano gli animali che ispirano più tenerezza nell'essere umano, laddove aracnidi, insetti e serpenti risultino essere molto meno teneri.

Vediamo adesso come distinguere i diversi tipi di condizione descritti in un albero decisionale.

## Tipi di condizione in un albero decisionale

### Axis-aligned vs. oblique

La prima distinzione che è possibile fare tra diverse condizioni riguarda il fatto che queste interessino una o più feature. In particolare, le condizioni *axis-aligned* interessano un'unica feature, mentre quelle *oblique* riguardano più feature. Tornando all'esempio precedente, la condizione $Gambe \geq 2$ è chiaramente axis-aligned, in quanto coinvolge solamente il numero di gambe dell'animale. Se, ad esempio, ci fosse stata una condizione del tipo $Gambe \geq Occhi$, avremmo avuto a che fare con una condizione oblique.

Spesso, gli alberi decisionali vengono addestrati esclusivamente con condizioni axis-aligned. D'altro canto, l'uso di condizioni oblique è potenzialmente molto potente, in quanto queste sono in grado di esprimere relazioni molto complesse tra dati; tuttavia, nella pratica, molto spesso (ab)usare delle condizioni oblique comporta performance inferiori al netto di maggiori costi in termini di tempo di addestramento.




## Binarie vs. non binarie

La seconda distinzione che esiste tra diverse condizioni riguarda quelle *binarie*, che hanno soltanto due possibili esiti, e *non binarie*, che hanno più di due possibili esiti. Prevedibilmente, gli alberi decisionali contenenti soltanto condizioni binarie sono detti *alberi binari*, mentre gli alberi contenenti anche condizioni non binarie sono detti *non binari*.

In questo caso, il compromesso è tra la generalizzazione 

TODO ESEMPIO

Le condizioni con troppa specificità, comunque, tendono a causare overfitting. Per questa ragione, gli alberi decisionali usano generalmente delle condizioni binarie.

## Come addestrare gli alberi decisionali?

Come tutti i modelli di apprendimento supervisionato, gli alberi decisionali sono addestrati per spiegare al meglio un insisem di esempi di training. Il training ottimale di un albero decisionale è un problema NP-hard. Quindi, il training è generalmente fatto mediante delle euristiche - un algoritmi di apprendimento semplice da creare che restituisce un ablero decisionale subottimo, ma vicino all'ottimo.

La maggior parte degli algoritmi usati per addestrare gli alberi decisionali usa un approccio *divide-et-impera*. L'algoritmo inizia creando un singolo nodo (la radice) ed aumenta l'albero in maniera ricorsiva usando un approccio *greedy*.

Ad ogni nodo, tutte le possibili condizioni sono valutate. L'algoritmo seleziona la migliore condizione, ovvero, la condizione con il punteggio più alto. Per adesso, ci limitiamo a sapere che il punteggio è una metrica che è correlata al task, e le condizioni sono selezionati per massimizzare questa metrica.

Per esempio, nel dataset Palmer Pengiuns, la maggio parte dei pinguini Adelie e Chinstrap hanno la lunghezza del becco maggiore a 16mm, mentre la maggior parte dei pinguinig Gentoo ha dei becchi più piccoli. Quindi, la condizione lunghezza_becco_mm > 16 permette di predire in maniera affidabile i pinguini Gentoo, ma non riesce a discerneere tra gli Adelie ed i Chinstrap. L'algoritmo considererà quindi questa condizione.

```mermaid
flowchart TD
A["lunghezza_becco_mm > 16"] --> B[Adelie o Chinstrap]
A --> C[Gentoo]
```

L'algoritmo quindi ripete in maniera ricorsiva ed indipendente o entrambi i nodi figli. Quando non si trova una condizione soddisfacente, il nodo diventa una foglia. La predizione della foglia è determianta come l'etichetta più rappresentativa negli esempi.

L'algoritmo è il seguente:

```py
def train_decision_tree(training_examples):
  root = create_root() # Create a decision tree with a single empty root.
  grow_tree(root, training_examples) # Grow the root node.
  return root

def grow_tree(node, examples):
  condition = find_best_condition(examples) # Find the best condition.

  if condition is None:
    # No satisfying conditions were found, therefore the grow of the branch stops.
    set_leaf_prediction(node, examples)
    return

  # Create two childrens for the node.
  positive_child, negative_child = split_node(node, condition)

  # List the training examples used by each children.
  negative_examples = [example for example in examples if not condition(example)]
  positive_examples = [example for example in examples if condition(example)]

  # Continue the growth of the children.
  grow_tree(negative_child, negative_examples)
  grow_tree(positive_child, positive_examples)
```

Vediamo i passi necessari ad addestrare un certo albero decisionale in dettaglio.

* Step 1: creiamo un nodo radice

```mermaid
flowchart TD

A["nodo radice"]
```

Step 2: accresciamo il nodo 1. La condizione x1 >= 1 viene trovata. Sono creati due nodi figli:

```mermaid
A["x1 >= 1 nodo radice"] --> Yes --> B["? nodo 3"]
A --> No --> C["? nodo 2"]
```

Step 3: accresdciamo il nodo 2. Non sono state trovate condizioni soddisfacenti. Per cui, il nodo diventa una foglia.

```mermaid
flowchart TD

A["x1 >= 1 nodo radice"] --> sì --> B["? nodo 3"]
A --> No --> C["foglia nodo 2"]
```

Step 4: accresciamo il nodo 3. La condizione "x2 >= 0.5" è stata individuata. Due nodi figli sono creati.

```mermaid
flowchart TD
  A["x1 >= 1 nodo radice"] --> sì --> B["x2 > 5 nodo 3"]
  A --> No --> C["foglia nodo 2"]
  B --> Si --> D["? nodo 5"]
  B --> No --> E["?nodo 4"]
```

Esistono altri metodi per accrescere gli alberi decisionali. Un'alternativa popolare è ottimizzare globalmente i nodi invece di usare una strategia divide-et-impera.

A seconda del numero e del tipo di feature di input, il numoer di possibili condizioni per un dato nodo può essere enorme, generalmente infiito. Ad esempio, data una condizione di soglia $feature_i \geq t$, la combinaizone di tutti i possibili valore di soglia $t \in \mathbb{R}$ è infiniat.

La routine responsabiel per individualre la miglireo condizione è chiamata *splitter*. Siccome deve testare un gran numero di possibili condizioni, gli splitter sono i colli di bottiglia quando si addestra un albero decisionale.

Il punteggio massimizzzato dallo splitter dipende dal task. AD esempio:

* Information Gaìni e Gini sono normalmente usati per la classiciazione.
* l'0errore quadratico medio è normalmente usato per la regressione

Ci sono molti algoretimi di splitting, ognuno con vario spporto per:

* tipo di feature; ad esempio, numerica, categorica, testuale;
* task: pèer esempio, classificazione binaria, multiclasse, regtressione;
* tipo di condizione: per esempio, condizione di soglia, obliqua, etc.;
* criterio di regolarizzaizone: per esempio, splitter essatti o approssimati per le condizioni di soglia.

Inoltre, ci sono deglle varianti equivalenti delgi splitter con diversi compromessi per l'uso di memoria, CPUI, e via dicendo.


## Classificazione binaria

Splitter per la classificazione binaria con feature numeriche

Vediamo il più semplice e comune algoritmo di splitting, che crea condizioni nella fomra $feature_i \geq t$ nel seguente setting:

* task di classificazione binaria
* senza valori mancanti negli esempi
* senza indici precalcolati sugli esempi

Assumiamo un insieme di $n$ campioni con una freatrure numerica ed una label bianrai "arancio" e "blu". Formalmente, il dataset può essere descritto come:

$$
D={(x_i, y_i)}_{i \in[1, n]}
$$

dove:

* $x_i$ è il valore di una featrure numerica in $\mathbb{R}$ (l'insieme di numeri reali)
* $y_i$ è una valore per la label di classificazione binaria tra arancio e blu

L'obiettivo è trovare un valore di soglia $t$ tale che dividendo i campioni $D$ nei gruppi $T(rue)$ ed $F(alse)$ secondo $x_i \geq t$ migliroaiamo la separazione delle label. Ad esmepio, più esempi arancioni saranno in $T$, e più esempi blu saranno in $F$.

L'entropia di Shanno è una misura di disordine. Per una label binaria:

* l'etnropia di Shanno è massima qunado le label negli esempi sono bilanciate ($50\%$ blu, $50\%$ arancioni)
* l'entropia di SHanno è minima (valore zero) quando le label negli esempi sono pure ($100\%$ blu o $100\%$ arancioni)

Formalmente, vogliamo trovare una condizione che diminuisce la somma pesata dell'entropia delle distribuzioni delle label in $T$ ed $F$. Il punteggio corrispondente è detto *information gain*, che è la differneza tra l'entropia di $D$ e quella dell'insieme ${T, F}$.

La seguente figura mostra una suddivisione errata, nella quale l'entropia rimane alta ed il guadagno informativo basso.

In contrasto, la seguente figura mostra uno split miglire nel quale le'ntropia diventa bassa (ed il guadagno informativo  alto).

Formalmente:

$$
T = {(x_i, y_i)|(x_i, y_i) \in D con x_i \geq t} \\
F = {(x_i, y_i)|(x_i, y_i) \in D con x_i < t} \\
R(X) = \frac{|{x|x \in X, x=pos}|}{|X|} \\
H(X) = -p log p - (1-p) log(1-p) con p = R(X) \\
IG(D, T, F) = H(D) - \frac{|T|}{|D|} H(T) - \frac{|F|}{|D|}H(F)
$$

con:

* $IG(D,T,F)$ guadagno infomrativo legato alla suddivisione di $D$ in $T$ ed $F$.
* $H(X) è l'entropia dell'insieme di campioni $X$.
* $|X|$ è il numero di elementi nell'insieme $|X|$.
* $t$ è il valore di sopglia.
* $pos$ è il valore della label *positivo*, ad esempio, blue nell'esempio prec edfentre. Scegelier una diversa label come positiva non cambia il valore dell'entropia o dell'information gain.
* $R(X)$ è il rapporto dei valori delle label positive nei campioni $X$.
* $D$ è il dataset.

Nel seguente esempio, consideriamo un datraset poer la classificazione binaria con una singola feature numerica $x$. La seguente figura mostra per differenti valori della soglia $t$ (sull'asse X):

1. L'istogramma della feature $x$.
2. Il rapporto di campioni "blu" negli insiemni $D$, $T$ ed $F$ secondo il valore di soglia.
3. L'entropia in $D$, $T$, ed $F$.
4. Il guadagno informativo, ovvero il delta, in termini di entropia, tra $D$ e ${T, F}$ pèersato per il numero di campioni.

Questi plot mostrano i seguenti:

* il plot di  frequenza mostra che le osserrvazioni sono relativamente ben diffuse con concentrazioni tra 18 e 60. Un valore dello spread ampio indica che ci sono molti split potenziali, il che è un bene per l'addestramento del modello.
* il rapporto di label blue nel dataset è di circa il 25%. Il plot relativo mostra questo per i valori di soglia tra 20 e 50:
  * l'insieme T contiene un eccesso di campioni blu (fino al 35% per la soglia 35)
  * l'insieme F contiene un deficit complementare di caompionio etichettati con blu (solo 8% per la soglia 35)
  Sia il "rapporto di label blu" sia il plot di entropia indicano che le label possono essere relativamente ben sepèarate in questo range di soglie.
* Questa osservazione è confermata nel plot "information gain". VEdiamo che il massimo guadagno informativo è ottenuto con $t \sim 28$ per un valore di circa $0.074$. Quindi, la condizione restituita dallo splitter sarà $x \geq 28$.
* Il guadagno informativo è sempre maggiore o uguale a zero. Converge a zero man mano che il valore di soglia va verso il suo valore massimo (minimo). In questi casi, o $F$ o $T$ diventano vuoti mentre l'altro contiene l'0iutenro dataset e mostra un'entropia uguale a quella in $D$. Il guadagno informatiov può anche essere zero quando $H(T)=H(F)=H(D)$. Alla soglia 60, il rapporto di label blue per sia $T$ sia $F$ è lo stesso di quello di $D$, ed il guadagno informatiov è nullo.

I valori candidati per $t$ nell'isnieme dei numeri reali ($\mathbb{R}$) sono infiniti. TTuttavia,d ato un numeor finito di campioni, osltmnatop un numero difnito di divisioni di $D$ in $T$ ed $F$ esiste. Quidni, solo un numero finito di valori di $t$ possono essere testati in modod singificativo.

Un approccio classico è quello di ordinare i valori $x_j$ in ordine crescente $x_{s(i)}$ in modo che:

$$
x_{s(i)} \leq x_{s(i+1)}
$$

Quindi, sit esta $t$ per ogni valore a metà tra valori ordinati consecutivi di $x_i$. Ad esempio, supponiamo di avere 1000 valori a virgola mobile per una certa feature. Dopo l'ordianmento, supponiamo che i primi due valori siano 8.5 e 8.7. In questo caso, il primo valore di soglia da testare dovrebbe essere 8.6.

Formalmente, consideriamo i seguenti valori candidati per $t$:

$$
X = \{\frac{x_{s(i)}+x_{s(i+1)}}{2}|x_{s(i)} \diff x_{s(i+1)}\}
$$

La complessità nel tempo di questo algoritmo è un $O(n log n)$, con $n$ il numero di campioni nel nodo (a causa dell'ordinamento dei valori delle feature). Quando applicato ad un albero decisionale, l'algoritmod i splitting viene applicato ad ogni nodo ed ogni feature. Notiamo che ogni nodo riceve circa la metàò degli esempi del suo nodo genitore. Quindi, in accordo al [teorema dell'esperto](https://it.wikipedia.org/wiki/Teorema_dell%27esperto), la complessità nel tempo di addestare un albero decisioanle con questo splitter è data da:

$$
O(mn log^2 n)
$$

dove:

* m è il numero di feature;
* $n$ è il numero di campioni di training.

In questo algoritmo, il valore delle feature non importa; soltanto l'ordine è importante. Per questra ragione, questo algoritmo lavora in modo indipendente dalla scala o dalla distribuzione dei valori delle feature. Questo è+ il motivo per cui non dobbiamo normalizzare o scalare le featrur numeriche quando addestriamo un albero decisionale.

## Overfitting e pruning

Usando l'algoritmo dfescritto in precedenza, possiamo addestrare un albero decisionale che classifichi perfettamente i campioni di training, a patto che questi siano separabili. Tuttavia, se il dataset contiene del rumore, questo albero andrà in overfitting sui dati, e mostrerà scarse abilità in fase di test.

La seguente figura mostra un dataset rumoroso con una relazione tra una feature $x$ e la label $y$. La figura mostra anche un albero decisioanle addestrato su qeusto dataset senza alcun tipo di regolarizzzione. Questo modello predice correttamente tutti i campioni di training (in pratica, le predizioni dle modello sono in grado di combaciare con gli esempi di training). Tuttavia, su un dataset contenente lo stesso pattern lineare con un diverso tipo di rumore, il modello offrirà performance subottimali.

Per limitare l'overfitting di un albeor decisionale, applichiamo uno o entrambi i seguenti criteri di regolarizzaizone mentre addestriamo l'albero stesso:

* impostare una profondità massiam: facciamo in modo che l'albero decisionale non vada oltre una massima profondità, come 10;
* impostiamo un numero minimo di campioni nelle foglie: una foglia con meno di un certo numero di campioni non sarà considerata per la divisoine.

La seguente figura illustra gli effetti di usare un numero minimo di campioni per foglia variabile. Il modello cattura un minor quantitativo di rumore.

TODO

Possiamo anche efefttuare la regolarizzaizone dopo l'addestramento rimuovendo in modo selettivo alcuni rami (pruning), ovvero, convertendo certi nodi non-foglia in foglia. UNa soluzione comune ad selezionare i rami da rimuovere è quella di usare und ataset per la validazione. Ovvero, se rimuovere un ramo migliora la qualità del modello sul dataset di valdiazione, quindi il ramo viene rimosso.

La seguente illustrazione mostra quesrta idea. Qui, testiamo se l'accuracy dik validazione dell'albero decsiionale è migliroata se il nodo non-foglia in verede è trasformato in foglia; ovvero, effettuando il pruning dei nodi arancvioini.


DA FIGURA 14

La segyunte figura illustra l'effetto di usare il 20% del dataset come validazione per effettaure il pruning dell'albero decisionale.


Notiamo che l'uso di un dataset di validazioen riduce il numero di esempi disponibili per l'addestramento iniziale dell'albero decisionale.

Molti modelli inoltre applicano più criteri. Ad sempio, possiamo usare i seguenti:

* applicare un numero minimo di campioni per nodo foglia
* applicare una profondità massima per limitare la crescita dell'albero decisionale
* effettuare il pruning dell'albero decisionale

Questi criteri introducono nuovi iperparametri che devono essere impostati (ad esempio, la massima profondità dell'albero), spesso con tuning degli iperparametri automatizzzato. Gli alberi decisionali sono in geenrale abbastanza veloci da addestrare usando l'ottimizzazione degli iperparametri in crss-validazione. Per esempio, su un dataset con "n" campioni:

* dividiamo i campioni di training in $p$ gruppi non-sovrapposti, per esempio $p=10$.
* per tutti i possibili valori degli iperprametri, valutiamo, su ogni gruppo, la qualità dell'albero decisionale addestrato sugli altri $p-1$ gruppi; facciamo poi la media delle valutazioni sui diversi gruppi;
* selezioniamo i valori degli iperparametri con la migliore valutazione media;
* addestriamo un albero decisionale finale usando tutti gli $n$ campioni con gli iperparametri selezionati.

In questa sezione abbiamo discusso il modo in cui gli alberi decisionali limintano l'overfitting. Nononstante questi metodi, l'underfitting e l'overfitting sono delle debolezze degli alberi decisionali. Le foreste decisionali introducono nuovi metodi per limtiare l'overfitting, come vedremo dopo.

## interpretazione diretta dell'albero decisionale

Gli alberi decisionali sono facili da interpretare. Detto questo, cambiare anche pochi esempi può modificare completamente la struttura (e quindi l'interpretazione) dell'albero decisionale.

!!!note "Nota"
    Specialmente quando il dataset contiene molte feature in qualche modo simili, l'albero decisionale appreso è solo uno di più alberi decisionali più o meno equivalnetni che fittano i dati.

Visto il modo in cui gli alberi decisionali sono costruiti, effettuando il partizionalmento dei campiioni di trainging, si può usare un albero decisioanle per interpretare il dataset (invece di modellarlo). Ogni foglia rappresnta un particolare angolo del dataset. 

## Importanza delle variabili

Per *importasnza delle variabili* (detto anche *feature importance*) si intende un punteggio che indica quanto "importante" sia una feature per il modello. Ad esempio, se per un dato modello con due feature in input $f_1$ ed $f_2$ l'importanza delle variabili sono $f_1 = 5.8, f_2=2.5$, allora la feature $f1$ è più importante per il modello della feature $f2$. Così come per altri modelli di machine learning, l'importanza delle variabili è un modo semplice di comprendere come funziona un albero decisionale.

Possiamo definire l'importanza delle feature in modo agnostico usando metodi come permutation impotrance.

Gli alberi decisionali hanno anche delle specifiche importanze per le variabili, come:

* somma dei punteggi parziali associati ad unac erta feaature
* numero di nodi con una data feature
* profondità media della prima occorrenza di unaf eature in tutti  i percorsi dell'albero

L'importanza delle variabili può differire in base a qualità come semantica, scala o proprietà. Inoltre, l'importanza delle variabili foirnisce diversi tipi di informazione circa modello, dataset, e processo di addestramento.

Ad esempio, il numero di condizioni contenenti una certa feature indca quanto un albero decisionale sta guardando a quella specifica feature, il che può indicare l'importanza della variabile. Dopo tutto, l'algoritmo di apprendimento non avrebbe usato una feature in diverse condizioni se questa non avesse avuot importanza. Tuttavia, la stessa feature che appare in più condizioni può anche indicare che il modello sta provando a generalizzare il pattern per quella feature, fallendo. Ad esempio, questo può accadere quando una feature è specifica per ogni campione (il nome e cognome), senza alcuna infomrazione da generalizzare.

D'altro canto, un alto valore di importanza per la variabile indica che rimuovere quella feature inficia il modello, il che è un'indicazione dell'importanza della variabile. Tuttavia, se il modello è robusto, rimuovere una qualsiasi delle feature non dovrebbe influenzare il modello.

Dato che diverse variabili informano su diversi aspetti del modello, osservare contestualmente l'importanza di diverse varaibili è informativo. Ad esempio, se una feature è importante in accordo a tutte le altre, è plausibile che sia molto importante. 

## Esempio con tensorflow-decision

Vediamo come usare la libreria TF-DF per addestrare, rifinire ed interpretare un albero decisionale.

Possiamo farlo sia in locale, sia da un notebook Colab. Per farlo, dovremo installare la libreria TensorFlow Decision Forests.

```sh
pipenv install tensorflow_decision_forests
```

All'apice del nostro codice, importiamo le seguenti librerie:

```py
import numpy as np
import pandas as pd
import tensorflow_decision_forests as tfdf
```

Useremo il dataset relativo ai Palmer Pengiuns, che contiene le misurazioni in termini di dimensione per tre specier di pinguini , ovvero il pigoscelide antartico (Chinstrap), il pinguino Gentoo, ed il pinguino di Adelia (Adelie).

Per prima cosa, carichiamo il dataset in memoria utilizznado Pandas:

```py
path = "https://storage.googleapis.com/download.tensorflow.org/data/palmer_penguins/penguins.csv"
dataset = pd.read_csv(path)
```

Visualizziamo la testa del dataset.

```py
dataset.head()
```

TODO: IMMAGINE

Notiamo come il dataset contenga diversi tipi di dato, sia numerici (ad esempio, bill_length_mm), sia categorici (ad esempio, sex). Vi sono inoltre delle feature mancanti. A differenza delle reti nuerali, tuttavia, le foreste decisionali sono in grado di supportare tutti questi tipi di feature in maneira nativa, per cui non dobbiamo effettaure encoding, normalizzazioni o roba del genere.

Per semplificare l'interpretabilità, convertiamo manualmente le specie dei pinguini in label intere:

```py
label = "species"

classes = list(pandas_dataset[label].unique())
print(f"Label classes: {classes}")
# >> Label classes: ['Adelie', 'Gentoo', 'Chinstrap']

pandas_dataset[label] = pandas_dataset[label].map(classes.index)
```

https://developers.google.com/machine-learning/decision-forests/practice?hl=en
