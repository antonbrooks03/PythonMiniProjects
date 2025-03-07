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
print("Welcome to FortNite.")
print("Your mission is to get the Vic Roy.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

q1 = input('You go down a hill. Where do you want to go? Type "straight" or "right" ')
if q1 == "right":
    q2 = input('You are now at Shifty Shafts. Do you want to loot a chest or pick up a shotgun off the floor? Type "chest" or "floor".')
    if q2 == "floor":
          q3 = input('You hear a opponent close by. You rush a player and are infront of him. Do you shoot him in the head, body, or feet? Type "head", "body", or "feet"')
          if q3 == "head":
                    print("You missed the shot and got boxed like a fish. He trap killed you. Game Over.")
          elif q3 == "body":
                    print("He was already low and you killed him only dealing 56 damage. Victory Royale!!!")
          elif q3 == "feet":
                    print("You are not Dequan. Those toes aren't yours. You got no-scoped. Game Over.")
    elif q2 == "chest":
          print("Myth was camping the chest. He killed you. Game Over.")
elif q1 == "straight":
    print("You ended up at Tilted Towers and got 200 pumped to the head! Game Over.")

# place \n in your code so it's easier to read