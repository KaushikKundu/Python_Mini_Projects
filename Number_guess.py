import random

top_of_range = input("Enter the top range: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("enter a number greater than zero")
        quit()
else:
    print("Pls enter a number , not any alphabet or symbols")
    quit()

randomNumber = random.randint(0, top_of_range)

# Five guesses, user enter a num, will check if num, then indicate bigger or lesser, 

guesses = 5

print("Let's start the game! You have five guesses to choose the actual number.")

while(guesses > 0):
    guesses = guesses - 1
    guess = input("Type a guess: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Pls enter a number , not any alphabet or symbols")
        quit()

    if( guess == randomNumber):
        print("You win!!! Jackpot Num: " + str(randomNumber))
        break
    elif(guess > randomNumber):
        print("Your guess is bigger than Jackpot Number")
    else:
       print("Your guess is lesser than Jackpot Number")

    if (guesses == 0) and (guess != randomNumber) :
      print("Game Over! Out of guesses!")





