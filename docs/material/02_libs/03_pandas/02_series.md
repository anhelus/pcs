# 2.3.2 - Le Series

## Le Series

Nella [lezione precedente](01_intro.md) abbiamo visto come ogni DataFrame sia in realtà composto da diverse colonne, ciascuna rappresentativa di una feature specifica. Nella pratica, Pandas ci offre un modo per estrarre singolarmente ciascuna di queste colonne mediante la classe [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html). Ad esempio, potremmo estrarre la serie relativa agli identificativi numerici dei passeggeri:

```py
names = df['Name']
names.head()

# Output restituito
0                              Braund, Mr. Owen Harris
1    Cumings, Mrs. John Bradley (Florence Briggs Th...
2                               Heikkinen, Miss. Laina
3         Futrelle, Mrs. Jacques Heath (Lily May Peel)
4                             Allen, Mr. William Henry
Name: Name, dtype: object
```

### Accesso agli elementi di una serie

Possiamo accedere ad un singolo elemento di una serie mediante una classica procedura di indicizzazione. Notiamo infatti come ogni campione all'interno della serie sia associato ad un indice numerico crescente il cui valore iniziale è pari a 0; pertanto, possiamo accedere all'$i$-mo elemento della serie richiamando l'$i-1$-mo indice, esattamente come accade per le liste o le sequenze.

```py
>>> names[0]
'Braund, Mr. Owen Harris'
```

!!!note "Nota"
   L'indicizzazione può essere anche usata per impostare il valore associato ad uno specifico indice della serie.

### Accesso agli elementi del dataframe

L'accesso agli elementi del dataframe può avvenire attraverso diverse modalità. In primo luogo, possiamo accedere allo specifico valore di una feature di un dato campione mediante il *chained indexing*:

```py
>>> df['Age'][1]
38
```

In alternativa, è possibile usare la funzione [`loc(row_idx, col)`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html) che, se chiamata su un oggetto di tipo `DataFrame`, ci permette di accedere al valore assunto dalla feature `col` per l'elemento in posizione `row_idx`:

```py
>>> df.loc[1, ('Age')]
38.0
```

La funzione `loc()` può operare anche su delle slice di dati:

```py
>>> df.loc[1:5, ('Age')]
1    38.0
2    26.0
3    35.0
4    35.0
5     NaN
```

o su insiemi di feature:

```py
>>> df.loc[1:5, ('Age', 'Sex')]
   Age     Sex
1  38.0  female
2  26.0  female
3  35.0  female
4  35.0    male
5   NaN    male
```

Sottolineamo che la funzione `loc()` opera sugli *indici di riga*. In questo caso, il nostro dataframe ha degli indici di riga interi, assegnati automaticamente in fase di lettura del dataframe. Nel caso decidessimo di usare una colonna del dataframe come indice, potremmo usare il metodo `set_index()`:

```py
df = df.set_index('Ticket')
```

Notiamo che, come al solito, le funzioni lavorano sul valore, e non sulla reference. Di conseguenza, se omettessimo l'assegnazione, `df` rimarrebbe invariato. Un modo per evitare di usare ogni volta l'operazione di assegnazione è quello di impostare il parametro `inplace` a `True`:

```py
df.set_index('Ticket', inplace=True)
```

In alternativa, possiamo decidere di impostare l'indice direttamente nel metodo `read_csv()` impostando il parametro `index_col`:

```py
df = pd.read_csv('titanic.csv', index_col='Ticket')
```

In questo caso, la funzione `loc()` dovrà essere utilizzata usando come parametri di lettura per righe i nuovi indici. Ad esempio:

```py
>>> df.loc['STON/O2. 3101282', 'Name']
'Heikkinen, Miss. Laina'
```

Oltre alla funzione `loc()` Pandas ci mette a disposizione la funzione `iloc()`, la quale ci offre la possibilità di selezionare un sottoinsieme di campion del dataframe mediante indici interi (da cui la `i`):

```py
>>> df.iloc[2:5, 2:4]
                  Pclass                                          Name
Ticket                                                                
STON/O2. 3101282       3                        Heikkinen, Miss. Laina
113803                 1  Futrelle, Mrs. Jacques Heath (Lily May Peel)
373450                 3                      Allen, Mr. William Henry
```

### Maschere booleane

Supponiamo di voler selezionare soltanto gli uomini maggiorenni presenti nel dataset del Titanic. Per farlo, possiamo usare un'istruzione che implementi delle logiche di tipo booleano:

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

Nella pratica, stiamo filtrando il dataset in base all'`AND` logico tra due condizioni:

* `df['Age'] > 18`: questa condizione genera una *maschera booleana* che è `True` soltanto se l'età per quel passeggero è maggiore di 18 anni;
* `df['Sex'] == 'male'`: questa condizione genera una maschera booleana che è vera soltanto se il genere del passeggero è maschile.

### La funzione `groupby`

Possiamo sfruttare la funzione [`groupby`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html) per raggruppare insiemi di dati (normalmente pertinenti a *categorie*).

Ad esempio, potremmo raggruppare i passeggeri per genere:

```py
>>> df.groupby(['Sex'])
```

Possiamo ovviamente estrarre delle statistiche a partire da questi raggruppamenti. Vediamo, ad esempio, l'età media dei passeggeri di sesso femminile e maschile:

```py
>>> df.groupby(['Sex'])['Age'].mean()
Sex
female    27.915709
male      30.726645
Name: Age, dtype: float64
```
