from individuo import Individuo

#Preferred Positions

class Data:
	def __init__(self, dataset):
		self.dataset = dataset
		self.gk = [] #1
		self.lb = [] #1
		self.cb = [] #2
		self.rb = [] #1
		self.cdm = [] #1
		self.cm = [] # 2 CM, CAM LM RM
		self.lw = [] # 1 
		self.st = [] # 1 ST CF
		self.rw = [] # 1

	def generate_data_set(self):
		for player in dataset:
			position = self.get_position()
			overall = player['Overall']
			price = player['Value']
			name = player['Name']
			individuo = Individuo(overall, price, name, postion)
