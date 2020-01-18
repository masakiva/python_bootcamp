import sys
import datetime
from recipe import Recipe


class Book:
    def __init__(self, name):
        if type(name) is not str or not name:
            sys.exit("ERROR: 'name' must be a non-empty string")
        self.name = name
        self.creation_date = datetime.datetime.now()
        self.last_update = self.creation_date
        self.recipes_list = {'starter': {}, 'lunch': {}, 'dessert': {}}

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for key in self.recipes_list:
            if name in self.recipes_list[key]:
                print(self.recipes_list[key][name])
                return self.recipes_list[key][name]
        sys.exit(f"ERROR: the recipe '{name}' is not in the book")

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if recipe_type not in ['starter', 'lunch', 'dessert']:
            sys.exit("ERROR: 'recipe' must be an object of class Recipe")
        return [*self.recipes_list[recipe_type]]

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            sys.exit("ERROR: 'recipe' must be an object of class Recipe")
        elif recipe.name in self.recipes_list[recipe.recipe_type]:
            print(f"ERROR: '{recipe.name}' is already in the book")
        else:
            self.recipes_list[recipe.recipe_type][recipe.name] = recipe
        self.last_update = datetime.datetime.now()
