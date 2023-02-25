# Approfondimento sul k-Means

## Vantaggi del k-Means

* relativamente semplice da implemenare
* in grado di scalare a grossi dataset
* garantisce la convergenza
* è possibile scegliere una posizione iniziale adeguata per i centroidi
* si adatta facilmente a nuovi campioni
* generalizza a cluster di diverse forme e dimensioni, come cluster ellittici

## Generalizzazione del k-means

Cosa accade quando i cluster sono di diverse densità e dimensioni? Vediamo nella seguente figura. Compariamo i cluster che intuitivamente possiamo individuare a sinistra con i cluster che vengono individuati dal k-means a destra. La comparazione mostra come il k-means possa avere dei problemi su certi dataset.

TODO: FIGURA

Per effettuare il clsutering di cluster non bilanciati come quelli mostrati nella figura precedente, possiamo adattare (o, meglio, generalizzare) il k-means. Nella figura 2, le linee mostrano i confini dei cluster dopo la generalizzazione del k-means come:

* a sinistra: mancanza di generalizzazione, il che risulta in un confine tra cluster antiintuitivo
* al centro: permette diverse dimensioni dei clsuter, il che risulta in cluster più intuitoivi di diverese dimensioni

## Svantaggi

* scelta del $k$ manualmente
* dipendenza dai valori iniziali: per un basso valore di $K$, possiamo mitrigare questa dipendenza eseguendo il k-means diverse volte con diversi valori iniziali e scegliere i migliori risultati. Man mano che $k$ aumenta, abbiamo bisogno di versioni avanzate del k-means per individuare miglioriv alori dei centroidi iniziali (ovvero il *seeding del k-means*).
* clustering di dati di varie dimensioni e densità: il k-means ha problemi nel clustering dei dati quando i cluster sono di varie dimensioni e densità. Per effettuare il clustering di questi dati, dobbiamo generalizzare il k-menas. Per generalizzarlo: http://www.cs.cmu.edu/~guestrin/Class/10701-S07/Slides/clustering.pdf
* clustering di outliner: i centroidi possono essere "trascinati" dagli outlier, o gli outlier potrebbero avere il loro cluster invece di essere ignorati. Dovremo considerare la rimozione degli outlier prima del clustering.
* scaling con il numero di dimensione: man mano che il numero di dimensioni aumenta, una misura di similarità basata sulla distanza converge ad un valroe costante per ogni possibile esempio. E' quindi necessario ridurre la dimensionalità oi usando la PCA sui dati delle feature o suando delle tecniche di clsutering spettrale.

In particolare, lo spectral clustering evita il problema della curse of dimensionality aggiungendo uno step *prima* dell'algoritmo:

1. ridurre la dimensionalità dei dati delle feature usando la PCA
2. proiettare tutti i data point in un sottospazio a minore dimensionalitàà
3. effettuare il clsutering dei dati in questo sottospazio usando l'algoritmo di nostra scelta

Quindi, lo spectral clustering non è un algoritmo di clustering separato, ma uno step predcdente al clustering che possiamo usare con un qualsioasi algoritmo di clsutering. https://github.com/petermartigny/Advanced-Machine-Learning/blob/master/DataLab2/Luxburg07_tutorial_4488%5B0%5D.pdf

## Implementazione del k-Means

Possiamo implementare ilm k_means usando le API k-Means di TensorFlow. L'APIO di TensorfLow ci permette di scalare il k-means fornendo le seguenti funzionalità:

* clusteering usnado mini-batches invece dell'intero dataset
* scelta 

ESEMPI

https://colab.research.google.com/gist/anhelus/2d436e290996d8fdb1b52cdf68417479/colab-manual-similarity-with-chocolates.ipynb

https://colab.research.google.com/github/google/eng-edu/blob/main/ml/clustering/clustering-supervised-similarity.ipynb?utm_source=ss-clustering&utm_campaign=colab-external&utm_medium=referral&utm_content=clustering-supervised-similarity

Reference del k-means seeding: https://arxiv.org/abs/1209.1960