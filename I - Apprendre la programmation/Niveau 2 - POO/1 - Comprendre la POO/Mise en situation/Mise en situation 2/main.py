# POO EXERCICE DE MISE EN SITUATION 2
# Code mal pensé car on passe l'âge en argument de la fonction SePresenter et non pas comme une variable d'instance ! Il n'est donc pas accesible dans EstMajeur
# Le mieux serait encore de passer l'âge directement dans le constructeur
# Pas de gestions d'erreurs sur le nom et l'âge !
class Personne:
    def __init__(self, nom: str, age: int):
        self.nom = nom # crée une variable d'instance : nom
        self.age = age # crée une variable d'instance : age
        print(f"Constructeur personne: {self.nom}")

    def SePresenter(self):
        print(f"Bonjour, je m'appelle {self.nom}", f"j'ai {self.age} ans", sep=", ")
        print("Je suis majeur" + "\n") if self.EstMajeur() else print("Je suis mineur" + "\n")

    def EstMajeur(self):
        return self.age >= 18

personne1 = Personne("Jean", 25)
personne1.SePresenter()

personne2 = Personne("Emilie",17)
personne2.SePresenter()