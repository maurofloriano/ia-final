from individuo import Individuo
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
        players.append(self.v_positions[self.V_POSITIONS['GK']][p])

        #  LB
        p = random.randint(0, len(self.v_positions[self.V_POSITIONS['LB']]) - 1)
        players.append(self.v_positions[self.V_POSITIONS['LB']][p])

        #  RB
        p = random.randint(0, len(self.v_positions[self.V_POSITIONS['RB']]) - 1)
        players.append(self.v_positions[self.V_POSITIONS['RB']][p])

        #  CB 1
        p = random.randint(0, len(self.v_positions[self.V_POSITIONS['CB']]) - 1)
        players.append(self.v_positions[self.V_POSITIONS['CB']][p])

        #  CB 2
        p = random.randint(0, len(self.v_positions[self.V_POSITIONS['CB']]) - 1)
        players.append(self.v_positions[self.V_POSITIONS['CB']][p])

        #  CDM
        p = random.randint(0, len(self.v_positions[self.V_POSITIONS['CDM']]) - 1)
        players.append(self.v_positions[self.V_POSITIONS['CDM']][p])

        #  CM
        p = random.randint(0, len(self.v_positions[self.V_POSITIONS['CM']]) - 1)
        players.append(self.v_positions[self.V_POSITIONS['CM']][p])

        #  CM
        p = random.randint(0, len(self.v_positions[self.V_POSITIONS['CM']]) - 1)
        players.append(self.v_positions[self.V_POSITIONS['CM']][p])

        #  LW
        p = random.randint(0, len(self.v_positions[self.V_POSITIONS['LW']]) - 1)
        players.append(self.v_positions[self.V_POSITIONS['LW']][p])

        #  ST
        p = random.randint(0, len(self.v_positions[self.V_POSITIONS['ST']]) - 1)
        players.append(self.v_positions[self.V_POSITIONS['ST']][p])

        #  RW
        p = random.randint(0, len(self.v_positions[self.V_POSITIONS['RW']]) - 1)
        players.append(self.v_positions[self.V_POSITIONS['RW']][p])

        for player in players:
            print player.position, player.name, player.overall

        return players

    def generate_data_set(self):
        for index, player in self.df.iterrows():
            if index > 1000:
                break
            position = self.get_position(player['Preferred Positions'])
            overall = player['Overall']
            price = player['Value']
            name = player['Name']
            individuo = Individuo(overall, price, name, position)
            self.v_positions[self.PLAYERS[individuo.position]].append(individuo)

        self.random_squad()
