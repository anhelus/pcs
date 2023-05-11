# 5.2.4 - Denoising autoencoders

I **denoising autoencoders** (DAE) sono utilizzati per rimuovere il rumore che affligge i dati originari.

Per farlo, viene utilizzata una funzione di regolarizzazione $\Omega$ alla funzione di costo. In particolare, la funzione di costo assume una forma del tipo:

$$
L_{DAE}(x, g(f(\tilde{x})))
$$

dove $\tilde{x}$ è una versione di $x$ corrotta da una qualche forma di rumore. I DAE provano quindi a rimuovere questo rumore, invece di limitarsi a riprodurre l'ingresso.
