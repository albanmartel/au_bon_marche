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
    """
    fonction is_customer
    poermet de demander au client s'il a déjà un compte client
    ou pas
    :param txt: texte attendu "Oui" ou  "OUI" ou "O" ou autrechose veut dire "Non"
    :return: Vrai ou Faux
    """
    test = False
    if (txt.upper() == "OUI" or txt.upper() == "O"):
        test = True
    else:
        test = False

    return test


def is_end_of_day(txt: str)->bool:
    """
    fonction is_end_of_day
    permet de dire si l'on est en fin de journée
    pour imprimer le bilan
    :param txt: texte attendu "Oui" ou  "OUI" ou "O" ou autrechose veut dire "Non"
    :return: Vrai ou Faux
    """
    test = False
    if (txt.upper() == "OUI" or txt.upper() == "O"):
        test = True
    else:
        test = False


def is_type_correct(texte: str, type_cible: str) -> bool:
    """
    fonction is_type_correct
    permet de contrôler la saisie d'un input
    en lui donnant le contenu récupéré par l'input et le type attendu de la saisie
    :param texte: texte de l'input
    :param type_cible: type appendu sous forme de chaîne de caractère "int", "float", "str
    :return: Vrai ou Faux et affiche une erreur quand une exception est levée
    """
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


def create_customer_Sophie(shop: Class_Shop) ->None:
    # Création d'un client
    customer_sophie = shop.f_create_customer("Delatour", "Sophie")
    #customer_sophie = shop.f_find_customer_by_surname("Delatour")
    print(f"Id de Sophie : {customer_sophie.id_customer}")
    order_sophie = shop.f_create_order(customer_sophie)
    # Ajouter des mandarines à la commande de Sophie
    order_sophie.f_add_product_quantity_price(1, 5, 2.8)
    # Ajouter des épinards à la commande de Sophie
    order_sophie.f_add_product_quantity_price(2, 4, 2.8)
    # retirer un kilo d'épinards à la commande de Sophie
    order_sophie.f_delete_one_product(1)
    print(f"La/Le client(e): {customer_sophie}")
    print(f"Elle a une commande de {order_sophie.display_products_quantity_and_price()}")
    order_sophie.calculate_total_price()
    print(f"Elle doit {order_sophie.order_price} €")



def main():
    print("AU BON MARCHé")
    shop = Class_Shop.Shop()
    # Initialiser le stock
    shop.f_create_stock()
    # Refactorisation de la cliente Sophie
    create_customer_Sophie(shop)
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
    # Vérification de la saisie numéro de produit
    while not is_type_correct(txt, "int"):
        print("Un entier était attendu !")
        txt = input ("Entrez le numéro de produit : ")
    print(f"Vous avez choisi {shop.f_find_product_by_id(txt)}")
    # trouver un produit par id ne fonctionne pas pour l'instant

if __name__ == "__main__":
    main()