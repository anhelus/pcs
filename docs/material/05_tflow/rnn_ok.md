# X - Recurrent Neural Network

Le Recurrent Neural Network sono un tipo di rete neurale specificamente sviluppata per elaborare dati di tipo sequenziale.

Le RNN sono un tipo di rete neurale artificiale (ANN) che è stata sviluppata per elaborare dati sequenziali, come il testo o l'audio, che hanno una struttura temporale. A differenza delle reti neurali feedforward (FFNN), che elaborano i dati in modo sequenziale e non mantengono alcuna informazione sulle osservazioni precedenti, le RNN sono progettate per elaborare dati sequenziali tenendo conto della loro dipendenza temporale.

La caratteristica distintiva delle RNN rispetto alle FFNN è l'uso di uno o più strati ricorrenti, in cui ogni neurone ha un'uscita che è dipendente dalla sua uscita precedente e dall'input corrente. Ciò consente alle RNN di mantenere una "memoria" delle informazioni che sono state passate attraverso la rete. Inoltre, le RNN sono in grado di elaborare sequenze di lunghezza variabile.

Ci sono diversi tipi di architetture di RNN, ma il più comune è il cosiddetto strato di memoria a corto termine (LSTM). Le LSTM sono state introdotte per risolvere il problema dell'esplosione del gradiente, un problema che si verifica quando si addestra una rete neurale profonda con algoritmi di backpropagation, in cui il gradiente diventa troppo grande e rende l'aggiornamento dei pesi instabile.

L'architettura LSTM è composta da quattro elementi principali: un gate di input, un gate di output, un gate di dimenticanza e una cella di memoria. Il gate di input controlla quanto delle informazioni dell'input corrente viene aggiunto alla cella di memoria, il gate di dimenticanza controlla quanto della cella di memoria viene dimenticata, mentre il gate di output controlla quanto della cella di memoria viene trasmessa all'uscita. La cella di memoria è dove viene memorizzata la "memoria" della RNN.

Le RNN possono essere utilizzate per una vasta gamma di applicazioni, tra cui la generazione di testo, la traduzione automatica, l'analisi del sentimento, la riconoscimento del parlato, la modellizzazione del linguaggio naturale e molte altre.

Per addestrare una RNN, si utilizza un algoritmo di backpropagation che propaga l'errore attraverso la rete e aggiorna i pesi dei neuroni in base all'errore commesso. Ci sono diversi algoritmi di backpropagation che possono essere utilizzati, come il backpropagation through time (BPTT) e il backpropagation con il truncation della backpropagation through time (TBPTT).

In sintesi, le RNN sono un tipo di rete neurale artificiale progettata per elaborare dati sequenziali, come il testo o l'audio, che hanno una struttura temporale. Le RNN mantengono una "memoria" delle informazioni che sono state passate attraverso la rete utilizzando uno o più strati ricorrenti, e possono essere addestrate utilizzando algoritmi di backpropagation come il BPTT e il TBPTT.

## LSTM

L'architettura LSTM (Long Short-Term Memory) è stata introdotta nel 1997 da Hochreiter e Schmidhuber come una soluzione per risolvere i problemi delle RNN tradizionali, ovvero il problema del vanishing gradient e dell'instabilità dell'apprendimento a lungo termine. Questi problemi si presentano quando si utilizzano RNN con strati ricorrenti per elaborare sequenze di dati molto lunghe o complesse.

L'architettura LSTM è composta da quattro elementi principali: un gate di input, un gate di output, un gate di dimenticanza e una cella di memoria. Ognuno di questi elementi svolge un ruolo importante nell'elaborazione dei dati in ingresso e nel mantenimento della memoria a lungo termine della rete.

Il gate di input controlla quanto delle informazioni dell'input corrente viene aggiunto alla cella di memoria, il gate di dimenticanza controlla quanto della cella di memoria viene dimenticata, mentre il gate di output controlla quanto della cella di memoria viene trasmessa all'uscita. La cella di memoria è dove viene memorizzata la "memoria" della RNN.

In particolare, il gate di input controlla quale informazione è utile per la rete, utilizzando una funzione sigmoidea per determinare il valore di ciascuna delle dimensioni dell'input. Successivamente, viene utilizzata una funzione tanh per ottenere i valori degli stati candidati, ovvero gli stati potenziali della cella di memoria.

Il gate di dimenticanza controlla invece quale informazione è inutile per la rete, utilizzando anch'esso una funzione sigmoidea per determinare il valore di ciascuna delle dimensioni dell'input. Successivamente, il risultato viene utilizzato per produrre un prodotto tra l'output del gate di dimenticanza e lo stato corrente della cella di memoria, in modo da dimenticare le informazioni non necessarie.

Infine, il gate di output controlla quale informazione deve essere trasmessa all'uscita, utilizzando una funzione sigmoidea per determinare il valore di ciascuna delle dimensioni dell'input e una funzione tanh per determinare l'output. Il risultato del gate di output viene quindi utilizzato per produrre l'output finale della rete.

In sintesi, l'architettura LSTM è una variante delle RNN che utilizza un insieme di porte di controllo per mantenere una memoria a lungo termine della sequenza di input. L'utilizzo di questi meccanismi di controllo rende le LSTM particolarmente adatte per l'elaborazione di sequenze lunghe e complesse.

## Vanishing gradient

Certo, il problema del vanishing gradient si verifica quando si utilizzano reti neurali profonde, ovvero reti neurali con molteplici strati nascosti, e l'errore di retropropagazione del gradiente si riduce a valori molto piccoli man mano che ci si avvicina ai primi strati della rete.

Durante l'addestramento di una rete neurale, si utilizza l'algoritmo di retropropagazione per aggiornare i pesi delle connessioni in modo da minimizzare l'errore di predizione. Il gradiente viene calcolato in base all'errore della rete rispetto all'output atteso e viene propagato all'indietro attraverso tutti gli strati della rete.

Il problema del vanishing gradient si verifica quando il gradiente diventa sempre più piccolo man mano che si va indietro nella rete, fino a diventare quasi nullo. Questo rende difficile l'aggiornamento dei pesi nei primi strati della rete, che quindi non ricevono informazioni utili per l'addestramento.

Questo problema si verifica perché durante la retropropagazione del gradiente, si moltiplica il gradiente per i pesi delle connessioni in ogni strato. Se i pesi delle connessioni sono tutti vicini a uno, il prodotto delle derivate diventa molto piccolo, e di conseguenza anche il gradiente.

Il problema del vanishing gradient può essere particolarmente grave quando si utilizzano funzioni di attivazione come la sigmoide, che hanno una derivata massima di 0.25, che si avvicina a 0 quando i valori in input sono molto grandi o molto piccoli. In questo caso, il prodotto delle derivate può diventare estremamente piccolo.

Per superare questo problema, sono state proposte diverse tecniche, come l'utilizzo di funzioni di attivazione con derivate più grandi (come la ReLU), l'utilizzo di tecniche di normalizzazione dei dati in input, l'utilizzo di tecniche di regolarizzazione per evitare l'overfitting e l'utilizzo di reti neurali ricorrenti come le LSTM che hanno meccanismi interni di controllo per mantenere la memoria a lungo termine e ridurre il problema del vanishing gradient.
