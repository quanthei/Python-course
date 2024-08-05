import time
import random 
import os

#---------------------------FUNCTIONS---------------------------
def clear_debugger():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

def generate_a_sequence(nb_elements_to_generate : int) -> str:
    sequence_generated = ""
    for i in range(nb_elements_to_generate):
        sequence_generated += str(random.randint(0,9))
    return sequence_generated

#---------------------------MAIN---------------------------
def main():
    user_points = 0
    sequence_to_find = ""
    while True:
        # On génère une séquence qui reste afficher 3 sec
        if user_points == 0 : 
            sequence_to_find += generate_a_sequence(4)
        else:
            clear_debugger()  # On clear le tour précédant
            sequence_to_find += generate_a_sequence(1)
        print("Retenez la séquence:")
        time.sleep(1)
        print(sequence_to_find)
        time.sleep(3)

        # On clear l'affichage
        clear_debugger()

        # On demande au user de rentrer sa réponse
        user_answer = input("Retapez la séquence : ")
        if user_answer == sequence_to_find: # bonne réponse
            user_points += 1 # on incrémente le score
            print(f"Bonne réponse, votre score est : {user_points}")
            time.sleep(3)
        else: # mauvaise réponse
            print(f"Mauvaise réponse, la séquence était : {sequence_to_find}, votre score final est de {user_points}")
            break

#---------------------------EXE---------------------------
main()
