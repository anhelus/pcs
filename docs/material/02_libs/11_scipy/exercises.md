# E11 - Introduzione a SciPy

## Esercizio E11.1

Scrivere una funzione che restituisca `True` se la matrice passata in ingresso è invertibile, `False` altrimenti. Usare SciPy.

### Soluzione S10.1

Ecco una possibile soluzione:

```py
from scipy import linalg

def invertibile(mat):
	""" Usiamo un operatore ternario.
	
	Il risultato è analogo alla seguente:
	if linalg.det(mat) != 0.:
		return True
	else:
		return False
	"""
	return True if linalg.det(mat) != 0. else False
```

## Esercizio E11.2

Scrivere una classe che, incorporando la funzione precedente, permetta di invertire una matrice.

### Soluzione S11.2

Ecco una possibile soluzione:

```py
from scipy import linalg
import warnings

class InversoreMatrici():

	def __init__(self, mat):
		self.mat = mat
		self.invertibilita = mat
	
	@property
	def mat(self):
		return self.__mat
	
	@mat.setter
	def mat(self, value):
		if value is None:
			raise ValueError('La matrice non può essere nulla')
		self.__mat = value
	
	@property
	def inv(self):
		return self.__inv

	@inv.setter
	def inv(self, value):
		if value is None:
			raise ValueError("L'inversa non può essere nulla")
		self.__inv = value
	
	@property
	def invertibilita(self):
		return self.__invertibilita
	
	@invertibilita.setter
	def invertibilita(self, value):
		if value is None:
			raise ValueError("La determinazione dell'invertibilità non può essere nulla")
		self.__invertibilita = True if linalg.det(value) != 0. else False
	
	def inverti(self):
		if self.invertibilita:
			self.inv = linalg.inv(self.mat)
		else:
			warnings.warn('La matrice non è invertibile')

a = np.array([[1, 2], [2, 5]])
i = InversoreMatrici(a)
i.inverti()
i.inv
```
