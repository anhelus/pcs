# Recurrent Neural Networks

Le Recurrent Neural Network (RNN) sono un tipo di rete usata per il trattamento di sequenze dati. Così come molti altri algoritmi di deep learning, le RNN sono relativamente antiche. Sono state create inizialmente negli anni '80, ma hanno espresso il loro potenziale soltanto negli ultimi anni, grazie all'aumento della potenza computazionale, oltre che della quantità di dati, e all'invenzione delle long short-term memory (LSTM) negli anni '90.

Grazie alla loro memoria interna, le RNN possoo ricoradre delle cose importanti sull'input ricevuto, il che le rende ottime nella predizione di ciò che avverrà ins eguito. Per questo motivo sono l'algoritmo preferenziale per modellare dati sequenziali come le sequenze. Le RNN possono formare una comprensione molto profonda di una sequenza e del suo contesto se comparate ad altri algoritmi.

## Come funzionano le RNN?

Per comprendere completamente le RNN, dobbiamo partire dalle reti [feed-forward](../01_nn/lecture.md). In una rete feed-forward, se escludiamo la backpropagation, l'informazione si muove soltanto in una direzione, ovvero dall'ingresso verso l'uscita. 

TODO FIGURA FEED FORWARD

Questo fa in modo che la rete non abbia alcuna memoria dell'input ricevuto, e non sia in grado di predire ciò che potrà seguire quell'input. In altri termini, la rete feed-forward non è in grado di apprendere nozioni di tipo sequenziale: non può ricordare alcuna nozione su ciò che è accaduto nel passato, ad eccezione dell'addestramento che ha ricevuto.

In una RNN, invece, l'informazione va attraverso un ciclo. QUando prende una decisione, considera l'input attuale, oltre a quello che ha appreso dagli input che ha ricevuto in precedenza.

TODO IMMAGINE RECURRENT

Una RNN ha una memoria normalmente a breve termine; se utilizzato con i layer LSTM, è in grado di avere anche una memoria a lungo termine.

Un altro modo per illustrare il concetto della memoria di una RNN è quella di spiegarlo con un esempio: immaginiamo di avere una normale rete feed-forward, e dargli la parola "neurone" ed elaborare la parola carattere per carattere. Nel momento in cui raggiunge il carattere u, ha già dimenticato i caratteri n ed e, il che rende praticamente impossibile per una rete di questo tipo predire quale carattere verrà ins eguito.

Una RNN è tuttavia in grado di ricordare questi caratetri grazie alla sua memoria interna. Per farlo, una RNN ha due ingressi: il dato presente, ed il passato recente. Questo è imporante perché la sequenza di dati contiene informazioni imporanti su ciò che segue.

Una rete feed-forward assegna, come tutti gli altri algoritmi di deep learning, una matrice dei pesi ai suoi input, e quindi produce l'output. Le RNN applicano dei pesi sia al presente, sia agli input precedenti. Inoltre, una RNN modifhcerà anche i pesi sia per il gradient descent che per la backpropagation nel tempo.

## Tipi di RNN

Esistono quattro tipi di RNN, ovvero le one-to-one, one-to-many, many-to-one, many-to-many.

TODO FIGURA

## BPTT

Per comprendere il concetto di backpropagation through time (BPTT) dovrem comprendere i concetti di forward e backpropagation.

La backpropagation è usata epr calcolare il gradiente di una funzione di costo rispetto ai pesi della rete neurale. L'algoritmo in pratca va all'indietro nei vari layer di gradiente per individuare le derivate parziali degli errori rispetto ai pesi. La backpropagation usa questi pesi per diminuire i margini di errore nel training.

Nelle reti neurali, effettuiamo la forward propaagation  per ottenreer l'output del nostro modello e controllare se questo è correto o meno per ottenere l'errore. La backpropagation va all'indietro nella rete neurale per trovare le derivate parziali dell'errore rispetto ai pesi, il che permette di sottarre questo valore dai pesi.

Queste derivate sono quinid usate dall'algoritmo a discesa di gradiente, che minimizza iterativamente una data funzione. Quindi modifica i pesi a seconda di quale decrementa l'errore. Di conseugenza, la bakcpropagtaion in pratica modifca i pesi del nostro modello durante l'addestramento.

