class Question():
    id_question = 0
    
    def __init__(self, question: str, choices: tuple, correct_answer: str):
        self.question = question
        self.choices = choices
        self.user_answer = None
        self.id_correct_answer = choices.index(correct_answer) + 1
        self.id_min_choice = 1
        self.id_max_choice = len(self.choices)
    
    def AskQuestion(self) -> bool:
        # Affiche la question à l'utilisateur
        self.DisplayQuestionAndAnswers()
        
        # Récupère la réponse de l'utilisateur
        self.user_answer = self.AskUserAnswer()
        
        # Vérifie la réponse de l'utilisateur
        if self.AnswerIsGood(self.user_answer, self.id_correct_answer):
            print("Bonne réponse", end="\n")
            return True
        print("Mauvaise réponse", end="\n")
        return False
        
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
            print(f"ERREUR : Vous devez rentrer un nombre entier entre {self.id_min_choice} et {self.id_max_choice} !")
        except ValueError:
            print("ERREUR : Veuillez rentrer uniquement des chiffres !")
        return self.AskUserAnswer()
       
    def AnswerIsGood(self, user_answer, correct_answer) -> bool:
        return user_answer == correct_answer
         
class Questionnaire():
    def __init__(self, questionnaire: list):
        self.questionnaire = questionnaire

    def GetStartedQuestionnaire(self):
        user_score = 0
        for question_data in self.questionnaire:
            ongoing_question = Question(*question_data)  # Décompose le tuple pour créer une instance de Question
            if ongoing_question.AskQuestion():
                user_score += 1
            print(f"\nScore actuel: {user_score}/{Question.id_question}")
                
        print(f"\nScore final : {user_score}/{len(self.questionnaire)}")

# Définition des questions
questionnaire_capitales = [
    ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"), 
    ("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    ("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
]

# Création d'une instance de Questionnaire
quizz_capital = Questionnaire(questionnaire_capitales)

# Démarrage du questionnaire
quizz_capital.GetStartedQuestionnaire()