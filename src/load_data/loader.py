import pandas as pd

class Loader:
    @staticmethod
    def load():
        return pd.read_csv('data/tweets_dataset.csv')