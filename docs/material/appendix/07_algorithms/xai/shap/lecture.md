# XAI con gli Shapley values

Gli Shapley values sono un approccio molto utiizzato per la teoria dei giochi coperativa che ha delle proprietà affascinati. 

## Spiegare un modello di regresisone lineare

Prima di usare i valori di Shapley per spiegare dei modelli complessi, è utile comprendere come funzioanno per dei modelli semplici. Uno dei tipi più semplice di modello è quello di regressione lineare. Usiamo il California housing dataset. Questo è fatto di 20.640 isolati di case in California nel 1990, con il nostro obiettivo che è quello di predire il logaritmo naturale del prezzo emediano di una casa a partire da otto diverse feature:

* MedInc: income medio in un isolato
* HouseAge età media delle case in un isolato
* AveRooms: numero medio di camere per ciascuna proprietà
* AveBedrms: numero medio di camere da letto per proprietà
* Population: popolazione dell'isolato
* AveOccup: numero medio di membri delle proprietà
* Latitude: latitudine dell'isolato
* Longitude: longitudine dell'isolato

```py
import pandas as pd
import shap
import sklearn

X, y = shap.datasets.california(n_points=1000)

X100 = shap.utils.sample(X, 100)

model = sklearn.linear_model.LinearRegression()
model.fit(X, y)
```

## Esame dei coefficienti del modello

Il modo più comune di comprendere un modello lineare è quello di esaminare i coefficienti appresi per ciascuna feature. Questi coefficienti ci indicano quanto dell'output del modello cambia quando cambiamo ciascuna delle feature dell'input.

```py
print('Coefficienti del modello: \n')
for i in range(X.shape[1]):
    print(X.columns[i], '=', model.coef_[i].round(5))
```

I coefficienti ci indicano cosa succede quando cambiamo il valore di uan feature di input, tuttavia da soli non sono un buon modo per misurare l'importanza complessiva di una feature. Questo avviene peché il valore di ogni coefficiente dipende dalla scala delle feature di input. Se per esempio dovessimo misurare l'età di una casa in minuti piuttosto che anni, il coefficiente per lo HouseAge dioventerebe 0.0115 /  (365 * 24 * 60). Chiaramente, il numero di anni passatp per una caasa non è diverso dal numero di minuti, ma il valore del suo coefficiente è molto più ampio. Questo significa che la magnitudine di un coefficiente non è necessariamente una buona misura dell'importanza della feature in un modello lineare.

Da qui: https://shap.readthedocs.io/en/latest/example_notebooks/overviews/An%20introduction%20to%20explainable%20AI%20with%20Shapley%20values.html#A-more-complete-picture-using-partial-dependence-plots
