import random

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\n--- Rock, Paper, Scissors ---")
        print(  "The Rule(Just in case you forget)"
                "Rock crushes Scissors"
                "Scissors cuts Paper"
                "Paper covers Rock")
        user_choice = input("Your choice: ").lower()

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f"Computer choose: {computer_choice}")

        # Game Logic
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this game")
            computer_score += 1

        # Display Scores
        print(f"Score  You: {user_score} | Computer: {computer_score}")

        # Play Again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\nFinal Score:")
            print(f'You: {user_score} | Computer: {computer_score}')
            print("Thanks for playing!")
            break

# Run the game
play_game()
