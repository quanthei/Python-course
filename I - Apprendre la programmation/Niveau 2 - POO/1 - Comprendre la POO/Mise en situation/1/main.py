# POO EXERCICE DE MISE EN SITUATION 1
# genre
#   False : Femme
#   True  : Homme
class Personne:
    def __init__(self, nom: str = "", age: int = 0, genre: bool = None):
        if nom == "":
            nom = self.DemanderNom()
        
        self.nom = nom  
        self.age = age
        self.genre = genre

    def SePresenter(self):
        # Afficher âge + prénom
        infos_personne = f"Bonjour, je m'appelle {self.nom}." 
        if self.age != 0:
            infos_personne += f" J'ai {self.age} ans."

        print(infos_personne)

        # Afficher genre 
        if self.genre == None: 
            print("Genre: Non précisé")
        elif self.genre: # Je suis un Homme
            print("Genre : Masculin")
        else: # Je suis une Femme
            print("Genre : Feminin")
    
        # Mineur/Majeur
        if self.age != 0:
            print(self.EstMajeur())

    def EstMajeur(self) -> bool:
        infos_personne = "Je suis "
        if self.age >= 18:
            infos_personne += "majeur"
        else:
            infos_personne += "mineur"
        if not self.genre: # Si on sûr et certain que la personne est une femme on ajoute un 'e'
            infos_personne += "e"

        return infos_personne

    def DemanderNom(self) -> str:
        while nom == "":
            nom = input("Merci d'indiquer votre prénom: ")
        return nom

personne1 = Personne("Jean", 25)
personne1.SePresenter()

personne2 = Personne("Emilie")
personne2.SePresenter()