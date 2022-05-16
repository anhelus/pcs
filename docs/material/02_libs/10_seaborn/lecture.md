# 10 - Seaborn

*Seaborn* è una libreria che estende [Matplotlib](../08_matplotlib/lecture.md) aggiungendone diverse funzionalità, tutte nell'ottica della data analysis, e sulla scia di quello che abbiamo presentato in Pandas nella lezione precedente. Ciò permette quindi di mantenere un'interfaccia molto simile a quella di Matplotlib, estendendone al contempo le possibilità. Vediamo qualche esempio.

## 10.1 - Installazione della libreria

Come in ogni altro caso, partiamo dall'installazione della libreria:

```sh
pip install seaborn
```

Una volta installata, potremo importarla utilizzando un alias:

```py
import seaborn as sns
```

## 10.1 - Lettura dei dati

Abbiamo detto che Seaborn è utile specialmente nel momento in cui si vogliono valutare visiamente le relazioni che intercorrono tra diverse feature presenti all'interno di un dataset.

In tal senso, proviamo innanzitutto a caricare un insieme di dati, affidandoci al metodo `load_dataset()`, che estrae uno dei dataset già presenti nella libreria. Ad esempio:

```py
tips = load_dataset('tips')
```

!!!note "I dataset"
    L'elenco dei dataset supportati da Seaborn è presente a [questo indirizzo](https://github.com/mwaskom/seaborn-data).

Ispezionando il tipo di `tips` possiamo scoprire che si tratta di un dataframe; di conseguenza, possiamo esplorarne liberamente la struttura utilizzando Pandas. In particolare, vediamo che questi sono organizzati secondo la seguente tabella:

```sh
  total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4
```

La struttura della tabella è la seguente:

* ogni riga è associata ad una specifica ordinazione;
* le colonne sono associate rispettivamente a conto (`total_bill`), mancia (`tip`), genere (`sex`), fumatore (smoker), giorno (`day`), orario (`time`) e numero di attendenti (`size`).

### 10.1.1 - Visualizzare le relazioni tra dati

Seaborn ci offre la funzione `relplot()` che ci permette di analizzare velocemente diversi aspetti inclusi del dataset. Ad esempio, potremmo vedere come cambiano contro e mancia al variare della giornata:

```py
sns.relplot(
    data=tips,
    x='total_bill',
    y='tip',
    col='day'
)
```

Notiamo che abbiamo passato al parametro `data` il valore `tips`, indicando quindi la sorgente dei dati. Metteremo poi sull'asse delle ascisse il conto totale, mentre su quello delle ascisse la mancia ricevuta. In ultimo, il parametro `col` ci permette di generare tanti grafici quanti sono i diversi valori presenti nella tabella `day`, ognuno dei quali rappresenterà ovviamente l'andamento dei conti e delle mance per quello specifico giorno.

![relplot_1](./images/relplot_1.png){: .center}

Un altro esperimento è quello che vede valutare la differenza tra conto e mance pagati da uomini e donne. In questo caso, inoltre, andiamo ad aumentare la dimensione del punto in maniera direttamente proporzionale alla mancia percepita.

```py
sns.relplot(
    data=tips,
    x='total_bill',
    y='tip',
    col='sex',
    size='tip')
```

![relplot_2](./images/relplot_2.png){: .center}

Una funzione simile alla `relplot()` è la `lmplot()`, che permette anche di mostrare un'approssimazione ai minimi quadrati.

## 10.2 - Analisi della distribuzione dati

Possiamo anche effettuare un'analisi della distribuzione delle variabili all'interno del nostro dataset. In tal senso, la funzione `displot()` ci permette di vedere come si vanno a distribuire i dati in base a determinate condizioni mediante l'uso di un istogramma.

Ad esempio, potremmo visualizzare la distribuzione dei clienti in base al loro genere ed al momento della giornata in cui effettuano la consumazione:

```py
sns.displot(
    data=tips,
    x='sex',
    col='time')
```

![distplot_tips](./images/distplot_tips.png)

## 10.3 - plot dati categorici

TODO: da qui

Esistono anche dei plot specializzati in seaborn ed orientati verso la visualizzazione di dati di tipo categorico. Questi possono essere aceduti mediante la funzione catplot(). Questi plot offrono diversi livelli di granularità. Al livello più fine, potremmo voler vedere ogni osservazione disegnando uno "swarm" plot, ovvero uno scatter plot che modfica la posizione dei punti lungo l'asse delle categorie in modo che non si sovrappongano.

sns.catplot(data=tips, kind="swarm", x="day", y="total_bill", hue="smoker")

In alternativa, potremmo usare dei violin plot che sfruttano la KDE per rappresentare la distribuzione sottostante dei punti.

sns.catplot(data=tips, kind="violin", x="day", y="total_bill", hue="smoker", split=True)

## 10.4 - Esempio: Heatmap

La sintassi usata da Seaborn è molto simile a quella usata da Matplotlib, con qualche piccola ed ovvia differenza. 

Una funzione molto utile è quella che ci permette di visualizzare le *heatmap*, che ci permettono di visualizzare rapidamente i valori in diversi tipi di matrici, come ad esempio quelle di correlazione (o, come vedremo più avanti, quelle di confusione). Questa funzione, quasi "banalmente", è chiamata `heatmap()`, e richiede almeno un parametro in ingresso, rappresentativo della matrice da cui sarà estratta la figura:

```py
a = rng.integers(low=0, high=100, size=(20, 20))
coeff = np.corrcoef(a)
fig, ax = plt.subplots()
sns.heatmap(corr)
plt.show()
```

Il risultato che otterremo sarà simile a questo:

![heatmap](./images/heatmap.png){: .center}
