from random import randint
from time import sleep
def get_user_guess():
    guess = int(input("Guess a number: "))
    return guess
def roll_dice(number_of_sides):
    first_roll = randint(1,number_of_sides)
    second_roll = randint(1,number_of_sides)
    max_val = number_of_sides*2
    print("max value is : " + str(max_val))
    guess = get_user_guess()
    if guess > max_val:
        print("higher than the maximum possible value")
    else:
        print("Rolling...")
    sleep(2)
    print(str(first_roll))
    print(str(second_roll))
    sleep(1)
    total_roll = first_roll + second_roll
    print("total_roll is: "+ str(total_roll))
    if guess == total_roll:
        print("You're winner!!")
    else:
        print("You lost! :(")


roll_dice(6)
