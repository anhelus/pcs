# 5.2.2 Undercomplete autoencoder

Gli *undercomplete autoencoder* sono tra i più semplici tra gli autoencoder. In particolare, questo tipo di autoencoder accetta un dato in ingresso provando a restituire lo stesso in uscita: in altre parole, dato un certo input $x$, creerà una rappresentazione nello spazio latente a partire dalla quale ricostruirà un output $\hat{x}$ minimizzando l'errore di ricostruzione $\hat{x}-x$. Ciò rende un undercomplete autoencoder una rete non supervisionata, visto e considerato che non richiede alcuna label per funzionare.

## Autoencoder e dimensionality reduction

L'uso primario di un undercomplete autoencoder è quindi la generazione di una rappresentazione compressa nello spazio latente del bottleneck, che può essere utilizzata come un'operazione di dimensionality reduction non lineare.

Ovviamente, quando pensiamo alla riduzione della dimensionalità, ci vengono in mente metodi come la PCA, che proietta i dati in uno spazio ad alta dimensionalità su un iperpiano a più bassa dimensionalità cercando di conservare le informazioni relative alla varianza degli stessi. Tuttavia, la PCA modella esclusivamente relazioni lineari: ciò è ovviamente limitante se comparato con un undercomplete autoencoder, in quanto questo tipo di modello può apprendere relazioni non lineari e, di conseguenza, lavorare su un insieme più ampio di dati. Nei fatti, rimuovendo tutte le funzioni di attivazione da un undercomplete autoencoder, ed utilizzando esclusivamente dei layer lineari, abbiamo un modello che compie un'elaborazione equivalente alla PCA.

!!!note "Manifold learning"
    Questa forma di dimensionality reduction non lineare è anche chiamata *manifold learning*.

## Reconstruction loss

La funzione di costo usata per addestrare un undercomplete autoencoder è chiamata *reconstruction loss* alla luce del fatto che valuta la bontà della ricostruzione del dato rispetto all'input originario. Normalmente, è possibile usare una funzione come la norma $L_1$ come loss:

$$
L = |x-\hat{x}|
$$

dove al solito $\hat{x}$ rappresenta l'output del decoder, mentre $x$ rappresenta il ground truth.

I più attenti avranno notato come la loss non abbia un termine di regolarizzazione esplicito. Di conseguenza, l'unico modo per assicurarsi che l'autoencoder non faccia altro se non "memorizzare" i dati in ingresso è quello di impsotare adeguatamente gli iperparametri del modello, ovvero dimensione del bottleneck e dell'encoder.
