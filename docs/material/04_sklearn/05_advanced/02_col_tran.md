# 4.5.2 - Preprocessing sui dataframe

Abbiamo visto come i dataset non siano sempre uniformi: infatti, alle volte, avremo feature numeriche accompagnate da altre feature di tipo categorico. Ciò comporta la necessità di applicare trasformazioni *ad hoc*, ciascuna tarata su una specifica feature.

Per farlo, un'idea potrebbe essere quella di applicare un trasformer su ogni feature che abbia bisogno di essere trasformata. Tuttavia, appare evidente come questo modo di procedere sia estremamente inefficiente nel momento in cui abbiamo a che fare con un numero di feature più o meno alto. Per aiutarci in questo compito, quindi, Scikit-Learn ci mette a disposizione un particolare trasformer, chiamato [`ColumnTransformer()`](http://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html), che permette di semplificare il processing di un numero arbitrario di feature.

## Un esempio

Immaginiamo di dover trasformare tutte le colonne del dataset tips, standardizzando quelle numeriche, e codificando quelle categoriche. Per farlo, possiamo usare un `ColumnTransformer()` come segue:

```py
import seaborn as sns
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OrdinalEncoder, StandardScaler

tips = sns.load_dataset('tips')
ct = ColumnTransformer(
    [('scaler', StandardScaler(), ['total_bill', 'tip']),
     ('encoder', OrdinalEncoder(), ['sex', 'smoker', 'day', 'time'])],
    remainder='passthrough'
)

ct.fit(tips)
ct.transform(tips)
```

!!!warning "Nota"
    Se non fosse chiaro, i `ColumnTransformer()` lavorano sui dataframe.

## `ColumnTransformer` e `Pipeline`

Possiamo anche combinare i `ColumnTransformer()` con le `Pipeline()`, usando al posto di un singolo transformer una pipeline di transformer. Ad esempio, se volessimo assegnare i dati mancanti usando un `SimpleImputer()` prima dello scaling, potremmo usare una pipeline da passare al transformer:

```py
from sklearn.impute import SimpleImputer

numerical_transformer = Pipeline(
    [('imputer', SimpleImputer()),
    ('scaler', StandardScaler())]
)

ct = ColumnTransformer(
    [('scaler', numerical_transformer, ['total_bill', 'tip']),
     ('encoder', OrdinalEncoder(), ['sex', 'smoker', 'day', 'time'])],
    remainder='passthrough'
)
```

!!!note "Nota"
    Ovviamente, anche un `ColumnTransformer()` può essere usato in una pipeline!
