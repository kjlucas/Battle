from Classes.game import Person, bcolors
from Classes.magic import Spell
import random
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 12, 124, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("meteor", 20, 200, "black")
quake = Spell("quake", 14, 140, "black")
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

player = Person(460, 65, 60, 34, [fire, thunder, blizzard, meteor, cure, cura])
enemy = Person(1200, 65, 45, 25, [fire, thunder, quake])

print(bcolors.FAIL + bcolors.BOLD + "An Enemy Attacks!" + bcolors.ENDC)
while player.get_hp() > 0:
    print("=============================")

    player.choose_action()
    choice = input("Your turn\nChoose action:")
    while (choice != '1') and (choice != '2'):
        choice = input("Choose valid action:")

    if choice is '1' and player.get_mp() <= 0:
        choice = '1'

    if choice is '1':
        print("You chose to attack")
        dmg = player.generate_dmg()
        enemy.take_dmg(dmg)
        print("You attacked for " + str(dmg) + " points of damage.   Enemy HP at " + str(enemy.get_hp()))
    else:
        player.choose_magic()
        if player.get_mp() < player.lowest_cost():
            print("You do not have enough mp to use magic, attacking...")
            dmg = player.generate_dmg()
            enemy.take_dmg(dmg)
            print("You attacked for " + str(dmg) + " points of damage.   Enemy HP at " + str(enemy.get_hp()))
        else:
            choice = int(input("Choose spell:"))
            while choice < 1 or choice > player.get_num_spells():
                choice = input("Choose valid action:")

            if player.get_mp() < player.mag[choice - 1].cost:
                print(bcolors.FAIL + "You do not have enough MP for that spell" + bcolors.ENDC)
            else:
                player.mp -= player.mag[choice - 1].cost
                spell = player.mag[choice - 1].name
                print("You chose " + spell)

                dmg = player.mag[choice - 1].dmg
                enemy.take_dmg(dmg)
                print(spell + " hit for " + str(dmg) +
                      " points of damage.    Enemy HP is at" +
                      str(enemy.get_hp()) + "\nYour MP is at " + str(player.get_mp()))

    if enemy.get_hp() <= 0:
        print("Enemy has been defeated")
        print(bcolors.BOLD + bcolors.UNDERLINE + bcolors.OKGREEN +
              "You are victorious" + bcolors.ENDC)
        break

    print("Enemy's turn")
    enemyChoice = random.randrange(1, 2)
    if enemyChoice is 1:
        dmg = enemy.generate_dmg()
        player.take_dmg(dmg)
        print("You were attacked for " + str(dmg) +
              " point of damage.     HP is at " +
              str(player.get_hp()))
    else:
        if enemy.get_mp() < enemy.lowest_cost():
            dmg = enemy.generate_dmg()
            player.take_dmg(dmg)
            print("You were attacked for " + str(dmg) +
                  " point of damage.     HP is at " +
                  str(player.get_hp()))
        else:
            enemyChoice = random.randrange(0, enemy.get_num_spells()-1)
            spell = enemy.mag[enemyChoice].name
            enemy.mp -= enemy.mag[enemyChoice].cost
            dmg = enemy.mag[enemyChoice].dmg
            player.take_dmg(dmg)
            print("You took " + str(dmg) +
                  " points of damage from enemy's " +
                  spell + ".  Your HP is at " + str(player.get_hp()))

    if player.hp <= 0:
        print(bcolors.BOLD + bcolors.FAIL + bcolors.UNDERLINE +
              "You have been defeated." + bcolors.ENDC)
        break
