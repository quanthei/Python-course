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
    # pizza.AfficherPizza()
    # (1) Que pizza vegi
    # if pizza.vegetarienne:
        # pizza.AfficherPizza()
    # (2) Que pizza pas vegi
    # if not pizza.vegetarienne:
        # pizza.AfficherPizza()
    # (3) Que pizza avec de la tomate
    # if "Tomate" in pizza.ingredients: pizza.AfficherPizza() 
    # (4) Que pizza à moins de 10 balles
    if pizza.prix < 10.0: pizza.AfficherPizza() 