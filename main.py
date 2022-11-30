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
    user_input = str(input("Choose Rock, Paper, or Scissors (type the word): ").title())

    computer_input = random.choice(list(information.keys()))  # Picks a random option for the computer

    # Checks to see if user inputted valid response
    if user_input not in information.keys():
        if user_input.lower() == "e":
            exit()
        
        print("Invalid response, try typing the complete word.\n")
        
        game()

    for info in information:

        # Checks if user won, lost, or tied to the computer
        if info == computer_input:
            print(f"I chose {computer_input}.")
            
            if user_input == information[info]["Tie"]:
                print("Tie!\n")
                game()
            
            elif computer_input == information[user_input]["Win"]:
                print("You won!\n")
                game()
            
            elif computer_input == information[user_input]["Lose"]:
                print("You lost!\n")
                game()
            
            else:
                print("ERROR\n")

if __name__ == '__main__':
    print("Welcome to a game of Rock, Paper, Scissors!\nTo play, please type the full word from the following options.\nTo exit, type 'e'.")
    game()
