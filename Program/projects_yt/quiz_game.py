print("Welcome to the Quiz Game!")
playing =  input(("Do you want to play?"))

if playing.lower() != "yes":
    quit()

print("Okay!, Let's play! :)")

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print('Correct!')
else:
    print('Incorrect!')

answer = input("What does GPU stand for? ")


