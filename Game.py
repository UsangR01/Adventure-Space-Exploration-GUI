from location import Location
from item import item
from negotiator import Negotiator
from enemy import Enemy
from hostage import Hostage
import time
import log
import img

"""
    This class is the main class of the "Adventure World" application. 
    'Adventure World' is a very simple, text based adventure game. Users 
    can walk around some scenery. That's all. It should really be extended 
    to make it more interesting!
    
    To play this game, use the main() method in the AdventureWorldGUI class.

    This main class creates and initialises all the others: it creates all
    rooms, creates the parser and starts the game. It also evaluates and
    executes the commands that the parser returns.
    
    This game is adapted from the 'World of Zuul' by Michael Kolling
    and David J. Barnes. The original was written in Java and has been
    simplified and converted to Python by Kingsley Sage.
    
    This version adds the beginnings of a GUI using Tkinter.
"""

class Game:

    def __init__(self):
        """
        Initialises the game.
        """
        self.create_locations()
        self.current_location = self.airport
        self.negotiator = Negotiator()
        self.entered_location = []

    def create_locations(self):
        """
            Sets up all room assets.
        :return: None
        """
        self.airport = Location("You have arrived the airport", False, False, False,
                                "images/Airport.jpg")
        self.defence_academy = Location("in the defence academy", False, False, False,
                                        "images/Defence_academy.jpg")
        self.bandit_den = Location("in a bandit den", True, True, False,
                                   "images/Bandit_den.jpg")
        self.train_station = Location("in a train station... WOW! they left some cash while fleeting", True, False,
                                      False, "images/Train_Station.jpg")
        self.industrial_zone = Location("in the industrial zone", True, False, False,
                                        "images/Industrial_zone.jpg")
        self.prison_facility = Location("in the prison facility... WOW! this map should direct me", True, False,
                                        False, "images/Prisons.jpg")
        self.city_center = Location("in the city center", False, False, False,
                                    "images/City_center.jpg")
        self.central_market = Location("in the central market... I must buy a bike as ransom", True, False,
                                       False, "images/Market.jpg")
        self.bureau_dechange = Location("in the bureau de change... Now let's change currency", True, False,
                                        False, "images/BDC.jpg")
        self.hospital = Location("in the hospital", False, False, False,
                                 "images/Hospital.jpg")
        self.central_mosque = Location("in the central mosque", False, False, False,
                                       "images/Mosque.jpg")
        self.black_market = Location("in the black market, A key? where could i use this", True, False,
                                     False, "images/Black_market.jpg")
        self.check_point = Location("in the check point", False, False, False,
                                    "images/Checkpoint.jpg")
        self.bandit_hideout = Location("in the bandit hideout", True, True, False,
                                       "images/Bandit_hideout.jpg")
        self.exchange_point = Location("in the exchange_point... GBP needed for ransom", False, False,
                                       True, "images/Exchange_point.jpg")

        """
        Set exits and neighbouring locations
        """
        self.airport.set_exit("west", self.bandit_den)
        self.airport.set_exit("east", self.defence_academy)
        self.airport.set_exit("south", self.train_station)

        self.defence_academy.set_exit("west", self.airport)
        self.defence_academy.set_exit("east", self.city_center)
        self.defence_academy.set_exit("south", self.central_market)

        self.bandit_den.set_exit("east", self.airport)

        self.train_station.set_exit("north", self.airport)

        self.city_center.set_exit("west", self.defence_academy)
        self.city_center.set_exit("east", self.hospital)
        self.city_center.set_exit("north", self.prison_facility)

        self.central_market.set_exit("north", self.defence_academy)
        self.central_market.set_exit("south", self.central_mosque)
        self.central_market.set_exit("west", self.industrial_zone)

        self.central_mosque.set_exit("north", self.central_market)

        self.industrial_zone.set_exit("east", self.central_market)

        self.hospital.set_exit("west", self.city_center)
        self.hospital.set_exit("south", self.check_point)

        self.prison_facility.set_exit("south", self.city_center)

        self.check_point.set_exit("north", self.hospital)
        self.check_point.set_exit("south", self.black_market)
        self.check_point.set_exit("west", self.bandit_hideout)

        self.black_market.set_exit("north", self.check_point)

        self.bandit_hideout.set_exit("east", self.check_point)

        self.central_mosque.set_exit("south", self.bureau_dechange)
        self.central_mosque.set_exit("west", self.exchange_point)
        self.bureau_dechange.set_exit("north", self.central_mosque)
        self.exchange_point.set_exit("east", self.central_mosque)
        self.bureau_dechange.set_exit("west", self.exchange_point)

        """
        Let's add items to each location and their corresponding weights.
        """
        self.airport.addItems(item("phone"))
        self.train_station.addItems(item("bonusCash"))
        self.defence_academy.addItems(item("AK47"))
        # self.defence_academy.addItems(item(" "))
        # self.defence_academy.addItems(item("knife"))
        self.prison_facility.addItems(item("map"))
        self.hospital.addItems(item("vitamins"))
        self.central_market.addItems(item("bike"))
        self.industrial_zone.addItems(item("bonusCash"))
        self.central_mosque.addItems(item("bonusCash"))
        self.black_market.addItems(item("key"))
        self.bureau_dechange.addItems(item("GBP"))

        """
        Let's add enemies to selected location
        """
        self.black_market.addEnemy(Enemy("thief"))
        self.bandit_den.addEnemy(Enemy("isis"))
        self.bandit_hideout.addEnemy(Enemy("bokoharam"))
        self.prison_facility.addEnemy(Enemy("ugm"))
        self.train_station.addEnemy(Enemy("heardsmen"))

        """
        Let's add hostage and kidnapper to the exchange location.
        """
        self.exchange_point.addHostage(Hostage("kidnapper"))
        self.exchange_point.addHostage(Hostage("chibok girls"))

    def print_welcome(self):
        """
        Return the welcome message as a string.
        :return: string
        """
        time.sleep(0.5)
        self.msg = \
        f'Touch down. You have arrived heat zone of kidnappers. Stay alert!\n Your current location is KADUNA Airport.\n' \
        f'Use the help command for location details. You may need to make a call to our local agents\n' \
        f'Your command words are: {self.show_command_words()}.'
        return self.msg

    def show_command_words(self):
        """
            Show a list of available commands.
        :return: list of commands as a string
        """
        return 'help', 'go', 'quit', 'dock', 'pick', 'use'

    def print_help(self):
        """
            Display some useful help text.
        :return: message
        """
        msg = \
        f'You are alone. This zone is deserted. ' \
        f'\nYour command words: {self.show_command_words()}'
        return msg

    def quit_command(self):
        """ Performs the QUIT command.
        :return: quit"""
        return quit()

    # def quit_command(self):
    #     should_quit = input("Are you sure you want to quit? (Y/N)")     # Prompt the user to confirm that they want to quit
    #     # If the user confirms, return True to indicate that the game should quit
    #     if should_quit.upper() == "Y":
    #         return True
    #     # If the user does not confirm, return False to indicate that the game should continue
    #     else:
    #         return False
    #
    # if quit_command():
    #     # Quit the game
    #     print("Quitting game...")
    #     return
    #     # Otherwise, continue playing the game
    # else:
    #     print("Continuing game...")

    def do_go_command(self, second_word):
        """
            Performs the GO command.
        :param secondWord: the direction the player wishes to travel in
        :return: text output
        """
        if second_word == None:
            # Missing second word...
            return 'Go where?'

        next_location = self.current_location.get_exit(second_word)     #if second word inputted by user is unknown
        if next_location == None:
            return f"River!, there is no access! {self.current_location.get_long_description()}"

        else:
            self.current_location = next_location       #if second word is a known direction
            log.log_move(second_word)
            if self.current_location.booby_trap == True and self.current_location.deadZone == False:    #if the location is booby trapped but not a deadzone
                return f'Booby trap, Dock!'

            elif self.current_location.deadZone == True and self.current_location.booby_trap == True:
                return f'Danger, You just ambushed in the dead zone\n' \
                       'Oh no! Better luck nest time\n'\
                       f'Game Over'
                # return quit()

            elif self.current_location.rescue_loc == True:
                return f'Ransom point, to use ransom item, input use command and second word'

            else:
                return f'{self.current_location.get_long_description()}'

    def pickup(self, second_word):
        """Creating the pickup items command"""
        if second_word == None:
            #Missing second word...

            msg = \
                f'I need clear instructions!!!' \
                f'\nPick what?'
            return msg

        else:
            if second_word in self.current_location.locationInv:
                self.negotiator.negotiator_bag.append(second_word)
                self.current_location.locationInv.remove(second_word)
                return f'You have picked a {second_word}'

    def use_up(self, second_word):
        """
        Use item at the ransom point
        :param second_word: item to be dropped
        return: None
        """
        if self.current_location != self.exchange_point:
            return f'"Use command" only to pay ransom... Not here'\
                   f'Pick an alternative command words from the list: {self.show_command_words()}'

        else:
            self.current_location = self.exchange_point
            if second_word == None:
                return 'Use what?'

            elif second_word in self.negotiator.negotiator_bag:
                log.log_use_up(second_word)
                if 'GBP' in self.negotiator.negotiator_bag:
                    self.negotiator.negotiator_bag.remove(second_word)

                    msg = \
                        f'You just used the {second_word} as ransom' \
                        f'\n"CONGRATULATION!!! HOSTAGE RESCUED", "YOU WIN"'
                    return f'{msg}' #, {quit()}

                elif 'GBP' not in self.negotiator.negotiator_bag:
                    return "You need the Ransom"
                else:
                    return f'{self.current_location.get_long_description()}'
            else:
                return f'{self.current_location.get_long_description()}'

    def dropOff (self, second_word):
        """
        Drop off item at the ransom point
        :param second_word: item to be dropped
        return: None
        """
        if second_word == None:
            #Missing second_word...
            return 'Drop what?'
        else:
            if second_word in self.negotiator.negotiator_bag:
                log.log_pickup(second_word)
                self.negotiator.negotiator_bag.remove(second_word)
                self.current_location.locationInv.append(second_word)
                return f'You just dropped {second_word}'

    def dock(self):
        """
        Performs the DOCK command.
        :param secondWord: the direction the player wishes to travel in
        :return: text output
        """
        if self.current_location.booby_trap == False:
            return
        else:
            self.negotiator.dropHealth()
            self.negotiator.healthStatus()
            #self.current_location.booby_trap = False
            msg = \
                f'Health status, {self.negotiator.showHealth()} out of 5'
        return msg