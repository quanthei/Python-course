#---------------------------------------FUNCTIONS---------------------------------------
def ask_user_name() -> str:
    answer_user_name = ""
    while answer_user_name == "":
        try:
            answer_user_name = input("Merci d'indiquer votre prénom: ")
        except:
            print("ERREUR: Saisie incorrecte, merci de rentrer uniquement des caractères alphabétiques !")
    return answer_user_name

def ask_user_age( 
                para_user_name : str
                ) -> int:
    answer_user_age = 0
    while answer_user_age == 0:
        try:
            answer_user_age = int(input(f"{para_user_name}, merci d'indiquer votre âge: "))
        except ValueError:
            print("ERREUR: Saisie incorrecte, merci de rentrer uniquement des chiffres entiers !")   
    return answer_user_age

def userAgeSituation(
                    para_user_age : int
                    ) -> str:
    if para_user_age <= 18:
        if para_user_age < 10: return "Vous êtes un enfant !"
        elif 13 <= para_user_age < 17: return "Vous êtes un ado"
        elif para_user_age == 17: return "Vous êtes presque majeur..."
        elif para_user_age == 18: return "Tout juste majeur ! Félécitations !"
        else: return "Vous êtes mineur !"
    elif para_user_age > 60: return "Vous êtes un senior !"
    else : return "Vous êtes majeur !"

def display_user_infos(
                       displayed_user_name : str,
                       displayed_user_age : int,
                       displayed_user_age_situation : str
                      ) -> str:
    return print(f"Vous vous appelez {displayed_user_name}, vous avez {displayed_user_age} ans.", displayed_user_age_situation, sep="\n", end="")
#---------------------------------------MAIN---------------------------------------
def main():
    #Ask user_name
    user_name = ask_user_name() 

    #Ask user_age
    user_age = ask_user_age(user_name)

    #User age situation
    user_age_situation = userAgeSituation(user_age)

    #Print user name and age
    display_user_infos(user_name, user_age, user_age_situation)

#---------------------------------------EXE---------------------------------------
main()
