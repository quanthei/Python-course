# --- DEFINITION ---
class Personne: 
    # Variable de classe
    ESPECE_ETRE_VIVANT = "Humain"

    # Construteur
    def __init__(self, nom: str = "", age: int = 0):
        if nom == "":
            nom = self.DemanderNom()  
        
        self.nom = nom
        self.age = age

    # Methodes statiques
    def AfficherInfosEtreVivant():
        print(f"Info être vivant: {Personne.ESPECE_ETRE_VIVANT}")
    
    # Autres méthodes
    def SePresenter(self):
        infos_pers = f"Bonjour je m'appelle {self.nom}"
        print(infos_pers) if self.age == 0 else print(infos_pers, f"J'ai {self.age} ans", sep=". ")

        print(f"{self.nom} est majeur !") if self.EstMajeur() else print(f"{self.nom} est mineur !")
                
    def DemanderNom(self) -> str:
        nom = input("Merci d'indiquer votre prénom : ")
        return nom 
    
    # EstMajeur -> True/False
    def EstMajeur(self) -> bool:
        return self.age >= 18

# --- UTILISATION ---
liste_personnes = [
                  Personne("Jean", 30),
                  Personne("Paul", 15),
                  Personne("Zoe", 20)
                  ]

for personne in liste_personnes:
    personne.SePresenter()