import pprint
import json
from constants import *
 
with open ("pinaceaeFile.json", 'r') as read_file:
    Pinaceae_Dictionary = json.load(read_file)

Eastern_American_Pines = {
    'Pinus strobus': Pinaceae_Dictionary['Pinus']['species']['Pinus strobus'],
    'Pinus rigida': Pinaceae_Dictionary['Pinus']['species']['Pinus rigida'],
    'Pinus serotina': Pinaceae_Dictionary['Pinus']['species']['Pinus serotina'],
    'Pinus taeda': Pinaceae_Dictionary['Pinus']['species']['Pinus taeda'],
    'Pinus palustris': Pinaceae_Dictionary['Pinus']['species']['Pinus palustris'],
    'Pinus banksiana': Pinaceae_Dictionary['Pinus']['species']['Pinus banksiana'],
    'Pinus sylvestris': Pinaceae_Dictionary['Pinus']['species']['Pinus sylvestris'],
    'Pinus nigra nigra': Pinaceae_Dictionary['Pinus']['species']['Pinus nigra nigra'],
    'Pinus resinosa': Pinaceae_Dictionary['Pinus']['species']['Pinus resinosa'],
    'Pinus pungens': Pinaceae_Dictionary['Pinus']['species']['Pinus pungens'],
    'Pinus virginiana': Pinaceae_Dictionary['Pinus']['species']['Pinus virginiana'],
    'Pinus echinata': Pinaceae_Dictionary['Pinus']['species']['Pinus echinata'],
    'Pinus glabra': Pinaceae_Dictionary['Pinus']['species']['Pinus glabra'],
    # 'Pinus clausa'  : Pinaceae_Dictionary['Pinus']['species']['Pinus clausa'],
    'Pinus elliotii': Pinaceae_Dictionary['Pinus']['species']['Pinus elliotii'],
}
with open('pinusFile.json', 'w') as write_file:
  json.dump(Eastern_American_Pines, write_file)



with open ('easternPinusSummaries.json', 'r') as read_file:
    Eastern_Pinus_Summaries = json.load(read_file)

class PinusSpecies:
    kind = 'Pinus'
    def __init__(self, species):
        self.species = species
        self.common_name = ''
        self.scientific_name = ''
        self.characteristics = {}

    def define_common_name(self, name):
        self.common_name = name

    def define_scientific_name(self, name):
        self.scientific_name = name

    def define_characteristics(self, characteristics):
        for key, value in characteristics.items():
            self.characteristics[key] = value
    
    def add_summary(self, summary):
        self.characteristics[long_desc] = summary

    def display_characteristics(self):
        print('The tree your entries keyed out is ' +
              '\n\n' + self.scientific_name + '\n') #
        print('Its common name is ' + self.common_name)#
        print('The distribution of this tree is ' +
              self.characteristics[distribution])#
        print('There are '+self.characteristics[needle_count] +
              ' needles per cluster and the needle length is ' + self.characteristics[needle_length]+' inches.')
        if self.characteristics[cone_length] == True:
            print('Cones are longer than three inches')
        if self.characteristics[cone_length] == False:
            print('Cones are shorter than three inches')
        if self.characteristics[cone_length] == BOTH:
            print('Cones can be larger or smaller than three inches')
        if self.characteristics[cone_shape] == True:
            print('Cones are longer than they are wide')
        if self.characteristics[cone_shape] == False:
            print('cones are wider than they are long')
        if self.characteristics[cone_shape] == ROUND:
            print('Cones are fairly round in shape')
        if self.characteristics[cone_prickles] == STOUT:
            print('The cones have stout prickles')
        if self.characteristics[cone_prickles] == THIN:
            print('The cones have thin prickles')
        if self.characteristics[cone_prickles] == THIN_LACKING:
            print('The cones range thin prickles to lacking prickles')
        if self.characteristics[cone_prickles] == LACKING:
            print('The cones lack prickles')
        if self.characteristics[old_cones] == True:
            print('There may be many old cones on the tree')
        else:
            print('old cones do not persist on the tree')
        if self.characteristics.get(twig_texture) != None:
            if self.characteristics[twig_texture] == True:
                print('Twigs are textured or rough near the needle attachment')
            else:
                print('Twigs lack texture or are smooth near needle attachment')
        if self.characteristics[fire_resislience] == True:
            print('The trunk may sprout again after a fire')
        if self.characteristics[fire_resislience] == False:
            print('This species is not known to sprout again after fire damage')

    def display_summary(self):
        if self.characteristics.get(long_desc) != None:
            print(self.characteristics[long_desc])

