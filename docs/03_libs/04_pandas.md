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

Pandas gestisce dati di tipo *tabulare*. Questi sono i dati maggiormente diffusi in ambito data science, se si esclusono le immagini, e sono quelli comunemente contenuti in fogli di calcolo o in database. Pandas permette di imporatre queste tabelle in una struttura apposita chiamata `DataFrame`.

Un DataFrame è una struttura dati bidimensionali che possono memorizzare dati di versi tipi (inclusi caratteri, interi, valori a virgola mobile, dati categorici e più) in colonne. E' simile ad un foglio di calcolo.

FARE ESEMPIO

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