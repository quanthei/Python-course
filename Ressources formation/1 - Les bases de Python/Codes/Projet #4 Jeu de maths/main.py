import random

NB_MIN = 1
NB_MAX = 10
NB_QUESTIONS = 4

def poser_question(
                  operateur_question : str
                  ) -> bool:
    a, b = random.randint(NB_MIN,NB_MAX), random.randint(NB_MIN,NB_MAX)
    user_answer_str = input(f"Calculez : {a} {operateur_question} {b} = ")
    user_answer_int = int(user_answer_str)
    if operateur_question == "+":
        if user_answer_int == a + b: return True
    elif operateur_question == "*": 
        if user_answer_int == a * b: return True
    return False

def definir_operateur() -> str:
    o = random.randint(0,1)
    if o == 1 :
       return "+"
    return "*"

def evaluer_copie(
                 reponses_correctes : int
                 ) -> str:
    moyenne = int(NB_QUESTIONS/2)
    if reponses_correctes == NB_QUESTIONS:
        return "Excellent !"
    elif reponses_correctes == 0:
        return "Révisez vos maths !"
    elif reponses_correctes > moyenne:
        return "Pas mal"
    return "Peu mieux faire"
        
def main():
    nb_points = 0
    for i in range(1,NB_QUESTIONS+1):
        print(f"Question n°{i} sur {NB_QUESTIONS} :")
        operateur = definir_operateur()
        if poser_question(operateur): 
            nb_points += 1
            print("Réponse correcte !")
        else: 
            print("Réponse incorrecte !")
        print("")
    evaluation = evaluer_copie(nb_points)
    print(f"Votre score est de {nb_points}/{NB_QUESTIONS} !", evaluation, sep="\n")
    
main()