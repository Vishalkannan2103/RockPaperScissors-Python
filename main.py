import random
options = ("rock", "paper", "scissor")
playing = True
while playing:
    user = None
    computer = random.choice(options)

    while user not in options:
        user = input("Enter a choice (rock, paper, scissor):")
    print(f"user:{user}")
    print(f"computer:{computer}")
    if user == computer:
        print("Ooh! its a tie!")
    elif user == "scissor" and computer == "rock":
        print("Yay! You Won!")
    elif user == "scissor" and computer == "paper":
        print("Yay! You Won")
    elif user == "paper" and computer == "rock":
        print("Yay! You Won")
    else:
        print("Oops! You Lose!")
    if not input("play again? (y/n):").lower() == "y":
        playing = False
        break
print("Thanks For Playing")

