#!/usr/bin/env python3
#-*-coding: utf-8 -*/-
from datetime import datetime
from typing import ClassVar
from dataclasses import dataclass

@dataclass
class Order:

    @classmethod
    def __init__(self, id_order: str, products: list, quantity_products: int, order_date: datetime) ->None:
        self.id_order = id_order
        self.products = products
        self.quantity_products = quantity_products
        self.order_date = order_date