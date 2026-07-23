#!/usr/bin/env python3
#-*-coding: utf-8 -*/-
from datetime import datetime
from typing import ClassVar
from dataclasses import dataclass
import Product

@dataclass
class Order:

    def __init__(self, id_order: str, quantity_products: int, order_date: datetime) ->None:
        self.id_order = id_order
        self.products = []
        self.quantity_products_ask = quantity_products
        self.order_date = order_date


    def f_add_product(self, product: Product) -> None:
        self.products.append(product)
        self.quantity_products_ask += 1


    def f_delete_product(self, product: Product) -> None:
        self._products.remove(product)


    def __str__(self):
        txt_products = ""
        for product in self.products:
            txt_products += product.__str__() + " "

        return f"Commande n°{self.id_order}\nListe des produits: {txt_products}\nNombre de produits: {self.quantity_products_ask}\nCommande créé le: {self.order_date}"
