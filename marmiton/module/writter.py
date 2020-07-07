import logging as lg
import pickle
import json
from os import sys

sys.setrecursionlimit(2000)

def writte_on_file_recip(name, category, person_number, direction, image_link, *ingredients):
    """This function writte or save recip on file recips"""
    #init dict for recips
    data = []
    total_scraped = 0
    #read in recips dictionnary
    try:
        with open('recips.json', 'rb') as fp:
            data = json.load(fp)
        print("*********Le fichier \" recips \" a bien été ouvert********")
    except FileNotFoundError as e:
        lg.critical('File "recips" not found \n python message => {}'.format(e))
    except EOFError as eof:
        lg.warning('Le fichier a été trouvé vide')
    finally:
        #verify if recip title not in recips_dict_key
        names_of_recip = []
        for entry in data:
            names_of_recip.append(entry['recip']['name'])
        if name not in names_of_recip:
            #add recip in recips dictionary
            data.append({'recip': {'name': name,
                                   'category': category,
                                   'person_number': person_number,
                                   'ingredients': ingredients,
                                   'preparation': direction,
                                   'url_image': image_link,
                                   }
                                });
            with open('recips.json', 'wb') as file_writte:
                json.dumps(data, file_writte)
                msg = print('\n \n ***La recette "{}" a bien été ajoué***\
                    \n\n***FIN DU PROGRAMME***'.format(name))
        else:
            msg = lg.warning('\n \n ***La recette "{}" existe déjà.***\
                 \n \n***FIN DU PROGRAMME***'.format(name))

        return msg
