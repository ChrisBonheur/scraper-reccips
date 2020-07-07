#! /usr/bin/env python3
#coding:utf-8

import requests
from bs4 import BeautifulSoup
import re
import logging as lg
from pickle import Unpickler, Pickler
# from time import sleep
# from os import sys

from module.writter import writte_on_file_recip

links_to_scrap = []
try:
    with open('new_links', 'rb') as fp:
        obj = Unpickler(fp)
        links_to_scrap = obj.load()
except FileNotFoundError as e:
    lg.warning('File not Found => {}'.format(e))

# url = 'https://www.marmiton.org/recettes/?type=platprincipal'
# page = 75
# while page <= 910:
#     response = requests.get(f'{url}&page={page}')
#     soup = BeautifulSoup(response.content, 'html.parser')
#     # print(soup)ok
#     recipes = soup.find_all(class_='recipe-card')
#     # print(recipes)ok
#     for recipe in recipes:
#         link_a = recipe.find('a').get('href')
#         if link_a not in links_to_scrap:
#             links_to_scrap.append(link_a)
#             with open('new_links', 'wb') as fp:
#                 obj = Pickler(fp)
#                 obj.dump(links_to_scrap)
#             print('ajouté')
#         else:
#             print('Déjà enregistré')
#     page += 1
#     print((f'Scrapé {page}'))


# sys.setrecursionlimit(1500)

# categories = "entre platprincipal dessert amusegueule sauce accompagnement boisson"
# categories = categories.split(" ")
recette = 0
for link in links_to_scrap:
    url = link
    response = requests.get(url)

    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        try:
            name = soup.find('div', {'class', 'content-recipe'}).find('h1', {'class', 'main-title'}).text
            categorie = 'Plat principal'
            ingredients = soup.find('ul', {'class', 'recipe-ingredients__list'}).find_all('li')
            ingredients = [ingredient.find('div').text for ingredient in ingredients]
            person_number = soup.find('div', {'class', 'recipe-infos__quantity'}).\
            find('span', {'class', 'title-2'}).text
            image_link = soup.find('picture').find('img').get('src')
            preparation = soup.find('ol', {'class', 'recipe-preparation__list'}).find_all('li')
            preparation = [direction.text for direction in preparation]

        except AttributeError as e:
            lg.warning('Attribute error => {}'.format(e))
        else:
            writte_on_file_recip(name, categorie, person_number, preparation, image_link, \
                                 ingredients)
            links_to_scrap.remove(link)
            with open('new_links', 'wb') as fp:
                obj = Pickler(fp)
                obj.dump(links_to_scrap)
            recette += 1
            print('Ajouté')
            print('Recette ajouté : {}'.format(recette))
