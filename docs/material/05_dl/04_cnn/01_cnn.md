# 5.4.1 - Convolutional neural networks

Le **convolutional neural networks** (*CNN*) sono un tipo di rete neurale specializzato nell'elaborazione di dati che hanno una topologia riconducibile ad una griglia temporale. Un tipico esempio di applicazione delle CNN sono le immagini, che nell'ambito informatico sono rappresentate come griglie bidimensionali (o tridimensionali) di pixel.

Il termine *convolutional* nel nome suggerisce inoltre che la rete si basa su una specifica operazione matematica di tipo lineare, chiamata **convoluzione**, che viene usata al posto della generica moltiplicazione matriciale in uno o più strati della rete; vediamola più nel dettaglio.

## La convoluzione

Per comprendere i principi sottostanti l'operazione di convoluzione è utile fare un breve esempio. Supponiamo di voler tracciare la posizione di una navicella spaziale mediante un sensore laser, il quale restituirà un output $x(t), x \in \mathbb{R}$ rappresentativo della posizione della navicella al tempo $t, t \in \mathbb{R}$. In altre parole, il fatto che sia $x$ sia $t$ definite nel dominio dei valori reali farà sì che potremo avere una diversa lettura del sensore laser ad ogni istante di tempo.

Supponiamo adesso che l'uscita del sensore sia affetta da rumore; in tal caso, potremmo voler effettuare diverse misurazioni della posizione della navetta allo scopo di ottenere una stima più precisa della sua posizione. Ovviamente, però, dovremo dare maggiore rilevanza alle misure più recenti, per cui dovremo trovare un modo per farlo dando un peso opportuno a ciascun valore considerato, magari usando una funzione di peso $w(a)$, con $a$ un parametro di "età" associato alla misura. Applicando questa media pesata per ciascun istante $t$, avremo una nuova funzione composta $s$ che fornirà la seguente stima della posizione della navicella:

$$
s(t) = \int x(a) w(t-a) \delta a
$$

Questa operazione, chiamata per l'appunto *convoluzione*, è tipicamente denotata utilizzando la seguente notazione:

$$
s(t)  = (x * w)(t)
$$

!!!note "Ritorno al futuro"
    Notiamo che, limitatamente a questo specifico caso, se $t-a < 0$, allora $w = 0$, onde fare in modo che la funzione non guardi al futuro. In generale, comunque, la convoluzione è definita per qualsiasi funzione per la quale è possibile definire le relazioni precedenti.

##### Convoluzione discreta

Nella terminologia delle CNN, il primo argomento (ovvero la funzione $x$) è chiamato *input*, mentre il secondo argomento (la funzione $w$) è chiamato *kernel*.

Ovviamente, l'idea che un sensore laser possa fornire la misura ad ogni istante temporale non è realistica. Normalmente, infatti, lavoriamo con tempi discreti, con un sensore che fornisce dati ad intervalli all'incirca regolari; realisticamente quindi potremo presumere che il nostro laser fornisca una misura (ad esempio) una volta al secondo. L'indice temporale $t$ potrà quindi considerare soltanto valori interi e discreti. Di consequenza, potremo definire la convoluzione discreta come:

$$
s(t) = (x * w)(t) = \sum_{a=-\infty}^{\infty} x(a) w(t-a)
$$

Nelle CNN, l'input è di solito un array di dati multidimensionali, mentre il kernel è un array di parametri multidimensionale adattato all'algoritmo di apprendimento. Dato che ogni elemento sia dell'input sia del kernel deve essere salvato all'interno della memoria del calcolatore, possiamo ipotizzare che queste funzioni siano zero ovunque, tranne che nell'insieme finito di punti per i quali stiamo effettuando l'osservazione.

##### Convoluzione multidimensioanle

Nell'esempio precedente abbiamo applicato una convoluzione su di un unico asse. Tuttavia, è possibile applicare 

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
