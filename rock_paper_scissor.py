import random
rock = ('''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''')

paper = ('''     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)''')

scissor = ('''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)''')

options = [rock, paper, scissor]
computer = random.choice(options)

choice = input("What do you want to play? Rock, Paper or Scissor? ").lower()

if choice == "rock":
    print(rock)

    print("Computer Chooses:")
    print(computer)

    if computer == scissor:
        print("You Win!")

    if computer == paper:
        print("You Lose!")

    if computer == rock:
        print("Draw!")

elif choice == "paper":
    print(paper)

    print("Computer Chooses:")
    print(computer)

    if computer == scissor:
        print("You Lose!")

    if computer == paper:
        print("Draw!")

    if computer == rock:
        print("You Win!")

elif choice == "scissor":
    print(scissor)

    print("Computer Chooses:")
    print(computer)

    if computer == rock:
        print("You Lose!")

    if computer == paper:
        print("You Win!")

    if computer == scissor:
        print("Draw!")

else:
    print("Invalid Choice!")
