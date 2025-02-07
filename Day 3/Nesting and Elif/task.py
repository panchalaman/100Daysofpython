print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age <= 12:
        bill = 5
        print(f"You bill is ${bill}.")
    elif age <= 18:
        bill = 7
        print(f"Your bill is ${bill}.")
    else:
        bill = 12
        print(f"Your adult ticket is ${bill}.")
    photos = input("Do you want photos taken, y for Yes and n for No")
    if photos == 'y':
        bill += 3

    print(f"Final bill is {bill}")

else:
    print("Sorry you have to grow taller before you can ride.")
