# nom, prix, ingrédients, végétarienne

class Pizza:
    def __init__(self, nom: str, prix: float, ingredients: tuple, vegetarienne: bool = False):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vegetarienne = vegetarienne

    def AfficherPizza(self):
        veg_str = ""
        if self.vegetarienne:
            veg_str += " - VEGETARIENNE"
        print(f"PIZZA {self.nom}: {self.prix}€" + veg_str)
        print(", ".join(self.ingredients))
        print()

menu_pizzas = [
              Pizza("4 fromages", 12, ("Brie", "Emmental", "Conté", "Parmesan"), True),
              Pizza("Margherita", 9.5, ("Tomate", "Mozzarella", "Basilic"), True),
              Pizza("Reine", 10.5, ("Tomate", "Jambon", "Champignons", "Mozzarella")),
              Pizza("Burrata", 13.5, ("Tomate", "Champignons", "Burrata"), True)
              ]

for pizza in menu_pizzas:
    pizza.AfficherPizza()