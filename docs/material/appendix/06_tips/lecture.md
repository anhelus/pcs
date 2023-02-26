# Appendice E - Python

## Tabella degli operatori booleani

| Operatore | Operazione logica | Esempio           | Risultato |
| --------- | ----------------- | ----------------- | --------- |
| and       | AND               | 1 and 2           | True      |
| or        | OR                | True or False     | True      |
| not       | NOT               | True is not False | True      |

## Gestione delle Eccezioni

### I decorator

Prima di continuare a parlare dei metodi che è possibile definire all'interno di una classe Python, è necessario introdurre il concetto di *decorator*, ovvero una particolare notazione che viene usata in Python (ed in altri linguaggi di programmazione) per indicare una funzione che "decora" un'altra funzione.

#### Funzioni come oggetti

Python tratta le funzioni come degli *oggetti*. E' quindi possiible che una funzione *restituisca una funzione*:

```py
def main_character(series):
	def supernatural():
		return "Sam Winchester"
	
	def breaking_bad():
		return "Walter White"
	
	if series == "Supernatural":
		return supernatural
	elif series == "Breaking Bad":
		return breaking_bad
```

Il valore di ritorno è quindi un oggetto. Possiamo provare a chiamarlo dal nostro script:

```py
>>> mc = main_character("Supernatural")
```

Se provassimo a mandarlo a schermo trattandolo come una variabile, avremmo in uscita una reference a funzione:

```py
>>> print("Function reference: {}".format(mc))
Function reference: <function main_character.<locals>.supernatural at 0x00000170C448BA60>
```

Per visualizzare il risultato, trattiamolo come se fosse una chiamata a funzione:

```py
>>> print("Function outcoming value: {}".format(mc()))
Function outcoming value: Sam Winchester
```

#### Funzioni come argomenti di altre funzioni

Possiamo passare una fuzione come argomento ad un'altra funzione:

```py
def favorite_series(func):
	def internal_check():
		print("Checking my favorite series...")
		func()
		print("Got it!")
	return internal_check

def check():
	print('Sons of Anarchy')
```

Dal nostro script:

```py
>>> print_fav_series = favorite_series(check)
>>> print_fav_series()
Checking my favorite series...
Sons of Anarchy
Got it!
```

Vediamo quindi come la funzione passata come argomento sarà correttamente chiamata internamente al metodo `favorite_series`.

#### Definizione ed uso di decorator

La sintassi che abbiamo usato è, per dirla con Manzoni, *ampollosa*. Python ci offre quindi una sintassi equivalente, ma molto più accessibile, per usare una funzione come argomento di un'altra funzione, ovvero i decorator. Infatti:

```py
@favorite_series
def print_fav_series_decorated():
	print('Breaking Bad')

>>> print_fav_series_decorated()
Checking my favorite series...
Breaking Bad
Got it!
```
