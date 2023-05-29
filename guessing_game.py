from statistics import mean, median, mode 
import random

amount_attempt = []

score_board = []


def start_game():
    
    print('==> Welcome to the "Guess The Number" game! <==')
    print('* The instructions: Guess a number between 1 and 100! *')
    
    attempt = 0
    player_guess = 0
    
    answer = random.randint(1,100)
    
    if len(score_board) >= 1:
        best_score = score_board[0]
        print(f"Best Score: {best_score}")
         
    while player_guess != answer:
        
        player_guess = (input("Enter your guess: "))
        
        try:
            player_guess = int(player_guess)
            if player_guess >= 101 or player_guess <= 0:
                raise ValueError("That number is out of range.")
                
        except ValueError as error:
            print(f"Oops, that isn't supposed to happen! {error} Please try again.")
            
        else:

            if player_guess == answer:
                attempt +=1
                break
            elif player_guess > answer:
                print("It's lower!")
                attempt += 1
                continue
            elif player_guess < answer:
                print("It's higher!")
                attempt +=1
                continue
    
    
    amount_attempt.append(attempt)
    score_board.append(attempt)
    score_board.sort()

    attempt_mean = mean(amount_attempt)
    attempt_median = median(amount_attempt)
    attempt_mode = mode(amount_attempt)

    print("You got the guess correct!")
    print(f"It took you {attempt} attempt(s) to get the number.")
    print(f"Here are your stats: \nMean: {attempt_mean} \nMedian: {attempt_median} \nMode: {attempt_mode}")
    
    play_again = input("Would you like to play again? (Y/N):  ")

    while play_again.upper() != "Y" and play_again.upper() != "N": 
        play_again = input("I am sorry. I did not understand that, do you want to play again? (Y/N): ") 

    if play_again.upper() == "Y":
        start_game()
    elif play_again.upper() == "N":
        print("Thank you for playing!")

start_game()