#-----------------------------CONST & VAR-----------------------------
UN_POUCE_EN_CM = 2.54 # 1 pouce = 2.54 cm
UN_CM_EN_POUCE = 0.394 # 1 cm = 0.394 pouces
converter_mode = 0
unite_origine = "Pouces"
unite_finale = "Cm"
coeff_de_conversion = UN_POUCE_EN_CM

#-----------------------------FUNCTIONS-----------------------------
def ask_user_type_convertion() -> int:
    # Message d'accueil
    print("-----CONVERTISSEUR POUCES & CM-----")

    # Ask le user
    answer_type_convertion_int = 0
    while answer_type_convertion_int == 0:
        print("Vous souhaitez convertir : ", "1 - Pouces --> Cm : saisir 1", "2 - Cm --> Pouces : saisir 2", sep="\n")
        try:
            answer_type_convertion_str = input("Merci de saisir le mode que vous souhaitez utiliser : ")
            answer_type_convertion_int = int(answer_type_convertion_str) # Check que mon user à bien rentrer un nombre entier
        except:
            print(f"ERREUR: {answer_type_convertion_str} n'est pas une saisie valide !", "Merci de faire votre choix entre 1 ou 2", sep="\n")
        else:
            if answer_type_convertion_int != 1 and answer_type_convertion_int != 2: # Check que mon user à bien rentrer 1 ou 2 et non pas autre chose
                print(f"ERREUR: {answer_type_convertion_str} n'est pas une saisie valide !", "Merci de faire votre choix entre 1 ou 2", sep="\n")
                answer_type_convertion_int = 0

    return answer_type_convertion_int

def ask_user_valeur_a_convertir(conversion_mode : int) -> float:
    # On definit le sens de conversion -> par défaut : mode 1
    global unite_origine, unite_finale, coeff_de_conversion
    if conversion_mode == 2: unite_origine, unite_finale, coeff_de_conversion = unite_finale, unite_origine, UN_CM_EN_POUCE  # Ici on réalise un swap de valeur en cas de mode 2 + le coeff de conversion
    
    # Demande à l'utilisateur la valeur à convertir
    valeur_a_convertir_float = 0.00
    while valeur_a_convertir_float == 0.00:
        try:
            valeur_a_convertir_str = input(f"Merci d'indiquer la valeur en {unite_origine} que souhaitez vous convertir en {unite_finale} :")
            valeur_a_convertir_float = float(valeur_a_convertir_str)
        except:
            print(f"{valeur_a_convertir_str} n'est pas une saisie valide !", "Merci de saisir un chiffe au format '0.00' ", sep="\n")

    # On return la valeur à convertir
    return valeur_a_convertir_float

#-----------------------------MAIN-----------------------------
def main():
    # Demande à mon utilisateur le mode qu'il souhaite utiliser
    converter_mode = ask_user_type_convertion()

    # On demande au user le chiffre qu'il souhaite convertir
    valeur_a_convertir = ask_user_valeur_a_convertir(converter_mode)

    # On réalise la conversion
    valeur_convertie = round(float(valeur_a_convertir * coeff_de_conversion), 2) # On arrondi le résultat à deux chiffres après la virgule

    # On affiche le résultat de la conversion
    print(f"{valeur_a_convertir} {unite_origine} est égal à {valeur_convertie} {unite_finale}")

#-----------------------------EXE-----------------------------
main()