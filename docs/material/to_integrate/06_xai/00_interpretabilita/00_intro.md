# Modelli interpretabili

Il modo più semplice per ottener el'interpretabilità è usare solo un sottoinsieme di algoritmi che creano modelli interpretabili. La regressione lineare e logistica, oltre che gli alberi decisionali,. sono modelli interpretabili comunemente utilizzati.

Vediamone alcuni.

Un modello è lineare se la relazione tra le feature ed il target è modellata linearmente. Un modello con il vincolo della monotonicità assicura che la relaizone tra una fetaure e l'oibiettivo vada sempre nelal stessa direzione lungo l'intero range delle feature: in pratica, un aumento nel valore delle feature fa sempre aumentare (o diminuire) il valore di uscita, mentre un decremento fa sempre diminuire (o aumentare) il valore di uscita. La monotonictà è+ utile per l'interpetazione di un modello perché rende più semplice comprendere una relazione. Alcuini modelli possono automaticamente includere interazioni tra le feature per predire l'uscita obiettivo. POssiamo includere delle interazioni in qualsiasi tipo di modello creando manualmente delle *interaction features*. Le interazioni possono migliorare le perofrmance predittive, ma troppe interazioni, o interazioni troppo complesse, possono pregiudicare l'interpretabilità. Alcuni modelli gestiscono solo la regressione, altri solo laa classificazione,ed altri entrmabi.

| Algoritmo | Linearità | Monotonicità | Interazioni | Task |
| --------- | --------- | ------------ | ----------- | ---- |
| Regressione lineare | Sì | Sì | No | R |
| Regressione logistica | No | Sì | No | C |
| Alberi decisionali | No | Alcuni | Sì | C, R |
| RuleFit | Sì | No | Sì | C, R |
| Naive Bayes | No | Sì | No | C |
| k-NN | No | No | No | C, R |

Potremmo notare che sia la regressione lineare sia il naive bayes permettono spiegazioni lineari., Tuttavia, ciò è vero soltanto per il *logaritmo* dell'obiettivo: aumentare una feature di un punto aumenta il logaritmo della propabilità dell'obiettivo di un certo quantitativo a pattto che le altre feature rimangano le stesse.

# Regressione lineare

Un modello di regressione lineare predice l'obiettivo come somma pesata delle feature in ingresso. La linearità della relazione appresa rende facile l'interpretaizone. I modelli di regressione lineare sono stati a lungo usati dagli statitstici, ionfomratici, e in generale da chiunque debba risolvere problemi quantiativi.

I modelli lineari possono essere usati per modellare la dipendenza di un target di regressione $y$ da delle feature $x$. Le relazioni apprese sono lineari, e possono essere scritte per una singola istanza $I$ come segue:

$$
y = \beta_0 + \beta_1 x_1 + \ldots + \beta_p x_p + \epsilon
$$
https://christophm.github.io/interpretable-ml-book/limo.html