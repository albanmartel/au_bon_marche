#!/usr/bin/env python3
#-*-coding: utf-8 -*/-
from datetime import datetime

class Order:

    def __init__(self, id_order: str, order_date: datetime) ->None:
        self.id_order = id_order
        # dico (id_product, quantité) car la quantité appartient à chaque produit
        self.products = {}
        self.order_date = order_date


    def f_add_product(self, product_id: int, quantity: int):
        if product_id in self.products:
            self.products[product_id] += quantity
        else:
            self.products[product_id] = quantity

    def f_delete_one_product(self, product_id: int):
        if product_id in self.products:
            del self.products[product_id]

    def __str__(self):
        txt_products = ""
        for product in self.products:
            txt_products += product.__str__() + " "

        return f"Commande n°{self.id_order}\nListe des produits: {txt_products}\nNombre de produits: {self.quantity_products_ask}\nCommande créé le: {self.order_date}"

if __name__ == "__main__":
    order = Order("01", 0, datetime.today())
    print(order)

