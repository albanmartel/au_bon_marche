# Au bon marché

## Schéma descriptif du fonctionnement du programme

Magasin --> gère des --> clients
Client --> passe une ou des --> commandes 
Commandes  --> concerne des --> produits


CLASS Shop

DATA

FUNCTIONS

f_create_stock am

f_create_customer pp
f_add_customer_to_list pp
f_delete_customer pp
f_get_all_customer_list pp
f_find_customer_by_id pp
f_customer_by_name pp

f_create_product() pp
f_add_product_to_list() pp
f_delete_product() pp
f_get_all_product_list() pp
f_find_product_by_id() pp
f_find_product_by_name() pp
f_check_product_stock pp

f_create_order pp
f_delete_order pp
f_find_order_by_id pp 
f_add_order_to_customer
Update_stock_after_customer_payment
Edit_daily_money
Print_customer_ticket



CLASS Customer

DATA
id_client
surname (nom de famille)
first_name (prénom)
date creation fiche

FONCTIONS

f_find_order_by_id pp

ajouter qte
modifier quantité
supprimer produit
indiquer fin de saisie
payer une commande
demande facture
# demander un historique des commandes
ajout produit  am
suppression produit  am



CLASS Product

DATA
id (Identifiant)
name (nom du produit)
type (fruit ou legume)
unit (unité de mesure kg / pièce)
price (prix du produit)
stock (stock disponible mesure: unité de produit)

FONCTIONS
__str__(self):
name(self) -> str: am
name(self, value: str) -> None: am
type(self) -> str: am
type(self, value: str) -> None: am
unit(self) -> str: am
unit(self, value: str) -> None: am
price(self) -> float | None: am
price(self, value: float | None) -> None: am
stock(self) -> int | None: am
stock(self, value: int) -> None: am
f_has_enough_stock pp

CLASS Order(Commandes)

DATA
id_order (commande)
products (liste de produits de type tableau)
quantity_products (quantité du produit)
order_date (date de commande)
is_finish (La commande est-elle terminée) (Alban)
order_price (prix de la commande) (Alban)

FONCTIONS
add product (ajout produit)  pp A METTRE DANS CUSTOMER
ajouter produit am A METTRE DANS CUSTOMER
delete product (suppression produit) pp A METTRE DANS CUSTOMER
f_delete_one_product (suppression d'un seul produit de la commande) pp A METTRE DANS CUSTOMER
order_total (total_a_payer)


---

## Les Constantes

FRUITS = (
("Clémentine", "6", "2.9", "kg"),
("Datte", "4", "7", "kg"),
("Grenade", "3", "3.5", "kg"),
("Kaki", "3", "4.5", "kg"), 
("Kiwi", "5", "3.5", "kg"),
("Mandarine", "6", "2.8", "kg"), 
("Orange",  "8", "1.5", "kg"), 
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
