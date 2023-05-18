# 2.3.4 - DataFrame Manipulation

## DataFrame Visualization

Pandas provides native support for Matplotlib to visualize the data contained in a DataFrame.

In this regard, we can use the `plot()` function on a series or an entire DataFrame. For example, we can plot the ages of the passengers:

```py
df['Age'].plot()
plt.show()
```

This will produce the result shown in figure 1:

<figure markdown>
  ![plot_ages](./images/plot_ages.png)
  <figcaption>Figure 1 - Ages of the passengers in the Titanic dataset</figcaption>
</figure>

We can also plot the entire `DataFrame`:

```py
df.plot()
plt.show()
```

This will result in figure 2:

<figure markdown>
  ![plot_titanic](./images/plot_titanic.png)
  <figcaption>Figure 2 - The Titanic dataset (in a plot)</figcaption>
</figure>

Of course, we can also use Pandas to plot other types of charts, such as histograms. To do this, we use the appropriate sub-functions of `plot`:

```py
df['Age'].plot.hist()
plt.show()
```

The result is shown in figure 3.

<figure markdown>
  ![ages_hist](./images/hist_ages.png)
  <figcaption>Figure 3 - Histogram of the ages of the passengers</figcaption>
</figure>

!!!note "Pandas and Seaborn"
    Pandas integrates naturally with the Seaborn library, which we will cover in one of the [upcoming lessons](../04_visualization/02_seaborn.md).

## Handling Missing Values

Anyone who has tried at least once to perform a data acquisition campaign knows well that it is (almost) never a straightforward procedure. For example, a sensor failure could result in the loss of a certain set of data for a period of time, or a user of our system could omit their age, which would then not be included in the final dataset.

These events put us in a "sticky" situation related to the management of datasets that contain one or more *missing values*. For example, let's take the first six rows of the Titanic dataset:

```sh
   PassengerId  Survived  Pclass                                               Name     Sex   Age  SibSp  Parch            Ticket     Fare Cabin Embarked
0            1         0       3                            Braund, Mr. Owen Harris    male  22.0      1      0         A/5 21171   7.2500   NaN        S
1            2         1       1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1      0          PC 17599  71.2833   C85        C
2            3         1       3                             Heikkinen, Miss. Laina  female  26.0      0      0  STON/O2. 3101282   7.9250   NaN        S
3            4         1       1       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1      0            113803  53.1000  C123        S
4            5         0       3                           Allen, Mr. William Henry    male  35.0      0      0            373450   8.0500   NaN        S
5            6         0       3                                   Moran, Mr. James    male  

.
