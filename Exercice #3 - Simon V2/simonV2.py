import os
import random
import time

def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

def generate_a_sequence(existing_sequence: list, new_items_to_generate: int) -> list:
    new_sequence = existing_sequence
    for i in range(1, new_items_to_generate + 1):
        new_sequence.append(random.randint(0,9))
    return new_sequence

def reponse_correct(correct_sequence: str, sequence_proposed_by_user: str) -> bool:
    if sequence_proposed_by_user != correct_sequence:
        return False
    return True

def main():
    sequence_to_find = []
    score = 0
    while True:
        # Generate a sequence
        if sequence_to_find == []: # first tour
            sequence_to_find = generate_a_sequence(sequence_to_find, 4)
        else:
            sequence_to_find = generate_a_sequence(sequence_to_find, 1)

        #Afficher la sequence au user durant 3s puis au clean
        sequence_to_find_str = ""
        for i in sequence_to_find:
            sequence_to_find_str += str(i)
        print(f"Voici la sequence à retenir:", sequence_to_find_str, end="\n", flush=True)
        time.sleep(3)
        clear_screen()

        # On demande la réponse au user
        user_answer = input("Réecriver la séquence: ")
        if not reponse_correct(sequence_to_find_str, user_answer):
            print("Vous avez perdu !", f"La bonne réponse était: {sequence_to_find_str}", sep="\n")
            break
        
        score += 1
        print("Bonne réponse !", f"Vous avez {score} points", sep="\n")
        time.sleep(5)
        clear_screen()

main()