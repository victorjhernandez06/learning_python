print("Welcome to the Quiz Game!")
playing =  input(("Do you want to play?"))

if playing.lower() != "yes":
    quit()

print("Okay!, Let's play! :)")

answer = input("What does CPU stand for? ").lower()
if answer.lower() == "central processing unit":
    print('Correct!')
else:
    print('Incorrect!')

answer = input("What does GPU stand for? ").lower()
if answer.lower() == "graphics processing unit":
    print('Correct!')
else:
    print('Incorrect!')

answer = input("What does RAM stand for? ").lower()
if answer.lower() == "random access memory":
    print('Correct!')
else:
    print('Incorrect!')

answer = input("What does PSU stand for? ").lower()
if answer.lower() == "power supply":
    print('Correct!')
else:
    print('Incorrect!')


