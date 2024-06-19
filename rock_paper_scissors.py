import random

# Function to print the choices
def print_choice(choice):
    if choice == 0:
        return """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
    elif choice == 1:
        return """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
    elif choice == 2:
        return """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
    else:
        return "Invalid choice"

# Function to determine the winner
def determine_winner(user, computer):
    if user == computer:
        return "It's a draw!"
    elif (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
        return "User Wins"
    else:
        return "Computer Wins"

# Get user's choice
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ")

if user_choice not in ["0", "1", "2"]:
    print("Wrong choice")
else:
    user_choice = int(user_choice)
    print(f"You chose {['Rock', 'Paper', 'Scissors'][user_choice]}")
    print(print_choice(user_choice))
    
    # Get computer's choice
    computer_choice = random.randint(0, 2)
    print(f"Computer chose {['Rock', 'Paper', 'Scissors'][computer_choice]}")
    print(print_choice(computer_choice))
    
    # Determine the winner
    result = determine_winner(user_choice, computer_choice)
    print(result)
