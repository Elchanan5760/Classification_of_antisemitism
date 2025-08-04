
from src.data_exploration.exploration import ExploreData

class GroupData:
    @staticmethod
    def all_exploration(df):
        explore = ExploreData(df)
        my_dict = {
            "total_tweets": explore.count_categories(),
            "average_length": explore.min_text(),
            "common_words": explore.most_common_words(),
            "longest_3_tweets": explore.longest_text(),
            "uppercase_words": explore.uppercase_words()
        }
        return my_dict