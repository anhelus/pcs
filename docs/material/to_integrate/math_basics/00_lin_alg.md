# Scalari, vettori, matrici, tensori

* Scalari: uno scalare è un singolo numero. Normalmente, è scritto in corsivo, ed appartiene ad uno dei classici insiemi insegnati nell'analisi matematica di base. Ad esempio, se scrivesismo $s \in \mathbb{R}$ staremmo dicendo che lo scalare contraddistinto con $s$ è un numero reale.
* Vettori: un vettore è dato da un insieme di scalari, ciascuno dei quali ordinato secondo un indice. Tipicament,e i vettori sono indicati in grassetto o con un cappello, come $\hat{x}$. Gli elementi di un vettore sono identificati dal loro indice, spesso indicato nel pedice; di cosneguenza, il primo elemento di $\hat{x}$ sarà $x_1$, il secondo $x_2$, e via discorrendo. Se supponaimo che ciascuno degli $n$ elementi del vettore appartenga all'insieme dei numeri reali $\mathbb{R}$, allora potremo scrivere che il vettore giace nell'insieme formato prendendo il prodotto cartesiano di $\mathbb{R}$ $n$ volte, ovvero $\mathbb{R}^n$. Un altro modo per rappresentare un vettore è identificarlo come un punto nello spazio, con l'$i$-mo elemento che rappresenta la coordinat alungo l'$i$-mo asse.
* Matrici: una matrice è un insieme bidimensionale di scalari, in cui ogni elemento è identifiacato mediante due indici invece di uno solo. Diamo di soito alle matrici dei nomi maiuscoli, come $A$. Se una matrice a valore reali $A$ ha un'altezza di $m$ (o, in altri termini, $m$ righe) ed una larghezza di $n$ (colonne), allora diciamo che $A \in \mathbb{R}^{m \times n}$. In questo caso, identifichiamo i singoli elementi usando due pedici, il primo per la riga, ed il secondo per la colonna; di conseguenza, $A_{11}$ sarà l'elemento in alto a sinistra della matrice $A$, mentre $A_{mn}$ quello in basso a destra.
* Tensori: in alcuni casi avremo bisogno di più di due assi; pensiamo, ad esempio, alle immagini a colori, che sono rappresentate con tre diverse matrici, una per il rosso, una per il verde, ed una per il blu. In questo caso, parliamo di un tensore, che possiamo indicare con **A**. In questo caso, supponendo un tensore a tre dimensioni, indicheremo con **A**$_{i,j,k}$ l'elemento alle coordinate $(i, j, k)$.

## Moltiplicazioni tra vettori

Il prodotto matriciale delle matrici $A$ e $B$ è una terza matrice $C$. Tuttavia, affinché questo prodotto sia possibile, il numero delle colonne di $A$ deve essere pari al numero di righe di $B$; in altri termini, se $A$ ha dimensioni $m \times n$, allora $B$ deve avere dimensioni $n \times p$ affinché $C$ abbia dimensioni $m \times p$.

L'operazione sarà definita come segue:

$$
C_{ij} = \sum_k A_{ik}B_{kj}
$$

!!!note "Prodotto elemento per elemento"
    Il prodotto matriciale differisce dal prodotto elemento per elemento, o *prodotto di Hadamard*, nel quale il risultato è una matrice che contiene il prodotto dei singoli elementi in posizioni omologhe delle matrici $A$ e $B$.

Il *prodotto interno* tra due vettori $x$ ed $y$ della stessa dimensionalità è dato dal prodotto matriciale di $x^Ty$, con $x^T$ vettore *trasposto* di $x$.

## Matrice identità e matrici inverse

DA QUI
