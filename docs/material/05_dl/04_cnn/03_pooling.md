

## Pooling

Un tlayer classico di una rete convoluzionale consiste di tre stage, come mostrato in figura 1. Nel primo stage, il layer efefttua diverse convoluzioni in parallelo, per produrre un insieme di attivazioni lineari. Nel secondo stage, ogni attivazione lineare passa attraverso una funzione di attivzione non lineare, come la funzione ReLU. Questo step è alle volte chiamato *detector stage*. Nel terzo stage, usiamo una *funzione di pooling* per modificare l'uscita del layer ulteriormente.

Una funzione di pooling rimpiazza l'uscita della rete ad una certa posizione con una statistica sommaria degli output circostanti. Ad esempio, la funzione di *max pooling* restituisce l'output massimo alll'interno di un intorno rettangolare. Altre funzionidi pooling popolari includono la media di un intorno rettangolare, la norma $L^2$ dello stesos, o una media pesata basata sulla distanza dal pixel centrale.

TODO FIGURA NN

In tutti i casi, il pooling ci aiuta a rendere la rappresentazione approssimativamente *invariante* a piccole traslazioni dell'input. L'invarianza alla traslazione implica che se trasliamo l'input di una piccola quantitaà, il valore della maggior aprte degli output del pooling non cambia. L'invarianza alle traslazioni locali può essere una proprietà utilse se ci importa più del fatto che una feature sia presente che della sua posizione esatta. Ad esempio, quando determiniamo se un'immagine contiene un volto, non dobbiamo conoscere la posizione degli occhi con accuratezza al pixel, ma semplicemente se vi è un occhio sulla parte sinistra del volto ed uno sulla parte destra. In altri contesti, è più importante preservare la poszione di una feature. PEr esempio, se vogliamo trovare un angolo definitoda due bordi che si incontrano ad uno specifico orientamento, dobbiamo preservare la posizione dei bordin abbastanza da testare se si incontrano.

Dato che il pooling "riassume" le risposte in un intorno, è pèossibile usare meno unità di pooling che di detector, in modo da creare una statistica "riassuntiva" su regioni spaziate a $k$ pixel di distanza piuttosto che ad 1 pixel di distanza. Questo migliora l'efficienza computazionale della rete perché il layer successivo ha approssimativamente $k$ volte meno input da elaborare. Quando il numero di parametri nel layer successivo è una funzione della sua dimensione dell'input (così come quando il layer successivo è completamente connesso e basato sulla moltiplicazione matriciale), questa riduzione nella dimensione dell'input può anche portare una efficienza statistica migliorata e ridurre i requisiti in termini  di memoria per memorizzare i parametri.

Per molti task, il pooling è essenziale per gestire gli input di diversa dimensione. Per esempio, se vogliamo classificare immagini di dimensioni variabili, l'input al layer di classificazione deve avere uan dimensione fissa. Questo si ottiene nromalmente variando la dimensione di un offset tra el regioni di pooling, in modo che il layer di classificazione rcieva sempre lo stesso unermo di statistiche riassunte indipendentemnete dalla dimensione dell'input. Per esempio, il layer di pooling finale della rete potrebbe essere definito per mandare in uscita quattro insiemi di statistiche riassuntive, una per ogni quadrante di un'immagine, indipendentemnete dalla dimensione dlla stessa.