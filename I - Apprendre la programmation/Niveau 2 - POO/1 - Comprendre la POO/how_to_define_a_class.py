###
# VOS PREMIERS PAS EN POO (PROGRAMMATION ORIENTÉE OBJET)
###
# - Différence programmation impérative / objet
# - Le plus simple possible
# - Exercices, mises en situation

# Personne  (entité -> class)
#    Données : nom, age
#    Actions :  (méthodes)
#       - SePresenter()
#       - DemanderNom() / input
#  [Personne "Jean"]     [Personne "Paul"]

# --- DEFINITION ---
class Personne:
    # Construteur
    def __init__(self, nom: str):
        print(f"Bonjour je m'appelle {nom}")

    def sePresenter():
        pass
    
    def demanderNom():
        pass    

# --- UTILISATION ---
personne1 = Personne("Thomas") # Je crée une personne

 