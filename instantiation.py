class Recipe:
    def __init__(self, name, ingredients, cost=10):
        self.name = name
        self.ingredients = ingredients
# Instantiate a Recipe object
my_recipe = Recipe("Spaghetti Bolognese", ["spaghetti", "tomato sauce", "ground beef"])
my_recipe_2 = Recipe("Ramen",["noodles", "sauce"])
# my_recipe_2 = Recipe.__init__("Ramen",["noodles", "sauce"])
my_recipe_3 = Recipe("beef stew", ["beef", "stew"], 12)


# Access the object's attributes
print("Recipe Name:", my_recipe.name)
print("ramen inredients: ", my_recipe_2.ingredients)
print(my_recipe_3.name)


class Dog:
     def walk(self):
         return "*walking*"

     def speak(self):
         return "Woof!"
     
class JackRussellTerrier(Dog):
     def talk(self):
         return super().speak()

bobo = JackRussellTerrier()
print(bobo.talk())
