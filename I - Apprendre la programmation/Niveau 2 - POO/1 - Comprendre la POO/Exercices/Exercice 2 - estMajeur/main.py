# --- DEFINITION ---
class Personne:
    # Construteur
    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = age

    def SePresenter(self):
        print(f"Bonjour je m'appelle {self.nom}", f"J'ai {self.age} ans", sep="\n")
    
    def demanderNom():
        pass    

    # EstMajeur -> True/False
    def estMajeur(self) -> bool:
        if self.age >= 18:
            return True
        return False
    
# --- UTILISATION ---
personne1 = Personne("Thomas", 24) # Je crée une personne
personne1.SePresenter()

if personne1.estMajeur():
    print(f"{personne1.nom} est majeur !")
else:
    print(f"{personne1.nom} est mineur !")