## Contractive autoencoders

I contractive autoencoder introducono un termine di regolarizzazione sulla rappresentazione intermedia $h=f(x)$, facendo in modo che le derivate di $f$ siano quanto più piccole possibile:

$$
\Omega(h) = \lambda \| \frac{\partial f(x)}{\partial x} \|_F^2
$$

La penalità $\Omega(h)$ è il quadrato della nofrma di Frobenius della matrice Jacobiana delle derivate parziali associate alla funzione di encoding.

Il nome **contractive** deriva dal modo in cui questo tipo di autoencoder modifica lo spazio delle feature. Nello specifico, i contractive autoencoder sono addestrati per resitstere a perturbazioni sugli input, incoraggiando a mappare un intorno di punti di input in un intorno di putni di output più piccolo. 


