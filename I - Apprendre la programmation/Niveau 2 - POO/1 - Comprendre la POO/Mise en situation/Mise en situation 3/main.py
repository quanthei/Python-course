# POO EXERCICE DE MISE EN SITUATION 3

# ---
class Chat:
    def __init__(self, nom: str = "inconnu"):
        self.nom = nom # crée une variable d'instance : nom

    def SePresenter(self):
        print(f"Bonjour, je suis un chat et je m'appelle {self.nom}")

# ---
class Personne:
    def __init__(self, nom: str = "inconnu"):
        self.nom = nom

    def SePresenter(self):
        print(f"Bonjour, je suis une personne et je m'appelle {self.nom}")

# ---
chat1 = Chat()
chat1.SePresenter()  # Bonjour, je suis un chat et je m'appelle inconnu

chat2 = Chat("Garfield")
chat2.SePresenter()  # Bonjour, je suis un chat et je m'appelle Garfield

personne1 = Personne("Jean")
personne1.SePresenter()  # Bonjour, je suis une personne et je m'appelle Jean