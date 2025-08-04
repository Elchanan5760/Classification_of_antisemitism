from src.services.loader import Loader
from src.data_exploration.grouping import GroupData
from src.services.json_manager import OnJson
if __name__ == "__main__":
    OnJson.dumps_json(GroupData.all_exploration(Loader.load()))