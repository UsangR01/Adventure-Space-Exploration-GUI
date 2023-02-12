"""
    Create a room described "description". Initially, it has
    no exits. The 'description' is something like 'kitchen' or
    'an open court yard'.
"""

class Location:

    def __init__(self, description:str, booby_trap:bool, deadZone:bool, rescue_loc:bool, image_path: str = None):
        """
            Constructor method.
        :param description: Text description for this location
        :param deadZone: Text status of this location
        """
        self.description = description
        self.exits = {}  # Dictionary
        # self.items = []
        self.booby_trap = booby_trap
        self.deadZone = deadZone
        self.rescue_loc = rescue_loc
        self.image_path = image_path
        self.enemy = []
        self.hostage = []
        self.locationInv = []

    def set_exit(self, direction, neighbour):
        """
            Adds an exit for a room. The exit is stored as a dictionary
            entry of the (key, value) pair (direction, room).
        :param direction: The direction leading out of this room
        :param neighbour: The room that this direction takes you to
        :return: None
        """
        self.exits[direction] = neighbour

    def get_short_description(self):
        """
            Fetch a short text description.
        :return: text description
        """
        return self.description

    def get_long_description(self):
        """
            Fetch a longer description including available exits.
        :return: text description
        """
        return f'Location: {self.description}, Exits: {self.get_exits()},\n {self.show_locationInv()}.'

    def get_exits(self):
        """
            Fetch all available exits as a list.
        :return: list of all available exits
        """
        all_exits = list(self.exits.keys())
        return all_exits

    def get_exit(self, direction):
        """
            Fetch an exit in a specified direction.
        :param direction: The direction that the player wishes to travel
        :return: Room object that this direction leads to, None if one does not exist
        """
        if direction in self.exits:
            return self.exits[direction]
        else:
            return None

    def show_locationInv(self):
        """
        Show the inventory of the location
        :return:
        """
        return f'Items found include: {[i for i in self.locationInv]}.'

    def addItems(self, item):
        """
        To add an item to a location, this item is automatically initialized with the room
        enemy and hostage to their respective list  in a given location
        """
        self.locationInv.append(item.name)

    def addEnemy(self, enemy):
        self.enemy.append(enemy)

    def addHostage(self, hostage):
        self.hostage.append(hostage)

    def show_enemy(self):
        enemyStr = ""
        for e in self.enemy:
            enemyStr += "" + e.getDescription()
        return enemyStr

    def show_all_enemy(self):
        return self.enemy

    def show_hostage(self):
        hostageStr = ""
        for h in self.hostage:
            hostageStr += "" + h.getDescription()
        return hostageStr

    def checkLocation_inventory(self):
        """This checks the content of a particular location
        :return: first item in the location"""
        try:
            return self.locationInv[0]
        except IndexError:
            return None
