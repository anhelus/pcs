Uno dei problemi princiapli degli algoritmi di deep learning è l'interpretabilità del modello.

Nella pratica, i modelli di deep learning sono trattati come delle "black box", e molte volte non abbiamo idea di:

* dove la rete sta guardando nell'immagine di input
* quale serie di neuroni sono attivati nel forward pass durante l'inferenza o la predizione
* come la rete arriva all'output finale

La domanda è: come facciamo a fidarci delle decisioni di un modello se non possiamo validare come ha fatto ad arrivare a queste decisioni?

Per aiutarci, esistono diversi metodi, tra cui Grad-CAM.

Il grad-CAM usa i gradienti di ogni "concetto" (per esempio quello di "classe cane") che fluisce nel layer convoluzionale finale per produrre una mappa di localizzazione (grossolana) che evidenzi le regioni più importanti nell'immagine allo scopo di predire il concetto.

Usando Grad-Cam, possiamo validare visivamente dove la rete sta guardando, verficiando che tia guardandoai pattern corrretti nell'immagine, e che si stia attivando attorno ad essi.

Se la rete *non* si sta attivando attorno a questi pattern/oggetti nell'immagini, allora:

* la rete non ha propriamente appreso i pattern sottostanti al dataset
* la procedura di training deve essere rivista
* possiamo collezionare dati aggiuntivi
* il nostro modello non è pronto per il deploy

## perchè dovremmo voler visualizzare le class activation maps nelle CNN?

vi è una vecchia leggenda urbana che mette in guardia i riercatori sui pericoli di fare il deploy di un modello senza prima verificare che sta funzionando adeguatamente.

in questo racconto, l'esercito USA voleva usare le reti neurali per individuare in modo automatico i carri armati camuffati.

ai ricercatori assegnati al progetto sono date 200 immagini: 100 contengono carri armati camuffati e nascosti negli alberi, 100 no contengono questi carri armati ed erano soltanto di alberi.

i ricercatori prendono questo dataset, lo dividono in uno split 50/50 per training e testing, e si assicurano che le label di classe siano bilanciate.

Una rete neurale viene addestrta sul training set, ed ottiene un'accuracy del 100%. I ricercatori sono molto soddisfatti di questo risultato, e lo applicano ai dati di test, ottenendo di nuovo un'accuratezza dle 100%.

i ricercatori chaimano il pentagono, e affermano che hanno appena risolto il problema.

alcune settimane dopo, ricevono però una chiamata dal pentagono, che afferma che la rete neurale che ha funzionato così bene in laboratorio funziona malissimo sul campo.

i ricercatori ripetono quindi i loro esperimenti, addestrando modello dopo modello usando diverse procedure, arrivando però sempre allo stesso risultato: accuracy del 100% sia su training, sia su testing.

a un certo punto, però, un ricercatore abbastanza astuto nota che le foto con i tank camuffati erano state catturate in un giorno soleggiato, mentre quella delle foreste in un giorno nuovlos.

in pratica, l'esercito aveva creato un algoritmo per individuare le nuovle.

Anche se ovviamente la veridicità di questa storia non è attendibile, ci permette di mostrare l'importanza dell'interpretabilità di un modello: se il team di ricercatori avesse usato Grad-CAM, sarebbe stato in grado di notare che il modello stava venendo attivato a riguardo della presenza o assenza di nuvole, e non sui carri armati.

## cosa è Grad-CAM?

Grad-CAM lavora 1. trovando l'ultimo layer convoluzionale nella rete e 2. esaminando le informazioni relative ai gradienti che fluiscono all'interno di questo layer.

L'output di Grad-CAM è una heatmap per una data class label . Possiamo usare questa heatmap per verificare visivamente dove sta guardando la CNN all'interno dell'immagine.


