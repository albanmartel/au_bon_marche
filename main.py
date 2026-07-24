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


def is_end_of_day(txt: str)->bool:
    test = False
    if (txt.upper() == "OUI" or txt.upper() == "O"):
        test = True
    else:
        test = False


def is_type_correct(texte: str, type_cible: str) -> bool:
    texte = texte.strip()

    if type_cible == "int":
        try:
            int(texte)
            return True
        except ValueError:
            raise ValueError("Saisie invalide : attendu un entier.")

    if type_cible == "float":
        try:
            float(texte)
            return True
        except ValueError:
            raise ValueError("Saisie invalide : attendu un float.")

    if type_cible == "str":
        # Une saisie est toujours une str (donc True si ce n'est pas vide ici)
        return len(texte) > 0

    raise ValueError("type_cible doit être 'int', 'float' ou 'str'.")


def main():
    print("AU BON MARCHé")
    shop = Class_Shop.Shop()
    # Initialiser le stock
    shop.f_create_stock()
    print("Un client entre dans le magazin")
    print("Bienvenue cher Client")
    surname = input("Quel est votre nom ? ")
    first_name = input("Quel est votre prénom ? ")
    print("Avez-vous un compte chez nous ?")
    yes_or_no = input("Oui(O)/Non(N): ")
    customer = None
    if is_customer(yes_or_no):
        customer = shop.f_find_customer_by_surname(surname)

    #Création du compte client
    if customer is None:
        customer = shop.f_create_customer(surname, first_name)
    # Création de la commande
    shop.f_create_order(customer.id_customer)
    print("Voici la liste des produits ?")
    # Imprimer la liste des produits
    for produit in shop.f_get_all_product_list():
        print(produit)
    print("Quel produit Voulez-vous acheter ?")
    txt = input ("Entrez le numéro de produit : ")



if __name__ == "__main__":
    main()