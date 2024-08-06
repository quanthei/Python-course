# --- DEFINITION ---
class Personne:
    # Construteur
    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = age

    def SePresenter(self):
        print(f"Bonjour je m'appelle {self.nom}", f"J'ai {self.age} ans", sep="\n")
    
    def DemanderNom():
        pass    

    # EstMajeur -> True/False
    def EstMajeur(self) -> bool:
        if self.age >= 18:
            return True
        return False
    
# --- UTILISATION ---
personne1 = Personne("Thomas", 24) # Je crée une personne
personne1.SePresenter()

if personne1.EstMajeur():
    print(f"{personne1.nom} est majeur !")
else:
    print(f"{personne1.nom} est mineur !")