# Matematica di un neurone

Diciamo che un certo percettrone riceve $n$ input $[x_1, \ldots, x_n]$ dove ad ogni connessione viene attribuito un peso corrispondente $[w_1, \ldots, w_n]$.

La prima operazione che viene effettuata moltiplica i valori di input per i loro pesi corrispondenti,e d aggiunge un termine di bias $b$ alla loro soma producendo un output $z$:

$$
z = w_1x_1 + w_2x_2 + \ldots + w_nx_n + b
$$

Possiamo in alternativa rappresentare questa operazione in forma più compatta come segue:

$$
z = \sum_{i=1}^n w_ix_i + b
$$

Questa somma pesata è un'operazione lineare. Se ogni neurone deve implementare da solo questo particolare calcolo, allora la rete neurale potrebbe apprendere soltanto un mapping lineare tra input ed output.

Di conseguenza, una seconda operazione è effettuata per ogni neurone che trasformi la somma pesata per l'applicazione di una funzione di attivazione non lineare $a()$:

$$
a(z) = a\(\sum_{i=1}^n w_ix_i + b\)
$$

Possiamo rappresentare l'operazione effeettuata da ciascun neurone in modo ancora più compatta, se dobbiamo integrare ilt ermine di bias nella somma come un altro peso, $%w_0$:

$$
a(z) = a\(\sum_{i=0}^n w_ix_i\)
$$

Quindi, ogni neurone impleemnta una funzione non lineare che mappa un inisiem di input verso un'attivazione di output.

## Addestramento di una rete

Addestrare una rete neurale prevede che si cerchi l'insieme di pesi che modella al meglioi pattern dei dati. E' un processo che impiega la backpropagation ed il gradient descent insieme. Entrambi questi algoritmi fanno uso esteso del calcolo.

Ogni volta che la rete viene attraversata in avanti (ovvero, dagli input verso l'output), ol'errore della rete può essere calcolato come la differenza tra l'output prodotto dalla rete ed il ground truth atteso,. per mezzo di una funzione di costo, come l'errore quadratico medio. L'algoritmo di backpropagation, quindi, calcola il gradiente (ovvero il "tasso" di cambio) di questo errore per cambiare i pesi. PEr farlo, richioede l'uso della *chain rule* e delle derivate parziali.

Per semplciità, consideriamo una rete fatta da due neuroni connessi da un singolo percorso di attivazione. Se dovessimo aprirli, scopriremmo che i neuroni effettuano queste operazioni in cascata:

TODO: METTI FIGURA

La prima applicazione della chain rule connette l'errore della rete rete all'input, $z_2$, della funzione di attivazione $a_2$ del secondo neurone, e conseguentemente al peso $w$ come segue:

$$
\frac{\partial error}{\partial w_2} = \frac{\partial error}{\partial a_2} \cdot \frac{\partial a_2}{\partial z_2} \cdot \frac{\partial z_2}{\partial w_2} = \delta_2 \cdot \frac{\partial z_2}{\partial w_2}
$$

Possiamo notare che l'applicazione della chain rule coinvolge, tra le altre cose, una moltiplicazione per la derivata parziale della funzioen di attivaizone del nuerone rispetto all'input $z_2$. Ci sono diverse funzioni di attivazioni tra cui scegliere, come la funzione sigmoidale o quella logistiica. Se dobbiamo prendere la funzione logistica come esempio, allora la sua derivata parziale sarà calcolata come segue:

$$
\frac{\partial a_2}{\partial z_2} = \frac{logistic(z)}{\partial z_2} = logistic(z_2) \cdot (1 - logistic(z_2))
$$

Possiamo quindi calcolare $\delta_2$ come segue:

$$
\delta_2 = logistic(z_2) \cdot (1 - logistic(z_2)) \cdot (t_2 - a_2)
$$

Qui, $t_2$ è l'attivazione attesa, e nel trovare la differenza tra $t_2$ ed $a_2$ stiamo, quindi, calcolare l'errore tra l'attivazione generata dalla rete ed il ground truth atteso.

Dal momento che stiamo calcolando la derivata della funzione di attivazione, questa dovrebbe essere continua e differenziabile in $\mathbb{R}$. Nel caso delle reti neurali, il gradiente dell'errore viene propagato dall'output verso l'input (*backward*) su un gran numero di layer nascosti. Questo può fare in modo che il segnale d'errore diminuisce rapidamente a zero, sepcialmente se il valore massimo della derivata è già piccolo. Questo è conosciuto come *vanishing gradient*. La funzione ReLU è stata usata in modo molto popolare nel deep learning per alleviare questo problema, in quanto la sua derivata nella porzione positiva nel suo dominio è pari ad 1.

Il peso successivo all'indietro è più indietro nella rete, per cui l'applicazione della chian rule può essere estesa per connettere l'errore complessivo al peso $w_1$ come segue:

$$
\frac{\partial error}{\partial w_1} = \frac{\partial error}{\partial a_2} \cdot \frac{\partial a_2}{\partial z_2} \cdot \frac{\partial z_2}{\partial a_1} \frac{\partial a_1}{\partial z_1} \cdot \frac{\partial z_1}{\partial w_1} = \delta_1 \cdot \frac{\partial z_1}{\partial w_1}
$$

Se prendiamo di nuovo la funzione lgoistica come funzione di attivazione, possiamo calcolare $\delta_1$ come segue:

$$
\delta_1 = \frac{\partial error}{\partial a_2} \cdot \frac{\partial a_2}{\partial z_2} \cdot \frac{\partial z_2}{\partial a_1} \cdot \frac{\partial a_1}{\partial z_1} = \delta_2 \cdot w_2 \cdot logistic(z_1) \cdot (1 - logistic(z_1))
$$

Una volta calcolato il gradiente dell'errore della rete rispettoa d ogni peso, allora l'algoritmo a discesa di gradiente può essere applicato per aggiornare ogni peso per la successiva passata in avanti. Per il peso $w_1$, ad esempio, l'aggiornamento è il seguente:

$$
w_1^{t+1}=w_1^t + \(\eta \cdot \delta_1 \cdot \frac{\partial z_1}{\partial w_1}\)
$$

Da notare che qui abbiamo considerato una rete abbastanza semplice. Nelc aso di reti più complesse, le equazioni diventano rapidamente ingestibili.

Se la rete è addirittura caratterizzata da più rami che contengono più input, e  che vanno in più output, allora la sua valutazione coinvolge la somma di diverse chain rule, una per ogni percorso, in modo simile a come abbiamo derivato precedentemente la chain rule generalizzata.

https://machinelearningmastery.com/an-introduction-to-recurrent-neural-networks-and-the-math-that-powers-them/
