#!/usr/bin/env python3
#-*-coding: utf-8 -*/-
from multiprocessing import process
from os import name
from typing import ClassVar
from dataclasses import dataclass
from datetime import datetime

# Pour générer un id
import uuid

@dataclass
class Customer:

    def __init__(self, surname, first_name, creation_date):
        self.id = str(uuid.uuid4().hex)
        self.surname = surname
        self.first_name = first_name
        self.creation_date = creation_date



if __name__ == "__main__":
    print("Test de la classe Customer")
    Customer("Martin", "Arthur", datetime.today().strftime('%Y-%m-%d %H:%M:%S'))