La BPTT è praticamente la backpropagation fatta su una RNN "svolta". Il concetto di "svolgere" la rete è uno strumento concettuale e di visualizzazione, che ci aiuta a comprendere ciò che accade nella rete. La maggior parte delle volte quando si implementa una RNN la backpropagation è fatta in automatico, ma dobbiamo capire come affronta i problemi che possono sorgere durante lo sviluppo.

Possiamo vedere una RNN come una sequenza di reti neurali che si addestrano l'una dopo l'altra mediante la backpropagation.

L'immagien seguente mostra una RNN srotolata. In particolare, vediamo che non ci sono dei cicli, e che diversi step temporali sono visualizzati, con l'informazione passata da uno step temporale al successivo. Questa illustrazione mostra anche perchè una RNN può esere vista come una sequenza di reti neurali.

TODO FIGURA RNN

Con la BPTT la concettualizzazione dello srotolamento è richiesta dal momento che l'errore ad un dato istante temporale dipende dall'istante precedente.

ALl'interno della BPTT l'errore veiene back-propagato dall'ultimo step temproale al primo, attraversando tutti gli istanti temporali. Questo permette di calcolare l'erroe ad ogni istante, aggiornando i pesi. Notiamo che la BPTT può essere computazionalmente costosa se abbiamo un elevato numero di step temporali.

## Problemi comuni nelle RNN

Ci sono due problemi principali delle RNN. Per comprenderli, dobbiamo ricordare il concetto di gradiente.

Il gradiente è una derivata parziale rispetto ai suoi input. In pratica, è una misura di quanto la funzione cambia se cambiamo gli ingressi alla stesas.

Il graidente è anche la pendenza della funzione. Più alto è il gradiente, maggiore è la pendenza della funzione, e più velocemente il modello può apprendere. Ma se la pendenza è zero, il modello smette di apprendere. Un gradiente misura il cambio in tutti i pesi rispetto al cambio nell'errroe.

##### Exploding gradients

Il problema degli *exploding gradients* avviene quando l'algoritmo assegna un valore molto alto ai pesi; questo può essere risolto troncando o imponendo un limite ai gradienti.

##### Vanishing gradients

Il problema dei *vanishing gradient* avviene quando i valori di un gradiente sono troppo piccoli, ed il modello smette di apprendere o richiede troppo tempo per raggiungere un risultato. 

## RNN e LSTM

Le *long short-term memory network* (LSTM) sono un'estensione della memoria della RNN che le rende in grado di apprendere da esperienze che hanno dei grossi gap temporali tra loro.

Le LSTM fanno in modo da assegnare ai dati dei "pesi" che aiutano le RNN o a far entrare nuova informazione, o a scordarne, o a dare abbastanza importanza per impattare l'output.

Le unità di una LSTM sono usate come blocchi principali per i layer di un particolare tipo di RNN chiamata rete LSTM.

Le LSTM permettono alle RNN di ricordare gli ingressi in un lungo periodo di tempo. Questo è perché la LSTM contiene infomrazioni in una memoria da cui può leggere, scrivere, e cancellare informazioni.

Questa memoria può essere vista come una sorta di porta logica, che permette di decidere se memorizzare o meno informazione sulla base dell'importanza ad essa assegnata. L'importanza viene assegnata mediante l'uso di *pesi*, che sono a loro volta appresi dall'algoritmo. Questo signiica che la rete apprende nel tempo quale informazione è importante e quale non lo è.

In una cella LSTM abbiamo tre tipi di porte: input, forget, ed output. Queste porte dterminano se far entrare nuovi input (input gate), cancellare l'informazione perché non ritenuta importante (forget gate), o fare in modo che influenzi l'uscita al momento attuale (output gate).

FIGURA CON I DIVERSI TIPI DI GATE

I gate in una LSTM hanno una funzione di attivazione sigmoidale, il che significa che l'uscita va da zero ad uno. L'uso di questo tipo di celle permette di risolvere il problema dei vanishing gradients, perchè le LSTM sono in grado di mantenere il gradiente alto a sufficienza da mantenere l'addestramento relativamente breve e l'accuratezza elevata.
