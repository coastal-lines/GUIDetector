import json
from Helpers.Json.PatternsModel import Element

with open(r"c:\Temp\Photos\data\json.json") as jsonfile:
    my_json = json.load(jsonfile)
my_object = Element(my_json)
t=0