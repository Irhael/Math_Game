from models.calculator import Calc

def main() -> None:
    points: int = 0
    play(points)

def play(points: int) -> None: #
    difficulty: int = int(input('Enter the difficulty level[1, 2, 3 or 4]: '))
    calc: Calc = calc(difficulty) # Creating an object of the class Calc.
    print("Enter the result for the following operation: ")
    calc.show_operation() # Showing the operation to the player.

    answer: int = int(input())
    
    if calc.check_result(answer): # If the answer is correct, the player earns 1 point.
        points += 1
        print(f'Congratulations, you owned 1 point. You have {points} points(s).')

    # The player is asked if he wants to continue playing.
    continue_game: int = int(input('Do you want to continue? [1 -> Yes, 0 -> No]: '))
    if continue_game: # If the player wants to continue, the play function is called again.
        play(points)
    else:
        print(f'You earned {points} point(s).')
        print('Thanks for playing.')
        exit(0)












        
# __name__ is a special variable that gets the name of the module that is being executed.
if __name__ == '__main__': # This line is used to call the main function when the program is executed.
    main()
