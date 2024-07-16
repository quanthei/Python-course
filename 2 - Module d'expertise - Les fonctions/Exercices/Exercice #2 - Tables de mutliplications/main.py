import os

MIN_TABLE_M = 1
MAX_TABLE_M = 10

#---------------------------FUNCTIONS---------------------------
def clear_console():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

def afficher_table_multiplication(table_m: int, min: int, max: int, clear_console_before_print = False):
    if clear_console_before_print:
        clear_console()
    print(f"Voici la table de {table_m}:" + "\n", flush=True)
    for i in range (min, max + 1):
        resultat = i * table_m
        print(f"{i} X {table_m} = {resultat}", flush=True)

#---------------------------MAIN---------------------------
def main():
    # On demande au user quelle table il souhaite afficher
    table_multiplication_str = 0
    while True:
        table_multiplication_str = input("Merci d'indiquer la table de multiplication que vous souhaitez afficher: ")
        try:
            table_multiplication_int = int(table_multiplication_str)
        except:
            print(f"{table_multiplication_str} n'est pas une saisie valide !", "Merci d'indiquer uniquement des valeurs numériques...", sep="\n")
        else:
            break
    
    # Afficher la table souhaitez par le user
    afficher_table_multiplication(table_multiplication_int, MIN_TABLE_M, MAX_TABLE_M, True)

#---------------------------EXE---------------------------
main()
