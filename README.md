Schéma descriptif du fonctionnement du programme

Magasin --> gère des --> clients
Client --> passe une ou des --> commandes 
Commandes  --> concerne des --> produits


CLASS Magasin

data

FONCTIONS
Ajouter client
supprimer client
liste des clients
Editer bilan journée
Imprimer tiket client
stock_suffisant
stock d'un produit
mise a jourt du stock apres paiement client


CLASS Client

DATA
id
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



CLASS Produit

DATA
Identifiant
type (fruit ou legume)
unité
prix
stock_dispo

FONCTIONS





CLASS Commandes

DATA
id commande
id client_qui_commande
id_produit
quantite_produit
date_de_commande

FONCTIONS
ajout produit
suppression produit
total_a_payer
