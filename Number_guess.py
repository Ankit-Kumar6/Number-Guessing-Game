#This is a Guess Number game.
import random

guesses_taken = 0

print("Hello! What is your name?")
my_name = input()

number = random.randint(1, 20)
print(f"Well, {my_name}, I am thinking of a number between 1 and 20")

odd_number = number%2
even_number = number%2


for guesses_taken in range(7):
    print("Take a guess.")
    guess = int(input())

    if guess < number:
        diff = number - guess
        if diff in range (3):
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
    if guesses_taken == 4:
        print("Here's a hint for you.")
        if odd_number == 1:
            print("The number is an odd number.")
        elif even_number == 0:
            print("The number is an even number.")

if guess == number:
    guesses_taken = guesses_taken + 1
    print(f"Good job,{my_name}! you guessed it in {guesses_taken} guesses!")

if guess != number:
    print(f"Nope. The number I was thinking of was {number}.")
