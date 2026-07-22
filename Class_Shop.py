from datetime import datetime
from Customer import Customer

class Shop:

    # on cré une liste de customer vide pour l'ouverture du magasin
    def __init__(self):
        self.customer = []
        self.next_customer_id = 1

    def f_create_customer(self, surname, first_name):
        customer = Customer(
            self.next_customer_id,
            surname,
            first_name,
            datetime.now()
        )

        self.next_customer_id =  self.next_customer_id + 1
        return customer

    # creation dune fonction d'ajout du customer créé pour permettre une validation de la creation du customer
    def f_add_customer_to_list(self, customer):
        self.customer.append(customer)

### la suite pour test
shop = Shop()

customer1 = shop.f_create_customer("Dupont", "Jean")
customer2 = shop.f_create_customer("Martin", "Sophie")
print(customer1)
print(customer2)
