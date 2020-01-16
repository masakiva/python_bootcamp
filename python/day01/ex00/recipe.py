import sys


class Recipe:
    def __init__(self, name, ck_lvl, ck_time, ingr, desc, r_type):
        if type(name) is not str or not name:
            sys.exit("ERROR: 'name' must be a non-empty string")
        self.name = name
        if ck_lvl not in range(1, 6):
            sys.exit("ERROR: 'cooking_lvl' must be an integer between 1 and 5")
        self.cooking_lvl = ck_lvl
        if ck_time < 0:
            sys.exit("ERROR: 'cooking_time' must be a positive or null integer")
        self.cooking_time = ck_time
        if type(ingr) is not list:
            sys.exit("ERROR: 'ingredients' must be a list")
        if not ingr:
            sys.exit("ERROR: 'ingredients' must contain at least one element")
        for s in ingr:
            if type(s) is not str:
                sys.exit("ERROR: 'ingredients's' elements must be strings")
        self.ingredients = ingr
        if type(desc) is not str:
            sys.exit("ERROR: 'description' must be a string")
        self.description = desc
        if type(r_type) is not str:
            sys.exit("ERROR: 'recipe_type' must be a string")
        if r_type not in ['starter', 'lunch', 'dessert']:
            sys.exit("ERROR: 'recipe_type' must be either 'starter', 'lunch' or 'dessert'")
        self.recipe_type = r_type

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = "\n===== Recette pour '" + self.name + "' =====\n\n"
        txt += "Vous aurez besoin de ces ingrédients:\n"
        for each in self.ingredients:
            txt += "\t- " + each + "\n"
        txt += "La marche à suivre :\n" + self.description
        txt += "Le four devra être mis au niveau " + str(self.cooking_lvl) + " pour une cuisson de " + str(self.cooking_time) + " minutes.\n"
        txt += "Cette préparation se déguste en " + self.recipe_type + ".\n"
        return txt
