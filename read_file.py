from pickle import Unpickler, Pickler
import json
import logging as lg
from os import sys

sys.setrecursionlimit(2000)

recips = []

try:
    with open('recips.json') as fp:
        data = json.load(fp)
        for entry in data:
            recips.append(entry['recip'])
except FileNotFoundError as fne:
    lg.critical('File "recips.json" not found \n python message => {}'.format(e))
except EOFError as efe :
    lg.critical('Fichier vide \n python msg => {}'.format(efe))
else:
    # print(recettes)
    total_recettes = 0
    for recip in recips:
        total_recettes += 1
        #details ingredients from recips file
        recip_name = recip['name']
        recip_category = recip['category']
        recip_direction = recip['preparation']
        recip_direction = " ".join(recip_direction)
        recip_ingredients = recip['ingredients']
        recip_person_number = recip['person_number']
        recip_image_link = recip['url_image']

        # print('RECETTE N°{}'.format(i))
        print('Nom : {} \n'.format(recip_name))
        print('Categorie : {} \n'.format(recip_category))
        print('Nombre de personne(s) : {} \n'.format(recip_person_number))
        print('Ingredients : ')
        for ingredient in recip_ingredients:
            print('***{} \n'.format(ingredient))
        print('PREPARATION : \n {}'.format(recip_direction))
        print('Lien de l\'image : {}'.format(recip_image_link))

    print("Total recettes : {}".format(total_recettes))
