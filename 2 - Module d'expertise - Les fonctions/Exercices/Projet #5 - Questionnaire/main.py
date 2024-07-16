import random

#---------------------------FUNCTIONS---------------------------
def ask_question_and_stock_answer(id_question: int) -> str:
    # Ask question to user
    if id_question == 1:
        print("""Quelle est la capitale de la France ?"
        (A) Paris
        (B) Nice
        (C) Marseille
        (D) Lille
        """)
    elif id_question == 2:
        print("""Qui est le président de Total ?"
        (A) P.Pouyané
        (B) B.Arnault
        (C) S.Dassault
        (D) E.Macron""")
    
    elif id_question == 3:
        print("""Quel est la couleur des voitures les plus accidentées en France ?"
        (A) Noir
        (B) Vert
        (C) Rouge
        (D) Gris""")
   
    elif id_question == 4:
        print("""Qui a gagné l'EURO 2024 ?"
        (A) France
        (B) Angleterre
        (C) Allemagne
        (D) Espagne""")

    # Let the user enter is answer
    admited_answers = ["a","b","c","d"]
    user_answer = ""
    while True:
        user_answer = input("\nVotre réponse: ").lower()
        if user_answer in admited_answers:
            return user_answer
        print(f"{user_answer} n'est pas une saisie correcte !", "Merci de répondre a,b,c ou d...", end="\n")
    
def answer_correct(question_id: int, given_answer: str) -> bool:
    correct_answers = [(1,"a"),(2,"a"),(3,"c"),(4,"d")]
    if given_answer == correct_answers[question_id-1][1]:
        return True
    return False

#---------------------------MAIN---------------------------
def main():
    while True:
        # Generate question
        question_id = random.randint(1,4)
        
        # Ask the user a random question + stock the answer
        user_answer = ask_question_and_stock_answer(question_id)

        # Evaluate user answer
        if answer_correct(question_id, user_answer):
            print("Bravo !", f"{user_answer} est la bonne réponse !", sep="\n")
        else:
            print(f"{user_answer} n'est pas la bonne réponse !", sep="\n")

        # Replay ?
        is_replay = input("\nDo you wanna replay?" + "\nYes (enter 'Y')" + "\nNo (enter 'N')")
        if is_replay.lower() == "n":
            break
            
#---------------------------MAIN---------------------------
main()