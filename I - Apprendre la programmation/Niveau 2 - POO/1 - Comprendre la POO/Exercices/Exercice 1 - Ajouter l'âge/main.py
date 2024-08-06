# --- DEFINITION ---
class Personne:
    # Construteur
    def __init__(self, nom: str):
        self.nom = nom

    def SePresenter(self):
        print(f"Bonjour je m'appelle {self.nom}")
    
    def demanderNom():
        pass    

# --- UTILISATION ---
personne1 = Personne("Thomas") # Je crée une personne
personne1.SePresenter()
