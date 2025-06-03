"""Cave class for Hunt the Jaycee"""
class Cave:
    """Defines attributes and methods for cave objects"""
    def __init__(self, cave_name):
        self.name = cave_name
        self.description = None
        self.linked_caves = {}

    def set_name(self, cave_name):
        """Sets the cave name"""
        self.name = cave_name

    def get_name(self):
        """Gets the cave name"""
        return self.name

    def set_description(self, cave_description):
        """Sets the cave description"""
        self.description = cave_description

    def get_description(self):
        """Gets the cave description"""
        return self.description

    def describe(self):
        """Prints the cave's description"""
        print(self.description)

    def link_caves(self, cave_to_link, direction):
        """Populates dictionary of linked caves"""
        self.linked_caves[direction] = cave_to_link
        print(self.name + " linked caves:" + repr(self.linked_caves))

    def get_details(self):
        """Prints details about the current cave"""
        print(self.name)
        print("----------")
        print(self.description)
        for direction, cave in self.linked_caves.items():
            print("The " + cave.get_name() + " is " + direction)

    def move(self, direction):
        """Allows movement between liked caves"""
        if direction in self.linked_caves:
            return self.linked_caves[direction]
        else:
            print("You can't go that way, theres a wall dingus. ")
            return self
