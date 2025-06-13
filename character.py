"""Character class for Hunt the Jaycee"""
class Character:
    """Defines attributes and methods for VCharacter objects"""
    def __init__(self, char_name, char_description):
        """Sets the class attributes"""
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        """Displays information about the character"""
        print(self.name + " Is here!")
        print(self.description)

    def set_conversation(self, conversation):
        """Sets what the character can say"""
        self.conversation = conversation

    def talk(self):
        """Allows character to talk to the player"""
        if self.conversation is not None:
            print(self.name + " says:" + self.conversation)
        else:
            print(self.name + " does not want to talk touy you. ")

    def fight(self):
        """Allows characters to fight the player"""
        print(self.name + " does not want to fight you.")
        return True

class Enemy(Character):
    """Defines attributes and methods for the Enemy sub-class"""
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, item_weakness):
        """sets the weakness to make squaring up easier"""
        self.weakness = item_weakness

    def get_weakness(self):
        """make squaring up easier"""
        return self.weakness

    def fight(self, combat_item):
        """lets them square up"""
        if combat_item == self.weakness:
            print("You fend off " + self.name + " with " + combat_item + " Blade of Miquella")
            return True
        else:
            print(self.name + " Swallows you whole! You died. ")
            return False

class Hero(Character):
    """Defines attributes and methods for the Hero sub-class"""
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

