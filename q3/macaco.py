#Wanessa Alves da Silva - 200161143000265

class Macaco():

	def __init__(self, nome, bucho):
		self.nome = nome
		self.bucho = bucho

	def comer(self, alimento1, alimento2, alimento3):
		self.bucho = alimento1, alimento2, alimento3

	def verBucho(self):
		print(self.bucho)		

	def digerir(self):
		self.bucho = "NADA"
		print("Estou com Fome:", self.bucho)

