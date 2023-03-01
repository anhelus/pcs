# 3.4 - Manipolazione dei DataFrame

## Visualizzazione dei DataFrame

Pandas ci offre un supporto nativo a Matplotlib per permettere la visualizzazione dei dati contenuti all'interno di un dataframe.

In tal senso, possiamo usare la funzione `plot()` su una serie o su un intero dataframe; ad esempio, potremmo plottare le età dei passeggeri:

```py
df['Age'].plot()
plt.show()
```

ottenendo il risultato mostrato in figura 1:

<figure markdown>
  ![plot_ages](./images/plot_ages.png)
  <figcaption>Figura 1 - Le età dei passeggeri nel dataset Titanic</figcaption>
</figure>

Possiamo anche fare il plot dell'intero `DataFrame`:

```py
df.plot()
plt.show()
```

che risulterà nella figura 2:

<figure markdown>
  ![plot_titanic](./images/plot_titanic.png)
  <figcaption>Figura 2 - Il dataset Titanic</figcaption>
</figure>

Ovviamente, è possibile usare Pandas anche per fare il plot di altri tipi di grafico, come ad esempio gli istogrammi. Per farlo, si usano le apposite sotto-funzioni di `plot`:

```py
df['Age'].plot.hist()
plt.show()
```

Il risultato è mostrato in figura 3.

<figure markdown>
  ![ages_hist](./images/hist_ages.png)
  <figcaption>Figura 3 - Esempio di istogramma calcolato a partire dalle età dei passeggeri</figcaption>
</figure>

!!!note "Pandas e Seaborn"
    Pandas si integra in maniera naturale anche con la libreria Seaborn, di cui tratteremo in una delle [prossime lezioni](../04_visualization/02_seaborn.md).

<!-- ## Drop, Fill -->

## Operazioni statistiche sui dataframe

Pandas ci mette a disposizione delle funzioni, simili a quelle offerte da NumPy, per calcolare delle statistiche per ciascuna delle colonne presenti in un DataFrame. Ad esempio, possiamo calcolare la media usando la funzione [`mean()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mean.html):

```py
>>> df.mean()
PassengerId    446.000000
Survived         0.383838
Pclass           2.308642
Age             29.699118
SibSp            0.523008
Parch            0.381594
Fare            32.204208
dtype: float64
```

Ovviamente, esistono funzioni anche per calcolare varianza ([`var()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.var.html)), mediana ([`median()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.median.html)), deviazione standard ([`std()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.std.html)), e via discorrendo.

Particolarmente interessante è la funzione `describe()`, che ci mosta tutte le statistiche più significative per ognuna delle feature considerate.

```py
>>> df.describe()
       PassengerId    Survived      Pclass         Age       SibSp       Parch        Fare
count   891.000000  891.000000  891.000000  714.000000  891.000000  891.000000  891.000000
mean    446.000000    0.383838    2.308642   29.699118    0.523008    0.381594   32.204208
std     257.353842    0.486592    0.836071   14.526497    1.102743    0.806057   49.693429
min       1.000000    0.000000    1.000000    0.420000    0.000000    0.000000    0.000000
25%     223.500000    0.000000    2.000000   20.125000    0.000000    0.000000    7.910400
50%     446.000000    0.000000    3.000000   28.000000    0.000000    0.000000   14.454200
75%     668.500000    1.000000    3.000000   38.000000    1.000000    0.000000   31.000000
max     891.000000    1.000000    3.000000   80.000000    8.000000    6.000000  512.329200
```

<!-- # TODO: apply, map, sample -->
