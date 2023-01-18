# SHAP

SHAP (SHapley Additive exPlanations) è un metodo per spiegare le predizioni individuali basato sui valori di Shapley.

## Definizione

L'obiettivo di SHAP è spiegare la predizione di un'istanza $x$ calcolando il contributo di ogni feature alla predizione. Il metodo di spiegazione SHAP calcola i valori di Shapley. I valori delle feature di un'istanza agiscono come dei giocatori all'interno di una colaizione. I valori di Shapley ci dicono come distribuire la ricompensa (ovvero, la predizione) tra le diverse feature.

TODO: TUTTO QUELLO CHE STA PRIMA

## Esempi

Nel notebook addestriamo un XGBoost a predire il rischio per il cancro uterino. Usiamo SHAP per spiegare le singole predizioni. Dato che una random forest è un insieme di alberi, possiamo usare TreeSHAP; invece di affidarci ad una distribuzione condizionale, vedremo la distribuzione marginale.

L'interpretazione è quindi legata ai valori di Shapley.

### Force plot

Visualizziamo l'attribuzione delle feature usando i valori di Shapley come delle "forze". Ogni valore delle feature è una forza che o aumenta o diminuisce la predizione. La predizione inizia dalla baseline, che è la media di tutte le predizioni. Nel force plot, ogni valore di Shapley è una freccia che spinge per incrementare (valori positivi) o diminuire (valori negativi) la predizione. Queste forze si bilanciano nel punto di predizione vero e proprio per quell'istanza.

TODO FIGURE + SPIEGAZIONE

I valori di Shapley possono essere combinati in spiegazioni globali. Se eseguiamo SHAP per ogni istanza, otteniamo una matrice di valori di Shapley. Questa matrice ha una riga per ogni istanza, ed una colonna per ciascuna feature. POssiamo interpretare l'intermo modello analizzando i valori di Shapley in questa matrice.

Iniziamo con la feature importance per SHAP.

#### SHAP Feature IMportance

L'idea dietro la SHAP feature importance è semplice: le feature con dei valori di Shapley più grandi in assoluto sono importanti. Dal momento che vogliamo l'importanza globale, mediamo i valori assoluti di Shapley per ogni feature nei dati:

$$
I_j = \frac{1}{n}\sum_{i=1}^n | \phi_j^{(i)}|
$$

Quindi, ordiniamo le feature in ordine decrescente di importanza, ed effettuiamo il plot. La seguente figura mostra la SHAP feature importance per l'XGBoost plottato prima.

TODO: FIGURA

La SHAP feature importance è un'alternativa alla permutation feature importance. Vi è una grossa differenza tra le due misure: la permutation feature importance è basata sulla diminuizione delle performance del modello. SHAP è invce basato sulla magnitudine delle feature attribution.

Il plot delle feature importance è sì utile, ma contiene poche informazioni. Per un plot più informativo, vediamo il sumamry plot.+

## Summary plot

Il summary plot combina la feature importance con gli effetti delle feature. Ogni punto sul summary plot è il valore di Shapley per una feature ed un'istanza. La posizione sull'asse y è determianta dalla feature, mentre quella sull'asse x dal valore di Shapley. Il colore rappresenta il valore della feature, da basso ad alto. I punti sovrapposti sono diffusi nella direzione dell'asse y, di modo che si abbia un senso della distribuzione dei valori di shapley per la feature. Le feature sono ordinate secondo la loro importanza.

TODO FIGURA

Nel summary plot, vediamo le prime indicazioni della relazione tra il valore di una feature e l'impatto sulla predizione. Ma per vedere la forma esatta della relazione, dobbiamo vedere lo SHAP dependence plot.

### SHAP Dependence Plot

La SHAP feature dependence può essere consideraato il plot di interpretazione globale più semplice:

1. selezioniamo una feature
2. per ogni campione, plottiamo un punto con il valore delle feature sull'asse X ed il corrispondente valore di Shapley sull'asse y
3. fatto

Matematicamente, il plot contiene i seguenti punti:

$$
{(x_j^(i), \phi_j^(i))}_{i=1}^n
$$

La seguente figura mostra la SHAP feature dependence tra anni e contraccentivii ormonali:

TODO

I dependence plot sono un'alternativa ai partial dependence plot ed agli accumulated local effects. Mentre il PDP e l'ALE mostrano gli effetti medi, gli SHAP dependence mosrano anche la varianza sull'asse y. Specialmente nei casi di interazion, gli SHAP dependence plot saranno molto più dispersi sull'asse delle y. Il dependence plot può essere migliorato evidenziando queste interazioni tra feature.

