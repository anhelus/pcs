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


if __name__ == '__main__':
    draco = Persona('Draco', 'Malfoy', 12)
    print(draco.nome)
    print(draco.eta)
