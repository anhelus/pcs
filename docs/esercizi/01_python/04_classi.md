# Risoluzione degli esercizi

1. Creiamo due classi: la prima è la classe `Quadrato`, che modella tutti i quadrati; la seconda è la classe `Cerchio`, che modella tutti i cerchi. Entrambe devono discendere da una classe base chiamata `Figura`.

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


q = Quadrato(5)
print('Lato: {} - Perimetro: {} - Area: {}'.format(q.lato, q.perimetro(), q.area()))

c = Cerchio(5)
print('Raggio: {} - Perimetro: {} - Area: {}'.format(c.raggio, c.perimetro(), c.area()))
```
