# --- DEFINITION ---
class Personne: 
    # Construteur
    def __init__(self, nom: str = "", age: int = 0):
        if nom == "":
            self.nom = self.DemanderNom()
        else:
            self.nom = nom
        self.age = age

    def SePresenter(self):
        infos_pers = f"Bonjour je m'appelle {self.nom}"
        if self.age == 0:
           print(infos_pers) 
        else:
            print(infos_pers, f"J'ai {self.age} ans", sep=". ")

            if self.EstMajeur():
                print(f"{self.nom} est majeur !")
            else:
                print(f"{self.nom} est mineur !")
                
    def DemanderNom(self) -> str:
        nom = input("Merci d'indiquer votre prénom : ")
        return nom 
    
    # EstMajeur -> True/False
    def EstMajeur(self) -> bool:
        return self.age >= 18
    
# --- UTILISATION ---
personne1 = Personne("Thomas", 24) # Je crée une personne
personne1.SePresenter()

personne2 = Personne()
personne2.SePresenter()
