user_name = ""
user_age = 0

#Ask user_name
while user_name == "":
    try:
        user_name = input("Merci d'indiquer votre prénom: ")
    except:
        print("ERREUR: Saisie incorrecte, merci de rentrer uniquement des caractères alphabétiques !")
#Ask user_age
while user_age == 0:
    try:
        user_age = int(input(f"{user_name}, merci d'indiquer votre âge: "))
    except :
        print("ERREUR: Saisie incorrecte, merci de rentrer uniquement des chiffres entiers !")   

#Print user age and name
print(f"Vous vous appelez {user_name} et vous avez {user_age} ans", end=".")