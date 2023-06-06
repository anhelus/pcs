# LIME

I modelli di tipo Local Surrogate sono modelli interpretabili usati per spiegare predizioni singole di modelli di machine learning. In particolare, partono dal paper di LIME (Local Interpretabile model-agnostic explanations) nel quale gli autori propongono un'implementazione concreta di questo tipo di modello. I modelli surrogati sono addestrati ad approssimare le predizioni di un modello a black box. Invece di addestrare un modello globale, LIME si focalizza sull'addestramento di un modello surrogato locale per spiegare le predizioni inviduali.

L'idea alla base di LIME è abbastanza intuitva. per prima cosa, non dobbiamo considerare i dati di training, ed immaginiamo che abbiamo soltanto il modello a scatola nera dove possiamo mandare in input i dati ed ottenre le predizioni del modello. Possiamo "testare" il modello quanto spesso vogliamo. L'obiettivo è comprendere perché i modello di machine learning ha fatto una certa predizione. LIME testa cosa è accaduto alle predizioni quando diamo varianti dei nostri dati nel modello di machine learning. Genera un nuovo dataset che consiste di campioni perturbati del dataset iniziale e le predizioni corrispondenti del modello black box. Su questo nuovo dataset LIME addestra un modello interpretabile che viene pesato dalla vicinanza delle istanze campionate all'istanza di interesse. Il modello interpretabile può essere ad esempio un albero decisionale. Deve essere una buona approssimazione delle predizioni del modello di machine learning *localmente*, ma non *globalmente*. Questo tipo di accuracy è anche chiamata *local fidelity*.

Matematicamente, i local surrogate model possono essere espressi come segue:

$$
explanation(x) = \arg \min_{g \in G} L(f, g, \pi_x) + \Omega(g)
$$

dove:

* $x$ è l'istanza da spiegare;
* $g$ è il modello da spiegare;
* $L$ è la fujnzione di costo che spiega quanto la spiegazione è vicina alla predizione fatta dal modello originale $f$;
* $\Omega(g)$ è la complessità del modello;
* $G$ è l'insieme delle possibili spiegazioni;
* $\pi_x$ è la misura di prossimità chje indica qunato è grande l'intorno id $x$ che possiamo considerare per la spiegaizone.

Nella pratica, LIME ottimizza soltanto la loss. L'utente deve determinare la complessità selezionando il numero massimo di feature che il modello deve usare.

In pratica:

* scegliamo l'istanza di interesse per la quale vogliamo avere una spiegazione della predizione black box
* perturbiamo il dataset ed toteniamo le predizioni black box per questi nuovi punti
* pensiamo i nuovi campioni secondo la loro prossimità alle istanze di interesse
* addestriamo un modello pesato ed interpretabile sul dataset con le variazioni
* spieghiamo le predizioni interpretando il modello locale

## valori di Shapley

Una predizione può essere spiegata presupponendo che ogni feature in $x$ sia un "giocatore" all'interno di un gioco dove la predizione è la ricompensa finale. In tal senso, i valori di Shapley ci dicono come distribuire equamente la "ricompensa" tra le feature.

### idea generale

Pensiamo al seguente scenario.

Abbiamo addestrato un modello di machine learning a predire i prezzi degli appartamenti. Per un certo appartamento predice $300.000$ €, e dobbiamo sppiegare questa predizione. L'appartamento ha un'area di $50$ metri quadri, è al secondo piano, è vicino ad un parco, e non consente i gatti.

La predizione media per tutti gli appartamenti è di 310.000. Quanto hja contribuito ciascun valore delle feature alla predizione rispetto alla predizione media?

La risposta è semplice per i modelli di regressione lineare. L'effetto di ciascuna feature è il peso della feature moltiplicato per il valore della feature. Tuttavia, per modelli più complessi abbiamo bisongo di un'altra soluzione che, in questo caso, viene dalla teoria dei giochi cooperativi. I valori di Shapley sono un metodo per assegnare le ricompense a dei giocatori a seconda del loro contributo alla ricompensa totale. In pratica, i giocatori cooperano in una coalizione ricevendo un cerrto profitto in cambio.

In pratica, il gioco è il task della predizione per una singola istanza nel dataset. Il guadagno è l'effettiva predizione per una singola istanza meno la predizione media per tutte le istanze. I giocatori sono i valori della feature dell'istanza che collaborano per ricevere il guadagno (ovvero, per predire un certo valore). Ad esempio, nel caso precedente, i valori park-nearby, cat-banned, area-50 e floor-2nd hanno collaborato per ottenere una predizione di 300.00. Il nostro obiettivo è spiegare la differenza tra la predizione (300.000) e quella media (310.000).

La risposta potrebbe essere:

* la vicinanza ad un parco ha contribuito per 30.000
* l'area di 50 metri quadri ha contribuito per 10.000
* il secondo piano per 0
* il fatto che i gatti non sono ammessi per -50.000

I contributi somamndoli valogono -10.000, ovvero la predizione finale da cui sottaiamo il prezzo medio predetto per gli appartamenti.

## SHAP

Questa tecnica è stat proposta a partire dai valori di Shapley.

L'obiettivo è spiegare la predizione di un'istanza $x$ calcolando il contributo di ogni feature alla predizione. SHAP calcola i valori di Shapley dalla teoria dei giochi cooperativa. I valori delle feature di un'istanza sono i giocatori in una coalizione. I valori di Shapley ci dicono come distribuire equamente la ricompensa tra le feature. Un giocatore può essere considerato come un singolo valore di una feature. Un giocatore può anche essere considerato come un gruppo di valori. Per esempio, per spiegare un'immagine, i pixel possono essere raggruppati in superpixel, e la predizione diminuita tra di essi., Rispetto ai valori di Shapley, abbiamo che SHAP è un metodo di feature attribution additivo, un po' come LIME. SHAP specifica le spiegazioni come:

$$
g(z^{'}) = \phi_0 + \sum_{j=1}^M \phi_j z_j^{'}
$$

dove $g$ è il modello che spiega, $z^{'}\in{0,1}^M$ il vettore delle coalizioni, $M$ la dimensione massima della coalizeion, e $\phi_j \in \mathbb{R}$ il valore di Shapley per una feature $j$.

https://christophm.github.io/interpretable-ml-book/shap.html