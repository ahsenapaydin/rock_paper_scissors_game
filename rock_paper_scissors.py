# List containing the three actions of the game
actions_computer = ["rock", "paper", "scissors"]
actions_player = ["rock", "paper", "scissors","exit"]
# Import the random library
import random

# Initialize the scores
i = 0  # Player's score
j = 0  # Computer's score

#if both player and computer want to play again, loop will repeat.
def play_again():

# Initialize the scores
  i = 0  # Player's score
  j = 0  # Computer's score

  # Continue the game until one player reaches a score of 2
  while i <2  and j < 2:
    # Select a random action for each player in every rounde
    player = input((actions_player))
    if player == "exit":
          return False
    if player != "rock" and player != "paper" and player != "scissors":
        print("Invalid input. Please enter rock, paper, or scissors.")
        continue
    computer = random.choice(actions_computer)

    # Print the players' choices
    print("Player chooses:", player)
    print("Computer chooses:", computer)

    # 1 - Tie Condition
    if player == computer:
        print("Tie! Both players chose the same action.")

    # 2 - Winning Conditions
    elif player == "rock" and computer == "paper":
        print("Computer wins this round!")
        j += 1
    elif player == "paper" and computer == "scissors":
        print("Computer wins this round!")
        j += 1
    elif player == "scissors" and computer == "rock":
        print("Computer wins this round!")
        j += 1
    else:
        print("Player wins this round!")
        i += 1

    # Print the score after each round
    print("Player  score:", i)
    print("Computer score:", j)
    print()  # Empty line for better readability between rounds

  # Announce the final winner
  if i == 2:
    print("Player wins the game!")
  elif player == "exit":
    print("Thanks for playing!")
  elif j == 2:
    print("Computer wins the game!")
  else:
    print()
  return True

while True:
  if not play_again():
    break

# Ask the player if they want to play again
  yes = True
  no = False  
  players_want = input("Do you want to play the game again (yes / no): ")
  computers_want = random.choice([True,False])
  if players_want == "no" and computers_want == "no":
    print("Both player and computer don't want to play again. See you next time.")
    break
  elif players_want == "yes" and computers_want == "yes":
    print("Let's play again!")
    # The loop will naturally restart
  elif players_want == "no" and computers_want == "yes":
    print("Player doesn't want to play again. See you next time.")
    break
  elif players_want == "yes" and computers_want == "no":
    print("Computer doesn't want to play again. See you next time.")
    break  

