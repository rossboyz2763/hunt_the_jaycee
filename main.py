"""imports cave from Cave class"""
from cave import Cave
from character import Enemy
from character import Hero

road = Cave("Road")
road.set_description("A large road with a guy named ken laying on the sidewalk, you help him up as he may be of use to you later on. ")
buss_stop = Cave("Buss Stop ")
buss_stop .set_description("A small cave with ancient markings.")
car_park = Cave("Car Park")
car_park.set_description("A dark cave with a figure standing in the corner. ")
main_gate = Cave("Main Gate")
main_gate.set_description("A cave that leads to an exit. ")
side_gate = Cave("Side Gate")
side_gate.set_description("A side gate where parents drop their kids off. ")
main_ent = Cave("Main Entrance")
main_ent.set_description("The entrance that connects the main and side gates. ")
a_block = Cave("A Block")
a_block.set_description("The A block, mainly used the PE thoery lessons. ")
b_block = Cave("B block")
b_block.set_description("The B block, mainly used for english or maths. ")
quad = Cave("Main Quad")
quad.set_description("the main quad. ")
ramp_bot = Cave("Start of ramp ")
ramp_bot.set_description("The bottom of the ramp. ")
ramp_mid = Cave("Middle of ramp ")
ramp_mid.set_description("The middle of the ramp. ")
ramp_top = Cave("Top of ramp")
ramp_top.set_description("The Top of the ramp. ")
Cr1 = Cave("")
Cr1.set_description("Computers go brrrr")


ryan = Enemy("Ryan", "A victim of his own success")
ryan.set_conversation(" rizzes you emma gyatt")
ryan.set_weakness("Ken")
car_park.set_character(ryan)

Jaycee = Enemy("Jaycee", "Blade Of Macdonalds. ")
Jaycee.set_conversation("I eat big macs every day")
Jaycee.set_weakness("ken")
Cr1.set_character(Jaycee)

Ken = Hero("Ken Quisquino", "A guy with drumsticks. ")
Ken.set_conversation("im going to eat you. ")

road.link_caves(car_park, "South")
car_park.link_caves(road, "North")
car_park.link_caves(buss_stop, "West")
car_park.link_caves(main_gate, "East")
buss_stop.link_caves(car_park, "East")
main_gate.link_caves(car_park, "West")


current_cave = road
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
