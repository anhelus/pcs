# 2.3.2 - Series

## Series

In the [previous lesson](01_intro.md), we saw that each DataFrame is composed of different columns, each representing a specific feature. In practice, Pandas offers a way to extract each of these columns individually using the [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html) class. For example, we can extract the series related to the numeric passenger IDs:

```py
names = df['Name']
names.head()

# Output
0                              Braund, Mr. Owen Harris
1    Cumings, Mrs. John Bradley (Florence Briggs Th...
2                               Heikkinen, Miss. Laina
3         Futrelle, Mrs. Jacques Heath (Lily May Peel)
4                             Allen, Mr. William Henry
Name: Name, dtype: object
```

### Accessing elements of a series

We can access a single element of a series using indexing. Each sample within the series is associated with an increasing numerical index starting from 0. Therefore, we can access the $i$-th element of the series by referring to the $i-1$ index, similar to accessing elements in lists or sequences.

```py
>>> names[0]
'Braund, Mr. Owen Harris'
```

!!!note "Note"
    Indexing can also be used to set the value associated with a specific index of the series.

### Accessing elements of the dataframe

Accessing elements of the dataframe can be done in different ways. First, we can access the specific value of a feature for a given sample using *chained indexing*:

```py
>>> df['Age'][1]
38
```

Alternatively, we can use the [`loc(row_idx, col)`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html) function. When called on a `DataFrame` object, it allows us to access the value of the `col` feature for the element at position `row_idx`:

```py
>>> df.loc[1, 'Age']
38.0
```

The `loc()` function can also operate on data slices:

```py
>>> df.loc[1:5, 'Age']
1    38.0
2    26.0
3    35.0
4    35.0
5     NaN
```

or on sets of features:

```py
>>> df.loc[1:5, ['Age', 'Sex']]
   Age     Sex
1  38.0  female
2  26.0  female
3  35.0  female
4  35.0    male
5   NaN    male
```

It's important to note that the `loc()` function operates on *row indices*. In this case, our dataframe has integer row indices assigned automatically during the dataframe's creation. If we decide to use a column of the dataframe as an index, we can use the `set_index()` method:

```py
df = df.set_index('Ticket')
```

Note that functions operate on the value, not the reference. Therefore, if we omit the assignment, `df` remains unchanged. To avoid using the assignment operation every time, we can set the `inplace` parameter to `True`:

```py
df.set_index('Ticket', inplace=True)
```

Alternatively, we can directly set the index in the `read_csv()` method by setting the `index_col` parameter:

```py
df = pd.read_csv('titanic.csv', index_col='Ticket')
```

In this case, the `loc()` function should be used by providing the new row indices as read parameters

. For example:

```py
>>> df.loc['STON/O2. 3101282', 'Name']
'Heikkinen, Miss. Laina'
```

In addition to the `loc()` function, Pandas provides the `iloc()` function, which allows us to select a subset of dataframe samples using integer indices (`i` in `iloc()` stands for integer):

```py
>>> df.iloc[2:5, 2:4]
                  Pclass                                          Name
Ticket                                                                
STON/O2. 3101282       3                        Heikkinen, Miss. Laina
113803                 1  Futrelle, Mrs. Jacques Heath (Lily May Peel)
373450                 3                      Allen, Mr. William Henry
```

### Boolean masks

Suppose we want to select only adult males from the Titanic dataset. We can use a boolean logic statement to achieve this:

```py
>>> men = df[(df['Age'] > 18) & (df['Sex'] == 'male')]
>>> men.head()
    PassengerId  Survived  Pclass                            Name   Sex   Age
0             1         0       3         Braund, Mr. Owen Harris  male  22.0   
4             5         0       3        Allen, Mr. William Henry  male  35.0   
6             7         0       1         McCarthy, Mr. Timothy J  male  54.0   
12           13         0       3  Saundercock, Mr. William Henry  male  20.0   
13           14         0       3     Andersson, Mr. Anders Johan  male  39.0   
```

In practice, we are filtering the dataset based on the logical `AND` between two conditions:

* `df['Age'] > 18`: this condition generates a *boolean mask* that is `True` only if the age for that passenger is greater than 18 years.
* `df['Sex'] == 'male'`: this condition generates a boolean mask that is true only if the passenger's gender is male.

### The `groupby` function

We can use the [`groupby`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html) function to group sets of data that are usually relevant to *categories*.

For example, we can group passengers by gender:

```py
>>> df.groupby(['Sex'])
```

We can also extract statistics from these groupings. Let's see the average age of female and male passengers:

```py
>>> df.groupby(['Sex'])['Age'].mean()
Sex
female    27.915709
male      30.726645
Name: Age, dtype: float64
```