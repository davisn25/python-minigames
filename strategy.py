import random

print("Hello!")
print("This is a strategy game\n")

print("archer is weak against all unities but when it attacks don't receive damage")
print("warrior is the strongest unity of game")
print("chariot is very fast and damage less than the warrior\n")

print("archer= 1, warrior= 2, chariot= 3\n")

archer_health = 30
warrior_health = 70
chariot_health = 50
health = archer_health + warrior_health + chariot_health

archer_health1 = 30
warrior_health1 = 70
chariot_health1 = 50
health1 = archer_health + warrior_health + chariot_health

while(health > 0 or health1 > 0):
    enemy = random.randrange(0, 3)

    if(enemy == 0):
        print("enemy archer")
    elif(enemy == 1):
        print("warrior")
    else:
        print("enemy charriot")

    move = input("chose your move ")

    if(enemy == 0):
        if(move == "1" or move == "archer"):
            archer_health1 -= int(random.randrange(10, 16))
            print("health:", archer_health1)
        elif(move == "2" or move == "warrior"):
            warrior_health -= int(random.randrange(5, 11))
            print(warrior_health)
        elif(move == "3" or move == "chariot"):
            chariot_health -= int(random.randrange(6, 12))
            print(chariot_health)
    elif(enemy == 1):
        if(move == "1" or move == "archer"):
            archer_health -= int(random.randrange(25, 31))
            print(archer_health)
        elif(move == "2" or move == "warrior"):
            warrior_health -= int(random.randrange(10, 21))
            print(warrior_health)
        elif(move == "3" or move == "chariot"):
            chariot_health -= int(random.randrange(15, 22))
            print(chariot_health)
    elif(enemy == 2):
        if(move == "1" or move == "archer"):
            archer_health -= int(random.randrange(22, 31))
            print(archer_health)
        elif(move == "2" or move == "warrior"):
            warrior_health -= int(random.randrange(10, 31))
            print(warrior_health)
        elif(move == "3" or move == "chariot"):
            chariot_health -= int(random.randrange(10, 21))
            print(chariot_health)

    if(health < 0):
        break