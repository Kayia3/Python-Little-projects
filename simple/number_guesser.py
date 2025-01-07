import random

print("Try to guess a number")

## this is the top range for the random range list of numbers
top_of_the_range = input("Please enter a number: ")

if top_of_the_range.isdigit():
    top_of_the_range = int(top_of_the_range)

    if top_of_the_range < 0:
        print("Please enter a positive number\n")
        quit()
else:
    print("Please enter  number next time\n")
    quit()

#the range from 0 to the number chosen
random_number = random.randint(0,top_of_the_range)

tries = 0
while True:
    tries+=1
    guest_input =input("Make a guess: \n")
    if guest_input.isdigit():
        guest_input = int(guest_input)
    else:
        print("Next time please enter a valid number")
        break
    if guest_input == random_number:
        print("You guess it!!")
        break
    else:
        if guest_input > random_number:
            print("You are above the number")
        else:
            print("You are below the number")
   
print("Congrats!!! You got it in ", tries," tries")