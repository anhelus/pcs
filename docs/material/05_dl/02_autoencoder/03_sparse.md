# 5.2.3 - Sparse autoencoder

Gli sparse autoencoder sono simili agli undercomplete autoencoder, con un'unica, importantissima differenza, legata al fatto che il criterio di training che utilizzano introduce un termine di *sparsity penalty* $\Omega(h)$ sul bottleneck $h$, per cui la loss assume la forma:

$$
L(x, g(f(x))) + \Omega(h)
$$

dove $g(h)$ è l'output del decoder, ed $h=f(x)$ è l'output dell'encoder.

In termini pratici, la sparse penalty introduce una penalità sul numero di nodi introdotti ad ogni strato nascosto dell'encoder e del decoder, prevenendo il fatto che la rete neurale attivi più neuroni del necessario ed agendo (nei fatti) come funzione di regolarizzazione.

Gli sparse autoencoder sono quindi regolarizzati per essere *sparsi*, in modo da rispondere alle feature statistiche univoche per il dataset su cui sono addestrati, invece che agire come una sorta di funzione identitià. In altre parole, la regolarizzazione fa in modo che la rete attivi dei layer dedicati alla scoperta di feature specifiche per i dati di training.

Possiamo pensare alla funzione $\Omega(h)$ come ad un semplice termine di regolarizzazione aggiunto ad una rete feedfowrard il cui task primario è quello di riprodurre l'output a partire dall'input (*unsupervised learning*), ed eventualmente effettuare un task supervisionato che dipende dalla sparsità delle feature.

## Reconstruction loss

Il termine $\Omega(h)$ può essere integrato nella funzione di costo esprimendolo come segue:

$$
\Omega(h) = \lambda \sum_i |h_i|
$$
