# Rock, paper, scissors game
import random

information = { "Rock" : {"Lose" : "Paper",
                        "Win" : "Scissors",
                        "Tie" : "Rock"
                        },
                "Paper" : {"Lose" : "Scissors",
                        "Win" : "Rock",
                        "Tie" : "Paper"
                        },
                "Scissors" : {"Lose" : "Rock",
                        "Win" : "Paper",
                        "Tie" : "Scissors"
                        }
}

def game():
    user_input = str(input("Choose Rock, Paper, or Scissors: ").title())

    computer_input = random.choice(list(information.keys()))  # Picks a random option for the computer

    for info in information:

        # Checks if user won, lost, or tied to the computer
        if info == computer_input:
            print(f"I chose {computer_input}.")
            
            if user_input == information[info]["Tie"]:
                print("Tie!")
                return game()
            
            elif computer_input == information[user_input]["Win"]:
                print("You won!")
                return game()
            
            elif computer_input == information[user_input]["Lose"]:
                print("You lost!")
                return game()
            
            else:
                print("ERROR")

if __name__ == '__main__':
    game()