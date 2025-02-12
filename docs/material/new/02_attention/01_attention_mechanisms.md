# Meccanismo di attention

L'attention mechanism venne introdotto da Bahdanau nel 2014 (https://arxiv.org/abs/1409.0473) per risolvere il problema del collo di bottiglia che merge dall'uso di vettori di codifica a lunghezza fissa, con il decoder che ha accesso limitato all'informazione fornita dall'input. Questo diventa problematico specialmente nelc aso di sequenze lunghe o complesse, dove la dimensionalità della rappresentazionesarà forzata ad essere la stessa di quella di frasi più semplici o corte.

Da notare che il meccanismo di attention di Bahdanau è diviso nel calcolo passo passo di *alignment scores*, *weights*, e del *context vector*.

1. Alignment scores: il modello di allineamento prende gli stati nascosti del decoder $h_i$ ed il precedente output del decoder $s_{t-1}$ per calcolare uno score $e_{t,1}$ che indica quanto bene gli elementi della sequenza di input si allineano allk'oputput corrente alla posizione $t$. Il modello di allineamento è rappresentato da una funzione $a(\cdot)$ che può essere implementata usando una rete neurale feedforward:

$$
e_{t,i}=a(s_{t-1},h_i)
$$

2. pesi: i pesi $\alpha_{t,i}$ sono calcolati applicando un'operazione di softmax agli alignment score calcolati in precedenza:

$$
\alpha_{t,i} = softmax(e_{t,i})
$$

3. context vector: un context vector unic, $c_t$, viene inviato al decoder ad ogni step temporale. Viene calcolato come la somma pesata di tutti i $T$ stati nascosti codificati:

$$
c_t = \sum_{i=1}^T \alpha_{t,i} h_i
$$

In particolar,e nell'implementazione originale vi era un RNN sia per l'encoder sia per il decoder.

Ad ogni modo, il meccanismo di attention può essere riformulato in una forma generale che può essere applicata ad una qualsias task sequence-to-sequence (seq2seq), dove l'informazione potrebbe non necessariaemnte essere correlata in maniera sequenziale.

## Il meccaqnismo di attention generale

Il *general attention mechanism* sua tre componenti principali, ovvero le *query* $Q$, le chiavi $K$ e i values $V$.

SE dobbiamo comparare questi tre componenti al meccanismo di attention propost da Bahdanau, la query sarà analoga all'output precedente del decoder, $s_{t-1}$, mentre i values saranno anaolghi agli input codificati $h_i$. Nel meccahinsmo di attention di Bahdanau, le chiavi ed i valori sono  lo stesso vettore.

Possiamo pensare al vettore $s_{t-1}$ come una query eseguita su un database di coppie chiave-valore, mentre le chiavi sono i vettori e gli stati nascosti $h_i$ i valori.

Il general attention mechainsm effettua i seguenti calcoli:

1. ogni query vector $q=s_{t-1}$ viene conforntato con un database di chiave per calcolare un punteggio. Questa operazione di matching viene effettauta come prodotto scalare della specifica query considerata con ogni vettore chiave $k_i$:

$$
e_{q, k_i} = q \cdot k_i
$$

2. Gli score sono passati attraverso un'operazione di softmax per generare i pesi:

$$
\alpha_{q, k_i} = softmax(e_{q, k_i})
$$

L'attention generale viene qunind i calcolata dalla somma pesata dei value ve tors $v_k-i$, dove ogni value vecotr viene accoppiato con una chaive corrispondente:

$$
attention(q, K, V) = \sum_i \alpha_{q, k_i V_{k_i}}
$$

Nel contesto dlela machine translation, ad ogni parola in una sequenza di input sarà attribuita la sua query, chaive, e value vectrors. Questi vettori sono generati moltilpicando la rappresentazione dell'encoder della specifica parola considerata con tre diverse matrici di peso che sarebbero state genrate durante l'addestramento.

In pratica, quando il meccanismo di attention generalizzato viene prensentato una sequenza di parole, prende il query vector attribuito ad alcuen parole specifiche nelle sequenze e lo misura rispetto ad ogni chiave nel database. Nel fralo, cattura come la parola conmsiderata si correla alle altre nella sequenza. Quindi scala i valori in accordo ai pesi di attenzione calcolati dai punteggi per mantenere il focus su quelle parole rilevanit alla query. Nel farlo, viene prodotto un output di attenzione per la parola considerata.

