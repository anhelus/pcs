# 17 - Modelli supervisionati: regressione logistica

Esistono diversi problemi, tra cui quelli di classificazione multiclasse, che richiedono che l'uscita del sistema sia una stima di probabilità; per far questo, la *regressione logistica* è lo strumento "principe" da utilizzare.

Per comprenderne il funzionamento, supponiamo di creare un modello di regressione logistica che predica la probabilità che una mail ricevuta da un indirizzo sconosciuto sia di spam. Chiameremo questa probabilità come:

$$
p(mail|unknown)
$$

Se il modello afferma che la probabilità $p(mail|unknown) = 0.05$, allora, su $100$ mail ricevute da indirizzi sconosciuti, $5$ saranno di spam:

$$
spam = p(mail|unknown) \cdot mail_rec = 0.05 * 100 = 5
$$

Questo è un esempio di utilizzo della probabilità *as is*. In molti casi, tuttavia, mapperemo l'output della soluzione su un problema di classificazione binario, nel quale l'obiettivo è predire correttamente uno di due possibili label (in questo caso, *spam* o *non spam*).

## 17.1 - La funzione sigmoidale

Ci si potrebbe chiedere come un modello per la regressione logistica sia in grado di asicurarsi che l'uscita ricada sempre nell'intervallo tra $0$ ed $1$. In tal senso, questo è assicurato dall'uso della *funzione sigmoidale*, definita come segue:

$$
y = \frac{1}{1+e^{-z}}
$$

la cui formulazione grafica è la seguente:

<figure markdown>
  ![sigmoid](./images/sigmoid.png)
  <figcaption>Figura 1 - Interprete Python</figcaption>
</figure>

Nell'espressione precedente, notiamo che:

* $y$ è l'uscita della regressione logistica;
* $z$ è pari, per un generico modello lineare, a $b + w_1 x_1 + \ldots + w_N z_N$.

## 17.2 - Funzione di costo

La funzione di costo per la funzione logistica è chiamata *log loss*, ed è espressa come:

$$
LogLoss = \sum_{(x, y) \in D} -y log(y') - (1 - y) log (1 - y')
$$

dove:

* $(x, y)$ sono le coppie date da feature e label nel dataset $D$;
* $y$ è la label vera per un dato insieme di feature;
* $y'$ è il valore predetto.
