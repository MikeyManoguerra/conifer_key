import json
from constants import *
import pprint


with open("pinusFile.json", 'r') as read_file:
    Pinus_Dictionary = json.load(read_file)

with open("easternPinusSummaries.json", 'r') as read_file:
    Pinus_Summaries = json.load(read_file)

for key, value in Pinus_Dictionary.items():
    value['characteristics'].pop('short description', None)
    value['characteristics'].pop('full description', None)

for key, value in Pinus_Dictionary.items():
    value['characteristics'].pop('short description', None)
    value['characteristics'].pop('short description', None)
    value['characteristics']['needle_count'] = value['characteristics']["needles per cluster"]
    value['characteristics'].pop("needles per cluster", None)
    value['characteristics']['needle_length'] = value['characteristics']["needle length"]
    value['characteristics'].pop("needle length", None)
    value['characteristics']['old_cones'] = value['characteristics']["many old cones on tree"]
    value['characteristics'].pop("many old cones on tree", None)
    value['characteristics']['cone_length'] = value['characteristics']["cones longer than three inches"]
    value['characteristics'].pop("cones longer than three inches", None)
    value['characteristics']['cone_shape'] = value['characteristics']["cones longer than wide"]
    value['characteristics'].pop("cones longer than wide", None)
    value['characteristics']['cone_prickles'] = value['characteristics']["cone prickle type"]
    value['characteristics'].pop("cone prickle type", None)
    fire_variable = value['characteristics'].get(
        "trunk sprouts after fire", 1)
    value['characteristics']['fire_resilience'] = fire_variable
    value['characteristics'].pop("trunk sprouts after fire", None)
    twig_variable = value['characteristics'].get(
        "twigs rough near needle", 1)
    value['characteristics']['twig_texture'] = twig_variable
    value['characteristics'].pop('twigs rough near needle', None)

for key, value in Pinus_Dictionary.items():
    for sum_key, sum_value in Pinus_Summaries.items():
        if key == sum_key:
            value['characteristics']['description'] = sum_value

pp = pprint.PrettyPrinter(depth=5)
# pp.pprint(Pinus_Dictionary)


with open('djangoPinus.json', 'w') as write_file:
  json.dump(Pinus_Dictionary, write_file)
