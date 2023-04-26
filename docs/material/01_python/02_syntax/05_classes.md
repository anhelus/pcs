# 1.2.5 - Classi ed OOP

Python offre un esteso supporto alla programmazione orientata agli oggetti. Prima di proseguire, però, è opportuno introdurre brevemente questo concetto.

## La programmazione orientata agli oggetti

Quello della *programmazione orientata agli oggetti* (OOP) è un paradigma di programmazione che permette di creare nuovi tipi definiti dall'utente, da intendersi come complementari ai tipi definiti dal linguaggio di programmazione. In tal senso, la OOP sposta il focus dalle *funzioni*, centrali nei linguaggi come il C e nel paradigma procedurale, ai *dati*.

In tal senso, si arriva a dire che *nella OOP tutto è un oggetto*.

## Classi

Una *classe* è un prototipo per un determinato tipo di dati definito dall'utente. Ad esempio:

* la classe `Studente` rappresenta tutte le proprietà e le azioni associate ad uno studente;
* la classe `Auto` rappresenta tutte le proprietà e le azioni associate ad un'auto;
* la classe `Motore` definisce i comportamenti dei motori;

e via discorrendo.

In generale, quindi, può esistere una classe per ogni tipologia di oggetti presenti nel mondo, sia esso reale o informatico.

Importante è non confondere la classe con il *singolo oggetto*, chiamato *istanza*. Ad esempio:

* lo studente Angelo Cardellicchio è un'istanza della classe `Studente`;
* l'auto Opel Corsa targata AB 123 CD è un'istanza della classe `Auto`;
* l'auto Hyundai Tucson CD 321 AB è un'istanza della classe `Auto`;
* l'auto Opel Corsa targata AA 123 CC è un'altra istanza della classe `Auto`.

## Metodi ed attributi

Ogni classe ha dei *metodi*, che caratterizzano delle azioni che è possibile effettuare su ogni istanza della classe, e degli *attributi*, ovvero delle caratteristiche dell'istanza.

In particolare, ogni nuovo tipo, chiamato *classe*, avrà opportuni *attributi* e *metodi*, ognuno dei quali accessibile dall'esterno mediante opportuni *modificatori*.

Ad esempio, l'auto Opel Corsa targata AB 123 CD ha una casa costruttrice (Opel), un modello (Corsa), una targa (AB 123 CD), una cilindrata, e via dicendo.

!!!note "Approfondimento"
	Possiamo approfondire i concetti alla base della OOP in [questa appendice](../../appendix/05_oop/lecture.md).

## Classi in Python

Per definire una classe, dovremo usare la parola chiave `class`:

```py
class NomeClasse(ClasseBase):
	# Attributi e metodi di classe...
```

Con la sintassi precedente, abbiamo creato una classe chiamata `NomeClasse` discendente da una classe base (`ClasseBase`).

### Il metodo `__init__`

La maggior parte dei linguaggi di programmazione utilizza il concetto di *costruttore* per creare un'istanza di una classe. Il Python, tuttavia, non prevede l'utilizzo di un costruttore vero e proprio, quanto piuttosto di un metodo di *inizializzazione* dei singoli attributi dell'istanza. Da qui deriva il nome del metodo, ovvero `__init__`:

```py
class NomeClasse(ClasseBase):

	def __init__(self, *args, **kwargs):
		# ...
		self.arg_1 = arg_1
		# ...
```

!!!tip "Unpacking"
	Con la sintassi `*args` e `**kwargs` vogliamo rappresentare l'azione di *unpacking* di (rispettivamente) una lista ed un dizionario, mediante la quale stiamo passando tutti i valori contenuti all'interno della sequenza.

Occorre prestare particolare attenzione all'uso della keyword `self`, che permette di riferirsi alla specifica istanza di una classe (per chi ha familiarità con i linguaggi come il C++, è concettualmente simile alla parola chiave `this`). Ad esempio:

```py
class Persona(object):

	def __init__(self, nome, cognome, eta=18):
		self.nome = nome
		self._cognome = cognome
		self.__eta = eta
```

Questo snippet ci permette di evidenziare quattro punti:

