import random
randnum = random.randint(1,10)
yes = "test"
def intro():
    print("yo wassup it's me ur fortune teller")
    print("im super lazy so u can figure out how the game works")
    print("say 'roll' when you want a fortune")
    print("say 'stop' for no more")
def roll():
    randnum = random.randint(1, 10)
    print(randnum)
    if randnum < 4:
        print("FAILURE")
    elif randnum > 7:
        print("GOOD JOB")
    else:
        print("AVERAGE")
while True:
    intro()
    yes = input("say something")
    if yes == "roll":
        roll()
    elif yes == "stop":
        break