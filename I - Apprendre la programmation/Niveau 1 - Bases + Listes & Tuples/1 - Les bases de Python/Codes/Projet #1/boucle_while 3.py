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

def display_user_infos(
                       displayed_user_name : str,
                       displayed_user_age : int
                      ) -> str:
    return print(f"Vous vous appelez {displayed_user_name} et vous avez {displayed_user_age} ans", end=".")
#---------------------------------------MAIN---------------------------------------
def main():
    #Ask user_name
    user_name = ask_user_name() 

    #Ask user_age
    user_age = ask_user_age(user_name)

    #Print user name and age
    display_user_infos(user_name, user_age)

#---------------------------------------EXE---------------------------------------
main()
