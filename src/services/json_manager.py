import json
from src.data_exploration.grouping import GroupData

class OnJson:
    @staticmethod
    def dumps_json(my_dict):
        try:
            json_object = json.dumps(my_dict, indent=4)
            with open(r"C:\Users\HOME\PycharmProjects\Classification_of_antisemitism\results\exploration.json", "w") as outfile:
                outfile.write(json_object)
        except Exception as ex:
            print(f"Error: {ex}")