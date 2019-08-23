#Wanessa Alves da Silva - 200161143000265
class  BombaCombustivel:

	def __init__(self, capacidade, preco):
		self.capacidade = capacidade
		self.preco = preco

	def abastecerPorValor(self, valor):
		litros = round((valor/self.preco),4)
		self.capacidade -= litros
		print("Você abasteu {} litros".format(litros))

	def abastecerPorLitro(self, litro):
		gasto = round((litro*self.preco),4)
		self.capacidade -= gasto
		print("Você abasteu R$ {}".format(gasto))

	def alterarPreco(self, newPreco):
		self.preco = newPreco
		print("Novo Preço do litro é:", self.preco)

	def encherBomba(self, newCapacidade):
		if(newCapacidade <= 30000):
			self.capacidade = newCapacidade
			print("A bomba está com {} litros disponiveis".format(self.capacidade))
		else:
			print("Bomba sem espaço suficiente!!")	

		


