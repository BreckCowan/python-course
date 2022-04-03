import random

colors = ['red', 'green', 'blue', 'yellow', 'black', 'white', 'purple', 'orange', 'teal', 'pink', 'brown', 'gray', 'indigo', 'violet']

while True:
    color = colors[random.randint(0, len(colors) - 1)]
    guess = input("Guess a color: ")

    while True:
        if (color == guess):
            break
        else:
            guess = input("Try again: ")
    
    print("You guessed it!")

    play_again = input("Play again? (y/n): ")

    if play_again.lower() == 'n':
        break
print("Thanks for playing!")
