def play():
    import random

    print("Hello!")
    print("This is a strategy game\n")

    print("archer is weak against all unities but when it attacks don't receive damage")
    print("warrior is the strongest unity of game")
    print("chariot is very fast and damage less than the warrior\n")

    print("archer= 1, warrior= 2, chariot= 3\n")

    class Army:
        def __init__(self, health = 100):
            self.health = health

        def show_health(self):
            print(f"Health: {self.health}")

        def __str__(self):
            return "army"

    class Archer(Army):
        def __init__(self):
            super(Archer, self).__init__()
            self.name = "archer"
            self.damage = int(random.randrange(10, 16))
            self.defense = 15
    class Warrior(Army):
        def __init__(self):
            super(Warrior, self).__init__()
            self.name = "warrior"
            self.damage = int(random.randrange(15, 23))
            self.defense = 30
    class Chariot(Army):
        def __init__(self):
            super(Chariot, self).__init__()
            self.name = "chariot"
            self.damage = int(random.randrange(13, 25))
            self.defense = 25

    archer = Archer()
    warrior = Warrior()
    chariot = Chariot()
    first_army = [archer, warrior, chariot]

    archer1 = Archer()
    warrior1 = Warrior()
    chariot1 = Chariot()

    end = False
    times = 0

    while(not end):
        enemy = random.choice([chariot1.damage, warrior1.damage, archer1.damage])

        if (enemy == chariot1.damage):
            print("        /¯¯¯¯¯|\n"
                  "       /      |\n"
                  "|¯¯¯¯¯¯       |\n"
                  "|     /\¯¯¯/\ |           Carroça inimiga!\n"
                  "|    /__\./__\|   ====\n"
                  "|____\  / \  /|===D\n"
                  "      \/___\/\n")
        elif(enemy == warrior1.damage):
            print("/¯¯¯¯¯¯¯¯¯¯¯¯¯¯\ \n"
                  "|              |\n"
                  "|              |\n"
                  "| |¯¯¯|  |¯¯¯| |   Guerreiro inimigo!\n"
                  "| |   |__|   | |\n" 
                  "| |          | |\n"
                  "\_|          |_/\n")
        else:
             print("   /(\n"
                   "  /  \ \n"
                   " /    )\n"
                   "⟨#-------->   Arqueiro inimigo!\n"
                   " \    )\n"
                   "  \  / \n"
                   "   \(\n")

        move = input("Choose your attack: ")

        if(move == "1" or move == "archer"):
            unit = archer
            unit_defense = archer.defense
            unit_attack = archer.damage
            unit_health = archer.health
        elif(move == '2' or move == "warrior"):
            unit_defense = warrior.defense
            unit_attack = warrior.damage
            unit_health = warrior.health
        elif(move == '3' or move == "chariot"):
            unit_defense = chariot.defense
            unit_attack = chariot.damage
            unit_health = chariot.health

        att = unit_defense - enemy
        unit_health -= att

        print("- {:2d} | - 10\n"
              "* {:2d} | * 90".format(att, unit_health))

        times += 1
        end = times == 5

if(__name__ == "__main__"):
    play()