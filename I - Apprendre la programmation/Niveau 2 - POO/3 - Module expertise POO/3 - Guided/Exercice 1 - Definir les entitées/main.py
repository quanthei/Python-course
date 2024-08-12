class Question():
    id_question = 0
    
    def __init__(self, question: str, choices: tuple, correct_answer: str):
        self.question = question
        self.choices = choices
        self.user_answer = None
        self.id_correct_answer = choices.index(correct_answer) + 1
        self.id_min_choice = 1
        self.id_max_choice = len(self.choices)
    
    def AskQuestion(self):
        # Display question to user
        self.DisplayQuestionAndAnswers()
        
        # Get user answer
        self.user_answer = self.AskUserAnswer()
        
        # Verify user answer
        if self.AnswerIsGood():
            print("Bonne réponse")
        else:
            print("Mauvaise réponse")
        print()
        
    def DisplayQuestionAndAnswers(self):
        Question.id_question += 1
        print(f"----- QUESTION N°{Question.id_question} -----")
        print(f"  {self.question}")
        for i in range(len(self.choices)):
            print("  ", i+1, "-", self.choices[i])
        print()

    def AskUserAnswer(self) -> int:
        user_answer_str = input(f"Votre réponse (entre {self.id_min_choice} et {self.id_max_choice}): ")
        try:
            user_answer_int = int(user_answer_str)
            if self.id_min_choice <= user_answer_int <= self.id_max_choice:
                return user_answer_int
            print(f"ERREUR : Vous devez rentre un nombre entier rentre {self.id_min_choice} et {self.id_max_choice} !")
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres !")
        return self.AskUserAnswer()
       
    def AnswerIsGood(self) -> bool:
        if self.user_answer == self.id_correct_answer:
            return True
        return False
            
    
    
"""def lancer_questionnaire(questionnaire):
    score = 0
    for question in questionnaire:
        if poser_question(question):
            score += 1
    print("Score final :", score, "sur", len(questionnaire))"""

questionnaire = (
    ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"), 
    ("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    ("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
                )

q1 = Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris")
q1.AskQuestion()