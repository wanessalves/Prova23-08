#Wanessa Alves da Silva - 200161143000265
class ContaCorrente:

		def __init__(self, correntista, numeroConta, saldoConta):

			self.numeroConta = numeroConta
			self.saldoConta = saldoConta
			self.correntista = correntista



		def alterarNome(self, newName):
			self.correntista = newName
			print("Nome do Correntista:", self.correntista)

		def deposito(self, valorDeposito):
			self.saldoConta += valorDeposito
			print("Seu saldo é:", self.saldoConta)

		def saque(self, valorSaque):
			if(self.saldoConta >= valorSaque):
				self.saldoConta -= valorSaque
				print("Seu saldo é:", self.saldoConta)
			else:
				print("Saldo Insuficiente")

			