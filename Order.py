#!/usr/bin/env python3
#-*-coding: utf-8 -*/-
from datetime import datetime
from typing import ClassVar
from dataclasses import dataclass

@dataclass
class Order:

    def __init__(self, id_order: str, quantity_products: int, order_date: datetime) ->None:
        self.id_order = id_order
        self.products = []
        self.quantity_products_ask = quantity_products
        self.order_date = order_date


    def f_add_product(self, product):
        self.products.append(product)


    def f_delete_product(self, product):
        self._products.remove(product)


    def __str__(self):
        return f"Commande n°{self.id_order}\nListe des produits: {self.products}\nNombre de produits {self.quantity_products_ask}\nCommande créé le {self.order_date}"
