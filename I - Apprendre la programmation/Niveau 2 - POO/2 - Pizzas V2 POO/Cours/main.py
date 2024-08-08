# nom, prix, ingrédients, végétarienne

class Pizza:
    def __init__(self, nom: str, prix: float, ingredients: tuple):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients

    def AfficherPizza(self):
        print(f"PIZZA {self.nom}: {self.prix}€")
        print(", ".join(self.ingredients))
        print()
        
pizza1 = Pizza("4 fromages", 8.5, ("Brie", "Emmental", "Conté", "Parmesan"))
pizza1.AfficherPizza()