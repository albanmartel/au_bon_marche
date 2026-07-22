# Au bon marché

## Schéma descriptif du fonctionnement du programme

Magasin --> gère des --> clients

Client --> passe une ou des --> commandes 

Commandes  --> concerne des --> produits

---

CLASS Shop

DATA

FUNCTIONS
f_create_customer
f_add_customer_to_list
f_delete_customer
f_get_all_customer_list
f_find_customer_by_id
f_customer_by_name
Edit_daily_money
Print_customer_ticket
Check_sufficient_stock
Check_product_stock
Update_stock_after_customer_payment
f_create_product


CLASS Customer

DATA
id_client
surname (nom de famille)
first_name (prénom)
date creation fiche

FONCTIONS
init customer (ajouter client)
delete customer (supprimer client)
ajouter une commande
ajouter produit
ajouter qte
modifier quantité
supprimer produit
supprimer une commande
indiquer fin de saisie
payer une commande
demande facture
demander un historique des commandes
ajout produit
suppression produit



CLASS Product

DATA
id (Identifiant)
name (nom du produit)
type (fruit ou legume)
unit (unité de mesure kg / pièce)
price (prix du produit)
stock (stock disponible mesure: unité de produit)

FONCTIONS


CLASS Orders(Commandes)

DATA
id_order (commande)
products (liste de produits de type tableau)
quantity_products (quantité du produit)
order_date (date de commande)

FONCTIONS
add product (ajout produit) 
delete product (suppression produit)
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

