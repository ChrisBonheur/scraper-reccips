from pickle import Unpickler

with open('recips', 'rb') as file_read:
    obj_read = Unpickler(file_read)
    recettes = obj_read.load()

# print(recettes)
i = 0
for name, content in recettes.items():
    i += 1
    #details ingredients from recips file
    recip_name = name
    recip_category = content['recip_category']
    recip_direction = content['recip_direction']
    recip_direction = " ".join(recip_direction)
    recip_ingredients = content['recip_ingredients']
    recip_person_number = content['recip_person_number']
    recip_image_link = content['recip_image_link']
    
    print('RECETTE N°{}'.format(i))
    print('Nom : {} \n'.format(recip_name))
    print('Categorie : {} \n'.format(recip_category))
    print('Nombre de personne(s) : {} \n'.format(recip_person_number))
    print('Ingredients : ')
    for ingredient in recip_ingredients:
        print('***{} \n'.format(ingredient))
    print('PREPARATION : \n {}'.format(recip_direction))
    print('Lien de l\'image : {}'.format(recip_image_link))
