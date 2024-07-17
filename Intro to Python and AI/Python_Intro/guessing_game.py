import random
while True:
    randnum = random.randint(1,100)
    guess = 101
    play_again = "n"
    while not guess == randnum:
        guess = int(input("make a guess"))
        if guess > randnum:
            print("way to big")
        elif guess < randnum:
            print("way to small (that's what she said lol")
        elif guess == randnum:
            print("u got it")
    play_again = input("play again? (y/n lower case)")
    if play_again == "n":
        break