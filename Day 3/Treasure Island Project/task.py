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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
first_move = input("Would you like to move left or right?")

if first_move == "right":
    print("You fall into a hole. Game over...")
else:
    second_move = input("You come to a river. Do you swim across, or wait?")
    if second_move == "swim":
        print("You drown in the river. Game over...")
    else:
        print("A few hours pass.. suddenly three doors appear in front of you. One is red, one is blue, and one is yellow.")
        third_move = input("Which color door do you choose?")
        if third_move == "red":
            print("You fall into the deep pit of hell and burn to death.. Game over...")
        elif third_move == "blue":
            print("You are suddenly sucked into the void of space. Out there waiting is a giant galatic beast. He eats you for a snack. Game over...")
        else:
            print("You found the one piece! Winner!")
