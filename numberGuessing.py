import math
import random

"""
User inputs the lower bound and upper bound of the range.
The compiler generates a random integer between the range and store it in a variable for future references.
For repetitive guessing, a while loop will be initialized.
If the user guessed a number which is greater than a randomly selected number, the user gets an output “Try Again! You guessed too high“
Else If the user guessed a number which is smaller than a randomly selected number, the user gets an output “Try Again! You guessed too small”
And if the user guessed in a minimum number of guesses, the user gets a “Congratulations! ” Output.
Else if the user didn’t guess the integer in the minimum number of guesses, he/she will get “Better Luck Next Time!” output."""

#taking inputs
lower = int(input("give lower bound: "))
upper = int(input("give upper bound: "))

number = random.randint(lower,upper)

maxGuess = round(math.log(upper - lower + 1, 2)) #the maximum number needed to find the number of range (upper-lower+1) in log2
print("\n\tYou've only ",
       maxGuess, 
      " chances to guess the integer!\n")

guessCount = 0

while guessCount < maxGuess:

    guessNumber = int(input("sayı tahmin ediniz: "))
    guessCount += 1

    if guessNumber > number:
        print("Try Again! You guessed too high")
        print("Your remaining rights: ",(maxGuess-guessCount))
    elif guessNumber < number:
        print("Try Again! You guessed too low")
        print("Your remaining rights: ",(maxGuess-guessCount))
    else:
        print("“Congratulations")
        break
if guessCount == maxGuess:
    print("Better Luck Next Time!!")
