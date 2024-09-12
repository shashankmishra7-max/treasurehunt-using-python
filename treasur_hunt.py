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
print("You are at cross road.Where do you want to go?")
choice_1= input("Type 'left' for left or Type 'right' for right").lower()
if choice_1 == "left" :
 choice_2 = input("you have near lack . Type 'swim' for swim and Type 'wait' for wait").lower()
 if choice_2 == 'wait' :
  choice_3 = input("You are in the room.There is three door. 'blue','red','green'")
  if choice_3 == 'red' :
   print("There is fir in the room . Game over")
  elif choice_3 == 'blue' :
   print("There is Treasure . You won The Game")
  elif choice_3 == 'green' :
   print("There is lion in the room . Game over")
  else :
   print("Invalid enter . Game Over")

 else :
  print("Game over.You are attack by fishes")
else :
 print("You fell in trap .Game Over")