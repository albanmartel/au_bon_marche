#!/usr/bin/env python3
#-*-coding: utf-8 -*/-

from typing import ClassVar
from dataclasses import dataclass
from datetime import datetime
import Order
import Product


@dataclass
class Customer:

    def __init__(self, id: str, surname: str, first_name: str, creation_date: datetime, first_order_id) ->None:
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
        # Un client a au moins une commande
        self.order = [Order.Order(first_order_id, datetime.today())]

    def get_orders(self):
        return self.order


    def __str__(self):
        return f"client n°{self.id_customer} : {self.first_name} {self.surname} - Créé le {self.creation_date}"


    def f_add_order(self, order: Order) -> None:
        self.order.append(order)


    def f_delete_order(self, order: Order) -> None:
        self.order.remove(order)

    def f_find_order_by_id(self, order_id):
        for order in self.order:
            if order.id_order == order_id:
                return order
        return None


if __name__ == "__main__":
    customer = Customer("01", "Martin", "Arthur", "2021-07-07")
    product = Product.Product(1, "Mandarine", "Fruit", "6", 2.8, "kg")
    print(customer)
    order = Order.Order("01", 0, datetime.today())
    customer.f_add_order(order)
    customer.f_add_product(product)
    orders_list = customer.get_orders()
    print(orders_list)
    print(customer.get_orders()[:1][0])
    customer.f_delete_order(order)
