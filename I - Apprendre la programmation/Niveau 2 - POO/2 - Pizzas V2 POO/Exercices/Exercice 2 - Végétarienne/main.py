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

menu_pizzas = [
              Pizza("4 fromages", 12, ("Brie", "Emmental", "Conté", "Parmesan")),
              Pizza("Margherita", 9.5, ("Tomate", "Mozzarella", "Basilic")),
              Pizza("Reine", 10.5, ("Tomate", "Jambon", "Champignons", "Mozzarella")),
              Pizza("Burrata", 13.5, ("Tomate", "Champignons", "Burrata"))
              ]

for pizza in menu_pizzas:
    pizza.AfficherPizza()