### SHAP Interaction values

L'effetto di interazione è l'effetto addizionale combinato dopo aver considerato i singoli effetti delle feature. L'indice di itnerazione di Shapley dalla teoria dei giochi è definito come:

$$
\phi_{i,j} = \sum_{S \subseteq {i, j}} \frac{|S|!(M-|S|-2)!}{2(M-1)!}\delta_{ij}(S)
$$

dove $i \neq j$ e:

$$
\delta_{ij}(S) = \hat{f}_x(S \cup {i}) - \hat{f}_x (S \cup {j}) è \hat{f}_x(S)
$$

Questa formula sottrae l'effetto principale delle feature in modo che si abbia l'effetto di interazione puro dopo aver tenuto conto degli effetti individuali. Mediamo i valori rispetto a tutte le possibili coalizioni di feature $S$, come nel calcolo dei valori di Shapley. Quando calcoliamo i valori di interazione di SHAP per tutte le feature, otteniamo una matrice per istanza con dimensioni $M \times M$, dove $M$ è il numero di feature.

Come possiamo usare l'interaction index? Per esempio, per colorare automaticamente lo SHAP feature dependence plot con l'interazione più fprte:

TODO

## Clustering

Possiamo effettuare il clustering dei nostri dati mediante i valori di Shapley. L'obiettivo del clustering è trovare dei gruppi di istanze simili. Normalmente, il clustering è basato sulle feature. Le feature sono spesso a scale differenti. Per esempio, l'altezza potrebbe essere misurata in metri, l'intensità di colore da $0$ a $100$ e l'output di alcuni sensori tra $-1$ ed $1$. La difficoltà sta nel calcolare le distanze tra istanze con queste feature differenti e non comparabili.

Il clustering SHAP lavora effettuando il clustering dei valori di Shapley per ogni istanza. Questo significa che clusterizziamo le istanze per la similarità delle loro spiegazioni. Tutti i valori SHAP hanno lsa stessa unità - l'unità dello spazio di predizione. Possiamo usare un qualsiasi metodo di clustering.

## Vantaggi

Dal momento che SHAP calcola i valori di Shapley, si applicano i vantaggi di questi: SHAP ha un fondamento teorico solido nella teoria dei giochi. La predizione è equamente distribuita tra i valori della feature. Otteniamo delle CONTRASTIVE??? EXPLAINATION che comparano la predizione con quella media.

SHAP permette di connettere LIME ai valori di Shapley. Questo è utile quindi a comprendere al meglio entrambi i metodi. PErmette anche di unificare il campo dell'interpretabilità.

SHAP ha un'implementazione veloce per i modelli basati su alberi decisionali.

La velocità di calcolo rende possibile calcolare molti valori di Shapley richiesti per l'interpretazione globale del modello (ovvero feature imporatnce, dependecn, interactions e summary plot).

## svantaggi

9.6.11 Disadvantages
KernelSHAP is slow. This makes KernelSHAP impractical to use when you want to compute Shapley values for many instances. Also all global SHAP methods such as SHAP feature importance require computing Shapley values for a lot of instances.

KernelSHAP ignores feature dependence. Most other permutation based interpretation methods have this problem. By replacing feature values with values from random instances, it is usually easier to randomly sample from the marginal distribution. However, if features are dependent, e.g. correlated, this leads to putting too much weight on unlikely data points. TreeSHAP solves this problem by explicitly modeling the conditional expected prediction.

TreeSHAP can produce unintuitive feature attributions. While TreeSHAP solves the problem of extrapolating to unlikely data points, it does so by changing the value function and therefore slightly changes the game. TreeSHAP changes the value function by relying on the conditional expected prediction. With the change in the value function, features that have no influence on the prediction can get a TreeSHAP value different from zero.

The disadvantages of Shapley values also apply to SHAP: Shapley values can be misinterpreted and access to data is needed to compute them for new data (except for TreeSHAP).

It is possible to create intentionally misleading interpretations with SHAP, which can hide biases 73. If you are the data scientist creating the explanations, this is not an actual problem (it would even be an advantage if you are the evil data scientist who wants to create misleading explanations). For the receivers of a SHAP explanation, it is a disadvantage: they cannot be sure about the truthfulness of the explanation.
