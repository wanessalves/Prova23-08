#Wanessa Alves da Silva - 200161143000265
class Pessoa:

	def __init__(self, nome, idade, peso, altura):
		self.nome = nome
		self.idade = idade
		self.peso = peso
		self.altura = altura

	def envelhecer(self, newIdade):
		self.idade = newIdade

	def engordar(self, newPeso):
		self.peso = newPeso
		print("Seu peso é:", self.peso)

	def emagrecer(self, novoPeso):
		self.peso = novoPeso
		print("Seu peso é:", self.peso)

	def crescer(self):
		if(self.idade < 21):
			self.altura += 0.5
			print("Sua altura é:", self.altura)	  
		else:
			print("Sua altura é:", self.altura)	  

