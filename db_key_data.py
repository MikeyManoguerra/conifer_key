import json
import pprint
with open("djangoPinusKey.json", 'r') as read_file:
    Pinus_Key = json.load(read_file)



with open("djangoPinus.json", 'r') as read_file:
    Pinus_List = json.load(read_file)


# create temp dict object that simulates the keys in database
pk_dict = {}
for tree in Pinus_List:
    t = tree['scientific_name']
    pk_dict.update({tree['scientific_name']: Pinus_List.index(tree)})


# takes json with tree names and replaces it with primary keys of trees in DB
for node in Pinus_Key:
    for key, value in node.items():
        if key == 'child_a':
            if value == 'PinusGenus':
                this_tree = node['object_id_a']
                node['object_id_a'] = pk_dict[this_tree]
        if key == 'child_b':
           if value == 'PinusGenus':
               this_tree = node['object_id_b']
               node['object_id_b'] = pk_dict[this_tree]        

# pp = pprint.PrettyPrinter(depth=5)
# pp.pprint(Pinus_Key)

# seperation of files for future understandabiityy
with open('finalDicotKey.json', 'w') as write_file:
    json.dump(Pinus_Key, write_file)

