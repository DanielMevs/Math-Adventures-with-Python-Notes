from random import randint as ri


def greet():
    name = input("What's your name?")
    print(f"Hello, {name}")


def numberGame():
    greet()
    number = ri(1, 100)
    print("I'm thinking of a number between 1 and 100.")
    guess = int(input("Enter your guess: "))

    while(guess):
        if number == guess:
            print("That's correct! The number was ", number)
            break
        elif number > guess:
            print("Nope, higher")
        else:
            print("Nope. Lower.")


numberGame()
