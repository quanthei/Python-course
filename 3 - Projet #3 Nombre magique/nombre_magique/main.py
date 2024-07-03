import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)
NB_VIES = 3

nombre = 0
vies_restantes = NB_VIES

#-----------------------------FUNCTIONS-----------------------------
def ask_user_nombre_proposition(
                               nb_min : int,
                               nb_max : int
                               ) -> int:
    answer_user_nombre_magique = 0
    while answer_user_nombre_magique == 0:
        try:    
            answer_user_nombre_magique = int(input(f"Quel est le nombre magique entre {nb_min} et {nb_max} : "))
        except:
            print("ERREUR : Merci de rentrer uniquement des valeurs numériques !", "Merci de réassayer !", sep="\n")
        else:
            if answer_user_nombre_magique < nb_min or answer_user_nombre_magique > nb_max:
                print(f"ERREUR : {answer_user_nombre_magique} n'est pas compris entre {nb_min} et {nb_max} !", "Merci de réassayer !", sep="\n")
                answer_user_nombre_magique = 0
    return answer_user_nombre_magique

def evaluer_proposition_user(
                            nb_propose : int,
                            nb_magique : int,
                            ) -> str:
    global vies_restantes
    if nb_propose == nb_magique: return "Bravo, vous avez gagné !" + "\n" + f"{nb_propose} était bien le nombre magique !"
    else:
        res_vie = diminuer_vie()
        if res_vie == -1:
            return f"Vous avez perdu !" + "\n" + f"Le nombre magique était {NOMBRE_MAGIQUE} !"
        else:
            if nb_propose < nb_magique: return f"Le nombre magique est plus grand que {nb_propose} !"  "\n" + f"Il vous reste {vies_restantes} vie(s)..."
            else: return f"Le nombre magique est plus petit que {nb_propose} !" + "\n" + f"Il vous reste {vies_restantes} vie(s)..."
        
def diminuer_vie() -> int:
    global vies_restantes
    vies_restantes -= 1
    while vies_restantes > 0:
        return 0 #still have life
    else:
        return -1 #plus de life
        
#-----------------------------MAIN-----------------------------
def main():
    global nombre
    while not nombre == NOMBRE_MAGIQUE and not vies_restantes == 0:
        #Ask user for a proposal
        nombre = ask_user_nombre_proposition(NOMBRE_MIN,NOMBRE_MAX)
        # Evalute + print user answer
        res = evaluer_proposition_user(nombre, NOMBRE_MAGIQUE)
        print(res)
#-----------------------------EXE-----------------------------
main()

