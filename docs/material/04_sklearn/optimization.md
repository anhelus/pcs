# Reti neurali

## Ottimizzazione

Abbiamo visto che ci sono due componenti chiave nel contesto dei task collegati alla classificazione.

1. Una funzione di scoring parametrizzata, che mappa l'input ad un punteggio.
2. Una funzione di costo che misura la qualità di un certo insieme di parametri sulla base di quanto bene i punteggi assegnati concordano con i label di ground truth nei dati di training. Abbiamo visto che ci sono molti modi e versioni di questo.

Concretamente, ricordiamo che le funzioni lineari hanno la forma del tipo:

$$
f(x_i, W) = W x_i
$$

In generale, un insieme di parametri $W$ che produce le predizioni $\hat{y}_i$ per dei campioni $x_i$ consistenti con le label di ground truth $y_i$ ha un valore per la funzione di costo $L$ molto basso. Vediamo qual è l'ultimo componente di tutto ciò, ovvero l'ottimizzazione. Questo è il processo di individuare l'insieme di parametri $W$ che minimizza la funzione di costo.

## Visualizzare la funzione di costo

La funzione di costo sono normalmente definite in spazi ad elevata dimensionalità, il che le rende difficili da visualizzare. Tuttavia, possiamo trovare delle intuizioni andando a vedere ciò che accade in spazi di tipo monodimensionali o bidimensionali.

