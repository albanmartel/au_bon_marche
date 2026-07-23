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


    @classmethod
    def f_add_product(self, product):
        self.products.append(product)


    @classmethod
    def f_delete_product(self, product):
        self._products.remove(product)