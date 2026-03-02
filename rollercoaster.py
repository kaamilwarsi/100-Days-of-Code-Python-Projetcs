print("Welcome to the RollerCoaster Ticket Counter")

height = int(input("What is your height (in centimeters)? "))
bill = 0

if height >= 130:
    print("Congratulations, you can ride our rollercoaster")

    age = int(input("What is your age? "))
    if age <= 11:
        print("Unfortunately, you are not eligible for a rollercoaster ride yet. We hope to see you once you turn 12 years old!")
    if age < 18:
        print("Congratulations, you are eligible for a rollercoaster.\nPeople under 18 years pay $7")
        bill += 7
    if age >= 18:
        print("Congratulations, you are eligible for a rollercoaster.\nPeople over 18 years pay $12")
        bill += 12

    picture = input("Do you want your pictures to be taken on the rollercoaster? (y/n)? ")
    if picture == "y":
        bill += 3
        print(f"Alright, your total bill is ${bill}")
    else:
        print(f"Alright, your total bill is ${bill}")
else:
        print("Unfortunately, you are not eligible for a rollercoaster. Our minimum height requirement is 130 centimeters.")
