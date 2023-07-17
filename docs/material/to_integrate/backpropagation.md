# Backpropagation: un esempio

Per questo tutorial, useremo una rete nurale con due input, duie neuroni nello strato nascosto, e due neuroni di output. Inoltre, sia lo strato nascosto sia quello di output avranno un bias.

TODO: IMMAGINE DA DRAW.IO

Per avere di numeri su cui lavorare, impostiamo dei valori iniziali epr i pesi, per i bias, e per gli input/output di trianing.

| Peso | Valore |
| :----: | :------: |
| $w_1$ | $0.15$ |
| $w_2$ | $0.20$ |
| $w_3$ | $0.25$ |
| $w_4$ | $0.30$ | 
| $w_5$ | $0.40$ | 
| $w_6$ | $0.45$ | 
| $w_7$ | $0.50$ | 
| $b_1$ | $0.35$ | 
| $b_2$ | $0.60$ | 
| $i_1$ | $0.05$ | 
| $i_2$ | $0.10$ | 
| $o_1$ | $0.01$ | 
| $o_2$ | $0.99$ |

L'obiettivo della backpropagation è ottimizzare i pesi in modo che la rete neurale possa apprendere a mappare correttamente una coppia arbitraria di input ed output. Per questo esempio, dati gli input $0.05$ e $0.10$, vogliamo che la rete mandi in output $0.01$ e $0.99$.

## Il forward pass

Per iniziare, vediamo quello che la rete predice dati i pesi ed i bias precedenti e gli input $0.05$ e $0.10$. Per farlo, mandiamo questi input in avanti attraverso la rete.

Calcoleremo l'ingresso totale ad ogni neurone dello strato nascosto, filtrarlo usando una funzione di attivazione (useremo la logistica), e ripetere il processo con i neuroni del layer di uscita.

Ecco come calcolare l'ingresso totale ad $h_1$:

$$
\begin{align}
net_{h_1} = w_i \cdot i_1 + w_2 \cdot i_2 + b_1 \cdot 1 = 0.15 \cdot 0.05 + 0.2 \cdot 0.1 + 0.35 \cdot 1 = 0.3775
\end{align}
$$

Applichiamo quindi la funzione logistica per opttenree l'output di $h_1$:

$$
out_{h_1} = \frac{1}{1+e^{-net_{h_1}}} = \frac{1}{1 + e^{-0.3775}} \sim 0.593
$$

Lo stesso processo per $h_2$ ci porta ad un valore $out_{h_2} \sim 0.597$.

Ripetiamo questo processo per i neuroni del layer di output, usando l'output dai neuroni dello strato nascosto come input. L'output per $o_1$ sarà quindi pari a:

$$
net_{o_1} = w_5 \cdot out_{h_1} + w_6 \cdot out_{h_2} + b_2 \cdot 1 \sim = 1.106 \\
out_{o_1} = \frac{1}{1+e^{-net_{o_1}}} = \frac{1}{1+e^{-1.106}} \sim 0.751
$$

Per $o_2$, otterremo $out_{o_2} \sim 0.773$.

### Errore

Calcolo dell'errore per ogni neurone usando l'errore quadrati cco medio:

$$
E = \sum \frac{1}{2} (target - output)^2
$$

In pratica, l'output target per $o_1$ è di 0.01, ma la rete neurale ha dato in uscita $0.735$, per cui:

$$
E_{o_1} = \frac{1}{2} (target_{o_1} - out_{o_1})^2 = \frac{1}{2} (0.01 - 0.751)^2 \sim 0.275
$$

mentre per $o_2$:

$$
E_{o_2} \sim 0.023
$$

L'erore totale è la somma di questi errori:

$$
E_{tot} = E_{o_1} + E_{o_2} \sim 0.298
$$

## Backward pass

L'obiettivo della backpropagation è quello di aggiornare ognuno dei pesi nella rete in modo che facciano in modo che l'outptu vero e proprio sia vicino all'output target,. qunindi minimzzando l'errore per ogni nuerone di output e nella rete intere.

Partiamo dal layer di output. Consideriamo $w_5$. Vogliamo sapere qunaod  un cambio in $w_5$ influeisce sull'errore totale che, in notazione matematica, implica la derivata parziale di $E_{tot}$ rispetto a $w_5$. Possiamo applicare la cosiddetta chiain rule:

$$
\frac{\partial E_{tot}}{\partial w_5} = \frac{\partial E_{tot}}{\partial out_{o_1}} \cdot \frac{\partial out_{o_1}}{\partial net_{o_1}} \cdot \frac{\partial net_{o_1}}{\partial w_5}
$$

Cerchiamo di calcolarew ogni parte di qeusta equazione. Per prima cosa, riportiamo l'errore totale in funzione di $out_{o_1}$:

$$
E_{tot} = \frac{1}{2} (target_{o_1} - out_{o_1})^2 + \frac{1}{2} (target_{o_2} - out_{o_2})^2
$$

Da cui:

$$
\frac{\partial E_{tot}}{\partial out_{o_1}} = 2 \cdot \frac{1}{2}(target_{o_1} - out_{o_1})^{2-1} \cdot -1 + 0 = \\
= - (target_{o_1} - out_{o_1}) \sim 0.741
$$

TODO: DA "Next, how much does the output of"

https://mattmazur.com/2015/03/17/a-step-by-step-backpropagation-example/

## Riferimenti bibliografici

Rumelhart, D. E., Hinton, G. E., & Williams, R. J. (1986). *Learning representations by back-propagating errors*. Nature, 323(6088), 533-536.