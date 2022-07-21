print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("Do you want to go on the boat? Y or N ").lower()
if choice1 == 'y':
    print("You go on the boat.")
    choice2 = input("Do you want to go to the island? Y or N ").lower()
    if choice2 == 'y':
        print("You go to the island.")
        choice3 = input("Do you want to go to the cave? Y or N ").lower()
        if choice3 == 'y':
            print("You go to the cave.")
            choice4 = input(
                "Do you want to go to the treasure? Y or N ").lower()
            if choice4 == 'y':
                print("You go to the treasure.")
                print("You found the treasure!")
            else:
                print("You go to the treasure.")
                print("You found the treasure!")
        else:
            print("You go to the cave.")
            print("You found the treasure!")
    else:
        print("You go to the island.")
        print("You found the treasure!")
