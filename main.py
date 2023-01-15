# Rock, paper, scissors game
import random
import sys

information = { "Rock" : {
                        "Lost" : "Paper",
                        "Win" : "Scissors",
                        "Tie" : "Rock"
                        },
                "Paper" : {
                        "Lost" : "Scissors",
                        "Win" : "Rock",
                        "Tie" : "Paper"
                        },
                "Scissors" : {
                        "Lost" : "Rock",
                        "Win" : "Paper",
                        "Tie" : "Scissors"
                        }
}

def game_input():
    '''Function asks user for input'''
    user_input = str(input("Choose Rock, Paper, or Scissors (type the word): ").title())

    # Picks a random option for the computer
    computer_input = random.choice(list(information.keys()))

    # Checks to see if user inputted valid response
    if user_input not in information:
        if user_input.lower() == "e":
            sys.exit()
        print("Invalid response, try typing the complete word.\n")
        game_input()
    else:
        game(computer_input, user_input)

def game(computer_input, user_input):
    '''Checks to see if user won'''
    # Used to state what the result of the round was
    results = ["Win", "Lost", "Tie"]
    
    if computer_input in information.keys():
        for result in results:
            # Checks to see if game result value matches user_input
            if information[computer_input][result] == user_input:
                print(f"The computer chose {computer_input} and resulted in a {result} for the computer!\n")
                game_input()


if __name__ == '__main__':
    print('''Welcome to a game of Rock, Paper, Scissors!
        \nTo play, please type the full word from the following options.
        \nTo exit, type 'e'.''')
    game_input()