## Uso di num,pyu e scipy

Vediamo come implementare il genereal attention mechanism usando le librerie NumPy e Scipy in Python. Per semplicità, calcoliamo inizialmente l'attention per la prima parola in una sequenza di quattro. A questo punto,g eneralizziamo il codice per caolcolare l'output di attention per tutte le quattro parole in forma matriclae.

Iniziamo per prima cosa definendo gli embedding delle quattro diverse parole per calcolare l'attention. Nella pratica, quyesti embedding sarebbero stati generati da un encoder; per questo esempio, li definirnemeo manualmente.

# encoder representations of four different words
word_1 = array([1, 0, 0])
word_2 = array([0, 1, 0])
word_3 = array([1, 1, 0])
word_4 = array([0, 0, 1])

Lo step succesivo genera le matrici dipeso, che alla fine moltiplicheremo per gli embedding per genrare le query, key, e vvalyes. Qui generiamo queste matrici dei pesi in maniera casuael; tuttavia, nella pratica, qeusti sarebbero stati appresi durante il training.

...
# generating the weight matrices
random.seed(42) # to allow us to reproduce the same attention values
W_Q = random.randint(3, size=(3, 3))
W_K = random.randint(3, size=(3, 3))
W_V = random.randint(3, size=(3, 3))

Botiamo come il numeor di righe di ciascuna di queste matrici è+ uguale alla diemnsione dei word embedding (in questo caso tre) per permetterci di effettuare la moltiplicazione amtriciale.

Di consequenza, query, key e value vector perr ogni parola sono  genrati moltiplicando ogni wmebdding per ciascuna delle matrici dei pesi.

...
# generating the queries, keys and values
query_1 = word_1 @ W_Q
key_1 = word_1 @ W_K
value_1 = word_1 @ W_V

query_2 = word_2 @ W_Q
key_2 = word_2 @ W_K
value_2 = word_2 @ W_V

query_3 = word_3 @ W_Q
key_3 = word_3 @ W_K
value_3 = word_3 @ W_V

query_4 = word_4 @ W_Q
key_4 = word_4 @ W_K
value_4 = word_4 @ W_V

Considerando solo la prima parola, lo step successivo peswa il suo query vector rispetto a tutti i key vector usando un'operazione di prodotto scalare.

...
# scoring the first query vector against all key vectors
scores = array([dot(query_1, key_1), dot(query_1, key_2), dot(query_1, key_3), dot(query_1, key_4)])

I valori di punteggio sono quindi pasati attravero un'operazione di softmax per generare i pesi. Prima di farlo, è rpatica comune dividerli epr il quadrato della dimensionalità dei key veector (in questo caso tre) per mantenere stabili i gradienti.

...
# computing the weights by a softmax operation
weights = softmax(scores / key_1.shape[0] ** 0.5)

Infine, l'output di attention viene calcoalto come somma pesata di tutti i quattro value vector.

...
# computing the attention by a weighted sum of the value vectors
attention = (weights[0] * value_1) + (weights[1] * value_2) + (weights[2] * value_3) + (weights[3] * value_4)

print(attention)

Il codice completo è il seguente, implementanto ilk tuttto in forma matriciale per generar eun oiutput di attention per tutte e quattro le parole in un'unica passata:

from numpy import array
from numpy import random
from numpy import dot
from scipy.special import softmax

# encoder representations of four different words
word_1 = array([1, 0, 0])
word_2 = array([0, 1, 0])
word_3 = array([1, 1, 0])
word_4 = array([0, 0, 1])

# stacking the word embeddings into a single array
words = array([word_1, word_2, word_3, word_4])

# generating the weight matrices
random.seed(42)
W_Q = random.randint(3, size=(3, 3))
W_K = random.randint(3, size=(3, 3))
W_V = random.randint(3, size=(3, 3))

# generating the queries, keys and values
Q = words @ W_Q
K = words @ W_K
V = words @ W_V

# scoring the query vectors against all key vectors
scores = Q @ K.transpose()

# computing the weights by a softmax operation
weights = softmax(scores / K.shape[1] ** 0.5, axis=1)

# computing the attention by a weighted sum of the value vectors
attention = weights @ V

print(attention)
