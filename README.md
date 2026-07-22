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

### CLASS Customer *Client*

_DATA_

| Paramètre | Description |
| :--- | :--- |
|**id_customer**| *identifiant client* |
|**surname**| *nom de famille* |
|**first_name**| *prénom* |
|**date creation**| *fiche* |

_FONCTIONS_

| Fonction | Description |
| :--- | :--- |
|**init customer** | *ajouter client*|
|**delete_account** | *Supprimer le compte client* |
|**add_order** | *Créer et ajouter une nouvelle commande au client* |
|**delete_order** | *Annuler ou supprimer une commande existante* |
|**complete_entry** | *Indiquer la fin de la saisie des articles* |
|**Pay_order** | *payer une commande* |
|**request_invoice** | *demander une facture* |
|**get_order_history** | *Consulter l'historique des commandes* |
|**add_product** | *ajouter un produit* |
|**add_quantity** | *Augmenter la quantité d'un produit* |
|**del_product** | *supprimer un produit* |
|**complete_entry** | *Indiquer la fin de la saisie des articles* |


---

### CLASS Product *Produit*

_DATA_

| Paramètre | Description |
| :--- | :--- |
|**id_product** | *Identifiant produit* |
|**name** | *nom du produit* |
|**type** | *fruit ou légume* |
|**unit** | *unité de mesure kg / pièce* |
|**price** | *prix du produit* |
|**stock** | *stock disponible mesure: unité de produit* |

_FONCTIONS_

---

### CLASS Orders *Commandes*

_DATA_

| Paramètre | Description |
| :--- | :--- |
|**id_order** | *commande* |
|**products** | *liste de produits de type tableau* |
|**quantity_products** | *quantité du produit* |
|**order_date** | *date de commande* |

_FONCTIONS_

| Fonction | Description |
| :--- | :--- |
|**add product** | *ajout produit* | 
|**delete product** | *suppression produit* |
|**order_total** | *total_a_payer* |

---

## Les Constantes

```
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
```

## Copier le projet

```
git clone https://github.com/albanmartel/au_bon_marche.git
```

## Projet FMS Académie Python Java 2026
