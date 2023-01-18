# Valori di Shapley

Una predizione può essere spiegata assumendo che ogni valore delle feature di un istanza sia un "giocatore" in un gioco dove la posta in gioco è data dalla predizione. I valori di Shapley (un metodo della teoria dei giochi) ci dicono come distribuire la posta tra le diverse feature.

## Idea generale

Supponiamo il seguente scenario.

Abbiamo addestrato un modello di machine learning a predire i prezzi degli appartamenti. Per un dato appartamento, predice una cifra di $300.000$ €, la quale però va spiegata. L'appartamento ha un'area di $50$ $m^2$, è collocato al secondo piano, è vicino ad un parco, e non accetta gatti.

La predizione media per gli appartamenti in generale è di $310.000$ €. Quanto contribuisce il valore di ciascuna feature alla predizione media?

La risposta è semplice per un modello a regressione lineare. L'effetto di ogni feature è il peso della feature moltiplicato per il valore della stessa. Questo funziona grazie alla linearità del modello. Per modelli più complessi, abbiamo bisogno di una soluzione differente. Ad esempio, LIME suggerisce dei modelli locali per stimare gli effetti. Un'altra soluzione è relativa alla teoria dei giochi cooperativa: i valori di Shapley, ovvero un metodo per assegnare dei premi ai giocatori a seconda del contributo che hanno avuto alla posta complessiva. In pratica, i giocatori cooperano in una coalizione, e ricevono un certo profitto da questa cooperazione.

Nel contesto del machine learning, il *gioco* è il task di predizione per una singola istanza del dataset. Il *guadagno* è la predizione per questa istanza, a cui dobbiamo sottrarre la predizione media per tutte le istanze. I *giocatori* sono i valori delle feature dell'istanza che collaborano a ricevere un guadagno (ovvero, predire un certo valore). Nell'esempio dell'appartamento, i valori delle feature `park-nearby`, `cat-banned`, `area-50` e `floor-2nd` lavorano insieme per ottener ela predizione di 300.000. L'obiettivo è spiegare la differenza tra la predizione ottenuta (300.00) e quella media di 310.000.

La risposta potrebbe ad esempio essere: la feature `park-nearby` ha contribuito per 30.000; la feature `area-50` per 10.000; la feature `floor-2nd` per 0; `cat-banned` per -50.000. I contributi, sommandosi, danno esattamente -10.000, ovvero la predizione finale a cui dobbiamo sottrarre il prezzo medio predetto per l'appartamento.

#### Come calcolare il valor di Shapley per una feature

Il valore di Shapley è il contributo marginale di una feature su tutte le possibili combinazioni di feature.

Valutiamo il contributo della feature `cat-banned` quando è aggiunta all'insieme di `park-nearby` ed `area-50`. Simuliamo solo che park-nearby, cat-banned ed area-50 siano in una combinazione estraendo in modo casuale un altro appartamento dai dati ed usando il suo valore per la feature `floor`. Il valore `floor-2bd` è stato rimpiazzato dal valore estratto casualmente `floor-1st`. Quindi prediciamo il prezzo degli appartamenti con questa combinazione, ed otteniamo 310.000. In un secondo step, rimuoviamo `cat-banned` dall'insieme, rimpiazzandolo con un valore casuale della feature `allowed/banned`. Nell'esempio considerato, abbiamo `cat-allowed`. Prediciamo il prezzo per l'insieme di `park-nearby` ed `area-50`, ed otteniamo 320.000. Il contributo di `cat-banned` era pari a 310.000 - 320.000 = -10.000. Questa stima dipende dai valori degli appartamenti estratti casualmente che sono serviti da "donatori" per i valori delle feature cat e floor. Otterremo delle stime migliori se ripetiamo questo step di campionamento mediando i contributi.

Ripetiamo questi calcoli per tutte le possibili combinazioni. Il valore di Shapley è la media di tutti i contributi marginali a tutte le possibili coalizioni. Ovviamente, il costo computazionale cresce in maniera esponenziale al numero di feature. Una soluzione per mantenere il tempo di calcolo gestibile è quella di calcolare i contributi per soltanto pochi valori delle possibili coalizioni.

Vediamo tutte le coalizioni di valori delle feature che sono necessarie per determinare i valori di Shapley per `cat-banned`.

Partiamo da:

1. nessun valore delle feature
2. park-nearby
3. area-50 
4. floor-2nd
5. park-nearby + area-50
6. park-nearby + floor-2nd
7. area-50 + floor-2nd
8. park-nearby + area-50 + floor-2nd

In pratica, per ognuna di queste coalizioni, calcoliamoil valore predetto per il prezzo dell'appartamento con e senza il valore della feature `cat-banned`, e vediamo la differenza per ottenere il contributo marginale. Il valore di Shapley è la media pesata di tutti i contributi marginali. Rimpiazziamo i valori delle feature delle feature che non sono in una coalizione con dei valori casuali delle feature dal dataset per ottenere una predizione a partire dal modello di machine learning.

Se stimiamo i valori di Shapley per tutti i possibili valroi delle feature, otteniamo la distribuzione completa delle predizioni (meno la media) tra i valori delle feature.

## Esempi ed interpretazione

L'interpretazione del valore di Shapley per il valore delle feature $j$ è: il valore ella $j$-ma feature ha contribuito $\phi_j$ alla predizione di questa particolare istanza se comparato alla predizione media per il dataset.

