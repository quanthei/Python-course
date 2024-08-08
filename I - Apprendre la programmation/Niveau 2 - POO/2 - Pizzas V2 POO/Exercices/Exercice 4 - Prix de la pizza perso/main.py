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

class PizzaPersonnalisee(Pizza):
    def __init__(self):
        super().__init__("Personnalisée", 0, [])
        self.DemanderIngredientsUtilisateur()

    def DemanderIngredientsUtilisateur(self) -> str:
        while True:
            new_ingredient = input("Ajoutez un ingrédient (ou ENTER pour terminer): ")
            if new_ingredient == "":
                return None
            self.ingredients.append(new_ingredient)
            print(f"Vous avez {len(self.ingredients)} ingredient(s): {', '.join(self.ingredients)}")
    
menu_pizzas = [
              Pizza("4 fromages", 12, ("Brie", "Emmental", "Conté", "Parmesan"), True),
              Pizza("Margherita", 9.5, ("Tomate", "Mozzarella", "Basilic"), True),
              Pizza("Reine", 10.5, ("Tomate", "Jambon", "Champignons", "Mozzarella")),
              Pizza("Burrata", 13.5, ("Tomate", "Champignons", "Burrata"), True),
              PizzaPersonnalisee()
              ]

def tri_personnalisé(element):
    return element.prix

menu_pizzas.sort(key=tri_personnalisé, reverse=True)

for pizza in menu_pizzas:
    pizza.AfficherPizza()