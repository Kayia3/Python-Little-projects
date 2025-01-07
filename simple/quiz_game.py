print("Welcome to my computer quiz")

playing = input("Do you want to play?\n")

if playing.lower() != "yes":
    quit()

print("Let's go")

points = 0

answer = input("What CPU stand for?\n")
if answer.lower() == "central processing unit":
    print("Correct!")
    points +=1
else:
    print('Incorrect!')  

answer = input("What GPU stand for?\n")
if answer.lower() == "graphic processing unit":
    print("Correct!")
    points +=1
else:
    print('Incorrect!')

answer = input("What RAM stand for?\n")
if answer.lower() == "random access memory":
    print("Correct!")
    points +=1
else:
    print('Incorrect!')

answer = input("What PSU stand for?\n")
if answer.lower() == "power supply unit":
    print("Correct!")
    points +=1
else:
    print('Incorrect!')

print("You have got {} points".format(points))  

