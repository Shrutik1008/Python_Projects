import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").strip().lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid input. Please try again.")

def determine_winner(user_choice, computer_choice):

    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def display_result(user_choice, computer_choice, winner):

    if winner == 'tie':
        print(f"It's a tie! Both you and the computer chose {user_choice}.")
    elif winner == 'user':
        print(f"You win! {user_choice} beats {computer_choice}!")
    else:
        print(f"You lose! {computer_choice} beats {user_choice}!")

def main():

    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, winner)
        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1
        print(f"Score: User {user_score} - Computer {computer_score}")
        while True:
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again in ['yes', 'no']:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        if play_again == 'no':
            break

if __name__ == '__main__':
    main()
