import random
rpc = {
    0: "rock",
    1: "paper",
    2: "scissors",
}


def computer_move():
    r = random.randint(0,2)
    return rpc[r]



print("This is Rock paper scissors game made with Python.")
print("You will be playing against computer, type rock, paper, or sicssors when the game starts.")
print("The first player to win two times wins the game.")
win, draw, lose, i = 0, 0, 0, 0
while True:
    i += 1
    print("Round ",i)
    while True:
        player = input("Enter your move(rock or paper or scissors): ")
        if player == "rock" or player == "paper" or player == "scissors":
            break
        else:
            print("Please enter valid move, try again.")
    comp = computer_move()
    print("You: ",player," Computer: ",comp)
    if player == comp:
        draw += 1
        print("It's a draw!")
    elif (player == "rock" and comp == "scissors") or (player == "paper" and comp == "rock") or (player == "scissors" and comp == "paper"):
        win += 1
        print("You win!")
    else:
        lose += 1
        print("You lose!")
    print("Current score:")
    print("Win: ",win," Draw: ",draw, " Lose: ",lose)

    if win >= 2:
        print("You have won the game!!")
        print("Good game!")
        break
    elif lose >= 2:
        print("Computer has won the game!!")
        print("Better luck next time.")
        break
    else:
        continue