#!/usr/bin/env python3
#-*-coding: utf-8 -*/-
from multiprocessing import process
from os import name
from typing import ClassVar
from dataclasses import dataclass
from datetime import datetime

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
        self.id = id
        self.surname = surname
        self.first_name = first_name
        self.creation_date = creation_date



if __name__ == "__main__":
    print("Test de la classe Customer")
    Customer("Martin", "Arthur", datetime.today().strftime('%Y-%m-%d %H:%M:%S'))