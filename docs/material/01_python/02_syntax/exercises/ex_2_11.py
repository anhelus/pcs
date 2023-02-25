from abc import ABC, abstractmethod
from math import pi


class Figura(ABC):

    def __init__(self, perimetro=0, area=0):
        self.perimetro = perimetro
        self.area = area

    @property
    def perimetro(self):
        return self.__perimetro

    @perimetro.setter
    def perimetro(self, value):
        if value < 0:
            raise ValueError("L'area non può essere negativa.")
        self.__perimetro = value

    @property
    def area(self):
        return self.__area
    
    @area.setter
    def area(self, value):
        if value < 0:
            raise ValueError("L'area non può essere negativa.")
        self.__area = value

    @abstractmethod
    def calcola_perimetro(self):
        pass

    @abstractmethod
    def calcola_area(self):
        pass


class Quadrato(Figura):

    def __init__(self, lato, area=0, perimetro=0):
        super().__init__(perimetro, area)
        self.lato = lato

    @property
    def lato(self):
        return self.__lato

    @lato.setter
    def lato(self, value):
        self.__lato = value

    def calcola_perimetro(self):
        self.perimetro = self.lato * 4

    def calcola_area(self):
        self.area = self.lato ** 2


class Cerchio(Figura):

    def __init__(self, raggio, area=0, perimetro=0):
        super().__init__(perimetro, area)
        self.raggio = raggio

    @property
    def raggio(self):
        return self.__raggio

    @raggio.setter
    def raggio(self, value):
        self.__raggio = value

    def calcola_perimetro(self):
        self.perimetro = 2 * pi * self.raggio

    def calcola_area(self):
        self.area = pi * (self.raggio ** 2)


q = Quadrato(5)
q.calcola_area()
q.calcola_perimetro()
print(f'Lato: {q.lato} - Perimetro: {q.perimetro} - Area: {q.area}')

c = Cerchio(5)
c.calcola_area()
c.calcola_perimetro()
print(f'Raggio: {c.raggio} - Perimetro: {c.perimetro} - Area: {c.area}')
