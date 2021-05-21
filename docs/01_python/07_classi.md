# Classi in Python

Così come il C++, Python ha un esteso supporto per la programmazione orientata agli oggetti.

La definizione di una classe in Python avviene come segue:

```py
class ClassName(BaseClass):
	# Class body
```

Notiamo che, a differenza del C++, nel quale la classe viene definita all'interno di un header, qui la definizione avviene contestualmente alla dichiarazione della firma della classe.

## Costruttori

Il linguaggio Python non prevede l'utilizzo di un costruttore vero e proprio, quanto piuttosto di un metodo di inizializzazione degli attributi della classe. Questo metodo assume lo stesso nome per ogni classe, ovvero `__init__`:

```py
class ClassName(BaseClass):

	def __init__(self, *args, **kwargs):
		# ...
		self.arg_1 = arg_1
		# ...
```

!!!note "Nota"
	La sintassi `*args` e `**kwargs` rappresenta, rispettivamente, l'*unpacking* di liste e dizionari. Ciò significa che come argomento non si passa la lista o il dizionario, ma i valori (o le coppie chiave/valore) ivi contenuti.

Notiamo l'uso della parola chiave `self`. Questa, in qualche modo, richiama il `this` del C++: infatti, si riferisce alla specifica istanza della classe. Ad esempio:

```py
class Person(object):

	def __init__(self, first_name, last_name, age=18):
		self.first_name = first_name
		self._last_name = last_name
		self.__age = age
```

!!!note "Nota"
	In Python, tutte le classi derivano da una classe generica `object`.

## Modificatori di accesso

Python prevede, come il C++, l'uso di modificatori di accesso ai dati; nello specifico, ritroviamo `public`, `protected` e `private`.

Per contraddistinguere i tre tipi di variabili, si utilizzano gli underscore come suffisso al nome della stessa; in particolare, un unico underscore indica un membro `protected`, mentre un doppio underscore indica un membro `private`.

```py
class Person(object):

	def __init__(self, first_name, last_name, age=18):
		self.first_name = first_name
		self._last_name = last_name
		self.__age = age
```

!!!note "Nota"
	I membri protetti sono facilmente accessibili dall'esterno della classe. Infatti:
	> ```py
	  p = Person('Jax', 'Teller')
	  print(p.first_name)
	  print(p._last_name)
	  try:
	  	  print(p.__age)
	  except AttributeError:
	  	  print('Age is private!')
	  ```

	risulterà in:
	> ```bash
	  Jax
	  Teller
	  Età è privato!
	  ```

Contestualmente, è possibile usare la stessa convenzione definire metodi per l'accesso a variabili `protected` e `private`.

## Classi e metodi

I metodi di una classe sono definiti in questo modo:

```py
def metodo(self, *args, **kwargs):
	pass
```

E' importante notare come il primo attributo di un normale metodo di classe sia sempre la parola `self`. Questa non deve però essere specificata quando lo si chiama dall'esterno: basta infatti chiamarlo usando l'operatore `.` da un'istanza della classe:

```py
# ...
p = Person()
p.metodo(*args, **kwargs)
# ...
```

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

### `@classmethod`

E' possibile definire i cosiddetti *metodi di classe* mediante il decorator `@classmethod`:

```py
@classmethod
def from_string(cls, person_string: str):
	fn, ln, age = person_string.split(' ')
	return Person(fn, ln, age)
```

A differenza dei normali metodi definiti all'interno di una classe, i metodi di classe passano implicitamente un riferimento alla classe (`cls`) e non all'istanza (`self`). Questo significa che sono dei metodi pensati per applicarsi all'intera classe, e non alla singola istanza; normalmente, vengono usati per creare dei costruttori alternativi, come nel caso precedente, nel quale creiamo una persona a partire da una stringa.

Per chiamare un metodo di classe, ci riferiamo al nome della classe stessa, e non alla singola istanza:

```py
pb = Person.from_string('Bobby Munson 58')
print("{} {}".format(pb.first_name, pb._last_name))
```

### `@staticmethod`

Così come in C e C++, è possibile definire metodi statici, che in questo caso sono maggiormente assimilabili alla loro concezione del C++. Infatti, nell'ambito della classe, un metodo statico non accetta né la classe, né una specifica istanza, ma si comporta come una funzione "semplice", che però è possibile chiamare dall'interno della classe. Ad esempio:

```py
@staticmethod
def check_is_valid(first_name):
	# return False if len(first_name) < 2 else True
	# return len(first_name) < 2
	return False or len(first_name) >= 2
```

!!! note "Nota"
	In questo metodo, abbiamo usato una sintassi chiamata *shorthand ternary operator*, mentre commentato troviamo il classico operatore ternario, o una versione più semplice.

```py
>>> print(pb.check_is_valid('Li'))
True
>>> print(Person.check_is_valid('X'))
False
```

### `@abstractmethod`

I metodi astratti sono definibili nel caso si stiano implementando delle classi astratte (ovvero classi in cui alcuni metodi non sono implementati) o, nel caso estremo, interfacce (ovvero classi in cui nessun metodo è implementato). Per usarli, la nostra classe deve discendere da un particolare tipo di classe Python chiamato **Abstract Base Class**, abbreviato in `ABC`, e contenuto nel package `abc`:

```py
from abc import ABC

class BaseClass(ABC):

	# some methods...

	@abstractmethod
	def method_to_override(self):
		pass
```

I metodi contrassegnati con il decorator `@abstractmethod` andranno implementati nelle classi derivate (operazione di *override*):

```py
class DerivedClass(BaseClass):

	# some methods...

	def method_to_override(self):
		do_something()
```

## Proprietà

A differenza delle classi implementate in C++, finora non abbiamo usato i getter ed i setter. Per farlo, possiamo usare sia degli opportuni metodi (nel nostro caso, ad esempio, potremmo usare un metodo `get_first_name(self)`, un metodo `set_first_name(self, fn)`, e via dicendo), o, in maniera più *pythonic*, il decorator `@property`, che ci offre un modo integrato per definire ogni attributo della classe.

!!!note "Note"
	In realtà, il decorator `@property` si riferisce ad una funzione con quattro parametri:

	> ```py
	property(fget=None, fset=None, fdel=None, doc=None)
	```

	che rappresentano:
	* `fget` funzione per ottenere il valore dell'attributo;
	* `fset` funzione per impostare il valore dell'attributo;
	* `fdel` funzione per cancellare l'attributo;
	* `doc` funzione per la documentazione dell'attributo.

Le best practice ci dicono di adattare i nostri attributi, rendendoli privati, ed accedendovi soltanto mediante il decorator `@property`:

```py
class PersonProperty():

	def __init__(self, first_name, last_name, age):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
	
	@property
	def first_name(self):
		return self.__first_name
	
	@first_name.setter
	def first_name(self, value):
		if len(value) < 2:
			raise ValueError('Name must be longer than two characters')
		else:
			self.__first_name = value
	
	# ...
```

```py
>>> pp = PersonProperty('Draco', 'Malfoy', 12)
>>>	print(pp.first_name)
Draco
>>> pp = PersonProperty('', 'Granger', 18)
ValueError: Name must be longer than two characters
```
