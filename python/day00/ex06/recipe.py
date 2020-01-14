import sys

cookbook = {
        'sandwich': {
            'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
            'meal': 'lunch',
            'prep_time': 10
            }
        }

cookbook['cake'] = {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': 60
        }

cookbook['salad'] = {
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': 15
        }


def printrecipe(key):
    print(f"===== Recipe for {key} =====")
    print("Ingredients list:")
    for ingr in cookbook[key]['ingredients']:
        print(f"\t- {ingr}")
    print(f"To be eaten for {cookbook[key]['meal']}.")
    print(f"Takes {cookbook[key]['prep_time']} minutes for cooking.")


def delrecipe(key):
    del cookbook[key]
    print("The", key, "recipe has been deleted.")


def addrecipe(name, ingr, meal, time):
    cookbook[name] = {
            'ingredients': ingr,
            'meal': meal,
            'prep_time': time
            }
    print("The", name, "recipe has been added in the cookbook.")


def printrecipenames():
    print("Here are the available recipes:")
    for i, recipe in enumerate(cookbook.keys(), 1):
        print(f"\t{i}. {recipe}")


print("Please select an option by typing the corresponding number:")
print("1: Add a recipe")
print("2: Delete a recipe")
print("3: Print a recipe")
print("4: Print the cookbook")
print("5: Quit")
choice = "0"
while choice != "5":
    choice = input(">> ")
    print()
    if choice == "1":
        name = input("Please enter the name of the recipe you would like to add: ")
        ingr = input("What ingredients do you need for this recipe? (use spaces to separate them) ")
        meal = input("Which meal? ")
        time = input("How many minutes does it takes for cooking? ")
        try:
            addrecipe(name, ingr.split(), meal, int(time))
        except ValueError:
            print("The cooktime must be an integer. No recipe has been added.")
    elif choice == "2":
        recipe = input("Please enter the recipe's name you would like to delete: ")
        print()
        if recipe in cookbook:
            delrecipe(recipe)
        else:
            print("The", recipe, "recipe is not in the cookbook. No recipe has been deleted.")
    elif choice == "3":
        print("Please enter the recipe's name to get its details:")
        recipe = input(">> ")
        print()
        if recipe in cookbook:
            printrecipe(recipe)
        else:
            print("The", recipe, "recipe is not in the cookbook.")
    elif choice == "4":
        printrecipenames()
    elif choice != "5":
        print("This option does not exist, please type the corresponding number.")
        print("To exit, enter 5.")
print("Cookbook closed.")
sys.exit()
