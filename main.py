"""imports cave from Cave class"""
from cave import Cave
from character import Enemy

cavern = Cave("Cavern")
cavern.set_description("A damp and dirty cave.")
grotto = Cave("Grotto")
grotto.set_description("A small cave with ancient markings.")
dungeon = Cave("Dungeon")
dungeon.set_description("A large cave with a Half rotted women sitting on a throne, you help her up as she may be of use to you later on. ")

ryan = Enemy("Ryan", "A victim of his own success")
ryan.set_conversation(" rizzes you emma gyatt")
ryan.set_weakness("malenia")
dungeon.set_character(ryan)

cavern.link_caves(dungeon, "South")
dungeon.link_caves(cavern, "North")
dungeon.link_caves(grotto, "West")
grotto.link_caves(dungeon, "East")

current_cave = cavern
while True:
    print("\n")
    current_cave.get_details()
    inhabitated = current_cave.get_character()
    if inhabitated is not None:
        inhabitated.describe()
    command = input("What do you want to do next? >  ")
    if command in ["North", "South", "East", "West"]:
        current_cave = current_cave.move(command)
    elif command == "Talk":
        if inhabitated is not None:
            inhabitated.talk()
    elif command == "Fight":
        if inhabitated is not None and isinstance(inhabitated, Enemy):
            fight_with = input("What do you want to fight with? ")
            if inhabitated.fight(fight_with) is True:
                print("Bravo, you win the battle.")
                current_cave.set_character(None)
            else:
                print("Go home peasent, your weak.")
        else:
            print("There is no one here to fight")
