import json
from Helpers.Json.LabeledData import OriginalElement, LabeledData


def OpenJsonFile():
    with open(r"c:\Temp\Photos\data\json.json") as jsonfile:
        my_json = json.load(jsonfile)
    my_object = LabeledData(my_json)
    return my_object