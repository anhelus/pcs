# 5.5.3 - Funzione di costo per una GAN

Nella [scorsa lezione](02_anatomy_gan.md) abbiamo discusso il processo di addestramento di una GAN. Tuttavia, la discussione non può essere completa senza tenere in considerazione la funzione di costo utilizzata. Questa dovrà essere progettata per riflettere la distanza tra la distribuzione dei dati generati e quella del meccanismo di generazione reale. Per farlo, sono stati proposti diversi approcci, tra cui i più utilizzati sono la [minimax loss](https://arxiv.org/abs/1406.2661) e la [Wasserstein loss](https://arxiv.org/abs/1701.07875). Vediamoli nel dettaglio.

!!!tip "Quante funzioni di costo?"
    Intuitivamente, una GAN dev prevedere due funzioni di costo: la prima governa l'addestramento del generatore, mentre la seconda quello del discriminatore. Tuttavia, è necessario che queste funzioni di costo lavorino congiuntamente; per far questo, il generatore influenza esclusivamente il termine che riflette la distribuzione dei dati falsi, mentre è l'output del discriminatore che ci permette di stabilire la direzione verso cui andremo a modificare i pesi.

## Minimax loss

In questa funzione di costo, che è anche quella proposta dagli autori che hanno definito il concetto di GAN, il generatore ed il discriminatore operano in maniera concorrente: il primo, infatti, cerca di minimizzare il valore assunto dalla funzione, mentre il secondo di massimizzarlo:

$$
L = E_x [\log(D(x))] + E_z [\log(1-D(G(z)))]
$$

Nell'espressione precedente, che deriva dalla definizione di cross-entropia tra la distribuzione reale e quella generata, abbiamo le seguenti quantità:

* $D(x)$ è il valore di probabilità stimato dal discriminatore che l'istanza di dati reali $x$ si riferisca alla classe positiva.
* $E_x$ è il valore atteso di tutte le istanze dei dati reali.
* $G(z)$ è l'output stimato dal generatore in risposta ad un certo rumore $z$.
* $D(G(z))$ è il valore di probabilità stimato dal discriminatore che $G(Z)$ sia reale.
* $E_z$ è il valore atteso su tutti gli input casuali del generatore (in altri termini, l'aspettazione su tutte le istanze generate $G(z)$).

Si nota subito come il generatore non possa influenzare il termine $\log(D(x))$, per cui questo tenterà di minimizzare il valore $\log(1 - D(G(z)))$.

!!!tip "Modified Minimax Loss"
    In realtà, sono gli stessi autori del paper originale a notare che la funzione di costo precedente è sensibile al problema dei vanishing gradient, che si presenta soprattutto durante le prime epoche di training, quando il compito del discriminatore è molto semplice. Di conseguenza, gli autori propongono anche una versione modificata della minimax loss, in cui il discriminatore prova a massimizzare il valore $\log(D(G(z)))$.

## Wasserstein Loss

La funzione di costo di Wasserstein si basa su una modifica nello schema di funzionamento della GAN, chiamata *Wasserstein GAN*, o *WGAN*, nella quale il discriminatore non effettua una classificazione binaria, ma restituisce semplicemente un numero maggiore di uno o minore di zero. In altre parole, il discriminatore prova a fare in modo che l'output per le istanze reali sia molto più grande di quello delle istanze generate.

!!!note "Discriminatore e critico"
    Dato che in una WGAN il discriminatore non esercita nei fatti un "giudizio", il nome che gli viene comunemente dato è quello di *critico*. Questa distinzione ha valenza sia pratica, sia teorica, e si manifesta nel fatto che i valori in ingresso alla loss di Wasserstein non possono essere delle probabilità.

La loss di Wasserstein ha una formulazione molto semplice. In particolare, la funzione di costo per il critico è data dalla formula:

$$D(x) - D(G(z))$$

mentre quella per il generatore è data da:

$$D(G(z))$$

In pratica, il critico prova a massimizzare la differenza tra i suoi output su istanze reali e quelli su istanze false, mentre il generatore prova a massimizzare l'output del critico sulle istanze generate.

Nelle formule precedenti:

* $D(x)$ è l'output del critico per l'istanza reale $x$.
* $G(z)$ è l'output del generatore quando ad un dato rumore $z$.
* $D(G(z))$ è l'output del critico per l'istanza generata $G(z)$.

!!!tip "Loss e earth mover distance"
    La formulazione della loss di Wesserstein deriva dalla [earth mover distance](https://en.wikipedia.org/wiki/Earth_mover's_distance).

Sperimentalmente è stato dimostrato come le WGAN siano meno vulnerabili al problema dei vanishing gradients. Inoltre, la funzione di costo è anche una vera metrica, ovvero una misura di distanza in uno spazio di distribuzioni di probabilità.
