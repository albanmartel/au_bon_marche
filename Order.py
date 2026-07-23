#!/usr/bin/env python3
#-*-coding: utf-8 -*/-
from datetime import datetime
import Product

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


    def f_add_product_quantity_price(self, product_id: int, quantity: int, price: float):
        if product_id in self.products:
            old_quantity = self.products[product_id][0]
            new_quantity = int(old_quantity) + quantity
            self.products[product_id] += str(new_quantity), str(price)
        else:
            self.products[product_id] = str(quantity), str(price)


    def f_delete_one_product(self, product_id: int):
        if product_id in self.products:
            del self.products[product_id]


    def __str__(self):
        txt_products = ""
        print(self.products)
        for product in self.products:
            tuple_product = self.products[product]
            txt_products += f"Id_product: {str(product)}\nQuantité: {str(tuple_product[0])}\nPrix/unité:{str(tuple_product[1])} €\n"

        return f"Commande n°{self.id_order}\nLe(s) produit(s): {txt_products}\nCommande créé le: {self.order_date}"
    


if __name__ == "__main__":
    print("Test la Classe Order")
    order = Order("01", datetime.today())
    #product = Product(1, "Mandarine", "Fruit", 6, 2.8, "kg")
    #order.f_add_product(1, 5)
    # Mandarine
    order.f_add_product_quantity_price(1,5, 2.8)
    # Epinard
    order.f_add_product_quantity_price(2, 4, 2.8)

    print(order)

