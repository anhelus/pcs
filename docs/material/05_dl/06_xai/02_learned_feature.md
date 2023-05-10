# Learne feature

Le CNN apprendono feature astratte e concetti dai pixel raw dell'immagine. Le tecniche di feature visualization visualizzano le feature apprese mediante la massimizzazione delle attivazioni. Invece, le tecniche di *network dissection* etichettano le unità delle reti neurali con dei concetti umani.

Le deep neural netowrk apprendono feature ad alto livello nei layer nascosti. Questa è una delle più grandi forze, e riduce la richiesta per l'ingegnerizzazione delle feature. Assumendo che si voglia cosruire un classificatore per immagini con una SVM. Le matrici di pixel grezzi non sono il miglior input per l'addestramento della SVM, per cui possiamo creare nuove feature basate sul colore, dominio di frequenza, edge detecto, e via. Con le NCN, l'immagine viene mandata nella rete nella sua forma grezza (pixel). La rete trasfrma l'immagine diverse volte. Per prima cosa, l'immagine va in molti layer convoluzoinali. In questi layer convoluzionali, la rete apprende nuove, ed incrementalmente complesse, feature. Qunid l'informazione trasformata dell'immagine va attraverso i layer completamente connessi, e viene trasformata in una classificazione opredizione.

Di soito:

* i primi layer convoluzionali apprendono delle feature come edge e semplici texture
* i layer convoluzionali successivi apprendono feature più complesse come texture e pattern
* gli ultimi layer convoluzionali apprendono feature come oggetti o parti di oggetti
* il layer completamente connesso apprede  a connettere le attivazioni dalle feature ad alto livello alle classi individuali.

## Feature visualization

L'approccio di rendere le feature apprese esplicite è chiamatl Feature Visualization. La feature visualization per un'unità di una rete neruale è svolta individuando l'input che massimizza l'attivazione di quell'unità.

PEr "unità" intendiamo i singoli neuroni, canali (chiamati anche *feature map*), interi livelli o la probabiità di classe ottenuta dalla classificazione.

I singoli neuroni sono unità atomiche della rete, per cui avremo la maggior parte dell'informazione creando delle visualizzazioni delle feature per ciascun neurone. Ma c'è un problema: le reti neurali spesso contengono milioni di neuroni. Guardare la feature visualization di ciascun neurone richiede molto tempo. I canali (chiamate anche *activation mapès*) sono una buona scelta come unità per la feature visualization. Possiamo andare un passo oltre, e visualizzare un intero layer convoluzionale.

TODO: COPIARE FIGURA 10.2

##### Feature visualiztion through optimization

In termini matematici, la feature visualization è un problema di ottimizzazione. Supponiamo che i pesi della rete neurale siano fissati, il che significa che la rete è addestrata. Stiamo cercando una nuova immagine che massimizzi l'attivazione media di un'unità, qui un singolo neurone:

$$
img^* = \argmax_{img} h_{n, x, y, z}(img)
$$

dove $h$ è l'attivazione del neurone, $img$ l'ingresso della rete, $x$ ed $y$ descrivono la posizione spaziale del neurone, $n$ specifica il layer, e $z$ è l'indice del canale. Per l'attivazione

https://christophm.github.io/interpretable-ml-book/cnn-features.html#feature-visualization
