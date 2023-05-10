# 5.2.4 - Denoising autoencoders

Piuttosto che aggiungere una penalità $\Omega$ alla funzione di costo, possiamo ottenere un autoencoder che apprende qualcosa di utile cambianod il termine dell'errore di ricostruzione nella funzione di costo.

Abbiamo visto che gli autoencoder minimizzano una funzione nella forma:

$$
L(x, g(f(x)))
$$

dove $L$ è una funzione di costo che penalizza $g(f(x))$ se non simile ad $x$, come ad esempio la norma $L^2$ della loro differenza. Questo fa in modo che la funzione composta $g \circ f$ apprenda una funzione identità.

In un **denoising autoencoder** viene invece minimizzata la funzione:

$$
L(x, g(f(\hat{x})))
$$

dove $\hat{x}$ è una copia di $x$ che è stata corrotta da una qualche forma di rumore. I denoising autoencoder devono quindi rimuovere questo rumore invece di limitarsi a copiare l'ingresso.

