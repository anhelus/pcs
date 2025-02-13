# 3.1.4 - Task, predizione ed esperienza

Abbiamo visto come un algoritmo di machine learning sia in grado di *apprendere* a partire da un insieme di dati. Per comprendere al meglio cosa questo significhi, possiamo rifarci direttamente alla definizione fornita da Tom Mitchell nel suo libro "Machine Learning" del 1997:

!!!cite "Definizione di apprendimento"
    *A computer program is said to learn from experience $E$ with respect to some class of tasks $T$ and performance measure $P$, if its performance at tasks in$T$, as measured by $P$, improves with experience $E$.*

Cerchiamo quindi di dare una definizione intuitiva per $T$, $E$ e $P$.

## Il task

Il *task* è il compito affidato all'algoritmo di machine learning, che di solito è troppo complesso da risolvere per un essere umano, o anche per un algoritmo puramente deterministico. Appare quindi ovvio come il processo di apprendimento *non* coincida con il task: l'apprendimento è infatti il mezzo che permette al nostro modello di imparare ad effettuare il compito assegnato. Ad esempio, qualora volessimo creare un robot in grado di camminare (e, quindi, di soddisfare il *task* del camminare), dovremmo istruirlo su come fare.

Per un algoritmo di machine learning, risolvere un task significa effettuare una qualche operazione su di un certo campione, inteso come un insieme di valori misurati in qualche modo. Tipicamente, un campione può essere rappresentato come un vettore $x \in \mathbb{R}^n$, con ogni valore $x_i$ feature dello stesso. Ad esempio, le feature associate ad un'immagine possono essere, a basso livello, i valori dei pixel presenti nella stessa.

Esistono diverse tipologie di task che possono essere trattate con algoritmi di machine learning. Oltre ai problemi di classificazione e regressione trattati nella [lezione introduttiva](01_intro.md), alcuni task che possono essere affidati ad un algoritmo di machine learning sono:

* **trascrizione**: sono i task in cui il sistema osserva una rappresentazione di un dato non strutturato, trascrivendone l'informazione sotto forma testuale. Ad esempio, nell'OCR il programma visualizza un'immagine che contiene del testo, restituendo lo stesso sotto forma di una sequenza di caratteri, mentre nel riconoscimento vocale l'algoritmo ha il compito di scrivere una sequenza di caratteri che rispecchino le parole pronunciate in una sorgente audio;

* **machine translation**: sono i task in cui il sistema traduce una sequenza di simboli in un certo linguaggio in una sequenza in un altro linguaggio. Un esempio di task di questo tipo è la traduzione di un testo dalla lingua inglese a quella italiana;

* **anomaly detection**: in un task di anomaly detection l'algoritmo valuta un insieme di eventi o oggetti, alla ricerca di campioni che risultino essere atipici. Un software di questo tipo potrebbe ad esempio controllare delle transazioni anomale sulla carta di credito.

## La performance

La capacità di un algoritmo di machine learning può essere valutata mediante una misura quantitativa specifica per il task svolto.

Per i task di classificazione, una delle misure più utilizzate è l'*accuracy*, che non è altro se non la proporzione di campioni per la quale il modello è in grado di produrre l'output corretto. Nella pratica, possiamo ottenere un'informazione equivalente considerando l'*error rate*, ovvero la proporzione di campioni per la quale il modello produce un output non corretto. I task di regressione invece prevedono l'utilizzo di una metrica differente che dia al modello un punteggio numerico valutato su ogni campione.

E' importante sottolineare come la performance vada misurata su dati che l'algoritmo *non* ha visto in precedenza, il che ci permette di "simularne" le performance nel mondo reale. Queste misure sono quindi valutate su un *insieme di test* separato dai dati usati per l'addestramento, che vanno per l'appunto a formare l'*insieme di training*.

La scelta della misura di performance può sembrare diretta ed oggettiva, ma spesso può essere difficile sceglierne una in grado di definire al meglio il comportamento desiderato del sistema. In alcuni casi, questo è legato alle difficoltà nello stabilire *ciò* che dovrebbe essere misurato. Ad esempio, in un task di trascrizione, sarebbe meglio usare l'accuracy del sistema nel trascrivere intere sequenze o una misura più granulare, che fa in modo che specifici elementi della sequenza siano corretti? Ancora, in un task di regressione, vanno maggiormente penalizzati tanti errori di piccola dimensione o pochi errori di grande dimensione? Queste scelte di design dipendono prevalentemente dall'applicazione.

## L'esperienza

L'*esperienza* viene fornita ad un algoritmo mediante un intero *dataset*, ovvero un insieme di molti campioni. Un esempio di dataset molto utilizzato per il test di algoritmi di machine learning è *Iris*, composto da un insieme di misure fatte su sepali e petali di $150$ piante di iris, ciascuna appartenente ad una tra tre differenti classi. In particolare, ogni singola pianta è un *campione* del dataset, la quale è a sua volta caratterizzata da quattro feature, ovvero lunghezza ed ampiezza sia di sepalo, sia di petalo.

In base al tipo di esperienza fornita dal dataset, l'algoritmo può essere *supervisionato* o *non supervisionato*; come abbiamo [già visto](01_intro.md), gli algoritmi di learning non supervisionato apprendono proprietà intrinseche della struttura del dataset, mentre quelli di learning supervisionato imparano a relazionare tali proprietà con una label o un target. In altri termini:

* l'apprendimento non supervisionato prevede l'osservazione di molti esempi di un vettore casuale $x$ a partire dai quali si apprende la distribuzione di probabilità $p(x)$, o delle proprietà interessanti della stessa;
* l'apprendimento supervisionato prevede l'osservazione di molti esempi di un vettore casuale $x$ a cui è associato un vettore $y$ a partire dai quali si apprende la distribuzione di probabilità $p(y|x)$.

Il termine *supervisionato* si origina quindi dal fatto che il target $y$ viene fornito da un "istruttore" che mostra al sistema di machine learning la "verità", figura che non è presente nell'apprendimento non supervisionato.

!!!note "Reinforcement learning"
    Gli algoritmi non fanno esperienza su di un dataset, ma apprendono ad interagire con un ambiente mediante un apposito loop di feedback.

## Descrivere un dataset

Il dataset è descritto in termini della cosiddetta *design matrix*, che contiene tante righe quanti sono i campioni disponibili, e tante colonne quante sono le feature. Ad esempio, il dataset Iris sarà caratterizzato da una design matrix del tipo $X \in \mathbb{R}^{150 \times 4}$, dove $X(i, 1)$ è la lunghezza del sepalo della pianta $i$, $X(i, 2)$ è l'ampiezza del sepalo della stessa pianta, e via dicendo. La design matrix definisce quindi ogni campione come un vettore della stessa lunghezza. Ad esempio, una design matrix non può contenere delle immagini con un numero diverso di pixel.

Nel caso dell'apprendimento supervisionato, alla design matrix si associa un vettore di label $y$, con $y_i$ che fornisce la label per il campione associato alla riga $i$-ma.
