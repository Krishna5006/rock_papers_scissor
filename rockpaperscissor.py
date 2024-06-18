import random
choose_number=input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
if (choose_number == "0"):
  print("You chose rock")
  print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif (choose_number == "1"):
  print("You chose paper")
  print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
elif (choose_number == "2"):
  print("You chose scissor")
  print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
else:
  print("Wrong choice")

computer_choice=random.randint(0,2)
print("Computer chose:")
if (computer_choice == 0):
  print("rock")
  print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif (computer_choice == 1):
  print("paper")
  print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
else:
  print("scissor")
  print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

choose_number=int(choose_number)
if choose_number == computer_choice:
    print("It's a draw!")
elif (choose_number == 0 and computer_choice == 2) or (choose_number == 1 and computer_choice == 0) or (choose_number == 2 and computer_choice == 1):
    print("User Wins")
else:
    print("Computer Wins")
