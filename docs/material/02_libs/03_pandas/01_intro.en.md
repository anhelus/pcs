# 2.3.1 - Introduction to Pandas

!!!tip "Accompanying Notebook"
    For this lesson, there is an *accompanying notebook* available at [this link](https://github.com/anhelus/pcs-exercises/blob/master/01_libs/02_visualization/03_pandas.ipynb).

!!!tip "Accompanying Notebook"
    For this lesson, there is an *accompanying notebook* available at [this link](https://github.com/anhelus/pcs-exercises/blob/master/01_libs/02_visualization/03_pandas.ipynb).

!!!tip "Accompanying Notebook"
    For this lesson, there is an *accompanying notebook* available at [this link](https://github.com/anhelus/pcs-exercises/blob/master/01_libs/02_visualization/03_pandas.ipynb).

[Pandas](https://pandas.pydata.org/) is used for reading and processing data from various sources such as CSV or Excel files, as well as text files and databases. Let's briefly see how to use this library, keeping in mind that we will delve deeper into its workings in subsequent lessons.

## Installation and Configuration of Pandas

As usual, the first step is to install the library in our working environment:

```sh
pip install pandas
```

We can then import the library into our scripts or notebooks:

```py
import pandas as pd
```

## Pandas and Data Handling

Pandas primarily handles *structured* data in a *tabular* form, similar to what is commonly found in spreadsheets or databases. These types of data are among the most prevalent and widely used in data analysis, excluding images. To model such data, Pandas provides a specific structure called [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html).

Dataframes are structures designed to hold data of various types. They are typically organized into rows and columns, similar to how spreadsheets and databases are organized. It is important to note that, conventionally, each row represents a *sample* in the dataset, while columns are associated with the values of different characteristics or *features* for each sample.

Let's use the Titanic dataset as an example, which is one of the most commonly used datasets for experimentation. First, we generate a dataframe representing the data contained in the dataset by reading the `titanic.csv` file, which can be downloaded from [this link](../../data/titanic.csv). To read the data, we will use the [`read_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) method, passing the relative path of the file:

```py
df = pd.read_csv('titanic.csv')
```

We can use the [`head()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html) method to display the first five rows of the dataframe.

```py
>>> df.head()
```

```sh
   PassengerId  Survived  Pclass                                               Name     Sex   Age  SibSp  Parch            Ticket     Fare Cabin Embarked
0            1         0       3                            Braund, Mr. Owen Harris    male  22.0      1      0         A/5 21171   7.2500   NaN        S
1            2         1       1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1      0          PC 17599  71.2833   C85        C
2            3         1       

 3                             Heikkinen, Miss. Laina  female  26.0      0      0  STON/O2. 3101282   7.9250   NaN        S
3            4         1        1       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1      0            113803  53.1000  C123        S
4            5         0       3                           Allen, Mr. William Henry    male  35.0      0      0            373450   8.0500   NaN        S
```

We can quickly see that each passenger is associated with features, from which we can infer their type (we will verify this shortly):

| Feature | Description | Type |
| ------- | ----------- | ---- |
| PassengerId | Unique identifier of the passenger | Integer |
| Survived | Indicates if the passenger survived | Integer/Boolean |
| Pclass | Represents the passenger's class | Integer |
| Name | Full name of the passenger | String |
| Sex | Gender of the passenger | String |
| Age | Age of the passenger | Decimal |
| SibSp | Abbreviation for "Siblings/Spouses," represents the number of siblings/spouses aboard for each passenger | Integer |
| Parch | Abbreviation for "Parents/Children," represents the number of parents/children aboard for each passenger | Integer |
| Ticket | Represents the ticket identifier of the passenger | String |
| Fare | Represents the fare paid by the passenger | Decimal |
| Cabin | Represents the cabin where the passenger stayed | String |
| Embarked | Represents the point of embarkation for the passenger | String |

Let's verify that our assumptions about the data types are correct. We can do this by using the `dtypes` property of the dataframe:

```py
>>> df.dtypes
PassengerId      int64
Survived         int64
Pclass           int64
Name            object
Sex             object
Age            float64
SibSp            int64
Parch            int64
Ticket          object
Fare           float64
Cabin           object
Embarked        object
dtype: object
```

We immediately notice the presence of three column types: `int64`, `float64`, and `object`. The first two are self-explanatory, but it's worth mentioning the `object` type, which is automatically associated with all strings.

!!!tip "Tip"
    Using the `object` type often poses several issues in the subsequent data analysis phase. Therefore, it might be a good idea to parameterize the `read_csv()` function using the [`dtype`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) parameter, which accepts a dictionary specifying the type of one or more columns. For example, if we wanted to specify that names are strings, we could use the `string` type:

    > ```py
      >>> types = {'Name': 'string'}
      >>> df = pd.read_csv('train.csv', dtype=types)
      >>> df.dtypes
      # ...
      Name            string
      # ...
      ```

It is clear that the dataset provides numerous properties for each embarked passenger. These properties can be used for in-depth analysis of the data from different perspectives, which we will discuss more extensively later.
