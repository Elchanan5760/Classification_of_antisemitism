import pandas as pn
class Cleaner:
    def __init__(self,df):
        self.df = df

    def drop_punctuation(self):
