# POO EXERCICE DE MISE EN SITUATION 2
# Code mal penser car on passe l'âge en argument de la fonction se présenter et non pas comme une variable d'instance ! Il n'est donc pas accesible dans EstMajeur
class Personne:
    def __init__(self, nom: str):
        self.nom = nom   # crée une variable d'instance : nom
        print(f"Constructeur personne: {self.nom}")

    def SePresenter(self, age: int):
        self.age = age # crée une variable d'instance : age

        print(f"Bonjour, je m'appelle {self.nom}", f"j'ai {self.age} ans", sep=", ")
        print("Je suis majeur" + "\n") if self.EstMajeur() else print("Je suis mineur" + "\n")

    def EstMajeur(self):
        return self.age >= 18

personne1 = Personne("Jean")
personne1.SePresenter(25)

personne1 = Personne("Emilie")
personne1.SePresenter(17)