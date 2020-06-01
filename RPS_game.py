# Rock, Paper, Scissors
# Play against a computer in this game of chance

# Importing the random library
import random;

# Declaring the main function
def main():

# Defining the variable to start the game and give the option to play again
    play_again = 'y';

# Creating the while loop 
    while play_again == 'y':

        print("Rock, Paper, Scissors the game.");
        print("Begin!");

        player_choice = get_player_choice()
        ai_choice = get_ai_choice()

        print("");
        print("You chose " + player_choice);
        print("The computer chose " + ai_choice);

        get_winner(player_choice, ai_choice)
        print("");

        if play_again != 'y':
            exit();
        else:
            play_again = input("Play Again? Enter 'y' to play again: ");
            print("");


# Function for getting user input from the player
def get_player_choice():

    print("Select a choice below");
    user = int(input("Rock = 1. Paper = 2. Scissors = 3: "))
    
    if user == 1:
        user = "ROCK";
            
    elif user == 2:
        user = "PAPER";
        
    elif user == 3:
        user = "SCISSORS";
            
    else:
        print("Not a valid selection, try again.");
        print("");            
        main();
        
    return user;

# Creating the 'AI' function
def get_ai_choice():

    ai = random.randint(1,3);
    if ai == 1:
        ai = "ROCK";
        
    elif ai == 2:
        ai = "PAPER";

    elif ai == 3:
        ai = "SCISSORS";

    return ai;

# Determining the outputs of the game with prompts
def get_winner(player_choice, ai_choice):
    
    if player_choice == ai_choice:
        print("It is a TIE!");

    elif player_choice == "ROCK" and ai_choice == "SCISSORS":
        print("ROCK crushes SCISSORS, you win!");
        
    elif player_choice == "PAPER" and ai_choice == "ROCK":
        print("PAPER covers ROCK, you win!");

    elif player_choice == "SCISSORS" and ai_choice == "PAPER":
        print("SCISSORS shreds PAPER, you win!");

    else:
        print("You lose!");
        

    
main();
