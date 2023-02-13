# E4 - Programmazione orientata agli oggetti in Python

## Esercizio 4.1

Scrivere una classe `Persona` applicando i concetti visti durante la lezione.

### Soluzione

Supponiamo che la classe `Persona` abbia tre attributi:

* un attributo `nome`, stringa rappresentativa del nome della persona;
* un attributo `cognome`, stringa rappresentativa del cognome della persona;
* un attributo `eta`, intero rappresentativo dell'età della persona.

Per prima cosa, scriviamo il metodo `__init__`:

```py
def __init__(self, nome, cognome, eta):
    self.nome = nome
    self.cognome = cognome
    self.eta = eta
```

Passeremo al metodo `__init__` tre parametri che, per semplicità, chiameremo proprio `nome`, `cognome` ed `eta`. Questi parametri andranno ad inizializzare gli omonimi attributi di classe.

Fatto questo, scriviamo tre proprietà, una per ciascun attributo:

```py
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

Notiamo come le proprietà `nome` e `cognome` siano fatte in modo che se la lunghezza della stringa passata risulta essere inferiore a due caratteri venga lanciato un errore di tipo `ValueError`. Analogamente, il valore della proprietà `eta` non potrà essere inferiore a zero.

Facciamo un esempio di uso della nostra classe mediante l'interprete Python:

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

!!!tip "Codice"
    Il codice completo per questo esercizio è disponibile a [questo indirizzo]()

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
