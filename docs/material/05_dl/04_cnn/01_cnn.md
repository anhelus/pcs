# 5.4.1 - Convolutional neural networks

Le **convolutional neural networks** (*CNN*) sono un tipo di rete neurale specializzato nell'elaborazione di dati che hanno una topologia riconducibile ad una griglia temporale. Un tipico esempio di applicazione delle CNN sono le immagini, che nell'ambito informatico sono rappresentate come griglie bidimensionali (o tridimensionali) di pixel.

Il termine *convolutional* nel nome suggerisce inoltre che la rete si basa su una specifica operazione matematica di tipo lineare, chiamata **convoluzione**, che viene usata al posto della generica moltiplicazione matriciale in uno o più strati della rete; vediamola più nel dettaglio.

## La convoluzione

Per comprendere i principi sottostanti l'operazione di convoluzione è utile fare un breve esempio. Supponiamo di voler tracciare la posizione di una navicella spaziale mediante un sensore laser, il quale restituirà un output $x(t), x \in \mathbb{R}$ rappresentativo della posizione della navicella al tempo $t, t \in \mathbb{R}$. In altre parole, il fatto che sia $x$ sia $t$ definite nel dominio dei valori reali farà sì che potremo avere una diversa lettura del sensore laser ad ogni istante di tempo.

Supponiamo adesso che l'uscita del sensore sia affetta da rumore; in tal caso, potremmo voler effettuare diverse misurazioni della posizione della navetta allo scopo di ottenere una stima più precisa della sua posizione. Ovviamente, però, dovremo dare maggiore rilevanza alle misure più recenti, per cui dovremo trovare un modo per farlo dando un peso opportuno a ciascun valore considerato, magari usando una funzione di peso $w(a)$, con $a$ un parametro di "età" associato alla misura. Applicando questa media pesata per ciascun istante $t$, avremo una nuova funzione composta $s$ che fornirà la seguente stima della posizione della navicella:

$$
s(t) = \int x(a) w(t-a) \delta a
$$



DA QUI


Questa operazione è chiamata  *convoluzione*. L'operazione convoluzione è tipicamente denotata con un asterisco:

$$
s(t)  = (x * w)(t)
$$

Nel nostro esempio, $w$ ha bnisogno di avere una funzione di densità di probabiòlità valida, o l'output non sarà una media pesata. Inoltre, $w$ deve essere $0$ per tutti gli argomenti negativi., o guarderà al futuro, che presumiobilmente è oltre le nostre capacità. Queste limtiazioni sono specifiche per il nostro esempio, comujnque. In generale, la convoluzione è definita per una qualsiasi funzione per la quael l'integrale precedente è definito e può essere usato per altro scopi oltre a prender le medie pesate.

Nella terminologia delle reti convoluzionali, il priomo argomento (ovvero la funzione $x$) alla convoluzione è spesso chiamato il suo *input*, mentre il secondo argomento (in qeusto esempio la funzione $w$) è il *kernel*. L'output è alle volte chiamato *feature map*.

Nel nostro campione, l'idea di un sensore laser che può fornire la misura ad ogni istante non è erealistica. Normalmente, quando laviramo con i dati su un computer, il tempo sarà discretizzato, ed il nostro sensore ci fornirà dati ad invervalli regolari. Nel nostro esempio, può essere più realistico presumere che il nostro laser fornisca una misurazione una volta al secondo. L'indice di tempo $t$ può quindi prendere soltanto valori interi. Se presumiamo che $x$ e $w$ siano definite soltanto sull'intero $t$, possiamo definire la convoluzione discreta come:

$$
s(t) = (x * w)(t) = \sum_{a=-\infty}^{\infty} x(a) w(t-a)
$$

Nelle applicazioni di machine learning, l'input è di solito un array di dati multidimesnsioanli, ed il kernel è di solito un array multidimensiopnael di parametri che sono adattati dall'algoritmo di apprendimento. Dato che ogni elemtno dell'input e del ckernel deve essere esplicitamente emmorizzato separatamente, normalmente ipotiziamo che queste funzioni siano zero onvuqne tranne nell'ìoinsieme di punti finito per i quali memorizziamo i valori. Questo singifica che nella pratica possiamo implmeentare al sommatoria infinita come una somma su un numero finito di eloemnetoi.

Infine, possiamo usare le convoluzioni su più di un asse per volta. Per esempio, se usiamo un'imamgine bidimensionale $I$ come input,. probabilmente vorremo usare un kernel bidimensionale $K$:

$$
S(i,j) = (I * K)(i, j) = \sum_m \sum_n I(m,n)K(i-m, j-n)
$$

La convoluzione è commutativa, il che significa che possiamo scrivere in maneir aequivalente:

$$
S(i,j) = (K*I)(i,j) = \sum_m \sum_n I(i-m, j-n) K(m,n)
$$

La proprietàò commutativa della convoluzione nasce dal fatto che abbiamo *inveritop* il kernel rispetto all'iunput,. nel senso che man mano che $m$ aumenta, l'indice nell'ingresso aumenta, ma l'indice nel kernel decrementa. Mentre la proprrioetà commutativa è utile per scirvere teorimi, non è normalmente una proprietà importante dell'0implementazione di una rete neurale. Invece, molte librerie di reti neurali implementano una funzioen correlata chiamata *cross-correlazione*é, che è identica alla convoluzione ma senza rovesciare il kernel:

$$
S(i,j) = (K * I)(i,j) = \sum_m \sum_n I(i+m, j+n) K(m,n)
$$

Molte libreire di machine learning implemnentano la cross-correlazione chiamadnoal convoluzoione.
