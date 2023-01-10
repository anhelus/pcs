# E10 - Visualizzazione dei dati in Seaborn

## Esercizio E10.1

Visualizzare la distribuzione dell'età dei diversi passeggeri del Titanic in base al loro genere.

Visualizzare inoltre il rapporto tra età e numero di fratelli/sorelle/coniugi in base al genere del passeggero.

### Soluzione S10.1

Per prima cosa, leggiamo il dataframe:

```py
df = pd.read_csv('titanic.csv')
```

Per visualizzare la distribuzione dell'età dei diversi passeggeri del Titanic in base al loro genere usiamo un `displot()`:

```py
sns.displot(
    data=df,
    x='Age',
    col='Sex')
```

![distplot](./images/distplot.png){: .center}

Per visualizzare inoltre il rapporto tra età e numero di fratelli/sorelle/coniugi in base al genere del passeggero usiamo un `catplot()`:

```py
sns.catplot(
    data=df,
    kind='violin',
    x='SibSp',
    y='Age',
    hue='Sex',
    split=True)
```

![catplot](./images/catplot_tips.png){: .center}

## Esercizio E10.2

Effettuiamo un'*analisi esplorativa* del dataset Titanic. In particolare, sfruttiamo Pandas e Seaborn per:

* verificare la correlazione tra le feature che riteniamo rilevanti, visualizzandola a schermo mediante una heatmap;
* analizzare la distribuzione statistica delle feature di tipo categorico e numerico;
* valutare la descrizione statistica delle diverse feature;
* dedurre empiricamente l'esistenza di eventuali relazioni tra le diverse feature;
* isolare quattro diversi tipi di soggetti (maschi adulti, femmine adulte, maschi giovani e femmine giovani), ed effettuare le precedenti analisi in maniera separata su ciascuno dei gruppi.