def buildClassDictionary(data_object, empty_di):
    """builds dictionary of classes with pre built data object"""
    for key, value in data_object.items():
        new_species = value
        species_name = key
        species_name = PinusSpecies(new_species['scientific name'])
        species_name.define_common_name(new_species['common name'])
        species_name.define_scientific_name(new_species['scientific name'])
        species_name.define_characteristics(new_species['characteristics'])

        empty_di[key] = species_name
    built_di = empty_di
    return built_di

def addSummariesToClassItems(genus_dict, summary_dict):
     for species_name, species_class_object in genus_dict.items():
        species_class_object.add_summary(summary_dict[species_name])

Pinus_Genus_Dictionary = {}
buildClassDictionary(Eastern_American_Pines, Pinus_Genus_Dictionary)
addSummariesToClassItems(Pinus_Genus_Dictionary, Eastern_Pinus_Summaries)
pp = pprint.PrettyPrinter(depth=5)
# pp.pprint(Pinus_Genus_Dictionary)
a = 'a'
b = 'b'
choose_a = 'choose_a'
choose_b = 'choose_b'
parent = 'parent'
current = 'current'

pinus_binary_location = {
    11: {
        a: '2 neeedles per cluster (if mix of two and three pick this)',
        b: 'more than two needles per cluster',
        choose_a: 21,
        choose_b: 22,
        parent: 'HEAD',
        current: 11
    },
    21: {
        a: 'cone prickles stout, all or some cones larger than 3 inches',
        b: ' cones smaller three inches, cone prickles thin or lacking ',
        choose_a: 31,
        choose_b: 32,
        parent: 11,
        current: 21

    },
    31: {
        a: 'cones longer than wide',  # elliotii
        b: 'cones wider than long or round on average',
        choose_a: 'Pinus elliotii',
        choose_b: 41,
        parent: 21,
        current: 31
    },
    41: {
        a: 'many old cones on tree',  # pungens
        b: ' not many old cones on tree',  # nigra
        choose_a: 'Pinus pungens',
        choose_b: 'Pinus nigra nigra',
        parent: 31,
        current: 41
    },
    32: {
        a: 'twigs rough near needles',
        b: ' twigs more smooth near needles',
        choose_a: 42,
        choose_b: 43,
        parent: 21,
        current: 32
    },
    42: {
        a: 'needles very short 1.5 -2 inches',  # banksiana
        b: 'needles 3-5 inches',  # echinata
        choose_a: 'Pinus banksiana',
        choose_b: 'Pinus echinata',
        parent: 32,
        current: 42
    },
    43: {
        a: 'many old cones on tree',
        b: 'not many old cones on tree',
        choose_a: 51,
        choose_b: 52,
        parent: 32,
        current: 43
    },
    51: {
        a: 'middle states,branches very fiberous, tough to break',  # virginiana
        b: 'southern state, broad leaf forest',  # glabra
        choose_a: 'Pinus virginiana',
        choose_b: 'Pinus glabra',
        parent: 43,
        current: 51
    },
    52: {
        a: 'tree needles 2-3 inches long',  # sylvestris
        b: 'tree needles 4-6 inches long',  # resinosa
        choose_a: 'Pinus sylvestris',
        choose_b: 'Pinus resinosa',
        parent: 43,
        current: 52
    },
    22: {
        a: 'Needles in bundles of 5',  # strobis
        b: 'Needles in bundles of 3-4',
        choose_a: 'Pinus strobus',
        choose_b: 33,
        parent: 11,
        current: 22
    },
    33: {
        a: 'cones more than three inches long',
        b: 'cones less than three inches long',
        choose_a: 44,
        choose_b: 45,
        parent: 22,
        current: 33
    },
    44: {
        a: 'needles 6-9 inches long, end buds brown',  # taeda
        b: 'needles 8-18 inches long, end buds white',  # paulustis
        choose_a: 'Pinus taeda',
        choose_b: 'Pinus palustris',
        parent: 33,
        current: 44
    },
    45: {
        a: 'cone prickles stout, located in northern or middle states',  # rigida
        b: 'cone prickles this or absent, located southern states',  # serotina
        choose_a: 'Pinus rigida',
        choose_b: 'Pinus serotina',
        parent: 33,
        current: 45
    }
}




#####Tree out of scope for now#######
# 'Pinus clausa
# {'dist': SOUTH,
#  'needle length': 2-4,
#  'twigs rough near needle': False,
#  'many old cones on tree': True,
#  'cones longer than three inches': False,
#  'cones longer than wide': ROUND,
#  'cone prickle type': STOUT
#  }
