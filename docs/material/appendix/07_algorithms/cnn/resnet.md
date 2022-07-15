# 1. il problema delle plain network

le normali reti di deep learning hanno i conv layer quindi i layer fully connected per i task di classificazione come AlexNet, ZFNet e VGGNet. Quando le plain networ sono abbastanza profonde, può avvenire il problema dei vainshing gradient.

Durante la backpropagation, uando le derivate parziali della funzione dell'errore rispetto all'attuale peso in gi iterazione di training, questo ha l'effetto di moltiplicare $n$ di di questi piccoli o grandi numeri per calcolare i gradienti dei layer frontali in una rete ad $n$ livelli.

quando la rete è profonda, e si moltiplicano $n$ di questi piccoli numeri, il gradiente diventerà zero (vanishing).

Quando la rete è prfonoda, e si moltiplicano $n$ di questi grossi numeri, il gradiente diventerà troppo grande (exploded).

Ci aspettiamo che le reti più profonde abbiano predizioni più accurate. Tuttavia, quando ciò non avviene, è probabile che ci sia un degradation problem legato ai vanishing gradient.

https://towardsdatascience.com/review-resnet-winner-of-ilsvrc-2015-image-classification-localization-detection-e39402bfa5d8

https://towardsdatascience.com/review-densenet-image-classification-b6631a8ef803

