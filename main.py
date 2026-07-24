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

def main():
    print("AU BON MARCHé")
    shop = Class_Shop.Shop()
    # Initialiser le stock
    shop.f_create_stock()
    print("Un client entre dans le magazin")
    print("Bienvenue cher Client")
    name = input("Quel est votre nom ?")
    surname = input("Quel est votre prénom ?")
    print()


if __name__ == "__main__":
    main()