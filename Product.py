#!/usr/bin/env python3
#-*-coding: utf-8 -*/-

from dataclasses import dataclass

class Product:

    def __init__(self, id: str, name: str, type: str, stock: int, price: float | int, unit: str ) -> None:
        """
        function init
        allow to initialize the product class
        :param name: The name of the product
        :param type: The type of product
        :param unit: The unit of the product
        :param price: The price of the product
        :param stock: The stock of the product
        """
        self.id_product = id
        self.name = name
        self.type = type
        self.stock = stock
        self.price = price
        self.unit = unit

    def __str__(self):
        return (
            f"Produit n°{self.id_product} : "
            f"{self.name} "
            f"({self.type}) - "
            f"{self.stock} {self.unit} - "
            f"{self.price} €"
        )

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

    # c'est au produit de verifier la quantité disponible
    def f_has_enough_stock(self, quantity):
        if  self.stock >= quantity
            return self.stock >= quantity
        return None


if __name__ == "__main__":
    print("Test de la classe Product")
    product = Product(1,"Mandarine", "Fruit", 6", 2.8, "kg")
    print(f"Nom: {product.name}")
    print(f"Type: {product.type}")
    print(f"Unité: {product.unit}")
    print(f"Prix: {product.price}")
    print(f"Stock: {product.stock} {product.unit}")

