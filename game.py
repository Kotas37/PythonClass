from monster import Monster
from player import Player
from random import randint

name = input("What is your name? ")

health = int(input("What would you like your hp to be? "))

pick = randint(1, 4)

how = randint(50, 100)

play = Player(name, health, how)

if pick == 1:
    mon = Monster("Goblin", 100)
elif pick == 2:
    mon = Monster("Slime", 50)
elif pick == 3:
    mon = Monster("Beast", 400)
elif pick == 4:
    mon = Monster("Man", 300)

keep = 1

game = 1

print(f"A wild {mon.objectName} with {mon.objectHp} HP appeared !!!")
print(f"You ({play.objectName}) have {play.objectHit} HP and {play.objectEn} energy!")
print("\n")

while game == 1:

    while keep == 1:

        fight = input("What would you like to do? (attack, magic, wait, or run): ")
        if fight == "attack":
            if play.objectEn > 20:
                p = randint(1, 40)
                m = randint(1, 20)
                mon.objectHp -= p
                print(f"The player does a normal attack that does {p} damage!")
                play.objectHit -= m
                print(f"The {mon.objectName} hits you and does {m} damage!")
                print("\n")
                enadd = 20
                play.objectEn -= enadd
                print(f"You lost {enadd} energy")
                print("\n")
            else:
                print(f"You only have {play.objectEn}. Type wait to gain more.")
                print("\n")


        elif fight == "run":
            runque = randint(1, 3)
            if runque == 1:
                print("Run didn't work")
                print("\n")
            elif runque == 3:
                print(f"You have successfully ran away from the {mon.objectName}!!!")
                keep = 2
            else:
                keep = -1

        elif fight == "magic":
            if play.objectEn > 50:
                p = randint(1, 80)
                m = randint(1, 90)
                print(f"The player does a Magic attack that does {p} damage!")
                play.objectHit -= m
                print(f"The {mon.objectName} hits you with sparkle dust and does {m} damage!")
                mon.objectHp -= p
                enadd = 50
                play.objectEn -= enadd
                print(f"You lost {enadd} energy")
                print("\n")
            else:
                print(f"You only have {play.objectEn}. Type wait to gain more.")

        elif fight == "wait":
            print(f"The player decided to wait...")
            atta = randint(1, 3)
            if atta == 1:
                m = randint(10, 30)
                play.objectHit -= m
                print(f"The {mon.objectName} hits you with a slap that does {m} damage!")
                print("\n")
                enadd = randint(10, 20)
            if atta == 2:
                m = randint(30, 60)
                play.objectHit -= m
                print(f"The {mon.objectName} smashes you with a hammer that does {m} damage!")
                print("\n")
                enadd = randint(10, 50)
            if atta == 3:
                m = randint(50, 100)
                play.objectHit -= m
                print(f"The {mon.objectName} shoots you with a magic beam that does {m} damage!")
                enadd = randint(10, 100)

            play.objectEn += enadd
            print(f"You gained {enadd} energy")
            print("\n")


        else:
            print("This does nothing...")
            print("-_-")
            print("\n")
        if keep == 1:
            print(f"You have {play.objectHit} HP and {play.objectEn} energy Left ")
            print(f"The {mon.objectName} has {mon.objectHp} HP left")
            print("\n")

        if mon.objectHp == 0 or mon.objectHp < 0:
            print(f"You have defeated the {mon.objectName}!!!")
            keep = 2
        if play.objectHit == 0 or play.objectHit < 0:
            keep = 3

    if keep == -1:
        end = randint(0, 3)
        if end == 0:

            print(
                "The angry mob of peasants is back and they are particularly displeased to see the coins in your "
                "pocket."
                "A riot"
                "breaks out in short order and you do no survive the the onslaught.")
        elif end == 1:
            print("You ran into more monsters and they killed you")
        elif end == 2:
            print("um this is something i left in cause im lazy lol\nanyways you die cause you run you sucker")
        else:
            print(f"You couldn't run and the {mon.objectName} killed you!!!!")
            keep = 0

        print(f"\n {play.objectName} lost")
    if keep == 2:
        print("\n")

    if keep == 3:
        print(f"\nYou died to a {mon.objectName}")
    pa = input("Would you like to play again?: (yes or no) ")
    if pa == "yes":
        name = input("What is your name? ")

        health = int(input("What would you like your hp to be? "))

        pick = randint(1, 4)

        how = randint(50, 100)

        play = Player(name, health, how)

        if pick == 1:
            mon = Monster("Goblin", 100)
        elif pick == 2:
            mon = Monster("Slime", 50)
        elif pick == 3:
            mon = Monster("Beast", 400)
        elif pick == 4:
            mon = Monster("Man", 300)

        keep = 1

        game = 1

        print(f"A wild {mon.objectName} with {mon.objectHp} HP appeared !!!")
        print(f"You ({play.objectName}) have {play.objectHit} HP and {play.objectEn} energy!")
        print("\n")

    else:
        keep = 0
        game = 0


print("\nThanks for playing!!!")



