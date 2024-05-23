print("Welcome to Treasure Island. Your mission is to find the treasure.")
user_choise = input("You're at a cross road. Where do you want to go? Type left or right \n")

if user_choise == "right":
    user_choise2 = input("Do you want to swimm or to wait? \n")
    if user_choise2 == "wait":
            user_choise3 = input("Which door? Red, Yellow or Blue?")
            if user_choise3 == "Red":
                print("Burned by fire. Game Over.")
            elif user_choise3 == "Yellow":
                print("You Win!")
            elif user_choise3 == "Blue":
                print("Eaten by beasts. Game Over")
            elif user_choise3 == "":
                print("Game Over")    
    else:
        print("Attacked by trout. Game over")
else:
    print("Fall in a hole. Game over")