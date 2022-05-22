# 12 - Introduzione al machine learning

Il *machine learning* è alla base di alcune tra le più importanti tecnologie odierne. Le sue applicazioni sono molteplici: si va dagli strumenti di traduzione automatica fino ai veicoli autonomi, passando per sistemi di videosorveglianza e software per scrivere codice.

In pratica, l'avvento del machine learning ha offerto un modo alternativo, e *più efficace*, di risolvere problemi estremamente complessi. Volendo riassumere il concetto alla base del machine learning, potremmo dire che questo rappresenta il procedimento che insegna ad un software, chiamato *modello*, a fare predizioni significative a partire da un insieme di dati. In altri termini:

!!!quote "Modello di machine learning"
    Un modello di machine learning rappresenta la relazione matematica intercorrente tra i dati che il sistema derivante utilizza per effettuare predizioni.

Come esempio, immaginiamo di creare un software che effettui la predizione del quantitativo di pioggia che cadrà in una zona. Per farlo, possiamo usare due approcci:

* nell'approccio *tradizionale*, creeremo una rappresentazione fisica dell'atmosfera e della superficie terrestre, risolvendo equazioni estremamente complesse come le Navier-Stokes;
* nell'approccio *basato sul machine learning*, daremo ad un modello un quantitativo adeguato (e, molto spesso, *enorme*) di dati riguardanti le condizioni meteorologiche, fino a che il modello stesso non apprenderà le relazioni sottostanti i diversi pattern di feature meteorologiche che permettono di produrre diversi quantitativi di pioggia.

In entrambi i casi, una volta completata l'implementazione (per l'approccio tradizionale) o l'addestramento (per l'approccio basato su machine learning) passeremo al software i dati sulla condizione meteorologica attuale, per poi predire il quantitativo di pioggia previsto.

TODO: DA QUI

# tipi di sistemi ML

I sistemi di ML ricadono in tre diverse categorie a seconda di come apprendono a fare predizioni:

* supervisionati
* non supervisionati
* reinforcement

## supervisioned

Il supervised learning effettua delle predizione dopo aver visto un gran numero di dati con le risposte corrette e quindi scopre le conessioni tra gli elementi nei dati che producono le risposte corrette. Questo è un po' come uno studente che apprende nuove nozioni studiando vecchi esami che contengono sia domande che risposte. Una volta che lo studente è stato addestrato sugli esami vecchi, è preparato a sostenere un nuovo esame. Questi sismtemi di ML sono chiamati supervisioanti in quanto un umano dà al suisteam i dat con i risultati corretti.

Due dei casi d'uso comuni per il supoervsied learning sono la regressione e la classificazione.

## regressione

Un modello di regressione predice un valore numerico. Ad esempio, un modello sul tempo che predice il quantitativo di pioggia in millimetri è un modello di regressione. Altri esempi sono:

* prezzi future delle case: dati metri quadri, località, numero di bagni e camere da letto, rati di interesse, costi di costruzioni ed altro, predice il prezzo della casa
* tempo necessario per arrivare ad una località: dato lo storico delle condizioni di traffico, preso da smartphone, sensori di traffico ed altro, la distanza dalla destinazione e le condizioni meteo, restituisce il tempo in minuti e secondi per arrivare a destinazione

## classificazione

i modelli di classificazione predicono la possibilità che qualcosa appartenga ad una categoria. a differenza dei modelli di regressione, il cui otuput è un numero, i modelli di classificazione mandano in output un valore che stabilise se qualcosa apparetenga o meno ad una certa cageoria. ad esempio, i modelli di classificzione sono usati per predire se un'email è di spam o se una foto contiene ungatto.

I modelli di classificzione si dividonon in due gruppi: i modelli di classificazione bianria e quelli di classificazione mlticlasse. I modelli di classificazione binaria mandano in output un valore da una classe che contiene solo due valori, ad esempio, un modello manda in output o pioggia o no pioggia. I modelli multiclasse invece mandano in output un valore da una classe che contiene più di due valori, ad esempioun modello che può amndare in usicta sia pioggia, neve, grandine o temporale.

## apprendimento non supervisionato

I modelli di apprendimento non supervisionato fanno rpedizioni a partire da dait che non contengono delle riposte corrette. Un modello di apprendimento non superivsioanto ha come oibettivo identificare dei patterns ignificativi tra dati. In altre parole, il modello non ha alcun indizio di come categorizzare ogni pezzo di dato, ma invece deve inferire le sue regole.

Un modello comunemente utilizzato pè quello che usa la tecnica chiamata clustering. Il modello individua dei punti che vanno a disposrsi secondo dei raggurppamenti naturali.

Il clustering differisce dalla classificazione perché le categorie non sono definite da noi. Ad esempio, un modello non supervisionato può effettuare un raggruppamento di un dataset sul tempo sulla base delle temperature, rivelando delle suddivisioni che definiscono le stagioni. Possiamo quindi provare a dare un nome a questi cluster in abse a come "comprendiamo" il dataset.

## il reinforcement learning

il reinforcement learning fa delle predizioni ottenendo delle ricompense o pnealità basate su azioni effettuate all'interndo di un ambiente. Un sistema di reinforcement leraning genera una policy che definisce la migliore strategia per ottenere la maggior parte dei requisiti.

Al momento, le applicazioni del reinforcement learning sono varie, come l'addestramento di robot per effetutare determinati task, come camminare ion una stanza, oppure creare dei programmi come Alpha Go che giochino al gioco del go.