1. la classe generica `object`, da cui derivano **tutte** le classi Python (ma la cui dichiarazione può comunque essere omessa);
2. il funzionamento della parola chiave `self`, che permette di associare agli attributi della singola istanza un determinato valore;
3. la possibilità di inserire tra i parametri dei valori opzionali e di default (in questo caso `eta`, che di default vale `18`);
4. la presenza di uno o due simboli `_` (*underscore*) davanti ad alcuni attributi.

Approfondiamo brevemente il punto 4.

### Modificatori di accesso

Python prevede l'uso di modificatori di accesso ai dati; nello specifico, troviamo i classici `public`, `protected` e `private`. Tuttavia, a differenza di altri linguaggi, per distinguere tra i tre modificatori di accesso si utilizzano uno o due *underscore* come suffisso al nome dell'attributo; in particolare, usare un *underscore* singolo indica un attributo protected, mentre un *underscore* doppio indica un attributo `private`. Nel nostro caso:

```py
class Persona(object):

	def __init__(self, nome, cognome, eta=18):
		self.nome = nome				# Membro "public"
		self._cognome = cognome			# Membro "protected"
		self.__eta = eta				# Membro "private"
```

!!!warning "Attenzione"
	Nonostante il modificatore di accesso, è possibile accedere ai membri protetti dall'esterno della classe. Infatti:
	> ```py
	  >>> p = Persona('Jax', 'Teller')
	  >>> print(p.nome)
      'Jax'
	  >>> print(p._cognome)
	  'Teller'
	  ```

	Questo non vale per gli attributi privati:

	> ```py
	  >>> try:
	  >>>     print(p.__eta)
	  >>> except AttributeError:
	  >>>	  print('Età è privato!')
	  Età è privato!
	  ```

Questa sintassi può ovviamente essere utilizzata per definire dei metodi protetti o privati.

!!!tip "Suggerimento"
	La sintassi che abbiamo mostrato nello snippet precedente è relativa alla *gestione delle eccezioni*.

### Metodi

La sintassi per definire il metodo di una classe è analoga a quella usata per definire una funzione.

```py
def metodo(self, *args, **kwargs):
	pass
```

Esiste tuttavia una differenza fondamentale: infatti, il primo attributo di un metodo appartenente ad una classe è *sempre* un riferimento all'istanza tramite la parola chiave `self`. Tale riferimento non va specificato quando il metodo viene chiamato dall'esterno:

```py
# ...
p = Persona()			# p è un'istanza di Persona
p.metodo(parametro)		# richiamo il metodo dall'istanza
# ...
```

Nel codice precedente, abbiamo usato l'operatore `.` per accedere a `metodo()` definito all'interno della classe `Persona`.

Approfondiamo adesso alcune particolari tipologie di metodi, ottenibili usando determinati decorator (cfr. appendice B).

#### Metodi di classe

Il decorator `@classmethod` ci permette di definire i cosiddetti *metodi di classe*:

```py
@classmethod
def builder_stringa(cls, stringa: str):
	nome, cognome, eta = stringa.split(' ')
	return Persona(nome, cognome, eta)
```

A differenza dei metodi standard, i metodi di classe hanno un riferimento alla classe (`cls`) e non all'istanza (`self`). Questo significa che sono dei metodi che si *applicano all'intera classe*, e non alla singola istanza. Un tipico esempio di utilizzo di un metodo di classe è mostrato nello snippet precedente, nel quale stiamo creando un oggetto di classe `Persona` a partire da una stringa.

!!!tip "Curiosità"
	Il metodo precedente è, di fatto, un'implementazione del design pattern Builder.

Per richiamare un metodo di classe occorre riferirsi al nome della classe stessa, e non ad una singola istanza:

```py
>>> persona = Persona.builder_stringa('Bobby Munson 58')
>>> print("{} {}".format(persona.nome, persona._cognome))
Bobby Munson
```

#### Metodi statici

Mediante il decoratore `@staticmethod` possiamo definire un metodo *statico*. In Python il funzionamento di un metodo di questo tipo è riassumibile in un comportamento assimilabile ad una funzione "semplice", definita però all'interno della classe, e richiamabile su istanze della stessa. Ad esempio:

