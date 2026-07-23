#!/usr/bin/env python3
#-*-coding: utf-8 -*/-

from typing import ClassVar
from dataclasses import dataclass
from datetime import datetime
import Order


@dataclass
class Customer:

    def __init__(self, id: str, surname: str, first_name: str, creation_date: datetime) ->None:
        """
        Function init de la classe Customer
        constructor de la classe Customer
        :param id: id of the customer
        :param surname: The surname of the customer
        :param first_name: The first name of the customer
        :param creation_date: Date of customer creation
        """
        self.id_customer = id
        self.surname = surname
        self.first_name = first_name
        self.creation_date = creation_date
        self.order = []

    def __str__(self):
        return f"client n°{self.id_customer} : {self.first_name} {self.surname} - Créé le {self.creation_date}"


    def f_add_order(self, order: Order) -> None:
        self.order.append(order)


if __name__ == "__main__":
    customer = Customer("01", "Martin", "Arthur", "2021-07-07")
    print(customer)
    print(customer.id_customer)
    print(customer.surname)
    print(customer.first_name)
