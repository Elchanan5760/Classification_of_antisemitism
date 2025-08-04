from src.load_data.loader import Loader
from src.data_exploration.exploration import ExploreData
if __name__ == "__main__":

    o1 = ExploreData(Loader.load())
    o1.count_category()
    o1.min_text()
    o1.longest_text()
    o1.most_common_words()
    o1.uppercase_words()