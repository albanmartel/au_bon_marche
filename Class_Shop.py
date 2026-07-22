from datetime import datetime

################### pour test
class Client:
    def __init__(self, id_client, surname, first_name, date_creation):
        self.id_client = id_client
        self.surname = surname
        self.first_name = first_name
        self.date_creation = date_creation

    def __str__(self):
        return f"Client n°{self.id_client} : {self.first_name} {self.surname} - Créé le {self.date_creation}"
############### pour test



class Shop:

    # on cré une liste de client vide pour l'ouverture du magasin
    def __init__(self):
        self.clients = []
        self.next_client_id = 1

    def f_create_customer(self, surname, first_name):
        client = Client(
            self.next_client_id,
            surname,
            first_name,
            datetime.now()
        )

        self.next_client_id =  self.next_client_id + 1
        return client

    # creation dune fonction d'ajout du client créé pour permettre une validation de la creation du client
    def f_add_client_to_list(self, client):
        self.clients.append(client)

### la suite pour test
shop = Shop()

client1 = shop.f_create_customer("Dupont", "Jean")
client2 = shop.f_create_customer("Martin", "Sophie")
print(client1)
print(client2)
