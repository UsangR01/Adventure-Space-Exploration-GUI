""""
the class item holds all possible items listed in various locations of the game
item param: description, name, weight
"""

class item:

    """"
    Create an item "name" and assign weight
    """
    def __init__(self, name:str):
        self.name = name

    def getDescription(self):
        return self.name