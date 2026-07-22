# Au bon marché

## Schéma descriptif du fonctionnement du programme

Magasin --> gère des --> clients

Client --> passe une ou des --> commandes 

Commandes  --> concerne des --> produits

---

### CLASS Shop *Magasin*

_DATA_

_FUNCTIONS_

| Fonction | Description |
| :--- | :--- |
|**f_create_customer** | *Créer client* |
|**f_add_customer_to_list** | *Ajouter client à la liste* |
|**f_delete_customer** | *Supprimer client* |
|**f_get_all_customer_list** | *Obtenir la liste de tous les clients)* |
|**f_find_customer_by_id** | *Trouver client par ID)* |
|**f_customer_by_name** | *Trouver client par nom)* |
|**edit_daily_money** | *Modifier l'argent du jour)* |
|**print_customer_ticket** | *Imprimer le ticket client)* |
|**check_sufficient_stock** | *Vérifier si le stock est suffisant)* |
|**check_product_stock** | *Vérifier le stock du produit)* | 
|**update_stock_after_customer_payment** | *Mettre à jour le stock après paiement client* |
|**f_create_product** | *Créer produit* |

---


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

