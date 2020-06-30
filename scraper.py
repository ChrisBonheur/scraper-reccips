#! /usr/bin/env python3
#coding:utf-8

import requests
from bs4 import BeautifulSoup
import re
import logging as lg
from pickle import Pickler

from module.writter import writte_on_file_recip

# url = 'https://larecette.net/les-recettes/gouter/'

# links_to_scrap = []
# page = 1
#
# while requests.get('{}/page/{}'.format(url, page)).ok:
#     response = requests.get('{}/page/{}/'.format(url, page))
#     soup = BeautifulSoup(response.text, 'lxml')
#     articles = soup.findAll('article')
#
#     for article in articles:
#         link_a = article.find('a', {'class': 'g1-frame'}).get('href')
#         links_to_scrap.append(link_a)
#     #debug
#     print('Page n°: {} scrapé !'.format(page))
#     #incremete i
#     page += 1
#
# with open('links_to_scrap', 'wb') as file_writte:
#     obj = Pickler(file_writte)
#     obj.dump(links_to_scrap)
#
# print("****************Fin d'ajout des urls à scraper**********")



for link in links_to_scrap:
    url = link

    response = requests.get(url)

    if response.ok:
        #get global pagee
        soup = BeautifulSoup(response.text, "lxml")
        #get recipe title
        recip_title = soup.find('div', {'class': 'entry-inner'}).find('h1', {'class': 'entry-title'}).text
        #get recip category
        recip_category = 'Goûter'
        #get recip ingredients
        recip_ingredients_list = soup.find('div', {'class': 'entry-content'}).find('ul').findAll('li')
        recip_ingredients = []
        [recip_ingredients.append(ingredient.text) for ingredient in recip_ingredients_list]
        #number of person
        recip_person_number = soup.find('div', {'class': 'entry-content'}).find('em')
        #link of image
        recip_image_link = soup.find('div', {'class': 'g1-frame-inner'}).find('img', {'class': 'wp-post-image'}).get("src")
        #get recip direction of cooking
        recip_direction = soup.find('div', {'class': 'entry-content'}).select('p')[2:]
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
