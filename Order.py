#!/usr/bin/env python3
#-*-coding: utf-8 -*/-
from datetime import datetime
import Product

class Order:

    def __init__(self, id_order: int, order_date: datetime) ->None:
        self.id_order = id_order
        # dico (id_product, quantité) car la quantité appartient à chaque produit
        self.products = {}
        self.order_date = order_date
        self.is_finished = False
        self.order_price = 0


    # à laisser ici car le produit appartient à une commande
    def f_add_product(self, product, quantity: int):
        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity

    def f_add_product_quantity_price(self, product, quantity: int, price: float):
        if product in self.products:
            old_quantity = self.products[product][0]
            new_quantity = old_quantity + quantity
            self.products[product] = (new_quantity, price)
        else:
            self.products[product] = (quantity, price)


    def f_delete_one_product(self, product):
        if product in self.products:
            del self.products[product]

    def __str__(self):
        txt_products = ""
        for product in self.products:
            quantity = self.products[product]
            txt_products += (
                f"Produit : {product.name}\n"
                f"Quantité : {quantity}\n"
            )
        return (
            f"Commande n°{self.id_order}\n"
            f"Le(s) produit(s):\n{txt_products}"
            f"\nCommande créée le: {self.order_date}"
        )

    def display_products_quantity_and_price(self):
        txt_products = ""
        print(self.products)
        for product in self.products:
            quantity, price = self.products[product]

            txt_products += (
                f"\nProduit : {product.name}\n"
                f"Quantité : {quantity}\n"
                f"Prix/unité : {price} €\n"
            )

        return (
            f"Commande n°{self.id_order}\n"
            f"Le(s) produit(s):\n{txt_products}"
            f"\nCommande créée le: {self.order_date}"
        )

    def calculate_total_price(self) -> None:
        total_price = 0

        for product in self.products:
            quantity, price = self.products[product]

            total_price += quantity * price

        self.order_price = total_price


    @property
    def order_price(self) -> float:
        return self._order_price


    @order_price.setter
    def order_price(self, price: float) -> None:
        self._order_price = price



