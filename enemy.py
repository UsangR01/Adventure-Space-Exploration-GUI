

class Enemy:
    """"
       Create an enemy "name" and assign dreadfullness
       """

    def __init__(self, name:str):
        self.name = name

    def getDescription(self):
        return self.name

