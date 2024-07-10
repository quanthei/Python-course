import time
#-------------------------FUNCTIONS-------------------------
def ask_user_the_program_to_start() -> int:
    user_choice_int = 0
    while user_choice_int == 0:
        user_choice_str = input("Merci de sélectionner le programme en indiquant 1, 2 ou 3 : ")
        try:
            user_choice_int = int(user_choice_str)
        except:
            print(f"ERREUR: {user_choice_int} n'est pas une saisie valide !")
    return user_choice_int

def convert_and_stock_time(remaining_time : int) -> str:
    min = remaining_time//60 # division entière (pas de virgules)
    sec = remaining_time-min*60
    return f"{min:02d}:{sec:02d}"

def display_x_sign_every_x_sec(sign : str, nb_sign : int, every_x_sec : int):
    for i in range(nb_sign):
        time.sleep(every_x_sec)
        print(sign, end="", flush=True)

def display_line(remaining_time):
    formated_remaining_time = convert_and_stock_time(remaining_time)
    print(f"Temps restant: {formated_remaining_time}",end="")
    display_x_sign_every_x_sec(".", 10, 1)
    print("")

def run_program(program_chosen : int):
    sec_in_min = 60
    if program_chosen == 1: # Oeufs à la coque : 3 minutes
        remaining_sec = sec_in_min * 3
    elif program_chosen == 2: # Oeufs mollets : 6 minutes
        remaining_sec = sec_in_min * 6
    else:
        remaining_sec = sec_in_min * 9 # Oeufs durs : 9 minutes

    while remaining_sec > 0:
        display_line(remaining_sec)
        remaining_sec -= 10
    
    print("Vos oeufs sont cuits !")
        
#-------------------------MAIN-------------------------
def main():
    # Display the main menu for the user
    print("""
*******************************************
**** PROGRAMME DE CUISSON DE VOS OEUFS ****
*******************************************                                            
* 1 - Oeufs à la coque : 3 minutes        *
* 2 - Oeufs mollets : 6 minutes           *
* 3 - Oeufs durs : 9 minutes              *
*******************************************
""")
    
    #Ask the user about the program he wants to run
    program_chosen = ask_user_the_program_to_start()

    #Start the program
    run_program(program_chosen)

#-------------------------EXE-------------------------
main()