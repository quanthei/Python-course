"""PYTHON - Fichier de rappels"""
nom, age = "", 0

def askForUserName() -> str:
    try:
        name_local = str(input("Quel est ton nom ? "))
    except:
        print("ERREUR: Merci de saisir une chaîne de caractères")
        name_local = askForUserName()
    else:
        return name_local

def askForUserAge() -> int:
    try:
         age_local = int(input("Quel est ton âge ? "))
    except:
        print("ERREUR : Merci de saisir une valeur numérique uniquement")
        age_local = askForUserAge()
    else:
        return age_local

def main():
    #Ask for user name
    nom = askForUserName()
    #Ask for user age
    age = askForUserAge()
    #Display the result
    print (f"Vous vous appelez {nom} et vous avez {age} ans", end=".")

main()













