from datetime import datetime
from socket import send_fds

from Customer import Customer
from Product import Product

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
    ("Choux de Bruxelles", "4", "4" "kg"),
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

    def create_stock(self) -> None:
        for fruit in FRUITS:
            produit = self.f_create_product(fruit[0], "Fruit", fruit[1], fruit[2], fruit[3])
            self.f_add_product_to_list(produit)
        for vegetable in VEGETABLES:
            produit = self.f_create_product(vegetable[0], "Légume", vegetable[1], vegetable[2], vegetable[3])
            self.f_add_product_to_list(produit)


if __name__ == "__main__":
    shop = Shop()
    shop.f_add_customer_to_list()

