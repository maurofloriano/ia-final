from individuo import Individuo
from team import Time
import random


# Preferred Positions
class Data:

    PLAYERS = {
        'GK': 0,
        'LB': 1,
        'LWB': 1,
        'CB': 2,
        'RB': 3,
        'RWB': 3,
        'CDM': 4,
        'CM': 5,
        'CAM': 5,
        'LM': 5,
        'RM': 5,
        'LW': 6,
        'ST': 7,
        'CF': 7,
        'RW': 8,
    }

    V_POSITIONS = {
        'GK': 0,
        'LB': 1,
        'CB': 2,
        'RB': 3,
        'CDM': 4,
        'CM': 5,
        'LW': 6,
        'ST': 7,
        'RW': 8,
    }

    def __init__(self, dataframe):
        self.df = dataframe
        self.v_positions = [None] * 9
        for index, v_position in enumerate(self.v_positions):
            self.v_positions[index] = []

        # self.gk = []  # 1
        # self.lb = []  # 1
        # self.cb = []  # 2
        # self.rb = []  # 1
        # self.cdm = []  # 1
        # self.cm = []  # 2 CM, CAM, LM, RM
        # self.lw = []  # 1
        # self.st = []  # 1 ST CF
        # self.rw = []  # 1

    def get_position(self, positions):
        v_positions = positions.split(' ')
        if v_positions:
            return v_positions[0]
        return positions

    def random_squad(self):
        players = []
        #  GK
        p = random.randint(0, len(self.v_positions[self.V_POSITIONS['GK']]) - 1)
        individuo = self.v_positions[self.V_POSITIONS['GK']][p]
        individuo.position_data = p
        players.append(individuo)

        #  LB
        p = random.randint(0, len(self.v_positions[self.V_POSITIONS['LB']]) - 1)
        individuo = self.v_positions[self.V_POSITIONS['LB']][p]
        individuo.position_data = p
        players.append(individuo)

        #  RB
        p = random.randint(0, len(self.v_positions[self.V_POSITIONS['RB']]) - 1)
        individuo = self.v_positions[self.V_POSITIONS['RB']][p]
        individuo.position_data = p
        players.append(individuo)

        #  CB 1
        p = random.randint(0, len(self.v_positions[self.V_POSITIONS['CB']]) - 1)
        individuo = self.v_positions[self.V_POSITIONS['CB']][p]
        individuo.position_data = p
        players.append(individuo)

        #  CB 2
        p = random.randint(0, len(self.v_positions[self.V_POSITIONS['CB']]) - 1)
        individuo = self.v_positions[self.V_POSITIONS['CB']][p]
        individuo.position_data = p
        players.append(individuo)

        #  CDM
        p = random.randint(0, len(self.v_positions[self.V_POSITIONS['CDM']]) - 1)
        individuo = self.v_positions[self.V_POSITIONS['CDM']][p]
        individuo.position_data = p
        players.append(individuo)

        #  CM
        p = random.randint(0, len(self.v_positions[self.V_POSITIONS['CM']]) - 1)
        individuo = self.v_positions[self.V_POSITIONS['CM']][p]
        individuo.position_data = p
        players.append(individuo)

        #  CM
        p = random.randint(0, len(self.v_positions[self.V_POSITIONS['CM']]) - 1)
        individuo = self.v_positions[self.V_POSITIONS['CM']][p]
        individuo.position_data = p
        players.append(individuo)

        #  LW
        p = random.randint(0, len(self.v_positions[self.V_POSITIONS['LW']]) - 1)
        individuo = self.v_positions[self.V_POSITIONS['LW']][p]
        individuo.position_data = p
        players.append(individuo)

        #  ST
        p = random.randint(0, len(self.v_positions[self.V_POSITIONS['ST']]) - 1)
        individuo = self.v_positions[self.V_POSITIONS['ST']][p]
        individuo.position_data = p
        players.append(individuo)

        #  RW
        p = random.randint(0, len(self.v_positions[self.V_POSITIONS['RW']]) - 1)
        individuo = self.v_positions[self.V_POSITIONS['RW']][p]
        individuo.position_data = p
        players.append(individuo)

        return players

    def generate_data_set(self):
        for index, player in self.df.iterrows():
            position = self.get_position(player['Preferred Positions'])
            overall = player['Overall']
            price = player['Value']
            name = player['Name']
            individuo = Individuo(overall, price, name, position, 0)
            self.v_positions[self.PLAYERS[individuo.position]].append(individuo)

    def generate_squads(self, qtd):
        random_squads = []
        for x in xrange(1, qtd):
            random_squads.append(Time(self.random_squad()))
        return random_squads
