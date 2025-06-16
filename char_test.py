"""this is a test for the character"""
from character import Enemy

ryan = Enemy("Ryan", "A victim of his own success")
ryan.describe()
ryan.set_conversation(" rizzes you emma gyatt")
ryan.talk()
ryan.set_weakness("ken")

fight_with = input("What do you want to fight with? ")
ryan.fight(fight_with)
