from datetime import datetime
from Customer import Customer
from Product import Product


class Shop:

    # on cré une liste de customer vide pour l'ouverture du magasin
    def __init__(self):
        self.customer = []
        self.products = []
        self.next_customer_id = 1
        self.next_product_id = 1


############ fonctions pour les clients
    def f_create_customer(self, surname, first_name):
        customer = Customer(
            self.next_customer_id,
            surname,
            first_name,
            datetime.now()
        )

        self.next_customer_id =  self.next_customer_id + 1
        return customer

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

    # creation d'une fonction d'ajout du customer créé pour permettre une validation de la creation du customer
    def f_add_customer_to_list(self, customer):
        self.customer.append(customer)

    def f_delete_customer(self, customer):
        if customer in self.customer:
            self.customer.remove(customer)



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

    # verifie le stock disponible
    def f_check_product_stock(self, product_id, quantity):
        product = self.f_find_product_by_id(product_id)

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

