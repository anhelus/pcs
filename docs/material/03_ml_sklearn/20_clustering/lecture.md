# 20 - Il clustering

Il *clustering* è l'operazione di categorizzare dei campioni in un dataset senza che questi abbiano necessariamente un'etichetta determinata a priori.

Per fare un esempio, potremmo suddividere i nostri album musicali sulla base delle sonorità ispirate dal loro ascolto: in questo caso, non ci staremmo affidando ad una certa "etichetta", come ad esempio l'anno di produzione o l'artista, ma ad un concetto molto più "empirico", ovvero la vicinanza o meno dell'album ai nostri gusti musicali.

Ovviamente, dato che nel clustering i campioni non considerano una label, stiamo parlando di apprendimento *non* supervisionato. Se i campioni fossero etichettati, avremmo una normale procedura di classificazione.

Il clustering può avere numerose applicazioni: ad esempio, potrebbe essere usato per segmentare il mercato mediante dei profili di clientela simili, oppure per suddividere le immagini in zone simili, o ancora per individuare delle anomalie all'interno di un insieme di dati.

Una volta che il clustering è completo, ad ogni cluster viene assegnato un certo *identificativo*, che ci permette in qualche modo di "condensare" e "riassumere" le informazioni dell'intero cluster. Quest'assegnazione può anche essere usata come ingresso ad altri sistemi di machine learning, ad esempio di classificazione, che possono usare l'identificativo assegnato come una vera e propria label.

## 20.1 - Tipi di clustering

La scelta di un algoritmo di clustering deve essere condotta sulla base della scalabilità dello stesso. Infatti, laddove alcuni algoritmi di clustering confrontano tra loro ogni possibile coppia di dati, con una complessità $O(n^2)$ per $n$ campioni, altri, come il k-means, effettuano un numero molto più limitato di operazioni, ottenendo una complessità nell'ordine di $O(n)$, il che cambia radicalmente la situazione nel caso di dataset con milioni di campioni. Tuttavia, ogni algoritmo ha anche diversi vantaggi e svantaggi che devono essere valutati sulla base dell'applicazione scelta.

In generale, abbiamo quattro diverse categorie di clustering:

* nel *centroid-based clustering*, i dati sono organizzati secondo la loro distanza da dei *centroidi*, ovvero dei campioni considerati come "base" per ciascun cluster. Questo tipo di algoritmi risulta essere mediamente efficace, ma è sensibile alle condizioni iniziali ed alla presenza di eventuali outliers;
* nel *density-based clustering*, i dati sono organizzati in aree ad alta densità. Ciò permette la connessione di cluster di forma arbitraria, e facilita inoltre l'individuazione di outlier, che per definizione sono nelle zone a minore densità di campioni. Possono però essere sensibili a dataset con densità variabile ed alta dimensionalità;
* nel *distribution-based clustering*, si suppone che i dati abbiano distribuzione gaussiana, e siano quindi suddivisibili come tali. Questo tipo di algoritmi non è efficiente se non si conosce a priori il tipo di distribuzione dei dati;
* nello *hierarchical clustering* viene creato un albero a partire dai dati. Questo tipo di clustering è particolarmente efficace nel caso si trattino certi tipi di dati, come ad esempio le tassonomie, e prevede che possa essere selezionato un numero ridotto di cluster tagliando l'albero al giusto livello.

## 20.2 - Workflow del clustering

L'esecuzione di un algoritmo di clustering prevede tre step:

1. nel primo, dobbiamo *preparare i dati*, effettuando le operazioni che abbiamo visto in precedenza per la classificazione e la regressione;
2. nel secondo, dovremo *definire una metrica di similarità*;
3. nel terzo, eseguiremo l'algoritmo vero e proprio.

Concentriamoci per un attimo sul secondo step. Definire una metrica di similarità significa nella pratica stabilire quando due campioni risultano essere simili tra loro. In tal senso, è possibile operare in due modi:

* la metrica può essere scelta *manualmente*, ovvero scegliendo le feature da considerare nella valutazione della distanza tra i campioni;
* oppure, la metrica può essere scelta in maniera *automatica* a partire da un *embedding*, ovvero da una rappresentazione a dimensionalità ridotta del dato iniziale.

