Il machine learning ci aiuta a trovare dei pattern nei dati - pattern che quindi usiamo per effettuare predizioni circa nuovi data point. Per ottenere delle buone predizioni, dobbiamo *costruire* il dataset e *trasformare* correttamente i dati.

## perché data preparation e feature engineering?

possiamo pensare alla feature engineering come ad un aiuto al modello per fargli comprendere il dataset nella stessa maniera in cui farebbe un esere umano. 

gli step necessari a costruire il nostro dataset, e prima di effettuare una trasformazione dei dati, sono:

1. collezione dei dati grezzi
2. identificazione delle feature ed etichettatura delle sorgenti
3. scelta di una strategia di campionamento
4. suddivisione dei dati

questi step dipendono molto da come abbiamo posto il nostro problema di machine learning.

In generale:

1. in caso di nuova analisi, partiamo scegliendo 1-3 feature che sembrano avere un buon potere predittivo. In questo modo, avremo una conferma a riguardo del fatto che il modello di ML funziona come atteso, e potremo costruire una baseline a partire da un paio di feature.


## dimensione e qualità del dataset

In generale, il modello è buono soltanto quanto i dati che hanno permesso di addestrarlo. Ma come facciamo a misurare la qualità del nostro dataset e miglioralra? e di quanti dati abbiamo bisogno per avere dei risultati utili? al solito: dipende.

## dimensione del dataset

Come regola, il modello dovrebbe essere addestrato su un numero di dati che sia di regola maggiore di almeno un ordine di grandezza rispetto al numero di parametri che è possibile addestreare. I modelli più semplici su grossi dataset generalmente battono i grossi modelli su piccoli dataset.

Ovviamente, non è facile quantificare "tanti" dati. Ad esempio, uno dei dataset più piccoli che esistano, ma che è comunque molto usato, è Iris, che contiene 150 immagini, mentre il dataset che viene spesso utilizzato come baseline epr i modelli più sofisticati di reti neurali convoluzionali è ImageNet, che conta più di 10 milioni di immagini.

## qualità di und ataset

Non è assolutamente utile avere tanti dati se questi non sono significativi. Ma come fare a stabilire la qualità di un dataset? Consideriamo in tal senso un approccio empirico, e di scegliere l'opzione che produce il risultato migliore. COn questo in mente, un dataset di buona qualità è quello che ci permette di avere successo con il problema di business che ci riguarda. In altre parole, i dati sono *buoni* se permettono di svolgere il task desiderato.

Ad ogni modo, mentre si collezionano i dati, è utile avere una definizione più concreta di qualità. Certi aspetto della qualità tendono a corrispondere a modelli con performance migiori

### affidabilità

l'affidabilità si riferisce al grado di confidenza che possiamo avere nei nostri dati. Un modello addestrato su dati affidabili è più probabile +
