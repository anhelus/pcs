# E4 - Programmazione orientata agli oggetti in Python

## E4.1

Scrivere una classe `Persona` applicando i concetti visti durante la lezione.

### S4.1 - Soluzione

Scriviamo la classe `Persona` come segue:

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
Draco
>>> print(draco.eta)
12
>>> hermione = PersonProperty('', 'Granger', 18)
ValueError: La lunghezza del nome non può essere inferiore a due caratteri.
```

Notiamo che, dal punto di vista dello script che richiama la classe, non ci sono differenze di sorta; tuttavia, la logica di validazione ci permette di evitare errori e situazioni incoerenti, ed è inoltre possibile sfruttare le proprietà per accedere agli attributi privati della classe.

## E4.2

Creiamo due classi: la prima è la classe `Quadrato`, che modella tutti i quadrati; la seconda è la classe `Cerchio`, che modella tutti i cerchi. Entrambe devono discendere da una classe base chiamata `Figura`.

### S4.2 - Soluzione

```py
from abc import ABC, abstractmethod
from math import pi

class Figura(ABC):

    @property
    def perimetro(self):
        return self.__perimetro

    @property
    def area(self):
        return self.__area
    
    @abstractmethod
    def perimetro(self):
        pass
    
    @abstractmethod
    def area(self):
        pass


class Quadrato(Figura):

    def __init__(self, lato):
        self.lato = lato
    
    @property
    def lato(self):
        return self.__lato
    
    @lato.setter
    def lato(self, value):
        self.__lato = value
    
    def perimetro(self):
        return self.lato * 4
    
    def area(self):
        return self.lato ** 2


class Cerchio(Figura):

    def __init__(self, raggio):
        self.raggio = raggio
    
    @property
    def raggio(self):
        return self.__raggio
    
    @raggio.setter
    def raggio(self, value):
        self.__raggio = value
    
    def perimetro(self):
        return 2 * pi * self.raggio
    
    def area(self):
        return pi * (self.raggio ** 2)


# Esempio di uso
q = Quadrato(5)
print('Lato: {} - Perimetro: {} - Area: {}'.format(q.lato, q.perimetro(), q.area()))

c = Cerchio(5)
print('Raggio: {} - Perimetro: {} - Area: {}'.format(c.raggio, c.perimetro(), c.area()))
```
