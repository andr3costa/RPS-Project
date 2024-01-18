from random import randint

def findWinner(p1choice,p2choice):
    if p1choice == p2choice:
        print("Tie.")
    elif p1choice == "r" and p2choice == "p":
        print("Player 2 Wins.")
    elif p1choice == "r" and p2choice == "s":
        print("Player 1 Wins.")
    elif p1choice == "p" and p2choice == "r":
        print("Player 1 Wins")
    elif p1choice == "p" and p2choice == "s":
        print("Player 2 Wins.")
    elif p1choice == "s" and p2choice == "r":
        print("Player 2 Wins")
    elif p1choice == "s" and p2choice == "p":
        print("Player 1 Wins")
    else:
        print("Invalid input(s)!")

mode = input("Do you want to play against a player or computer? (p/c): ")
p1 = input("Player 1, Rock, Paper, or Scissors? (r/p/s): ")

if mode == "p":
    p2 = input("Player 2, Rock, Paper, or Scissors? (r/p/s): ")
    findWinner(p1,p2)
elif mode == "c":
    choices = ["r","p","s"]
    choice = choices[randint(0,2)]
    print(f"Computer picked {choice}.")
    findWinner(p1, choice)
else:
    print("Invalid input!")