Il valore di Shapley vale sia per la classificazione (se abbiamo a che fare con delle probabilità) sia con la regressione.

Usiamo il valore di Shapley per analizzare le predizioni di un random forest che predice il cancro all'utero:

TODO: PREDIZIONE + COMMENTO

Per il dataset del bike rental, addestriamo un random forest a prdire il numero di bici a noleggio per la giornata, dato il tempo e le informazioni di calendario. La speigazione creata per la predizione del random forest di un certo giorno è la seguente:

TODO: CODICE, PREDIZIONE, FIGURA

Dobbiamo fare attenzione ad interpretare correttamente i valori di Shapley. I valori di Shapley sono il contributo medio del valore di una feature alla predizione in diverse coalizioni. I valori di Shapley NON sono la differenza nella predizione quando rimuoviamo la feature dal modello.

## valori di shapley nel dettaglio

Vediamo come efinire e calcolare i valori di Shapley.

Siamo interessati in come ogni feature influisca sulla predizione di un certo campione. In un modello lineare, calcolare gli effetti individuali è facile. Ricordiamo come appare la predizione per un modello lineare per una singola istanza:

$$
\hat{f}(x) = \beta_0 + \beta_1 x_1 + \cdots + \beta_p x_p
$$

dove $x$ è l'istanza per la quale vogliamo calcolare i contributi. Ogni $x_j$ è il valore di una feature, con $j = 1, \ldots, p$.Il valore $\beta_j$ è il peso corrispondente alla feature $j$.

Il contributo $\phi_j$ della j-ma feature sulla predizione $\hat{f}(x)$ è dato da:

$$
\phi_j(\hat{f}) = \beta_j x_j - E(\beta_j X_j) = \beta_j x_j - \beta_h E(X_j)
$$

dove $E(\beta_j Xh)$ è il valore atteso per l'effetto della feature $j$. Il contributo è dato dalla differenza tra l'effetto della feature e l'effetto medio. Ora che sappiamo quanto ogni feature ha cotnribuito alla predizione. Se sommiamo tutti i contributi delle feature per un'isstanza:

$$
\begin{aligned}
\sum_{j=1}^p \phi_j(\hat{f})&=\sum_{j=1}^p(\beta_j x_j - E(\beta_jX_j)) \\
&=(\beta_0+\sum_{j=1}^p \beta_j x_j) - (\beta_0 + \sum_{j=1}^pE(\beta_jX_j)) \\
&=\hat{f}(x)-E(\hat{f}(X))
\end{aligned}
$$

Questo è il valore predetto per l'istanza $x$, a cui sottraiamo il valore medio predetto. I contributi delle feature possono essere negativi.

Possiamo fare la stessa cosa per ogni tipo di modello? Sarebbe ottimo avere un tool agnostico. Dal momento che normalmente non abbiamo pesi simili in altri tipi di modello, abbiamo bisogno di una soluzione differente.

In aiuto ci viene la teoria dei giochi cooperativa. Il valore di Shapley è la soluzione per calcolare il contributo delle feature per le singole predizioni di ogni modello di machine learning.

## Valore di Shapley

Il valore di Shapley è definito mediante una funzione $val$ dei giocatori in $S$.

Il valore di Shapley di un valore di una feature è dato dal suo contributo alla posta generale, pesato e sommato su tutte le possiibli combinazioni di valori delle feature:

$$
\phi_j(val) = \sum_{S\subseteq{1, \ldots,p}} \frac{|S|!(p-|S|-1)!}{p!} (val (S \cup {j})-val(S))
$$

dove $S$ è un sottoinsieme delle feature usate nel modello, $x$ è il vettore dei valori delle feature dell'istanza da spiegare, e $p$ è il numero di feature. $val_x (S)$ è la predizione dei valori delle feature nell'insisem $S$ che sono marginalizzate rispetto alle feature non incluse in $S$:

$$
val_x(S) = \int \hat{f}(x_1, \ldots, x_p) d \mathbb{P}_{x \notin S} - E_X(\hat{f}(X))
$$

!!!note "Nota"
    Nei fatti, si effettuano più integrazioni per ogni feature che non è contenuta in $S$. 

!!!tip "Suggerimento"
    E' importante non confondersi tra i diversi usi della parola "valore". Il valore delle feature è il valore (numerico o categorico) di una feature e distanza; il valore di Shapley è il contributo di una feature alla predizione; il funzione valore è la funzione che regola la posta per una coalizione di giocatori.

Quello del valore di Shapley è l'unico metodo di attribuzione che soddisfa le proprietà di *efficienza*, *simmetria*, *dummy* ed *additività*, che possono insieme essere considerate per la definizione di una paga equa.

* efficienza: i contributi delle feature devono aggiungersi alla differenza della predizione per $x$ e la media.

$$
\sum_{j=1}^p \phi_j = \hat{f}(x) - E_X(\hat{f}(X))
$$

DA SYMMETRY

# Shap

SHAP (SHapley Additive exPlanations) è un metodo proposto da Lundberg e Lee nel 2017 (https://christophm.github.io/interpretable-ml-book/shap.html#fn69) per spiegare le predizioni individuali di un modello. SHAP è basato su un approccio legato alla teoria dei giochi.