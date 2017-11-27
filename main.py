import pandas as pd
from data import Data


if __name__ == "__main__":
    df = pd.read_csv('CompleteDataset.csv')
    df = df.fillna(0)
    data = Data(df)
    data.generate_data_set()
