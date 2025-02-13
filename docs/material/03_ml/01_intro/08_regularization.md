# 3.1.7 - Regolarizzazione

## Il No Free Lunch Theorem

La teoria matematica alla base del machine learning afferma che un algoritmo sia in grado di generalizzare usando un dataset di addestramento di cardinalità finita. Questo sembra contraddire alcuni principi logici di base: infatti, l'intuizione ci porta a dire che per inferire una legge che descriva ogni campione in un insieme occorre avere delle informazioni su ogni membro dello stesso.

Il machine learning "aggira" questo problema usando delle regole di tipo probabilistico. In altre parole, un modello di machine learning individua regole che sono *probabilmente* corrette sulla *maggiro parte* dei membri dell'insieme di dati.

Tuttavia, questo non risolve realmente il problema. Infatti, il *no free lunch theorem* (NFL) afferma che, considerando tutte le distribuzioni possibili per la generazione dei dati, ogni algoritmo mostra lo stesso errore di generalizzazione. In altre parole, non esiste un algoritmo di machine learning universalmente migliore degli altri.

Fortunatamente, l'NFL è valido soltanto considerando *tutte* le possibili distribuzioni di dati. Nella realtà, possiamo progettare degli algoritmi che si comportino bene sul nostro specifico problema. Questo significa che l'obiettivo del machine learning non è quello di ricercare un algoritmo universale, ma di comprendere che tipi di distribuzioni sono rilevanti per caratterizzare il nostro problema, e quali algoritmi sono in grado di avere un errore di generalizzazione basso su questo tipo di distribuzioni generatrici.

## Regolarizzazione

Il NFL richiede di progettare un algoritmo di machine learning che lavori bene su un task specifico, creando un insieme di preferenze nell'algoritmo di apprendimendo allineate con il problema da risolvere.

Finora, l'unico modo che abbiamo discusso per modificare un algoritmo è stato quello di cambiarne la capacità modificandone gli iperparametri. Tuttavia, procedere esclusivamente in questo modo è semplicistico: infatti, il comportamento di un modello è influenzato anche dall'identità specifica delle funzioni contenute nello spazio di ricerca. Ad esempio, la regressione lineare ha uno spazio delle ipotesi che consiste nell'insieme delle funzioni lineari dei suoi ingressi. Queste funzioni lineari possono essere utili per problemi dove la relazione tra gli input e gli output è quasi lineare, ma sono inadatte a problemi non lineari. 

!!!tip "Problemi non lineari"
    Per fare un esempio, una regressione lineare non può caratterizzare il rapporto tra $x$ e $sen(x)$.
    
Ciò ci suggerisce che si possa controllare il comportamento del modello scegliendo il tipo di funzioni da includere nello spazio di ricerca. Un modo per farlo è dare una certa *preferenza* per una soluzione rispetto ad un'altra: ciò implica che entrambe le funzioni potranno essere utilizzate, ma una delle due avrà un peso maggiore rispetto all'altra, che sarà scelta soltanto se si adatta ai dati di training in maniera *significativamente* migliore della soluzione più "pesante".

Ad esempio, possiamo modificare il criterio di addestramento per la regressione lineare per fare in modo che includa il *decadimento dei pesi*. Per farlo, dobbiamo minimizzare una funzione $L(w)$ che comprende sia l'errore quadratico medio sui dati di training, sia un criterio che esprima una preferenza per i pesi che abbiano una norma $L^2$ minore. Nello specifico:

$$
L(w) = MSE_{train} + \lambda w^t w
$$

dove $\lambda$ è un valore scelto a priori che controlla la forza della nostra preferenza per pesi più piccoli. In pratica, se $\lambda \rightarrow 0$ non imponiamo alcuna preferenza di minimizzazione dei pesi, metnre se $\lambda \rightarrow 1$ i pesi $w$ devono diventare piccoli. Minimizzare $L(w)$ fa in modo che i pesi scelti siano un compromesso tra il fitting dei dati di training ed il loro valore assoluto; in altri termini, avremo soluzioni a pendenza inferiore, o che danno peso ad un numero minore dif eature.

In generale, ad un modello che apprende una funzione $f(x; \theta)$ viene *regolarizzato* mediante una funzione di penalità aggiunta alla funzione di costo. Nel caso del decadimento dei pesi, la funzione di regolarizzazione è data da $\Omega(w) = w^T w$.

Esprimere una "preferenza" per una funzione rispetto ad un'altra permette quindi di controllare la capacità del modello includendo o escludendo membri dallo spazio delle ipotesi. In altre parole, includere una funzione dallo spazio delle ipotesi, escludendone un'altra, significa esprimere una preferenza infinitamente forte per la prima. Nell'esempio del decadimento dei pesi, abbiamo esplicitamente espresso la nostra preferenza per funzioni lineari con pesi piccoli; tuttavia, esistono molti altri modi per esprimere preferenze per diverse soluzioni; insieme, questi approcci sono conosciuti come **regolarizzazioni**, ovvero tutte quelle modifiche fatte ad un algoritmo di learning intese a ridurre l'errore di generalizzazione preservando quello di training. In tal senso, è opportuno seguire i dettami del NFL, andando a scegliere una forma di regolarizzazione *specifica* per il nostro problema, e che quindi si adatti a modello e dati analizzati.
