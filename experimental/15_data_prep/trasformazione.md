# Trasformare i dati

Trasformiamo i dati primariamente per la seguente ragione:

1. trasforamzioni obbligatori per la compatibilità dei dati. I campioni includono:

* convertire feature non numeriche in numeriche. Non possiamo fare la moltiplicazione matriciale di una stringa,per cui possiamo convertire la stringa ad alcune rappreesntazioni numeriche.
* ridimensionare gli input ad una dimensione fissa. I modelli lineari e lre reti neurali hanno un numero fisso di nodi di input, per cui i nostri dati di input devono avere sempre la stessa dimensione. PEr esempio, i modelli delle immagini devono ridimensionare le immagini in questo dataset ad una dimensione fissa.

2. trasformazioni opzionali che possono migliorare il modello a funzionare meglio. Gli esempi includono:

* la tokenizzazione delle feature testuali
* la normalizzazione delle feature nomeriche
* permettere ai modelli lineari di introdurre delle non linearità nello spazio delle feature

Il secondo tipo di trasformazioni non sono necessarie: il modello potrebeb essere eseguito senza di essi. Ma usare quete tecniche possono abilitare il modello per dare risultati migliori.

## quando trasformare i dati?

Si possono applicare le trasformazioni o quando si genrano i dati sul disco, o all'interno del modello.

Nel rpimo caso, abbiamo il vantaggio che i calcoli sono effettuati una volta sola, e si può guardare l'intero dataset a determinare la trasformazione. Nel secondo caso, invece, i modello prende i dati non trasfromati in ingresso, e li trasforma nel modello. Questo dà più flessibilità, in quando le trasformazioni possono essere modificate suglis tessi data file, anche se le trasformazioni possono includeere il tempo della latenza del modello.

!!!note "Nota"
    Nel secondo caso, le trasformazioni potrebbero essere efefttuate per *batch*, ovvero su un sottoinsieme dei dati. Quesot è pericoloso, perché ci potrebbero essere diverse normalizzazioni a seconda del batch considerato.

## Esploare, pulire e visualizzare i nostri dati

Esplorare e pulire i dati prima di effettuare una trasformazione è necessario. Ad esempio, potremmo fixare eventuali dati mancanti.

## tasformazione dati numerici

potremmo dover applicare due tipi di trasformazioni a dati numerici:

* normalizzazione - trasromare i dati numerici alla stessa scale di altri dati numerici
* bucketing - trasfromazione di dati numerici (normalmente continui) in dati categorici

## perché normalizzare le feature numeriche?

La normalizzazione di un dataset che ha feature numeriche copre diversi range (per esempio, età e stipendio). Quando diverse feature hanno diversi range, gli algoritmi potrebbero preferire quelle con peso "maggiore", e peggiorare il tempo di convergenza.

Le tecniche di normalizzazione sono normalmente quattro:

* scaling ad un certo range
* clipping
* log scaling
* z-score

Lo scaling in un certo range indica la conversione di una feature a floating point (ad esempio in un range da 0 a 100) in un range standard (normalmente 0-1 o -1-+1). Per effettuare questo scaling si usa la formula:

$$
y = \frac{(x - x_{min})}{(x_{max} - x_{min})}
$$

Per quello che riguarda il clipping delle feature, qualora il dataset contenga degli outlier ai suoi estremi, potremmo ad esempio limitarci a rimuovere tutte le feature al di sopra di una certa temperatura, o di usare delle soglie statistiche,come i tre sigma o i range interquaritli.

Un'altra possibilità è quella di calcoalre il logaritmo dei nostri valori, comprimendo un range ampio in uno più piccolo usando la funzione

$$
y = log(x)
$$

Questa scelta è utile quando la maggior parte dei campioni del nostro dataset sono concentrati in pochi valori.

Un'ultima possibilità è usare lo z-score, che rappresenta un esempio di scaling diferente facendo in modo che la nostra distribuzione abbia media nulla e deviazione standard unitaria. Viene calcolato con la seguente formula:

$$
y = (x - \mu)/\sigma
$$

## trasformazione dei dati categorici

Alcune delle nostre feature possono essere valori discreti che non sono in una relazione ordinata. Esempi includono le razze di cani, o anche i codici postali. Queste feature sono conosciute come feature *categoriche*, ed ogni valore è chimato *categoria*. Si possono rappresentare i valori categorici come stringhe o anche numeri, ma non possono essere trattati come se fossero dati di tipo numerico.

Spesso, dobbiamo praresenteare le feature che contengono valori interi come cateogirhce invece di numeriche. Ad esempio, consideriamo il codice postale, che è dato da numeri interi. Se per caso la si rappreesnta come una feature di tipo numerico, stiamo chiedendo al modello di individuare una realzione di tipo numerico tra diversi codici postali:per esempio, la differenza tra il codice postale di Bari (70120) e Taranto (74100) potrebbe essere stimata dal modello in 3980!

Le feature categoriche sono di solito memorizzate ed elaborate usando comunque rappresentazioni di tipo numerico (ma che mantengono il riferimetno al fatto che la feature è categorica).

Immaginiamo ad esempio una feature che rappresenti il giorno della settimana. Una modalità semplice di rappresentare tutti i possibili valori assunti dalla feature è quella di utilizzare un numero:

| Giorno | Rappresentazione |
| ------ | ---------------- |
| Lunedì | 1 |
| Martedì | 2 |
| Mercoledì | 3 |
| Giovedì | 4 |
| Venerdì | 5 |
| Sabato | 6 |
| Domenica | 7 |

In questa maniera, stiamo creando un vero e proprio dizionario, nel quale potremo accedere ad una chiave (la rappresentazione) che rappresenterà un determinato valore (il giorno).

Un altro modo di rappresentare questo tipo di feature è mediante una rappresentazione sparsa, in cui ogni valore è rappreentato come un vettore $V$ di lunghezza $m$, con $m$ numero di possibili valori. In particolare, tutti i valori di $V$ saranno pari a 0, tranne quello rappresentativo del valore attualmente assunto dalla feature. Ad esempio, la rappresentazione sparsa di lunedì è data da:

```py
lunedi = np.array([1 0 0 0 0 0 0])
```

mentre quella di giovedì:

```py
giovedi = np.array([0 0 0 1 0 0 0])
```

Questo tipo di rappresentazione ha due vantaggi:

* usando dei valori booleani per ciascun elemento del vettore, si risparmia spazio in memoria (nel caso precedente, 7 bit per il vettore contro gli 8 bit necessari a memorizzare anche un `byte`);
* una rappresentazione di questo tipo rende più semplice un eventuale calcolo matriciale.
