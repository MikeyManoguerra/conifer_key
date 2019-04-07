import json
from constants import *
import pprint
from pinusKey import pinus_binary_location


with open("pinusFile.json", 'r') as read_file:
    Pinus_Dictionary = json.load(read_file)

with open("easternPinusSummaries.json", 'r') as read_file:
    Pinus_Summaries = json.load(read_file)

for key, value in Pinus_Dictionary.items():
    value['characteristics'].pop('short description', None)
    value['characteristics'].pop('full description', None)

for key, value in Pinus_Dictionary.items():
    value['scientific_name'] = value['scientific name']
    value['common_name'] = value['common name']
    value['needle_count'] = value['characteristics']["needles per cluster"]
    value['needle_length'] = value['characteristics']["needle length"]
    value['old_cones'] = value['characteristics']["many old cones on tree"]
    value['cone_length'] = value['characteristics']["cones longer than three inches"]
    value['cone_shape'] = value['characteristics']["cones longer than wide"]
    value['cone_prickles'] = value['characteristics']["cone prickle type"]
    fire_variable = value['characteristics'].get(
        "trunk sprouts after fire", 1)
    value['fire_resilience'] = fire_variable
    twig_variable = value['characteristics'].get(
        "twigs rough near needle", 1)
    value['twig_texture'] = twig_variable

    value.pop('characteristics', None)
    value.pop('scientific name', None)
    value.pop('common name', None)


for key, value in Pinus_Dictionary.items():
    for sum_key, sum_value in Pinus_Summaries.items():
        if key == sum_key:
            value['description'] = sum_value

pinus_genus_list = []
for key, value in Pinus_Dictionary.items():
    pinus_genus_list.append(value)


pp = pprint.PrettyPrinter(depth=5)
pp.pprint(Pinus_Dictionary)
with open('djangoPinus.json', 'w') as write_file:
    json.dump(pinus_genus_list, write_file)

for key, value in pinus_binary_location.items():
    value['id'] = key
    value['characteristic_a'] = value['a']
    value.pop('a', None)
    value['characteristic_b'] = value['b']
    value.pop('b', None)
    if type(value['choose_a']) == int:
        value['child_a']='self'
        value['object_id_a']=value['choose_a']
    elif type(value['choose_a']) == str :
        value['child_a']= 'PinusGenus'
        value['object_id_a'] =  value['choose_a']
    value.pop('choose_a', None)
    if type(value['choose_b']) == int:
        value['child_b']='self'
        value['object_id_b']=value['choose_b']
    elif type(value['choose_b']) == str:
        value['child_b']= 'PinusGenus'
        value['object_id_b'] = value['choose_b']# whatever the primary key from the other table is
    value.pop('choose_b', None)
    value.pop('current', None)

pp = pprint.PrettyPrinter(depth=5)
pp.pprint(pinus_binary_location)

# with open('djangoPinusKey.json', 'w') as write_file:
    # json.dump(, write_file)
