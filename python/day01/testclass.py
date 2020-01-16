class Personnage:
    TYPE="AI"
    def __init__(self, name="moi"):
        self.name = name
        self.poste = "None"
        print("Initialisation de la classe: name=" + self.name)

    def func(self):
        print("Hello je suis " + self.name)
        print("      je suis " + self.poste)
