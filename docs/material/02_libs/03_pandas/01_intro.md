# 3.1 - Introduzione a Pandas

[Pandas](https://pandas.pydata.org/) viene usata per la lettura ed elaborazione dei dati provenienti da sorgenti di vario tipo, come ad esempio file CSV o Excel, ma anche file di testo e database. Vediamo quindi brevemente come usare la libreria, tenendo presente che ne approfondiremo il funzionamento anche durante le lezioni successive.

## Installazione e configurazione di Pandas

Al solito, il primo passo è sempre quello di installare la libreria nel nostro ambiente di lavoro:

```sh
pip install pandas
```

Possiamo quindi importare la libreria all'interno dei nostri script o notebook:

```py
import pandas as pd
```

## Pandas e la gestione dei dati

Pandas gestisce prevalentemente dati *strutturati* sotto forma *tabellare*, ossia simili a quelli comunemente contenuti all'interno dei fogli di calcolo o nei database. Questi dati sono sicuramente tra i più diffusi ed utilizzati nel contesto dell'analisi dei dati, ovviamente escludendo le immagini: in tal senso, per modellarli, Pandas ci mette a disposizione un'apposita struttura denominata [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html).

I dataframe sono quindi delle strutture atte a contenere dati di ogni tipo. Questi sono normalmente organizzati in righe e colonne, in maniera del tutto analoga a quella in cui sono organizzati i fogli di calcolo ed i database. Importante anche sottolineare come, per convenzione, le singole righe rappresentino i *campioni* del dataset, mentre le colonne siano associati ai valori assunti dalle diverse caratteristiche, o *feature*, di ciascun campione.

Facciamo un esempio usando il dataset Titanic, che è uno tra i più utilizzati a scopi di sperimentazione. Per prima cosa, generiamo un dataframe rappresentativo dei dati contenuti nel dataset, leggendo il file `titanic.csv`, che possiamo scaricare a [questo link](../../data/titanic.csv). Per leggere i dati, dovremo utilizzare il metodo [`read_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html), cui passeremo il percorso relativo del file:

```py
df = pd.read_csv('titanic.csv')
```

Usiamo il metodo [`head()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html) per mostrare a schermo le prime cinque righe del dataframe.

```py
>>> df.head()
```

```sh
   PassengerId  Survived  Pclass                                               Name     Sex   Age  SibSp  Parch            Ticket     Fare Cabin Embarked
0            1         0       3                            Braund, Mr. Owen Harris    male  22.0      1      0         A/5 21171   7.2500   NaN        S
1            2         1       1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1      0          PC 17599  71.2833   C85        C
2            3         1       3                             Heikkinen, Miss. Laina  female  26.0      0      0  STON/O2. 3101282   7.9250   NaN        S
3            4         1       1       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1      0            113803  53.1000  C123        S
4            5         0       3                           Allen, Mr. William Henry    male  35.0      0      0            373450   8.0500   NaN        S
```

Vediamo rapidamente che ad ogni passeggero sono associate delle feature, di cui possiamo inferire il tipo (lo verificheremo a breve):

| Feature | Descrizione | Tipo |
| ------- | ----------- | ---- |
| PassengerId | Identificativo univoco del passeggero. | Intero |
| Survived | Stabilisce se il passeggero è sopravvissuto. | Intero/booleano |
| Pclass | Rappresenta la classe del passeggero | Intero |
| Name | Nome completo del passeggero | Stringa |
| Sex | Genere del passeggero | Stringa |
| Age | Età del passeggero | Decimale |
| SibSp | Crasi di "Siblings/Spouses", rappresenta il numero di fratelli/sorelle/coniugi a bordo per ogni passeggero | Intero |
| Parch | Crasi di "Parents/Children", rappresenta il numero di genitori/figli a bordo per ogni passeggero | Intero |
| Ticket | Rappresenta l'identificativo per il ticket del passeggero. | Stringa |
| Tariffa | Rappresenta la tariffa pagata dal passeggero. | Decimale |
| Cabin | Rappresenta la cabina in cui allogiava il passeggero. | Stringa |
| Embarked | Rappresenta il punto di imbarco del passeggero. | Stringa |

Verifichiamo che le nostre ipotesi sul tipo di dato siano corrette; per farlo, possiamo usare la proprietà `dtypes` del dataframe:

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

Notiamo subito la presenza di tre tipi di colonna, ovvero `int64`, `float64` e `object`. Laddove i primi due sono autoesplicativi, merita una particolare menzione il tipo `object`, che viene associato automaticamente a tutte le stringhe.

!!!tip "Suggerimento"
	Normalmente, usare il tipo `object` comporta diversi problemi nella successiva fase di analisi dei dati. Potrebbe quindi essere una buona idea parametrizzare la funzione `read_csv()` mediante il parametro [`dtype`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html), che accetta un dizionario che specifica il tipo di una o più colonne. Ad esempio, se volessimo specificare che i nomi sono delle stringhe, potremmo usare il tipo `string`:

	> ```py
	  >>> types = {'Name': 'string'}
	  >>> df = pd.read_csv('train.csv', dtype=types)
	  >>> df.dtypes
	  # ...
	  Name            string
	  # ...
	  ```

Appare chiaro come il dataset ci illustri numerose proprietà per ogni passeggero imbarcato. Queste potranno quindi essere utilizzate per un'analisi approfondita della struttura dei dati sotto diversi aspetti e punti di vista; ne parleremo più estesamente nel seguito.
