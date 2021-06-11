# Cosa è Scikit-Learn?

Scikit-Learn è una grossa libreria per il machine learnign che supporta sia l'apprendimento supervisionato, sia l'apprendimento non supervisionato. Fornisce anche diversi tool per il model fitting, il data preprocessing, la selezione e valutazione del mdoello, e via dicendo.

## Installazione di Scikit-Learn

TODO

## Un po' di terminologia

Prima di andare avanti, è necessario sapere alcune cose.

### Dati e feature

Possiamo immaginare un dataset come una sorta di "matrice", nella quale le righe sono chiamate *campioni*, mentre le colonne sono chiamate *feature*.

I campioni sono delle osservazioni del fenomeno. Le feature sono le diverse variabili relative a ciascuna osservazione.

Per fare un esempio, immaginiamo di avere due sensori, uno di umidità ed uno di temperatura, che acquisiscono i dati ogni quindici minuti.

Immaginiamo di disporre le acquisizioni in un foglio di calcolo: su ogni riga, avremo un campione, nel quale vi è il momento di acquisizione, oltre ai valori letti di temperatura ed umidità, che potremo leggere per colonna. Le righe sono appunto i campioni, mentre le colonne (istante di acquisizione, temperatura ed umidità) sono le feature.

### Metodi di machine learning

La scelta principale dell'algoritmo di machine learning da utilizzare è legata al *tipo* di dati. Ma cosa significa *tipo di dati*?

Sostanzialmente, esistono due tipi di dati.

* dati indipendenti ed identicamente distribuiti (IID)
* serie temporali

#### Dati indipendenti ed identicamente distribuiti

I dati IID sono, come dice il nome stesso, *indipendenti* l'uno dall'altro. In altri termini, ciò significa che il valore di un campione non dipende dal valore di un altro. Un esempio sono le immagini.

#### Serie temporali

Le serie temporali sono invece fatte da dati dipendenti l'uno dall'altro, vincolati tra loro da vincoli temporali. Un esempio è un video, che è fatto da una sequenza di immagini.

### Stimatori

Gli algoritmi di machine learning sono generalmente definiti come *stimatori*. Scikit-Learn utilizza un'interfaccia comune per ciascun metodo: infatti, vedremo come, indipendentemente dal metodo scelto, useremo sempre i metodi fit, transform e predict, che, almeno in linea di massima, ci permetteranno rapidamente di cambiare i metodi di machine learning da utilizzare.

### Preprocessing

Molto spesso, è necessario effettuare delle operazioni di preprocessing (**mai usare preprocessamento**) sui dati. Questo perché questi possono essere viziati dall'assenza di valori in determinati ambiti, oppure è necessario scalarli. Scikit-Learn offre un intero package dedicato a questo.

train_test_split

Valutazione del modello con cross-validation

## Pipeline
