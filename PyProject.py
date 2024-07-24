#create function called display title() to display the
# title and programming specifications for the project
import random
def display_title():
    print("this is a guessing game \nwe will be using randint()"
          " to create random numbers from 1-10 guess right and you win.")
#create a function called play game() that uses the randint() function that gets the number that the player has to guess.

def play_game():
    # It then returns a random number between 1 and 10.
    random_number = random.randint(1, 10)
    guess = ""
    # Use a while statement so the user can guess the number until the guess is correct.
    while guess != random_number:
        guess = int(input("Guess from 1-10"))
        # If the user guess is higher than the random number then display the message 'Too high'.
        if (guess > random_number):
            print("Too high")
        # If the users guess is lower than the random number then display the message 'Too low'.
        if (guess < random_number):
            print("Too low")
        # If the user guess matches the random number display the message, 'You guessed it '.
        if (guess == random_number):
            print("You guess it")
            # Then, a return statement returns to the statement in the main() function that is after the call to the play game() function.
            return True
# create main() function to the function call statements.
def main():
    # From the main function, call the display title() function.
    display_title()
    # Then define a variable that will hold the value of yes.
    flags = "yes"
    # Create a loop that will check the variable, while the variable equals yes then call the play game function.
    while (flags == "yes"):
        play_game()
        flags = input("do you want to play again enter yes otherwise enter no")
        # Then allow the user to input if they want to play again. If yes, play again, if no end the program.
        if (flags == "no"):
            break
# Execute the main() function
main()