Nel primo caso questo avviene in modo abbastanza intuitivo: se, ad esempio, volessimo suddividere un insieme di scarpe in base a taglia e prezzo, potremmo considerare la distanza euclidea come rappresentativa dello "spazio" che intercorre tra due campioni. Questo approccio, tuttavia, è efficace soltanto nel caso di campioni a bassa dimensionalità.

Il secondo caso è invece preferibile nel momento in cui si vanno a considerare dei dati ad alta dimensionalità: infatti, in queste situazioni si rischia di incorrere nel fenomeno della *curse of dimensionality*, che rende difficile distinguere tra due campioni differenti, per cui si tende ad estrarre delle rappresentazioni "ridotte" dei dati a partire dalle quali applicare il concetto di distanza.

## 20.3 - Applicazione di un algoritmo di clustering: il K-Means

Vediamo adesso come usare il più conosciuto ed utilizzato algoritmo di clustering, ovvero il *k-means*, algoritmo centroid-based che raggruppa i campioni in $k$ diversi cluster assegnando ogni dato in base alla distanza dal centroide del cluster stesso. Il k-means ha diverse ipotesi alla base, tra cui la più restrittiva è una, ovvero quella legata alla conoscenza del numero iniziale di cluster $k$.

Una volta fissato questo valore, l'algoritmo lavora in tre step successivi:

1. al primo step, l'algoritmo sceglie casualmente $k$ centroidi tra i diversi dati a disposizione;
2. al secondo step, l'algoritmo assegna ogni punto al centroide più vicino, definendo i $k$ cluster iniziali;
3. al terzo step, l'algoritmo ricalcola il centroide considerando il valore medio di tutti i punti del cluster, e ritorna allo step 2.

Il k-means proseguirà fino a che i cluster calcolati al punto 2 non saranno stabili o, nei casi più complessi, fino a che non sarà raggiunto il numero massimo di iterazioni impostato in fase di inizializzazione. In figura possiamo osservare una spiegazione visiva del funzionamento dell'algoritmo.

![kmeans_conv](./images/kmeans_conv.gif)

## 20.4 - Clustering in Scikit Learn

Per implementare un algoritmo di clustering in Scikit Learn dovremo fare affidamento sulla classe [`KMeans()`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html), utilizzabile come segue:

```py
from sklearn.cluster import KMeans
import numpy as np

X = np.array([[1, 2], [2, 1], [5, 2], [3, 3]])
cl = KMeans()
cl.fit(X)
```

## 20.5 - Scelta del valore ottimale di cluster

La scelta del valore ottimale di $k$ è un procedimento emnpirico, in quanto non abbiamo a disposizione delle vere e proprie label per la verifica dell'uscita dell'algoritmo. In tal senso, abbiamo a disposizione sia delle metriche, che vedremo in seguito, sia degli approcci più qualitativi, che dipendono dai concetti di *cardinalità* e *magnitudine* del clustering.

In particolare, per *cardinalità* si intende il numero di campioni per ogni cluster, mentre per *magnitudine* la somma delle distanze di tutti i campioni in un cluster dal centroide. Immaginiamo di essere in un caso come quello descritto nella seguente figura.

![clustering_eval](./images/clustering_eval.png)

Prevedibilmente, il rapporto tra cardinalità e magnitudine dovrebbe essere all'incirca lineare. Quindi, come si può vedere dalla figura precedente, ci potrebbe essere qualcosa che non va con il cluster $4$.

A questo punto, avendo valutato empiricamente la possibile presenza di un problema qualitativo con il clustering, possiamo provare ad eseguire l'algoritmo per un valore crescente di $k$. Proviamo a plottare questo valore in rapporto alla somma delle magnitudini del risultato, che diminuirà all'aumentare di $k$; un valore ottimale per $k$ è quello che si ottiene quando questo grafico tende a stabilizzarsi, ad esempio considerando il valore per cui la derivata diventa maggiore di -1 (e quindi l'angolo della funzione dei $k$ è maggiore di $135°$).

![clustering_k](./images/clustering_k.png)
