#This is a Number Guessing game.
import random

guesses_taken = 0

print("Hello! What is your name?")
my_name = input()

number = random.randint(1, 20)
print(f"Well, {my_name}, I am thinking of a number between 1 and 20")

#This was for the hint, when you divide a number by 2 if the reminder is 1 then it's an odd number. If the remainder is 0 then it's an even number.
odd_number = number%2
even_number = number%2


for guesses_taken in range(7):
    print("Take a guess.")
    guess = int(input())

    if guess < number:
        diff = number - guess
        if diff in range (3):              #Here I added the diff var, so if the number is 5 and guess is 4, then the o/p will not throw "your guess is too low".
            print("Your guess is low!")
        else:
            print("Your Guess is too low!")
    if guess > number:
        diff = guess - number
        if diff in range (3):
            print("Your guess is high!")
        else:
            print("Your guess is too high!")
    if guess == number:
        break
    if guesses_taken == 4:     #Added a hint on the 4th guess.
        print("Here's a hint for you.")
        if odd_number == 1:         
            print("The number is an odd number.")     
        elif even_number == 0:
            print("The number is an even number.")

if guess == number:
    guesses_taken = guesses_taken + 1         #Because Guesses-taken startes from 0.
    print(f"Good job,{my_name}! you guessed it in {guesses_taken} guesses!")

if guess != number:
    print(f"Nope. The number I was thinking of was {number}.")
