import os
import time

MENU_PIZZAS = [
    "4 Fromages",
    "Végétarienne",
    "Hawaï",
    "Calzone"
    ]

#--------------------FUNCTIONS--------------------
def afficher_menu(nom_menu: str, menu_a_afficher: list, nb_plats_afficher: int = -1):
    if nb_plats_afficher != -1:
        menu_slicer = menu_a_afficher[0:nb_plats_afficher]
    else:
        menu_slicer = menu_a_afficher

    if len(menu_slicer) == 0: # On check si le menu n'est pas vide avant de l'afficher
        print(f"Le menu '{nom_menu.upper()}' ne contient aucun plat !")
    else: # On affiche le nom du menu + tous les plats qui le compose
        print(f"---- {nom_menu.upper()} ({len(menu_slicer)}) ----")
        for plat in range(len(menu_slicer)):
            print(f"{plat+1} - {menu_slicer[plat]}")
        # On affiche le premier et le dernier plat du menu
        print()
        print(f"-Premier plat du menu: {menu_slicer[0]}")
        print(f"-Dernier plat du menu: {menu_slicer[-1]}", end="\n")

def plat_existe_dans_menu(nom_plat: str, menu: list) -> bool:
    for plat in menu:
        if plat.upper().capitalize() == nom_plat:
            return True
    return False

def ajouter_plat_au_menu(menu_a_modifier: list):
    plat_a_ajouter = input("Merci de saisir le nom du plat que vous souhaitez ajouter au menu : ").lower().capitalize()
    # Check si le plat n'existe pas déjà dans le menu
    if plat_existe_dans_menu(plat_a_ajouter, menu_a_modifier):
        print(f"ERREUR: Le plat {plat_a_ajouter} existe d'ores et déjà dans ce menu !")
        time.sleep(3)
        return None
    menu_a_modifier.append(plat_a_ajouter)

#--------------------MAIN--------------------
def main():
    nom_du_menu = "Nos Pizzas"
    menu_a_modifier = MENU_PIZZAS

    while True:
        # On affiche le menu
        afficher_menu(nom_du_menu, menu_a_modifier)

        # Demande au user s'il souhaite ajouter une pizza
        print()
        print(f"Souhaitez-vous ajouter un plat au menu '{nom_du_menu}'", "(saisir 'o' pour oui ou 'n' pour non) ?", 
              sep="\n", end="\n")
        choix_user = input("Votre choix : ")
        if choix_user.upper() == "O":
            # On recup le nom du plat à rajouter
            ajouter_plat_au_menu(menu_a_modifier)
        elif choix_user.upper() == "N":
            break # on sort de la boucle si le user ne veut pas ajouter de plat au menu
        else:
            print("Merci de saisir uniquement 'O' ou 'N' !")
            # Apres 5 sec on clear le screen avant de reboucler
            time.sleep(3)
        print()

#--------------------EXE--------------------
main()