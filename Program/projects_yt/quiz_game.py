print("Welcome to the Quiz Game!")
playing =  input(("Do you want to play?"))

if playing != "yes":
    quit()

print("Okay! Let's play :)")
answer = input("What does CPU stand for? ")
if answer == "Central Processing Unit":
    print("Correct!")
else:
    print("Incorrect! The correct answer is Central Processing Unit.")    