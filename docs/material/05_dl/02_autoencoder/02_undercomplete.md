# 5.2.2 Undercomplete autoencoder

Gli **undercomplete autoencoder** (UAE) sono i più semplici tra gli autoencoder. In particolare, gli UAE accettano provano a dare in uscita un output quanto più fedele possibile all'input preso in ingresso; in altre parole, dato un certo input $x$, creerà una rappresentazione nello spazio latente a partire dalla quale ricostruirà un output $\hat{x}$ minimizzando l'errore di ricostruzione $\hat{x}-x$.

!!!tip "UAE ed approccio non supervisionato"
    Per come è stato descritto, un UAE è un tipo di rete neurale non supervisionata, visto e considerato che non richiede la presenza di una label per ricostruire l'input.

L'uso primario di un UAE è quindi generare una rappresentazione compressa $h$ dell'input $x$ nello spazio latente definito dal bottleneck. In quest'ottica, tale operazione può essere interpretata come una dimensionality reduction non lineare.

!!!note "UAE e dimensionality reduction"
    Ricordiamo che le tecniche di dimensionality reduction prevedono che i dati originari, definiti in uno spazio ad alta dimensionalità, siano riproiettati su un iperpiano a dimensionalità inferiore, cercando di conservare quanta più informazione possibile sullo spazio originario. In tal senso, la tecnica che ci viene subito in mente è la PCA, che tuttavia sfrutta proiezioni di tipo esclusivamente lineare. Di contro, un UAE è in grado di apprendere delle relazioni non lineari tra le componenti dell'ingresso proprio grazie alla presenza delle funzioni di attivazione, il che gli permette di lavorare su un insieme più ampio di dati. Di fatto, qualora rimuovessimo tutte le non linearità introdotte dalle funzioni di attivazione di un UAE, avremmo un'elaborazione puramente lineare.

La funzione di costo usata per addestrare un UAE è chiamata *reconstruction loss* alla luce del fatto che valuta quanto l'output del decoder $\hat{x}$ è simile al ground truth $x$. Per farlo, possiamo usare la norma $L_1$:

$$
L_{UAE} = |x-\hat{x}|
$$

!!!tip "Regolarizzazione"
    I più attenti avranno notato come la funzione di costo non abbia un termine di regolarizzazione esplicito. Di conseguenza, l'unico modo per assicurarsi che l'autoencoder non si limiti a *memorizzare* i dati in ingresso è quello di impostare adeguatamente gli iperparametri del modello, quali le dimensioni del bottleneck e dell'encoder.
