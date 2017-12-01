import pandas as pd
from data import Data
from genetico import AlgoritmoGenetico
from populacao import Populacao


def prepare_data(file_name):
    df = pd.read_csv(file_name, low_memory=False)
    df = df.fillna(0)
    data = Data(df)
    data.generate_data_set()
    return data


if __name__ == "__main__":
    data = prepare_data('CompleteDataset.csv')
    random_squads = data.generate_squads(1001)
    populacao = Populacao(random_squads)
    genetico = AlgoritmoGenetico(populacao, data)
    genetico.run(500)
