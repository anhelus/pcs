# Moduli

Possiamo interagire con l'interprete Python in diversi modi. Finora, quello che abbiamo maggiormente usato è stata l'interazione diretta con l'interprete, lanciandolo da terminale ed invocando di volta in volta le istruzioni necessarie. Ovviamente, questo presenta numerosi svantaggi: non abbiamo infatti syntax highlighting, non siamo in grado di recuperare le istruzioni una volta chiuso l'interprete, ed in generale non è un modo ottimale di programmare.

Possiamo quindi definire degli *script*, che saranno salvati sotto forma di file con estensione `py`, e conterranno tutte le istruzioni che vogliamo siano eseguite a runtime.

Esiste però un modo per replicare l'approccio che avevamo adottato in C e C++, ovvero quello di suddividere il codice in base alle funzionalità offerte; per farlo, occorre usare i *moduli*, ovvero dei file, sempre con estensione `py`, che contengono le definizioni alle classi o ai metodi da noi creati, che potranno quindi essere richiamati esternamente.

!!!note "Nota"
	La linea che contraddistingue gli script dai moduli è molto sottile, e nei fatti è facile confondersi utilizzandoli in maniera "intercambiabile". Ricordiamo però che, almeno in teoria, gli script dovrebbero essere esclusivamente *eseguiti*, mentre i moduli soltanto *invocati*.

!!!note "Interprete e nome di un modulo"
	L'interprete è in grado di risalire al nome di un modulo dal nome del file in cui è contenuto. Se, ad esempio, definiamo un modulo nel file **matematica.py**, l'interprete associerà a quel modulo il nome `matematica`. Detto nome è inoltre accessibile globalmente *e* dall'interno del modulo richiamando la variabile globale `__name__`.

Facciamo un esempio.

## Il modulo `matematica`

Creiamo un modulo `matematica` all'interno del file **matematica.py**; nel modulo, definiremo delle funzioni per il calcolo matematico. Ad esempio:

```python
# matematica.py

def somma(a, b):
	return a + b


def moltiplica(a, b):
	return a * b


def fibonacci(val_max):
	fib = [0, 1]
	fib += [(fib := [fib[1], fib[0] + fib[1]]) and fib[1] for i in range(val_max)]
	return fib
```

Definiamo ora, nella stessa cartella, uno script, e chiamiamolo **run.py**:

```python linenums="1"
# run.py
import matematica

if __name__ == "__main__":
	print(matematica.fibonacci(20))
```

Notiamo due cose:

1. stiamo richiamando la funzione `fibonacci()` definita nel modulo `matematica`; per farlo, usiamo la direttiva `import` (potete pensarla come analoga alla direttiva `#include` del C/C++);
2. alle righe 4-5, quella "strana" sintassi ci serve a dichiarare il `main`. Tuttavia, Python ci permette di ometterla, ed è utile soprattutto nel caso ci siano programmi complessi con passaggio di parametri multipli.

Proviamo quindi a lanciare lo script digitando l'istruzione `python run.py` da terminale. A schermo, se tutto è andato per il verso giusto, vedremo i primi dodici elementi della sequenza di Fibonacci.

!!!note "Import di funzioni"
	Nel nostro script, abbiamo usato esclusivamente la funzione `fibonacci()`; tuttavia, la direttiva `import` utilizzata fa sì che vengano importante anche le funzioni somma e moltiplica, che non utilizziamo. E' quindi buona regola, qualora non servano tutte le classi e funzioni definite all'interno di un modulo, usare una versione modificata della direttiva, che prende la forma di:

	> ```python
	  from modulo import funzione_o_classe
	  ```
	
	il che, nel nostro caso specifico, diventa:

	> ```python
	  from matematica import fibonacci
	  ```

!!!note "Alias"
	L'`import` permette anche di definire degli alias, che risultano particolarmente utili nel caso di nomi di package complessi. Ad esempio:

	> ```python
	  import matematica as mate
	  print(mate.fibonacci(20))
	  ```

### La funzione dir()

La funzione `dir()` ci permette di vedere tutti i nomi (sia di funzione, sia di classe) definiti da un modulo, e li restituisce sotto forma di lista. Ad esempio:

```python
>>> dir(matematica)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'fibonacci', 'moltiplica', 'somma']
```

!!!note "Nota"
	Oltre alle funzioni, classi e costanti da noi definite, nel modulo `matematica` sono definite in modo automatico tutta una serie di variabili, le quali saranno importate assieme alle definizioni necessarie nel caso si usi la direttiva `import` in maniera "approssimativa". Ad esempio:

	> ```python
	  import matematica
	  if __name__ == "__main__":
		print(matematica.__file__)
		print(matematica.fibonacci(20))
	  ```
	
	In questo caso, saremo in grado di accedere alla variabile `__file__` del modulo `matematica`, che indica il percorso relativo dello stesso all'interno del file system. Ovviamente, questa variabile non ci serve (quasi mai), per cui è evidente l'importanza dell'uso della direttiva `from`!

### Moduli della libreria standard

Python ha diversi moduli appartenenti ad una libreria standard, analogamente a quanto visto per C e C++. In particolare, alcuni moduli meritano una menzione:

* `sys`: è il modulo integrato nell'interprete, ed offre diverse utility necessarie al suo funzionamento;
* `os`: modulo delegato all'interazione con il sistema operativo su cui gira l'interprete;
* `time`: modulo usato per tutte le utility riguardanti il "cronometraggio" del tempo di esecuzione di una funzione;
* `datetime`: modulo usato per le funzionalità di data ed ora;
* `copy`: modulo usato per gestire, tra le altre cose, la deep copy di un oggetto.

Ovviamente, fare una lista esaustiva è pressoché inutile, oltre che ridondante, per cui si rimanda alla [Python Library Reference](https://docs.python.org/3/library/).

## Package

Chiudiamo con un accenno ad un ulteriore livello possibile nella struttura dei file di un programma (o libreria) Python, ovvero quello definito mediante i *package*.

In breve, questi sono dei veri e propri "contenitori" di moduli, che permettono di raggruppare moduli tra loro coerenti, di modo da facilitarne successivamente l'accesso ed il recupero; nella pratica, i package sono delle cartelle sul file system, contenenti al loro interno una serie di moduli ed un file (spesso lasciato vuoto) chiamato `__init__.py`, che permette all'interprete di riconoscere quella cartella come package.

L'accesso ad un modulo interno ad un package avviene modificando la direttiva `import` come segue:

```python
import nome_package.nome_modulo
# oppure...
from nome_package.nome_modulo import nome_funzione
```
