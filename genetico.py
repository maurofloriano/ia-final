import random
from team import Time
import matplotlib.pyplot as plt


class AlgoritmoGenetico:
    def __init__(self, populacao, data):
        self.populacao = populacao
        self.fit_medio = []
        self.fitMelhor = []
        self.data = data

    def deve_cruzar(self, alfa):
        deve = random.uniform(0.0, 1.0)
        if(alfa >= deve):
            return True
        return False

    def cruzamento(self, pai1, pai2):
        team1 = team2 = []
        aux = True
        for player1, player2 in zip(pai1.team, pai2.team):
            if aux:
                team1.append(player1)
                team2.append(player2)
                aux = False
            else:
                team1.append(player2)
                team2.append(player1)
                aux = True
        filho1 = Time(team1)
        filho2 = Time(team2)
        return [filho1, filho2]

    def deve_mutar(self, alfa):
        deve = random.uniform(0.0, 1.0)
        if(alfa >= deve):
            return True
        return False

    def mutacao(self, team):
        jogadores = self.data.v_positions[7]
        select_player = random.randint(0, len(jogadores) - 1)
        team[9] = jogadores[select_player]
        return team

    def run(self, geracoes):
        T = 0
        while(T < geracoes):
            selecionado = self.populacao.selecionar_melhor()
            self.fitMelhor.append(selecionado.fit)
            self.populacao.calcular_acumulado()
            selecionados = self.populacao.selecionar_individuos()
            self.populacao.populacao = selecionados
            i = 0
            while(i < len(selecionados)):
                if self.deve_cruzar(0.7):
                    filhos = self.cruzamento(self.populacao.populacao[i], self.populacao.populacao[i + 1])
                    self.populacao.populacao[i] = filhos[0]
                    self.populacao.populacao[i + 1] = filhos[1]
                i += 2
            i = 0
            while(i < len(self.populacao.populacao)):
                if self.deve_mutar(0.3):
                    time = self.mutacao(self.populacao.populacao[i].team)
                    self.populacao.populacao[i] = Time(time)
                i += 1
            T += 1
            index = 0
            indexAtual = 0
            fit = self.populacao.populacao[0].fit
            for index, individuo in enumerate(self.populacao.populacao):
                if(individuo.fit < fit):
                    fit = individuo.fit
                    indexAtual = index
            if(self.populacao.populacao[indexAtual].fit < selecionado.fit):
                self.populacao.populacao[indexAtual] = selecionado

            self.populacao.calcular_acumulado()
        plt.plot(self.fitMelhor)
        plt.show()
