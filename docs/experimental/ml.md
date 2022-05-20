# COsa è il machine learning?

Il machine learning è alla base di alcune tra le tecnologie più importanti usate al giorno d'oggi, dalle app di traduzione automatica ai veicoli autonomi.

Il ml offre un nuovo modo di risolvere i problemi e rispondere a questioni complesse. In termini basilari, il ML è il processi di addestrare un software, chiamato modello, per fare delle predizioni uitli a partire dai dati. Un modello di ML rappresenta quindi la relazione matematica tra gli elementi dei dati che un sistema di ML usa per effettuare delle predizioni.

Ad esempio, suppioniamo di creare un'app che predica le pioggie. Possiamo usare un approccio tradizionale o un approccio di ML. Usando un approccio tradizionale, creiamo una rappresentazione fisica dell'atmosfera terrestre e della superficie, calcolando grandi quantità di equiazioni di fluidodinamica. Questo risulta ovviamente essere incredibilmente difficile.

Usando un approccio basato sul ML, diamo al modello di ML un quantiativo enorme di dati sul tempo fino a che il modello stesso *apprende* le relazioni matematiche tra i pattern del tempo che producono diversi quantitativi di pioggia. Daremo quindi al modello i dati attuali sul tempo, e predirremo il quantitativo di pioggia.

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

il reinforcement learning fa delle predizioni ottenendo delle ricompense oi