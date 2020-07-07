import json
from pickle import Unpickler, Pickler


with open('recips.json', 'r') as fp:
    recipes = json.load(fp)


with open('recipes_binary', 'wb') as fp:
    obj_recipes = Pickler(fp)
    obj_recipes.dump(recipes)

    
