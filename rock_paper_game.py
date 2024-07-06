import random

def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, scissor): ").lower()
    while user_choice not in ["rock", "paper", "scissor"]:
        print("Invalid choice. Please choose again.")
        user_choice = input("Enter your choice (rock, paper, scissor): ").lower()
    return user_choice

def get_computer_choice():
    choices = ["rock", "paper", "scissor"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", 0, 0
    elif (user_choice == "rock" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "Paper wins!", 0, 1
    elif (user_choice == "rock" and computer_choice == "scissor") or \
         (user_choice == "scissor" and computer_choice == "rock"):
        return "Rock wins!", 1, 0
    elif (user_choice == "paper" and computer_choice == "scissor") or \
         (user_choice == "scissor" and computer_choice == "paper"):
        return "Scissor wins!", 0, 1

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result, user_points, computer_points = determine_winner(user_choice, computer_choice)
        print(result)
        
        user_score += user_points
        computer_score += computer_points
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
    
    print(f"Final Scores:\nUser: {user_score}\nComputer: {computer_score}")

if __name__ == "__main__":
    play_game()
