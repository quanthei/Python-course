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

# --- UTILISATION ---
personne1 = Personne("Thomas", 24) # Je crée une personne
personne1.SePresenter()
