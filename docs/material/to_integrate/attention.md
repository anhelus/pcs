https://machinelearningmastery.com/the-attention-mechanism-from-scratch/

# The Attention Mechanism

Il meccanismo alla base dell'*attention* è stato introdotto da Bahdanau (https://arxiv.org/abs/1409.0473) nel 2014 per affrontare il cosiddetto *bottleneck problem* che sorge nel momento in cui usiamo un vettore di codifica a lunghezza fissa, dove il decoder avrebbe accesso limitato all'informaizone fornita dall'input. Questo è problematico specialmente per sequenze lunghe e/o complesse, dove la dimensionalità delal loro rappresentazione sarebbe forzata alla stessa di sequenze più semplici o corte.

Il meccanismo è diviso in calcoli step-by-step di alignment scores, weights, e context vector.

1. Alignment scores: il cosiddetto *alignment model* prende lo stato nascosto codificato $h_i$ ed il precedente output del decoder $s_{t-1}$ per calcolare un punteggio $e_{t, i}$ che indica quanto bene gli elementi della sequenza di input si allineano con l'output attuale alla posizione $t$. L'alignment model è rappresentato da una funzione $a(.)$ che può essere implementato da una rete feedforward:

$$
e_{t, i} = a(s_{t-1}, h_i)
$$

2. Weights: i pesi $\alpha_{t,i}$ sono calcolati applicando una softmax agli alignment score calcolati in precedenza:

$$
\alpha_{t, i} = softmax(e_{t, i})
$$

3. Context vector: un context vector unico $c_t$ viene inviato al decoder ad ogni istante temporael. E' calcolato come somma pesata di tutti i $T$ stati nascosti dell'encoder:

$$
c_t = \sum_{i=1}^T \alpha_{t, i} h_i
$$

L'implementazione originaria era sotto forma di RNN. Tuttavia, il mecacnismo di attention può essere ri-formulato in forma generale che può essere applicata in ogni task di tipo *sequence-to-sequence*, dove l'informazione può non essere necessariaemnte correlata in modalità sequenziale.

## General attntion

La general attention fa uso di tre componenti principali, chiamati *query* (Q), keys K e values V.

Se dobbiamo comparare questi componenti all'attention mechanismo la query sarebbe analoga all'output del decoder precedente $s_{t-1}$, mentre i values sarebbero analoghi all'encoded inputs $h_i$. Nel meccanismo di attention di Bahdanau, le keys ed i values sono lo stesso vettore.

Il meccanismo di general attention effettua i seguenti calcoli:

1. ogni query vector $q=s_{t-1}$ viene confrontato con un databse di chaivi per calcolare un punteggio di score. Questa operazione viene calcoalta come il prodotto scalare della specifica query cosniderata con ogni key vector $k_i$:

$$
e_q k_i = q \cdot k_i
$$

2. Gli score passano attraverso una softmax per generare i pesi:

$$
\alpha_{q, k_i} = softmax(e_{q, k_i})
$$

La general attention è calcolata mediante una somma pesata dei vettori value $v_{k_i}$ dove ogni value vector è accoppiato ad una chiave corrispondente:

$$
attention(q, K, V) = \sum_i \alpha_{q, k_i} v_{k_i}
$$

Nel contesto della machine translation, ogni parola in una sequenza di input avrà vettori query, key, e value specifici. Questi vettori sono generati moltiplciando la rappresentazione dell'encoder della parola specifica considerata con tre diverse matrici dei pesi che sono state genrate durante l'addestramento.

In pratica, quando 

