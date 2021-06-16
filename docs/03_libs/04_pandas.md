# Introduzione a Pandas

Pandas è l'ultima delle librerie dell'ecosistema SciPy che tratteremo, ma ciò non toglie che è un pezzo *fondamentale* dell'intero framework, in quanto viene usata per la lettura ed elaborazione dei dati provenienti da sorgenti di vario tipo.

## Installazione e configurazione di Pandas

Al solito, provvediamo per prima cosa ad installare Pandas nel nostro ambiente di lavoro.

==="Pip" 
	```sh
	pip install pandas
	```
==="Pipenv"
	```sh
	pipenv install pandas
	```

Così come per le altre librerie (eccetto Jupyter), nel prosieguo presupporemo che Pandas sia importato nel nostro script (o, ancora meglio, nel nostro notebook):

```py
import pandas as pd
```

## I dati gestiti da Pandas

Pandas gestisce dati *tabulari*, ossia dello stesso tipo di quelli comunemente contenuti nei fogli di calcolo o nei database. Questi dati sono sicuramente tra i più diffusi ed utilizzati nell'ambito dell'analisi dati, se si escludono le immagini; per modellarli, Pandas ci mette a disposizione un'apposita struttura denominata `DataFrame`.

Un `DataFrame` altro non è se non una *struttura dati* di tipo bidimensionale, adatta a memorizzare dati di ogni tipo, inclusi stringhe, interi, float, ed altro. I dati sono organizzati in righe (*rows*) e colonne (*columns*), in maniera concettualmente analoga ad un foglio di calcolo o database; tuttavia, è importante sottolinare come, per convenzione, le singole righe rappresentino i *campioni* del dataset, mentre le singole colonne siano associate ai valori assunti dalle *feature* per ciascun campione.

## Il primo `DataFrame`

Facciamo un esempio. Scarichiamo il [Titanic Dataset](../../datasets/titanic.zip), e scompattiamo l'archivio. Al suo interno, troveremo tre file, ovvero *gender_submission.csv*, *test.csv* e *train.csv*. Per gli scopi di questa lezione, ci concentreremo soltanto sull'ultimo.

Spostiamolo per prima cosa all'interno della nostra cartella di lavoro. A quel punto, usiamo questo codice per caricarlo all'interno di un `DataFrame`:

```py
df = pd.read_csv('train.csv')
```

Usiamo il metodo `head()` per mostrare a schermo le prime cinque righe del DataFrame.

```py
>>> df.head()
   PassengerId  Survived  Pclass                                               Name     Sex   Age  SibSp  Parch            Ticket     Fare Cabin Embarked
0            1         0       3                            Braund, Mr. Owen Harris    male  22.0      1      0         A/5 21171   7.2500   NaN        S
1            2         1       1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1      0          PC 17599  71.2833   C85        C
2            3         1       3                             Heikkinen, Miss. Laina  female  26.0      0      0  STON/O2. 3101282   7.9250   NaN        S
3            4         1       1       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1      0            113803  53.1000  C123        S
4            5         0       3                           Allen, Mr. William Henry    male  35.0      0      0            373450   8.0500   NaN        S
```

Vediamo poi i tipi di ciascuna delle colonne.

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

### Le Series

Ogni colonna in un dataframe è chiamata Series.

Possiamo creare anche una Series da zero.


ages = pd.Series([22, 35, 58], name="Age")

## Come scrivere e leggere dati tabulari?

pandas sopporta l'integrazione con molti formati file o sorgenti dati. Importare i dati da ciascuna di queste sorgenti è fornita da una funzione con il prefisso read_*. In modo simile, i metodi to_* sono usato per memorizzare i dati.

Ad esempio, se vogliamo leggere un file csv:

titanic = pd.read_csv('data/titanic.csv')

pandas fornisce la funzione read_csv() per leggere i dati memorizzati in un file csv in un DataFrame. 

Vediamo le prime cinque righe di questo dataframe:

titanic.head()

## Selezionare un sottoinsiemi di dati

Per conoscere le dimensioni del dataframew, usiamo la funzione shape. QUesta ci restituisce il numero di righe (campioni) e le colonne le feature.

Volendo, possiamo selezionare solo alcune parti del nostro dataframe. Ad esempio, possiamo selezionare soltanto alcune colonne.

age_sex = titanic[["Age", "Sex"]]

In caso si voglia filtrare per righe, invece, si possono suare delel espressioni logiche. Ad esempio, selezioniamo tutto i dati di quelli superiori a 35 anni ed inferiori a 45.

<!-- TODO, mettere l'altra condizione -->

above_35 = titanic[titanic["Age"] > 35]

## plottare dati in Pandas

Per plottare i dati in Pandas, possiamo usare la funzione plot().

<!-- TODO plot su titanic -->
titanic[COLONNA].plot()

## Creare nuove colonne

Per creare nuove colonne:

dataframe['nome_nuova_colonna'] = dataframe['vecchia_colonna'] *  qualcosa

## statistiche

funzioni, come mean(), median()

la più interessante è describe, che ci restituisce tutte le statistiche che ci interessano

titanic.groupby("Sex")["Age"].mean()

## combinazione dati

usare la funzione concat