#!/usr/bin/env python3
#-*-coding: utf-8 -*/-
from multiprocessing import process
from os import name
from typing import ClassVar
from dataclasses import dataclass

@dataclass
class Product:
    products: ClassVar[list[Product]] = []

    @classmethod
    def get_products(cls) -> list[Product]:
        return cls.product

    def __init__(self, name: str, type: str, unit: str, price: float | int, stock: int ) -> None:
        """
        function init
        allow to initialize the product class
        :param name: The name of the product
        :param type: The type of product
        :param unit: The unit of the product
        :param price: The price of the product
        :param stock: The stock of the product
        """
        self.id = id
        self.name = name
        self.type = type
        self.unit = unit
        self.stock = stock
        self.price = price
        self.stock = stock
        Product.products.append(self)

    @property
    def name(self) -> str:
        return self.name


    @name.setter
    def name(self, value: str) -> None:
        self._name = value


    @property
    def type(self) -> str:
        return self.type


    @type.setter
    def type(self, value: str) -> None:
        self._type = value


    @property
    def unit(self) -> str:
        return self.unit


    @unit.setter
    def unit(self, value: str) -> None:
        self._unit = value


    @property
    def price(self) -> float | None:
        return self.price

    
    @price.setter
    def price(self, value: float | None) -> None:
        self._price = value



