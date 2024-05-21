import time
choice:list = ["rock", "paper", "scissor"]


computer:str = list(set(choice))[0]

while True:
    user_choice:str = input("Enter your choice: ")
    user_choice = user_choice.lower()

    if user_choice in choice:
        break
    else:
        print("Choose between rock, paper and scissor.")

print(f"Your choice: {user_choice}")
time.sleep(1)
print(f"Computer's choice: {computer}")

if choice.index(user_choice) > choice.index(computer):
    print("You win!")
elif choice.index(user_choice) < choice.index(computer):
    print("You lose!")
else:
    print("Draw")

