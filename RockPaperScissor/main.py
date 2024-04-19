rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_continue = True
while game_continue:
    choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if choice > 2 or choice < 0:
        print("You typed an invalid number, you lose!")
        game_continue = False
    else:
        if choice == 0:
            print(rock)
        elif choice == 1:
            print(paper)
        elif choice == 2:
            print(scissors)

        print("Computer choose :")
        import random

        comp_choice = random.randint(0, 2)
        print(comp_choice)
        if comp_choice == 0:
            print(rock)
        elif comp_choice == 1:
            print(paper)
        elif comp_choice == 2:
            print(scissors)

        if comp_choice > choice:
            print("You lose")
        elif comp_choice == choice:
            print("It's a draw")
        elif comp_choice < choice:
            print("You win")

    Continue=input("Enter YES to continue else enter N0 :\n")
    if Continue == "no":
        game_continue = False
        