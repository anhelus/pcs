# 5.2.3 - Sparse autoencoder

Gli **sparse autoencoder** (SAE) sono simili agli [UAE](02_undercomplete.md) con un'unica, importantissiam differenza: infatti, gli SAE introducono una regolarizzazione mediante un termine di *sparsity penalty* $\Omega(h)$, per cui la loss assume la forma:

$$
L_{SAE} = L_{UAE} + \Omega(h)
$$

In termini pratici, il termine di regolarizzazione introduce una penalità sul numero di nodi attivi in ogni layer nascosto dell'encoder e del decoder, facendo in modo che lo SAE eviti di attivare più neuroni di quelli strettamente necessari.

Uno SAE è quindi regolarizzato per essere *sparso* e rispondere alle feature statistiche specifiche per il dataset su cui sono addestrati, invece di agire come una sorta di funzione di identità. In altre parole, la sparse penalty fa in modo che la rete attivi esclusivamente i nodi dedicati alle feature rilevanti per i dati utilizzati per il training.
