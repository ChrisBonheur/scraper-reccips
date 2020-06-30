import logging as lg
import pickle

def writte_on_file_recip(name, category, person_number, direction, image_link, *ingredients):
    """This function writte or save recip on file recips"""
    #init dict for recips
    recips_dict = {}

    #read in recips dictionnary
    try:
        with open('recips', 'rb') as file_open:
            obj_unpickle = pickle.Unpickler(file_open)
            recips_dict = obj_unpickle.load()
            print("*********Le fichier \" recips \" a bien été ouvert********")
    except FileNotFoundError as e:
        lg.critical('File "recips" not found \n python message => {}'.format(e))
    except EOFError as eof:
        lg.warning('Le fichier a été trouvé vide')
    finally:
        #verify if recip title not in recips_dict_key
        if name not in recips_dict.keys():
            #add recip in recips dictionary
            recips_dict[name] = {'recip_category': category,
                            'recip_ingredients': ingredients,
                            'recip_person_number': person_number,
                            'recip_image_link': image_link,
                            'recip_direction': direction
                            }
            with open('recips', 'wb') as file_writte:
                obj_pickle = pickle.Pickler(file_writte)
                obj_pickle.dump(recips_dict)
                msg = print('\n \n ***La recette "{}" a bien été ajoué***\
                    \n\n***FIN DU PROGRAMME***'.format(name))
        else:
            msg = lg.warning('\n \n ***La recette "{}" existe déjà.***\
                 \n \n***FIN DU PROGRAMME***'.format(name))

        return msg
