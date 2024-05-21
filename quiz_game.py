print("Welcome to my quiz game!")

playing = input("Do you want to play? ")

if playing.lower() != "y":
    quit()

points = 0
answer = input("What is the full form of Wi-Fi? ")
if answer.lower() == "wireless fidelity":
    points += 5
    print(f"Points: {points}")
else:
    print("Incorrect!")
