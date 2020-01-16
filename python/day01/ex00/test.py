from book import Book
from recipe import Recipe

tourte = Recipe('tourte', 3, 15, ['tamago', 'kona', 'yasai', 'butter', 'cheese'], '', 'lunch')
tarte = Recipe('tarte', 3, 15, ['tamago', 'kona', 'kabocha', 'butter', 'cheese'], '', 'lunch')
livre = Book('recettes')
livre.add_recipe(tourte)
livre.add_recipe(tarte)
livre.get_recipe_by_name('tarte')
