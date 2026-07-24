from datetime import datetime

from Customer import Customer
from Product import Product
from Order import Order

FRUITS = (
    ("Clémentine", "6", "2.9", "kg"),
    ("Datte", "4", "7", "kg"),
    ("Grenade", "3", "3.5", "kg"),
    ("Kaki", "3", "4.5", "kg"),
    ("Kiwi", "5", "3.5", "kg"),
    ("Mandarine", "6", "2.8", "kg"),
    ("Orange", "8", "1.5", "kg"),
    ("Pamplemousse", "8", "2", "pièce"),
    ("Poire", "5", "2.5", "kg"),
    ("Pomme", "8", "1.5", "kg"),
)

VEGETABLES = (
    ("Carotte", "7", "1.3", "kg"),
    ("Choux de Bruxelles", "4", "4", "kg"),
    ("Chou vert", "12", "2.5", "pièce"),
    ("Courge Butternut", "6", "2.5", "kg"),
    ("Endive", "5", "2.5", "kg"),
    ("Épinard", "4", "2.6", "kg"),
    ("Poireau", "5", "1.2", "kg"),
    ("Potiron", "6", "2.5", "pièce"),
    ("Radis noir", "10", "5", "pièce"),
    ("Salsifis", "3", "2.5", "kg"),
)

class Shop:


    # on cré une liste de customer vide pour l'ouverture du magasin
    def __init__(self):
        self.customer = []
        self.products = []
        self.next_customer_id = 1
        self.next_product_id = 1
        self.next_order_id = 1


############ fonctions pour les clients
    def f_create_customer(self, surname, first_name):
        customer = Customer(
            self.next_customer_id,
            surname,
            first_name,
            datetime.now(),
            self.next_order_id
        )

        self.next_customer_id =  self.next_customer_id + 1
        self.next_order_id += 1
        return customer

    # creation d'une fonction d'ajout du customer créé pour permettre une validation de la creation du customer
    def f_add_customer_to_list(self, customer):
        self.customer.append(customer)

    def f_delete_customer(self, customer):
        if customer in self.customer:
            self.customer.remove(customer)

    def f_get_all_customer_list(self):
        return self.customer

    def f_find_customer_by_id(self, customer_id):
        for customer in self.customer:
            if customer.id_customer == customer_id:
                return customer
        return None

    def f_find_customer_by_surname(self, surname):
        for customer in self.customer:
            if customer.surname == surname:
                return customer

    ############ fonctions pour les commandes

    def f_create_order(self, customer):
        if customer is None:
            return None

        order = Order(
            self.next_order_id,
            datetime.now()
        )

        self.next_order_id += 1

        customer.order.append(order)

        return order

    def f_delete_order(self, customer, order):
        if customer is None:
            print("Client introuvable")
            return False

        if order is None:
            print("Commande introuvable")
            return False

        if order in customer.order:
            customer.order.remove(order)
            return True

        print("Cette commande n'appartient pas à ce client")
        return False

    def f_find_order_by_id(self, customer_id, order_id):
        customer = self.f_find_customer_by_id(customer_id)

        if customer is None:
            return None

        for order in customer.order:
            if order.id_order == order_id:
                return order

        return None

    ############ fonctions pour les produits
    def f_create_product(self, name, type, stock, price, unit):
        product = Product(
            self.next_product_id,
            name,
            type,
            stock,
            price,
            unit
        )
        self.next_product_id += 1
        return product

    def f_add_product_to_list(self, product):
        self.products.append(product)

    def f_delete_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def f_get_all_product_list(self):
        return self.products

    def f_find_product_by_id(self, product_id):
        for product in self.products:
            if product.id_product == product_id:
                return product
        return None

    def f_find_product_by_name(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None

    ############ fonctions diverses de gestion

    # verifie le stock disponible et retourne Bool
    def f_check_product_stock(self, product, quantity):
        if product is None:
            print("Produit introuvable")
            return False

        enough_stock = product.f_has_enough_stock(quantity)

        if not enough_stock:
            print(
                f"Stock insuffisant pour {product.name} : "
                f"demandé {quantity} {product.unit}, "
                f"disponible {product.stock} {product.unit}"
            )

        return enough_stock

    def f_create_stock(self) -> None:
        """
        function create_stock(self)
        Elle permet de créer les produits du stock
        :return: None
        """
        for fruit in FRUITS:
            produit = self.f_create_product(fruit[0], "Fruit", int(fruit[1]), float(fruit[2]), fruit[3])
            self.f_add_product_to_list(produit)
        for vegetable in VEGETABLES:
            produit = self.f_create_product(vegetable[0], "Légume", int(vegetable[1]), float(vegetable[2]), vegetable[3])
            self.f_add_product_to_list(produit)





