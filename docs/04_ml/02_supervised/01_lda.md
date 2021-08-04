La Linear Discriminant Analysis e la Quadratic Discriminant Analysis sono due classici classificatori con, come suggerisce il loro nome, una superficie di decisione lineare e quadratica, rispettivamente.


Questi classificatori sono attraenti perché hanno delle soluzioni in forma chiusa che possono essere facilmente calcolate, sono intrinsecamente multiclasse, e funzionano bene in pratica, e non hanno degli iperparametri da ottimizzare.

La LDA può essere usata per effettuare una riduzione della dimensionalità upervisionata, proiettando i dait di input su un sottospazio lineare che consiste delle direzioni che massimizzano la separazione tra classi (in un senso preciso, che vedremo a breve). La dimensione dell'output è necessariamente inferiore al numero delle classe, per cui queto è in generale una riduzione della dimensionalitàpiuttosto forte, ed ha senso soltanto in un ambito multiclasse.

Questo è implementato nel metodo transform. La dimensionalità desiderata può essere impsotata selezionando il parametro n_components. Questo parametro non ha alcuna influenza sui metodi fit e predict.

## Formulazione matematica

Sia LDA che QDA può essere derivata da dei semplici modelli probabilistici, atti a modellare la distribuzione condizionale dei dati $P(X|y=k)$ per ogni classe $k$. Le predizioni possono quindi essere ottenute usando la regola di Bayes, per ogni campione di training $x \in \mathbb{R}^d$:

$$
P(y=k|x) = \frac{P(x|y=k)P(y=k)}{P(x)} = \frac{P(x|y=k)P(y=k)}{\sum{P(x|y=l)\cdot P(y=l)}_{l}}
$$

e scegliamo la classe $k$ che massimizza questa probabilità a posteriori.

Più nello specifico, per la LDA e la QDA, $P(x|y)$ è modellato come una distribuzione gaussiana multivariata, con densità:

$$
P(x|y=k) = \frac{1}{(2\pi)^{d/2}|\sum_{k}|^{1/2}} exp (-\frac{1}{2}(x-\mu_{k})^t\sum_{k}^{-1}(x-\mu_{k}))
$$

dove $d$ è il numero di feature.

https://scikit-learn.org/stable/modules/lda_qda.html