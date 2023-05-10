







## Denoising autoencoders

I *denoising autoencoder*, come suggerisce il nome, sono degli autoencoder che rimuovono il rumore da un'immagine. Diversamente dagli autoencoder che abbiamo già visto, questi sono il primo tipo di autoencoder che non ha l'immagine di input come ground truth.

Nei denoising autoencoeder, diamo in pasto una versione rumorosa dell'immagine, dove il rumore è stato aggiunto mediante delle alterazioni di tipo digitale. L'immagine rumorosa viene mandata all'architettura dell'autoencoder, e l'output comparato con l'immagine di ground truth.

Il denoising autoencoder si libera del rumore apprendendo una rappresentazione dell'input dove il rumore può essere filtrato facilmente.

Anche se rimuovere il rumore direttamente dalle immagini sembra difficile, l'autoencoder fa questa operazione mappando i dati di input in un manifold a dimensionalità più bassa (come in un undercomplete autoencoder), dove il filtraggio del rumore diventa molto più semplice.

Essenzialmente, il denoising autoencoder lavora con l'auoto della riduzione della dimensionalità non lineare. La funzione di costo generalmente usata in questo tipo di reti è la loss L2 o L1.

