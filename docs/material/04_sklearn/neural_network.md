# Rete neurale

L'area delle reti nuerali è stata originariamente ispirata dall'obiettivo di modellare i sistemi neurali biologici, ma c'è stata successivamentre divergenza, ed è diventata una questione di ingegnerizzazione e di ottenere buoi risultati nei task di machine learning. Nonostante questo, iniziamo la discussione con una descrizione breve ed ad alto livello dei sistemi biologici che hanno ispirato buona parte di quest'area.

## MOtivazioni biologiche e connessioni

L'unità di calcolo base del cervello è chiamata *neurone*. Il sistema nervoso umano ha circa 86 miliardi di neuroni connessi tra loro mediante approssimativamente $10^14 - 10^15$ sinapsi. In figura 1, possiamo vedre un neurone biologico (a siunistra) ed un modello matematico di neurone (a destra).

TODO FIGURA 1

Ogni neurone riceve i segnali di ingresso dai suoi dendriti, e produce segnali di uscita lungo il suo singolo assione. L'assione si ramifica e si connette, mediante delle sinapsi, ai dendriti di altri neuroni. Nel modello computazionale di un neurone, i segnali che viaggiano lungo gli assoni (ad esempio, $x_0$) interagiscono in maniera moltiplicativa (ovvero, $w_0 x_0$) con le dendriti di altri neuroni sulla base della forza sinaptica a quella sinapsi (ad esempio, $w_0$). L'idea è che la forza sinaptica (i pesi $w$) siano in grado di essere apprese e controllino la forza di influenza (e la sua direzione: eccitatoria, con pesi positivi, o inibitoria, con pesi negativi) di un neurone rispetto all'altro. Nel modello base, i dendritri portano il segnale al corpo della cellula, dove sono sommati tra loro. Se la somma finale è oltre una certa soglia, il neurone può attivarsi, mandando un segnale lungo il suo assone. Nel dmodello cmputazionale, assumiamo che la temporizzazione dell'attivazione non conti, e che solo la frequenza delle attivazioni comunichi delle informaizoni. In base a questa interpetazioni, modelliamo il tasso di attivazione di un neurone con una funzione di attivazione $f$, che rappresenta la frequena dei picchi lungo l'assione.

Storicamente, una scelta comune per la ufnzione di attivazoine è la funzione sigmoidale $\sigma$, dal momento che prende un input a valori reali (la forza del segnale dopo la somma) e la comprime nel range tra $0$ ed $1$. In altre parole, ogni neurone effettua un prodotto tra gli input ed i suoi pesi, aggiunge i bias, ed applica la non linearità, nel caso di sigmoidale $\sigma(x) = \frac{1}{1+e^{-x}}$.

!!!note "Modello grossolano"
    Sottolineamo come questo modello di neurone biologico è molto grossolano. Nella realtà, esistono infatti motli tipi di neuroni, ognuno con diverse proprietà. I denditri effettuano dei calcoli non lineari molto complessi. Le sinapsi non sono solo un singolo peso, ma sono sistemi dinamici non  lineari complessi. Inoltre, la temporizzazione dell'attivazione è imporatnte, il che suggerisce che la nostra approssimazione non abbia valenza. 

## Il singolo neurone come classificatore lineare

La formulazione matematica della forward computation di un neurone è abbastanza semplice. Un neurone ha infatti la capacità di *piacere* (attivazione vicino ad uno) o meno (attivazione vicino a zero) certe regioni del suo spazio di ingresso. Quindi, con un'appropriata funzione di costo sull'output del neurone, possiamo modificare un singolo neurone in un classificatore lineare.

Ad esempio, possiamo interpretare il valore $\sigma (\sum_i w_i x_i + b)$ come la probabilità di una delle due classi di un problema binario $P (y_i = 1 | x_i; w)$. La probabilità dell'altra classe sarà $P(y_i = 0 | x_i; w) = 1 - P(y_i = 1 | x_i; w)$, dal momento che devono essere a sommma unitaria. Con questa interpretazione, possiamo formulare la cross-entropy loss, ed ottimizzarla ci porta ad un classificatore softmax binario (conosciuto anche come *regressore logistico*). Dal momento che la funzione sigmoidale è ristretta tra $0$ ed $1$, le predizioni di questo classificaote sono basate sul fatto che l'output del neurone sia maggiore o minore di $0.5$. Per quello che rioguarda la regolarizzazione, queste possono essere interpretate come *gradual forgetting*, dal momento che avrebbe l'effetto di portare tutti i pesi sinaptici $w$ verso zero dopo ogni aggiornamento del parametro.

https://cs231n.github.io/neural-networks-1/
