# 8.2 - Seaborn

Seaborn è una libreria che estende Matplotlib grazie a nuove funzionalità ed un'integrazione nativa con Pandas, libreria che tratteremo in una delle prossime lezioni.

In particolare, Seaborn offre una serie di strumenti già pronti per l'analisi statistica, offrendo un'interfaccia molto simile a quella di Matplotlib.

Vediamo qualche esempio.

## 8.2.1 - Relazioni all'interno di un dataset

Due dei metodi tradizionalmente utilizzati per mostrare le potenzialità di Seaborn sono `load_dataset()`, che ci permette di caricare uno dei dataset presenti con la libreria, e `relplot()`, funzione che ci mostra la relazione tra i dati presenti nel dataset caricato con la `load_dataset()`.

Per prima cosa, quindi, carichiamo il dataset `tips`, che contiene una serie di dati inerenti le mance fornite dai clienti ad un locale.

```py
tips = sns.load_dataset('tips')
```

Iniziamo analizzando la struttura dei dati.

Vediamo che abbiamo una sorta di *tabella* nella quale:

* ogni riga è associata ad una specifica ordinazione;
* le colonne sono associate rispettivamente a conto (`total_bill`), mancia (`tip`), genere (`sex`), fumatore (smoker), giorno (`day`), orario (`time`) e numero di attendenti (`size`).

La struttura della tabella è quindi la seguente:

```py
   total_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4
```

Mediante la funzione `relplot()` possiamo ad esempio analizzare il rapporto tra conto e mancia al variare della giornata:

```py
sns.relplot(
    data=tips,
    x="total_bill", y="tip", col="day"
)
```

In particolare, metteremo sull'asse delle ascisse il valore totale del conto, su quello delle ordinate la mancia ricevuta, e genereremo un numero di plot pari ai valori assunti dal dataset nella colonna `day`, come mostrato nella seguente figura.

![relplot_1](./images/relplot_1.png)

Un altro esperimento è quello che vede valutare la differenza tra conto e mance pagati da uomini e donne. In questo caso, inoltre, andiamo ad aumentare la dimensione del punto in maniera direttamente proporzionale alla mancia percepita.

```py
sns.relplot(
    data=tips,
    x='total_bill', y='tip', col='sex', size='tip'
)
```

![relplot_2](./images/relplot_2.png)

## 8.2.2 - Stima di una distribuzione

Oltre all'analisi delle relazioni intercorrenti 

Di solito l'analisi statistica prevede della conoscenza a riguardo della distribuzione delle variabili nel nostro dataset. La funzione displot() permette di visualizzare le distribuzioni, per esempio usadno degli istrogrammi ed effettuando delle stime come quella basata sulla KDE:

sns.displot(data=tips, x="total_bill", col="time", kde=True)

## plot dati categorici

Esistono anche dei plot specializzati in seaborn ed orientati verso la visualizzazione di dati di tipo categorico. Questi possono essere aceduti mediante la funzione catplot(). Questi plot offrono diversi livelli di granularità. Al livello più fine, potremmo voler vedere ogni osservazione disegnando uno "swarm" plot, ovvero uno scatter plot che modfica la posizione dei punti lungo l'asse delle categorie in modo che non si sovrappongano.

sns.catplot(data=tips, kind="swarm", x="day", y="total_bill", hue="smoker")

In alternativa, potremmo usare dei violin plot che sfruttano la KDE per rappresentare la distribuzione sottostante dei punti.

sns.catplot(data=tips, kind="violin", x="day", y="total_bill", hue="smoker", split=True)

### Esempio: Heatmap

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