#!/usr/bin/env python3
#-*-coding: utf-8 -*/-
from multiprocessing import process
from os import name
from typing import ClassVar
from dataclasses import dataclass

# Pour générer un id
import uuid

@dataclass
class Product:
    products: ClassVar[list[Product]] = []

    @classmethod
    def get_products(cls) -> list[Product]:
        return cls.product

    def __init__(self, name: str, type: str, stock: int, price: float | int, unit: str ) -> None:
        """
        function init
        allow to initialize the product class
        :param name: The name of the product
        :param type: The type of product
        :param unit: The unit of the product
        :param price: The price of the product
        :param stock: The stock of the product
        """
        self.id = str(uuid.uuid4().hex)
        self.name = name
        self.type = type
        self.stock = stock
        self.price = price
        self.unit = unit
        Product.products.append(self)

    @property
    def name(self) -> str:
        return self._name


    @name.setter
    def name(self, value: str) -> None:
        self._name = value


    @property
    def type(self) -> str:
        return self._type


    @type.setter
    def type(self, value: str) -> None:
        self._type = value


    @property
    def unit(self) -> str:
        return self._unit


    @unit.setter
    def unit(self, value: str) -> None:
        self._unit = value


    @property
    def price(self) -> float | None:
        return self._price


    @price.setter
    def price(self, value: float | None) -> None:
        self._price = value


    @property
    def stock(self) -> int | None:
        return self._stock


    @stock.setter
    def stock(self, value: int) -> None:
        self._stock = value


if __name__ == "__main__":
    print("Test de la classe Product")
    product = Product("Mandarine", "Légume", "6", "2.8", "kg")
    print(f"Nom: {product.name}")
    print(f"Type: {product.type}")
    print(f"Unité: {product.unit}")
    print(f"Prix: {product.price}")
    print(f"Stock: {product.stock} {product.unit}")

