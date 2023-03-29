# Esercitazione 4 - Visualizzazione dei dati in Python (Soluzioni)

!!!tip "Soluzioni"
    L'implementazione delle soluzioni è disponibile [questo notebook](https://github.com/anhelus/pcs-exercises/blob/master/01_libs/04_numpy_exercises.ipynb).

## Esercizio 4.1

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
