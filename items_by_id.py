#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Developer: Victor Vivas mail: victorhvivascit@gmail.com
# Date: 04_02_2021
import argparse
import json
import requests
import logging
#============================================================================================================================
#============================================== DEFINING ARGUMENTS ==========================================================
#============================================================================================================================

parse = argparse.ArgumentParser()
parse.add_argument("-se", "--seller", help="string with de seller id")
parse.add_argument("-si", "--site", help="string with de site id")
parse.add_argument("-m", "--multiple", help="Indicates that multiple sites/sellers will be sent, this must be separate by .")

#============================================================================================================================
#============================================== DEFINING FUNCTIONS ==========================================================
#============================================================================================================================


def get_category(dictionary, category_id, url="https://api.mercadolibre.com/categories/"):
    """Search in a dict the name of the category id and if not is there make a request in web"""
    if dictionary.get(category_id, False):
        name = dictionary[category_id]
    else:
        consulta = requests.get(url+category_id)
        consulta = json.loads(consulta.text)
        name = consulta["name"]
    return name


def get_caterories(url="https://api.mercadolibre.com/sites/MLA/categories"):
    """Get a list of categories and create and return a dictionary to consult later"""
    categories = requests.get(url)
    categories = json.loads(categories.text)
    categories_dict = {}
    for x in categories:
        categories_dict[x["id"]] = x["name"]
    return categories_dict


def get_products(site, user):
    """Get a request to with site id and seller id from the products of the same"""
    response = requests.get(f"https://api.mercadolibre.com/sites/{site}/search?seller_id={user}")
    response = response.text
    response = json.loads(response)
    response = response["results"]
    return response

#============================================================================================================================
#================================================   STARTING APP   ==========================================================
#============================================================================================================================


if __name__ == "__main__":
    args = parse.parse_args()
    try:
        if args.multiple and args.multiple.upper() == "YES":
            usrs = zip(args.seller.split("."), args.site.split("."))  # this can be improved, now the order its important.
            for x in usrs:
                logging.basicConfig(level=logging.INFO, filename=f"output_{x[0]}.log")
                log = logging.getLogger(f"Seller= {x[0]}")
                log.setLevel("INFO")
                resultados = get_products(x[1], x[0])
                categorias = get_caterories()
                log.info("id | title| category_id | name_category")
                for x in resultados:
                   id = x["id"]
                   title = x["title"]
                   category_id = x["category_id"]
                   name = get_category(categorias, x["category_id"])
                   log.info(f"{id}| {title}| {category_id}| {name}")
                   print(f"{id}| {title}| {category_id}| {name}")
        else:
            logging.basicConfig(level=logging.INFO, filename=f"log_{args.seller}.log")
            log = logging.getLogger(f"Seller= {args.seller}")
            log.setLevel("INFO")
            resultados = get_products(args.site, args.seller)
            categorias = get_caterories()
            log.info("id | title| category_id | name_category")
            for x in resultados:
                id = x["id"]
                title = x["title"]
                category_id = x["category_id"]
                name = get_category(categorias, x["category_id"])
                log.info(f"{id}| {title}| {category_id}| {name}")
                print(f"{id}| {title}| {category_id}| {name}")
    except Exception as e:
        print("Ocurrio una excepcion y se detuvo el proceso")
        log.error("Ocurrio una excepcion y se detuvo el proceso, por favor revise los datos suministrados")
