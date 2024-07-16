import os 
import time

#---------------------------FUNCTIONS---------------------------
def clear_console():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

def recuperer_et_afficher_infos_personne(id_personne : int) -> tuple:
    # Clear console
    clear_console()

    # Recuperer nom
    user_nom = ""
    while True:
        user_nom = input(f"Merci d'indiquer le nom de la personne nº{id_personne}: ")
        if len(user_nom) > 0:
            break
        print(f"Vous n'avez pas indiquer de nom pour la personne nº{id_personne} !")
    clear_console()
        
    # Recuperer âge
    user_age_int = -1
    while True:
        user_age_str = input(f"Merci d'indiquer l'âge de la personne nº{id_personne}: ")
        try: 
            user_age_int = int(user_age_str)
        except:
            print(f"{user_age_str} n'est pas une saisie valide !")
        else:
            break
    clear_console()

    # Afficher les infos
    print(f"La personne nº{id_personne} est {user_nom}, il/elle a {user_age_int} ans")
    print(f"{user_nom} comporte {len(user_nom)} lettres")

    return (id_personne, user_nom, user_age_int)

#---------------------------MAIN---------------------------
def main():
    nb_personnes_a_enregistrer_int = 0
    while True:  
        nb_personnes_a_enregistrer_str = input("Combien de personnes souhaitez-vous enregistrer: ")
        try: 
            nb_personnes_a_enregistrer_int = int(nb_personnes_a_enregistrer_str)
        except:
            print(f"Merci de saisir uniquement des valeurs numériques !")
        else:
            break
        
    clear_console()

    # Loop to get + afficher les infos
    users_infos = []
    for personne in range(1, nb_personnes_a_enregistrer_int + 1):
        users_infos.append(recuperer_et_afficher_infos_personne(personne))
        time.sleep(3)

    # Afficher toutes les personnes en fin de code
    for user in users_infos:
        print(user)
#---------------------------EXE---------------------------
main()
