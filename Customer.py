#!/usr/bin/env python3
#-*-coding: utf-8 -*/-

from typing import ClassVar
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Customer:
    customers: ClassVar[list[Customer]] = []

    @classmethod
    def get_customers(cls) -> list:
        return cls._customers

    @classmethod
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

    def __str__(self):
        return f"client n°{self.id_customer} : {self.first_name} {self.surname} - Créé le {self.creation_date}"
