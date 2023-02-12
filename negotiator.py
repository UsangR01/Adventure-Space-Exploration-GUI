import random
import time
from pprint import pprint           #pprint = pretty printing used to display class info in an easy way
delay=0.5

class Negotiator:

    def __init__(self):
        self.health = 5
        self.negotiator_bag = []

    def dropHealth(self):
        """ Negotiator loosing one health (value) from the initialized 5"""
        self.health -= 1

    def getHealth(self):
        """ Negotaitor picking up an extra health"""
        if self.health < 5:
            self.health += 1
        else:
            self.health = 5

    def showHealth(self):
        return f'Health Status: {self.health} of 5'

    def healthStatus(self):
        if self.health > 0:
            return
        else:
            print('You are out of Life!')
            time.sleep(0.5)
            print('Game Over')
            return quit()

    def show_negotiator_inv(self):
        """
        Print out name, life and the content in negotiator bag
        """
        return f'Bag contains: {self.negotiator_bag}, Health Status: {self.health}'  #, Bonus: {self.bonus}'

    def checkNegotiator_Bag(self):
        """This checks the content of the negotiators bag
        :return: first item in the bag"""
        try:
            return self.negotiator_bag[0]
        except IndexError:
            return None

    time.sleep(1)