"""imports cave from Cave class"""
from cave import Cave
from character import Enemy
from character import Hero

cavern = Cave("Cavern")
cavern.set_description("A large cave with a guy named ken laying on the ground, you help him up may be of use to you later on. ")
grotto = Cave("Grotto")
grotto.set_description("A small cave with ancient markings.")
dungeon = Cave("Dungeon")
dungeon.set_description("A dark cave with a figure standing in the corner. ")
cave_exit = Cave("Cave Exit")
cave_exit.set_description("A cave that leads to an exit. ")

ryan = Enemy("Ryan", "A victim of his own success")
ryan.set_conversation(" rizzes you emma gyatt")
ryan.set_weakness("Ken")
dungeon.set_character(ryan)

Jaycee = Enemy("Jaycee", "Blade Of Macdonalds. ")
Jaycee.set_conversation("I eat big macs every day")
Jaycee.set_weakness("ken")
cave_exit.set_character(Jaycee)

Ken = Hero("Ken Quisquino", "A guy with drumsticks. ")
Ken.set_conversation("im going to eat you. ")

cavern.link_caves(dungeon, "South")
dungeon.link_caves(cavern, "North")
dungeon.link_caves(grotto, "West")
dungeon.link_caves(cave_exit, "East")
grotto.link_caves(dungeon, "East")
cave_exit.link_caves(dungeon, "West")

current_cave = cavern
dead = False
while dead is False:
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
                print("Bravo, you won the battle.")
                current_cave.set_character(None)
            else:
                print("Go home peasent, your weak.")
                dead = True
        else:
            print("There is no one here to fight")
