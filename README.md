Schéma descriptif du fonctionnement du programme

Magasin --> gère des --> clients
Client --> passe une ou des --> commandes 
Commandes  --> concerne des --> produits


CLASS Shop

DATA

FUNCTIONS
f_create_customer
f_add_client_to_list
f_delete_customer
f_get_customer_list
Edit_daily_money
Print_customer_ticket
Check_sufficient_stock
Check_product_stock
Update_stock_after_customer_payment
f_create_product


CLASS Client

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



CLASS Commandes

DATA
id commande
id client_qui_commande
id_produit
quantite_produit
date_de_commande

FONCTIONS
total_a_payer
