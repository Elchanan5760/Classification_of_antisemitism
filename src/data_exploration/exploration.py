import pandas as pd

class ExploreData:
    def __init__(self,df):
        self.df = df
        self.category_0 = self.df[self.df['Biased']==0]
        self.category_1 = self.df[self.df['Biased']==1]

    def count_category(self):#Counts how many rows each category.
        my_dict = {}
        my_dict['antisemitic'] = len(self.category_1)
        my_dict['non antisemitic'] = len(self.category_0)
        my_dict['total'] = len(self.df)
        my_dict['unspecified'] = len(self.df) - (len(self.category_0)+len(self.category_1))
        print(my_dict)
        return my_dict

    def min_text(self):#The average length of words in the text.
        my_dict = {}
        my_dict['total'] = float(self.df['Text'].apply(lambda t: len(str(t).split())).mean())
        my_dict['antisemitic'] = float(self.category_1['Text'].apply(lambda t: len(str(t).split())).mean())
        my_dict['non antisemitic'] = float(self.category_0['Text'].apply(lambda t: len(str(t).split())).mean())
        print(my_dict)
        return my_dict

    def longest_text(self):#Returns 3 longest texts for each category.
        my_dict = {}
        longest = self.category_0.sort_values(by='Text',axis=0).head(3)
        my_dict['antisemitic'] = self.category_1.sort_values(by='Text',axis=0).head(3)['Text'].tolist()
        my_dict['non antisemitic'] = self.category_0.sort_values(by='Text',axis=0).head(3)['Text'].tolist()
        print(my_dict)
        return my_dict

    def most_common_words(self):#Returns 10 most common words into a list.
        my_dict = {}
        my_dict['total'] = pd.Series(' '.join(self.df.Text).lower().split()).value_counts()[:10].keys().tolist()
        my_dict['antisemitic'] = pd.Series(' '.join(self.category_1.Text).lower().split()).value_counts()[:10].keys().tolist()
        my_dict['non antisemitic'] = pd.Series(' '.join(self.category_0.Text).lower().split()).value_counts()[:10].keys().tolist()
        print(my_dict)
        return my_dict

    def uppercase_words(self):#Returns the amount of words only with capital letters.
        my_dict = {}
        my_dict['total'] = int(pd.Series(' '.join(self.df.Text).split()).apply(lambda w: w.isupper()).value_counts()[True])
        my_dict['antisemitic'] = int(pd.Series(' '.join(self.category_1.Text).split()).apply(lambda w: w.isupper()).value_counts()[True])
        my_dict['non antisemitic'] = int(pd.Series(' '.join(self.category_0.Text).split()).apply(lambda w: w.isupper()).value_counts()[True])
        print(my_dict)
