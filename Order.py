#!/usr/bin/env python3
#-*-coding: utf-8 -*/-
from datetime import datetime

class Order:

    def __init__(self, id_order: str, order_date: datetime) ->None:
        self.id_order = id_order
        # liste de couples (id_product, quantité) car la quantité appartient à chaque ligne de commande
        self.products = []
        self.order_date = order_date

    def f_add_product(self, product_id: int, quantity: int):
        self.products.append((product_id, quantity))


    # suppression de tous les produit concernés, sur toutes les ligne de la commande, sans se preoccuper de la quantité demandée.
    # je reconstruit une liste sans les produits concernés
    # à activer si un client commande plus que le stock ou se trompe
    def f_delete_one_product(self, product_id: int):
        self.products = [
            (id_product, quantity)
            for id_product, quantity in self.products
            if id_product != product_id
        ]


