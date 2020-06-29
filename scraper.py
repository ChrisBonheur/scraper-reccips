#! /usr/bin/env python3
#coding:utf-8

import requests
from bs4 import BeautifulSoup
import re
import logging as lg

from module.writter import writte_on_file_recip

url = 'http://www.recettesafricaine.com/category/les-recettes-africaines'

response = requests.get(url)

if response.ok:
    #get global pagee
    soup = BeautifulSoup(response.text, "lxml")
    #get recipe title
    recip_title = soup.find('article', {'class': 'post-1419'}).find('h2', {'class': 'entry-title'}).text
    #get recip category
    recip_category = ''
    #get recip ingredients
    recip_ingredients_list = soup.find('article', {'class': 'post-1419'}).findAll('li')
    recip_ingredients = []
    [recip_ingredients.append(ingredient.text) for ingredient in recip_ingredients_list]
    #number of person
    recip_person_number = 4
    #link of image 
    recip_image_link = soup.find('article', {'class': 'post-1419'}).find('img', {'class': 'wp-image-1421'}).get("src")
    #get recip direction of cooking
    recip_direction = soup.find('article', {'class': 'post-1419'}).select('p')[6:9]
    bloc_text_direction = []
    for phrase in recip_direction:
        bloc_text_direction.append(phrase.text)
    recip_direction = bloc_text_direction

    #my debug
    print('Nom recette : ', recip_title, "\n \n")
    print('Tableau ingredients : ', ['   *{}'.format(ingredient) for ingredient in\
        recip_ingredients], '\n \n')
    print('Nombre de personne : ',recip_person_number, '\n \n')
    print('Lien image : ', recip_image_link, '\n \n')
    print('Préparation : ', recip_direction, '\n \n')

    #writte on file recips
    writte_on_file_recip(recip_title, 
                        recip_category,
                        recip_person_number, 
                        recip_direction, 
                        recip_image_link,
                        recip_ingredients)
else:
    lg.critical("Impossible de se connecter à la page")