```py
@staticmethod
def nome_valido(nome):
	if len(nome) < 2:
		return False
	else:
		return True
```

Questo metodo è quindi liberamente richiamabile mediante l'operatore `.` da una singola istanza:

```py
>>> print(Persona.nome_valido('Li'))
True
```

Un'altra possibilità è richiamarlo sulla classe stessa:

```py
>>> print(Persona.nome_valido('X'))
False
```

#### Metodi astratti

Possiamo definire dei metodi *astratti* (cfr. Appendice C) mediante il decorator `@abstractmethod`. Per farlo, la nostra classe deve discendere dalla classe `ABC` (acronimo che sta per *Abstract Base Class*), contenuta nel package `abc`:

```py
from abc import ABC

class ClasseBase(ABC):

	# ...

	@abstractmethod
	def metodo_da_sovrascrivere(self):
		pass
```

I metodi contrassegnati con il decorator `@abstractmethod` dovranno essere implementati nelle classi derivate (in altre parole, dovremo farne l'*override*):

```py
class ClasseDerivata(ClasseBase):

	# ...

	def metodo_da_sovrascrivere(self):
		# ...
```

### Le proprietà

In molti linguaggi di programmazione si usano tradizionalmente i metodi *accessori* (*getter*) e *modificatori* (*setter*) per accedere agli attributi delle istanze di una classe. Python non vieta di farlo: ad esempio, possiamo scrivere un metodo `get_nome(self)` per accedere al nome di una persona, ed un metodo `set_nome(self, nome)` per impostare detta proprietà.

Tuttavia, è possibile usare una sintassi più compatta (e, in definitiva, maggiormente *pythonic*) mediante il decorator `@property`, che rappresenta una funzione a quattro parametri:

```py
property(fget=None, fset=None, fdel=None, doc=None)
```

In particolare:

* `fget` è la funzione usata per recuperare il valore dell'attributo;
* `fset` è la funzione usata per impostare il valore dell'attributo;
* `fdel` è la funzione per rimuovere l'attributo;
* `doc` è la funzione per documentare e descrivere l'attributo.

Grazie a `property`, potremo seguire le "best practice" della OOP, rendendo privati gli attributi della classe ed accedendovi mediante opportuni metodi.

```py
class Persona():

	def __init__(self, nome, cognome, eta):
		self.nome = nome
		self.cognome = cognome
		self.eta = eta

	@property
	def nome(self):
		return self.__nome

	@nome.setter
	def nome(self, value):
		if len(value) < 2:
			raise ValueError('La lunghezza del nome non può essere inferiore a due caratteri.')
		else:
			self.__nome = value

	@property
	def cognome(self):
		return self.__cognome

	@cognome.setter
	def cognome(self, value):
		if len(value) < 2:
			raise ValueError('La lunghezza del cognome non può essere inferiore a due caratteri.')
		else:
			self.__cognome = value

	@property
	def eta(self):
		return self.__eta

	@eta.setter
	def eta(self, value):
		if value < 0:
			raise ValueError("L'età non può essere negativa.")
		else:
			self.__eta = value
```

Alcune note:

* abbiamo riscritto la classe `Persona` in modo da trasformare tutti gli attributi in proprietà;
* per ogni proprietà, abbiamo specificato un getter, che restituisce il valore della stessa;
* oltre al getter, è stato specificato un setter, nel quale vi è anche una forma di validazione del valore passato in input.

Vediamo come usare la nostra nuova classe:

```py
>>> draco = Persona('Draco', 'Malfoy', 12)
>>>	print(draco.nome)
'Draco'
>>> print(draco.eta)
12
>>> hermione = Persona('', 'Granger', 18)
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 3, in __init__
    File "<stdin>", line 12, in nome
ValueError: La lunghezza del nome non può essere inferiore a due caratteri.
```

Notiamo che, dal punto di vista dello script che richiama la classe, non ci sono differenze di sorta; tuttavia, la logica di validazione ci permette di evitare errori e situazioni incoerenti, ed è inoltre possibile sfruttare le proprietà per accedere agli attributi privati della classe.
