# 5.2.5 - Variational autoencoder

Gli standard ed i variational autoencoder apprendono a rappresentare l'input in una forma compressa chiamata latent space o bottleneck. Quindi, lo spazio latente formato dopo l'addestramento del modello non è necessariamente continuo e, in effetti, potrebbe non essere facile da interpolare.

Ad esempio, questo è quello che un variational autoencoder apprenderebbe dall'input:

FOTO: IMMAGINE A SINISTRA CON ATTRIBUTI SIMLE; SKIN TONE; GENDER, BEARD, GLASSES, HAIR COLOR

Anche se questi attributi spiegano l'immagine e possoono essere usati per ricostruire l'immagine dallo spazio latente, non permettono agli attributi latenti di essere espressi in maniera probabilistica

I vairational autonecoder si occupano di spe ific argomenti, ed esprimono i loro attributi latenti come una distribuzione di probabilità, il che porta alla fomrazione di uno spazio continuo latente che può essere facilmente campionato ed interpolato.

Quando viene dato lo stesso input, un variational autoencoder costruirà gli attributi latenti nel seguente modo:



Gli attributi latenti saranno quindi campionati dalla distribuzione latente così formata ed inviati al decoder, ricostruendo l'input.

il motivo per cui gli attributi latenti possono essere espressi come una distribuzione di probabilità può essere facilmente compreso mediante espressioni di tipo statistico.

IOn tal senso, proviamo ad identificare le caratteristiche del vettore latente $z$ che ricostruisce l'output dato un certo input.- In pratica, vogliamo studiare le carateristriche del vettore latente dato un certo output $x[p(z|x)]$.

Anche se una stima esatta della distribuzione può essere molto costosa dal punto di vista analitico, un'opzione molto più semplice da seguire è quella di costruire un modello parametrizzato che psosa stimare la distribuzione per noi. Possiamo farlo minimizzando la divergenza KL tra la distribuzione originale e la nostra distribuzione parametrizzata.

Esprimendo la distribuzione parmaetrizzata come $q$, possiamo inferire gli attributi latenti usati nella ricostruzione dell'immagine.

Assumendo che la distribuzione a priori $z$ sia un modello gaussiano multivariato, possiamo costruire una distribuzione parametrizzata come una contentente due parametri, la media e la varianza. La corrispondente distribuzione viene quindi campionata ed inviata al decoder, che quindi procedere a ricostruire l'input dai punti campionati.

Tuttavia, nonostante questo appaia essere semplice in teoria, diventa impossibile da implementare poer che la backpropagation non può essere definita per un processo di campionamento casuale effettuato prima di inviare i dati al decoder. Di conseguenza, usiamo un trucco chiamato *reparametrization* - un modo per bipassare il processo di campionamento fatto dalla rete neurale.

Di che si tratta? Nella reparametrization, campioniamo casualmente un valore $\epsilon$ da una gaussian unitaria, e quindi lo scaliamo per la varianza della distribuione latente $\sigma$ e lo shiftiamo per la media $\mu$ dlela stessa.

Adesso, abbiamo lasciato dietro il processo di campionamento come qualcosa fatto al di fuori della pipeline di backpropagation, ed il valore dcampionato $\epsilon$ funziona come un altro input al modello, che viene inviato al bottleneck.

Una vista sotto forma di diagramma è mostrata in figura.

TODO: REPARAMETRIZATION

Per addestrare un VAR, usiamo due funzioni di costo, ovvero quella di ricostruzione e la divergenza KL.

La loss di reconstruction permette alla distribuzione di descrivere in maneir corretta l'input, focalizzandoci soltnanto sulla minimizzazione dell'errore di ricostruzione. Di conseguenza, la rete apprende delle distribuzioni molto strette. La divergenza KL fa in modo che ciò non accada, e prova a fare in modo che la distribuzione sia più vicina ad una gaussiana a media nulla e varianza unitaria.

La loss complessiva può essere espressa come:

$$
L = |x - \hat{x}|+\beta \sum_i KL(q_j(z|x)\|N(0,1))
$$

dove $N$ indica la distribuzione normale a media nulla e varianza unitaria, e $\beta$ è un certo fattore di peswo.

L'uso primario dei variational autoencoder può essere visto nei modelli generativi.

Campionare dalla distribuzione latente addestrata ed inviare i risultati al decoder può condurre ai dati generati in un autoencoder.
