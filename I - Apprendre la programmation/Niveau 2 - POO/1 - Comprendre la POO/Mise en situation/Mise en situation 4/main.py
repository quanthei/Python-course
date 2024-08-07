# POO EXERCICE DE MISE EN SITUATION 4

# ---
class Personne:
    def __init__(self, nom: str):
        self.nom = nom

    def SePresenter(self):
        print(f"Bonjour, je m'appelle {self.nom}")

# ---
def ajouter_personne(id_personne: int) -> str:
    nom = input(f"Nom de la personne {id_personne} à ajouter à la liste: ")
    return nom

noms = []
id_personne = 1

# Premier passage
noms.append(ajouter_personne(id_personne))

while True:
    if input(f"Si vous souhaitez ajouter une {id_personne + 1}ème personne entrez 'o': ").lower() == "o":
        id_personne += 1
        noms.append(ajouter_personne(id_personne))
    else:
        break

for nom in noms:
    Personne(nom).SePresenter()