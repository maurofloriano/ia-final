from individuo import Individuo

class Time:
	def __init__(self, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11):
		self.team = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11]
		self.price = self.get_price()
		self.fit = self.get_fit()
		self.acumulado = 0

	def get_price(self):
		price = 0
		for player in self.team:
			price += player.price
		return price

	def get_fit(self):
		return self.get_average() + self.get_corrector_factor(self.get_average())

	def get_corrector_factor(self, average):
		corrector_factor = 0
		for player in self.team:
			if(self.checkPlayer(player, average)):
				corrector_factor += player.overall - average
		return corrector_factor/len(self.team)



	def get_average():
		average = 0
		for player in self.team:
			average += player.overall
		return average/len(self.team)


	def checkPlayer(self, player, average):
		return player.overall > average