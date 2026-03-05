print(r''' _                                     
| |                                    
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ 
| __| '__/ _ \/ _` / __| | | | '__/ _ \
| |_| | |  __/ (_| \__ \ |_| | | |  __/
 \__|_|  \___|\__,_|___/\__,_|_|  \___|
                                       
''')

print('Welcome to the "Treasure Island Game".'
      " Your objective will be to make the right choices and find the hidden treasure.")

direction = input("Which direction do you want to move? Right or Left? ").lower()

if direction == "left":
    print("You made the right choice. You move forward.")

    action = input("You have reached near a river. Do you want to swim or wait? ").lower()

    if action == "wait":
        print("You made the right choice. A fisherman came around in his boat and you crossed the river in the boat.")

        door = input("After walking for a bit you come across three doors, Red, Blue and Yellow."
                     "Which one will you enter? ").lower()

        if door == "yellow":
            print("Congratulations! You made the right choice and found the treasure.\nYOU WIN!")

        elif door == "red":
            print("Unfortunately, you were burned by fire.\nGame Over!")

        elif door == "blue":
            print("Unfortunately, you were eaten by beasts.\nGame Over!")

        else:
            print("Invalid choice. Game Over!")

    elif action == "swim":
        print("Unfortunately, you were attacked by an Alligator.\nGame Over!")

    else:
        print("Invalid choice. Game Over!")

elif direction == "right":
    print("Unfortunately, you fell into a hole.\nGame Over!")

else:
    print("Invalid choice. Game Over!")
