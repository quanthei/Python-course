class Question():
    id_question = 0
    user_score = 0

    def __init__(self, question: str, answers: tuple, correct_answer: str):
        self.question = question
        self.answers = answers
        self.id_min_answer = 1
        self.id_max_answer = len(self.answers)
        self.user_answer = ""
        self.id_correct_answer = self.answers.index(correct_answer) + 1
    
    def AskQuestion(self):
        Question.id_question +=1

        print()
        print(f"QUESTION NUMÉRO {Question.id_question}")
        print()
        print(self.question)
    
        for answer in self.answers:
            print("  ", self.answers.index(answer) + 1 , "-", answer)
        print()

        # Ask user for his answer
        self.user_answer = self.AskUserAnswer()

        # Increment score if user answer is correct
        if self.UserAnswerIsCorrect(): 
            print("Bonne réponse !", flush=True)
            self.IncrementScore()
            print(f"Votre score est de {Question.user_score}/{len(questionnaire)}")
        else:
            print("Mauvaise réponse !", flush=True)
            print(f"Votre score est de {Question.user_score}/{len(questionnaire)}")

    def AskUserAnswer(self) -> int:
        user_answer_str = input(f"Votre réponse (entre {self.id_min_answer} et {self.id_max_answer}): ")
        try:
            reponse_int = int(user_answer_str)
            if self.id_min_answer <= reponse_int <= self.id_max_answer:
                return reponse_int
            print(f"ERREUR : Vous devez rentrer un nombre entre {self.id_min_answer} et {self.id_max_answer}")
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres !")
        return self.AskUserAnswer()

    def UserAnswerIsCorrect(self) -> bool:
        return True if self.id_correct_answer == self.user_answer else False

    def IncrementScore(self):
        Question.user_score += 1

questionnaire = (
                Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"), 
                Question("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
                Question("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
                )

for question in questionnaire:
    question.AskQuestion()