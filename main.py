#!/usr/bin/env python3
#-*-coding: utf-8 -*/-

"""
Ce fichier est le fichier de lancement de l'applications
" Au BON MARCHE"
Il permet d'utiliser toutes les classes créés
dans le répertoire du projet
@projet de l'académie FMS Python JAVA
Philippe PEYROUS
Alban MARTEL
"""
import Class_Shop

def is_customer(txt: str)->bool:
    test = False
    if (txt.upper() == "OUI" or txt.upper() == "O"):
        test = True
    else:
        test = False

    return test


def main():
    print("AU BON MARCHé")
    shop = Class_Shop.Shop()
    # Initialiser le stock
    shop.f_create_stock()
    print("Un client entre dans le magazin")
    print("Bienvenue cher Client")
    print("Avez-vous un compte chez nous ?")
    yes_or_no = input("Oui(O)/Non(N): ")
    surname = input("Quel est votre nom ?")
    first_name = input("Quel est votre prénom ?")
    customer = None
    if is_customer(yes_or_no):
        customer = shop.f_find_customer_by_surname(surname)

    if customer is None:
        customer = shop.f_create_customer(surname, first_name)
    print("Que voulez-vous acheter ?")




if __name__ == "__main__":
    main()