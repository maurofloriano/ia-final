from time import Time
from data import Data

def Populacao:
	def __init__(self, size)
		self.size = size
		self.populacao = []
		self.acumulado = 0
		self.selecionado = ''
		self.selecionados = []	

	def calculate_acumalate():
		self.acumulado = 0
		for time in populacao:
			self.acumualdo += time.fit
			time.acumulado = acumulado

	def selecionar_melhor():
		self.selecionado = self.populacao[0]
		for time in self.populacao:
			if time.fit > self.selecionado.fit:
				self.selecionado = time
		return self.selecionado

	def selecionar_individuos():
		self.selecionados = []
		i = 0
		while(i < self.size):
			i += 1
			randomNumber =  random.uniform(0.0, self.acumulado)
			for time in self.populacao:
				if time.acumulado > randomNumber:
					self.selecionados.append(time)
					break
		return self.selecionados