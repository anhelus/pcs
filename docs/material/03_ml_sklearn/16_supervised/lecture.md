# apprendimento supervisionato

l'apprendimento supervisioato è+ probabilmente la forma di machine learning più diffusa. Siccome i task di questo tipo son ben definiti, come l'identificazione di spam o la predizione di pioggia, ci sono più casi d'uso potenziali di quelli presenti nell'apprendimento non supervisioanto ed il reinforcement learning.

## Dati

I dati sono la forza che governa il ML. I dati sono di vario tipo: possono essere stinghe e numeri memrozziati all'interno di tabelle, o valori di pixelk e forme dìonda catturati all'interno di immaagini o file audio. I dati tra loro correlati sono memorizzati all'interno di dataset. Ad esempio, potremmo avere un dataset dei seguenti:

* immagini di gatti
* prezzi delle case
* informazioni meteo

I dataset sono fatti da singoli *campioni* che contengono *feature* ed una label nel caso di apprendimento supervisionato. Si può pensare ad un campione come ad una singola riga in un foglio di calcolo. Le feature sono i valori che un modello supervisioanto usa per predire la label. La label è la rispota, o il vlaore che vogliamo predire. In un modello meteo che predice le precipitazioni, le feature possono essere latitudine, longitudine, tempraatura, umidità, copertura delle nubi, direzione del vento e pressione atmosferica. La label potrebbe essere il quantitativo di pioggia caduto.

Degli esempi che hano sia le feature che le label sono chiamati campioni etichettati.

Esistono anche dei campiioni non etichettati, i quali contengono le feature, ma non le label. Dopo che creiamo il modello, questo può prediore l,e label a partire dalle feature.

## caratteristichye di un dataset

Un dataset è caratterizzato dalla dimensione (ovvero il numero dei campioni) e dall'eterogeneità (ovvero il range di casi che questi campioni sono in grado di trattare). Un buon dataset è grande e molto eterogeneo.

Alle volte peòr alcuni dataset sono sì grandi, ma hanno scarsa eterogeneità, mentre altri sono piccoli ed estremamente eterogenei. In altre parole, un grosso dataset non garantisce sempre adeguata eterogeneità, ed un dataset molto eterogeneo non sempre ha un numero sufficiente di campioni.

ADd esempio, un dataset meteo potrebbe contenere acquisizioni per ben cento anni, ma soltanto per il mese di luglio. Usare questo dataset per predire le precipitazioni in gennaio, ovviamente, produrrebbe dei risultati alquanto discutibili. Di converso, und ataset potrebbe contenere solo pochi anni, ma tutti i mesi. Qusto dataset potrebbe anch'esso produrre dei risultati non ottimali perchP non ha abbastanza anni per tenere in conto la variabilitàò.

## modello

Un modello è normalmente una collezione più o meno complessa di numeri che definiscono la relazione matematica tra uno specifico pattern di feature in ingresso ad uno specifico valore di una label di uscita. Il modello scopre questi pattern attraverso un processo di addestramento.

## addestramento

Prima che un modello possa effettuare delle predizioni deve essere addestrato. Per addestrare un modello, gli diamo un dataset con degli esempi etichettati. L'obiettivo è quindi quelo di trovar ela migliore soluzione per predire i valori a partire dalla feature. Il modello trova la migliroe soluzione comparando il valore predetto al valore vero e proprio della label. Sulla base della differenza tra il valore predetto e quello vero (chiamato *loss*, o costo), il mdoello aggiorna la sua soluzione. In altre parole, il modello apprende la relazione matematica tra le feature e la label in modo che possa fare la igliroe predizione su dati che non ha anocra visto.

Ad esempio, se il modello predice che a partire da un certo insieme di valori per le feature sono attese 10 cm di pioggia, ma il valore vero è di 5 cm, allora il modello modifica la sua soluzione in modo che la predizione sia più vicina a 5 cm. Dopo che il modello ha visto ad ogni esempio nel dataset (in alcuni casi più volte) arriva ad una soluzione che effettua la migliore predizione, in media, per ciascuno dei campioni.

Graficamente:

1. il modello prende un singolo esempio e fornisce una predizione

FIGURA 1 GOOGLE

2. il modello compara il suo valore predetto con il valore vero e proprio, ed aggiorna la sua soluzione

FIGURA 2 GOOGLE


3. il modello ripete questo processo per ogni campione etichettato nel dataset

FIGURA 3 GOOGLE

In questo modo, il modello apprende gradualmente la relazione corretta tra le feature e la label.  Questo graduale comprensione è il motivo per cui dataseet grossi ed eterogenei producono modelli mikgliori. Il modello ha visto più dati con un range più ampio di valrori, e ha rifinito la sua comprensione della relazione tra le feature e la label.

Druante il training, possono essere fatti dei piccoli modifiche alle configurazioni e feature usate dal modello per effettuare predizioni. Ad esempio, alcune feature hanno un potere predittivo superiore ad altre. Quindi si possono scegliere quali feature usare durante l'addestramento: ad esempio, supponiamo che un cdataset meteo contenga orario come feature: in questo caso, possiamo scegliere di aggiungere o rimuovere questa feature dirante l'addetramento per vedere se il mdoello fa delle previsioni migliori o peggiori con o seznza quest afeature.

## validaizone

il modello addestrato viene valutato per determinare come è andato l'apprendimento. Quando valutiamo un modello usiamo un dataset na diamo solo al modello le feature del dataset. Quindi compariamo le predizioni del modello ai valori veri delle label.

A seconda delle predizioni del modello, si può scegliere di effettuare un ulteriore addestramento e validazione prima di effetturane il deploy in un'applciazione reale.

## ionferenza

Una volta che siamo soddisfatti dal risultato della validaizone del modello, possiamo usarlo per fare predizione (chiamata inferenza) su esempi non etichettati. nell'esempio dell'applicazione meteo, daremmo al modello le condizioni meteo attuali, e questo predirrà il quantitativo di pioggia.

