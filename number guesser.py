import random

guessing_num = random.randrange(1,101)
print("Guess the number!")
for i in range(6):
    print("You have ", 5-i, " attempt left.")
    if 5-i == 0:
        print("You lose, the number was: ",guessing_num)
    else:
        guess = int(input("Your guess: "))
        if guess == guessing_num:
            print("You win!!")
            break
        elif guess > guessing_num:
            print("It is lower.")
        elif guess < guessing_num:
            print("It is higher.")
