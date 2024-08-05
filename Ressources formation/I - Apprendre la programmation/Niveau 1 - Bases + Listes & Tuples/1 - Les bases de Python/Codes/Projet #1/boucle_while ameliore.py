def ask_user_name() -> str:
    answer_user_name = ""
    while answer_user_name == "":
        try:
            answer_user_name = input("Merci d'indiquer votre prénom: ")
        except:
            print("ERREUR: Saisie incorrecte, merci de rentrer uniquement des caractères alphabétiques !")
    return answer_user_name

def ask_user_age(local_name : str) -> int:
    answer_user_age = 0
    while answer_user_age == 0:
        try:
            answer_user_age = int(input(f"{local_name}, merci d'indiquer votre âge: "))
        except ValueError:
            print("ERREUR: Saisie incorrecte, merci de rentrer uniquement des chiffres entiers !")   
    return answer_user_age

def main():
    #Ask user_name
    user_name = ask_user_name() 

    #Ask user_age
    user_age = ask_user_age(user_name)

    #Print user name and age
    print(f"Vous vous appelez {user_name} et vous avez {user_age} ans", end=".")

#Main
main()
