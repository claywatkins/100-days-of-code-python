import random
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

actions_list = [rock, paper, scissors]
cpu_random_action = random.randint(0,2)
player_action = int(input("Choose an action: 0 for rock, 1 for paper, 2 for scissors"))
print(f"You chose:\n{actions_list[player_action]}")
print(f"Computer chose:\n {actions_list[cpu_random_action]}")
if player_action == cpu_random_action:
    print("Its a draw")
elif player_action == 2 and cpu_random_action == 0:
    print("Computer wins")
elif player_action == 0 and cpu_random_action == 2:
    print("Player wins")
elif player_action == 1 and cpu_random_action == 2:
    print("Computer wins")
elif player_action == 2 and cpu_random_action == 1:
    print("Player wins")
elif player_action == 0 and cpu_random_action == 1:
    print("Computer wins")
elif player_action == 1 and cpu_random_action == 0:
    print("Player wins")
