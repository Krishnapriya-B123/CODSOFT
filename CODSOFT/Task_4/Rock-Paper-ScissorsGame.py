# ROCK-PAPER-SCISSORS GAME

import random

print("Welcome to Rock-Paper-Scissors Game")
print("Instructions:")
print("Type rock, paper, or scissors to play\n")

user_score = 0
computer_score = 0

while True:
    # User input
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.\n")
        continue

    # Computer selection
    computer_choice = random.choice(["rock", "paper", "scissors"])

    # Display choices
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Game logic
    if user_choice == computer_choice:
        print("Result: It's a tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("Result: You win!")
        user_score += 1

    else:
        print("Result: You lose!")
        computer_score += 1

    # Display score
    print(f"Score -> You: {user_score} | Computer: {computer_score}")

    # Play again option
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nThanks for playing!")
        break

    print()