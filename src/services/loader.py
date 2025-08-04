import pandas as pd
import data

class Loader:
    @staticmethod
    def load():
        return pd.read_csv(r'C:\Users\HOME\PycharmProjects\Classification_of_antisemitism\data\tweets_dataset.csv')