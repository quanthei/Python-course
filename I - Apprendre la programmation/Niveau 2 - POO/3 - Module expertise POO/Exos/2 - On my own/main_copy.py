# PROJET QUESTIONNAIRE V3 : POO
#
# - Pratiquer sur la POO
# - Travailler sur du code existant
# - Mener un raisonnement

#---------------------------CLASS---------------------------
class Question():
    # Class variables
    id_question = 0
    user_score = 0
    
    def __init__(self, question: str, answers: tuple, correct_answer: str):
        self.question = question # Question ask to user
        self.answers = answers # All the possibles answers of self.question
        self.user_answer = "" # User answer of self.question
        self.correct_answer = correct_answer # Correct answer of self.question
        self.id_min_answer = 1 
        self.id_max_answer = len(self.answers) # Lenght of self.answers
        
    def PlayQuestion(self):
        # Display the question to the user
        self.DisplayQuestion()
        # Get the user answer
        
        # Verify the user answer
        
        # Increment the score if needed
        
        
    def DisplayQuestion(self):
        # Increment id_question
        Question.id_question += 1
        
        # Display question
        print()
        print(f"----- QUESTION N°{Question.id_question} -----")
        print()
        print(self.question)
    
        # Display possible answers
        for answ in self.answers:
            print(f"{self.answers.index(answ)}. {answ}")
        print()
    
    def GetUserAnswer(self) -> int:
        while True:
            user_answer_str = input(f"Votre réponse (comprise entre {self.id_min_answer} et {self.id_max_answer}): ")
            # Check the user entered something
            if user_answer_str == "":
                    print(f"ERROR: Vous n'avez rien renseigné !", end="\n")
                    self.GetUserAnswer() # Recurssive calling if empty
            try:
                user_answer_int = int(user_answer_str)
            except:
                print(f"ERROR: {user_answer_str} n'est pas une réponse valide !", "Merci de renseigner uniquement un chiffre !",sep="\n", end="\n")
                self.GetUserAnswer() # Recurssive calling if error
            
    
    def VerifyUserAnswer(self):
        pass
        
    def IncrementScore(self):
        pass
        
#---------------------------CONST & VAR---------------------------
questionnaire =  [
    Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"), 
    Question("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    Question("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
                ]


#---------------------------MAIN---------------------------
def main():
    for question in questionnaire:
        Question.PlayQuestion(question)
        
#---------------------------EXE---------------------------
main()