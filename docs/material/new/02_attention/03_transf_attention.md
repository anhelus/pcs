Before the introduction of the Transformer model, the use of attention for neural machine translation was implemented by RNN-based encoder-decoder architectures. The Transformer model revolutionized the implementation of attention by dispensing with recurrence and convolutions and, alternatively, relying solely on a self-attention mechanism. 

Introduction to the Transformer Attention
Thus far, you have familiarized yourself with using an attention mechanism in conjunction with an RNN-based encoder-decoder architecture. Two of the most popular models that implement attention in this manner have been those proposed by Bahdanau et al. (2014) and Luong et al. (2015). 

The Transformer architecture revolutionized the use of attention by dispensing with recurrence and convolutions, on which the formers had extensively relied. 

… the Transformer is the first transduction model relying entirely on self-attention to compute representations of its input and output without using sequence-aligned RNNs or convolution.

– Attention Is All You Need, 2017.

In their paper, “Attention Is All You Need,” Vaswani et al. (2017) explain that the Transformer model, alternatively, relies solely on the use of self-attention, where the representation of a sequence (or sentence) is computed by relating different words in the same sequence. 

Self-attention, sometimes called intra-attention, is an attention mechanism relating different positions of a single sequence in order to compute a representation of the sequence.

– Attention Is All You Need, 2017.

# L'encoder

L'encoder consiste di uno stack di $N=6$ identici layer, dove ogni layer è composto da due sottolayer::

1. il primo sublayer implementa un meccanismo di multi-head self-attention. Abbiamo visto che il multi-head mechanism implementa $h$ head che riceve una (differente) versione proiettata delle query, key, e value, ognuno per produrre $h$ output in parallelo che sono quindi usati per generare un risultato finale.
2. il secondo sublayer è un fully connected feed-forward network che consiste di due trasformazioni lineari con elle attivazioni di tipo ReLU:

$$
FFN(x) = ReLU(W_1 x + b_1) W_2 + b_2
$$

I sei layer del transformer dell'encoder del transformer applicano la stessa trasformazione linere aa tutte le parole nella sequenza di input, ma ogni layer sfrutta diversi pesi $(W_1, W_2)$ ed i bias $(b_1, b_2)$ parametri per farlo.

Inoltre, ognuno di questi due sublayer ha una connessione residuale che lo circonda.

Ogni sublayer è anche succeduta da un layer di normalizzazione, layernorm(.), che normlaizza la somma calcolata tra il sublayer di input, x,m e l'output generato dal sublayer stesso, sublayer(x):

$$
layernorm(x + sublaayer(x))
$$

Un'importante considerazione da tenere in mente è che l'architettura transfoemr non può intrinsiecamente catturare ogni ifnormazione sulle posizioni relative delle parlnella sequeznqa dal momento che non fa uso delle ricorrenze. Questa inforamzione deve essere ineiettata introducendo dei *positional encodings* all'embedding di input.

I vettori di positional encoding sono della stessa dimensione degli input embeddings e sono generati usando funzioni seno e coseno a diverse frequenze. Quindi, sono semplicemente sommate agli input embedding per iniettare l'informazione posizionale.

# Il decoder

Il decoder codnivide diverse similarità con l'encoder.

Il decoder è anche questo composto di uno stack di $N=6$ layer identici che sono composti di tre sublayer:

1. il primo sublayer riceve l'output precedente dello stack di decodifica, lo auenta con informazione posizionle, ed iomplementa su di esso la multi-head self-attention. Anche se l'encoder èp progettato epr trattare tutte le parole nella sequenza di input indipendentemtne dalla loro posizione lnella sstessa, il decoder viene modificato per fare attenzione soltanto alle parole precedenti. Quindi, la prediuzione per una parola alla posizione $i$ può dipendere solo dagli output consociuti dalle parole che vengono prima nella sequenza. Nel meccanismo di attenzione multi-head che implementa più funzioni singole di attenzione in maniera parallela questo viene ottenuto introducendo una maschera sui valori oprdotti dalla moltiplicazione scalare delle matrici $Q$ e $K$. Qeusta maschera viene implemettata sopprimendo i valori matriciali che sarebbero altrimenti corrispondenti a delle connessioni non consentite.
