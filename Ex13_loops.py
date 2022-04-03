import random

x = 0.0
people = []

while x < 8:
    person = input("Type a name: ")
    people.append(person)
    x += 1
print(random.choice(people))

import random

print("This is a color guessing game")

colors = ["blue","green","red","yellow","white","black","brown","orange","yellow","pink"]

print(colors)

print("Guess the color which i have selected")

z = random.randint(0,len(colors)-1)

y = colors[z]

print(y)

x = 0

while x==0:

    user = str(input("Please enter your guessed color : ")).lower()

    if user == y:

        print("WoW! you guessed correctly genious!!!", user)

        q = str(input("Do you want to play again Yes/No : ")).lower()

        if q == "yes":

            z = random.randint(0,len(colors)-1)

            y = colors[z]

            print("Game have been refreshed now guess my new color or it could be same :D :P ")

        elif q == "no":

            x = 1

            del user

        else:

            print("Invalid Input Please try again")

    elif user != y:

        print("Oops You guessed it wrong ")

        again = str(input("would you like to give another try type 'YES' or wanna quit type 'NO'")).lower()

        if again == "yes":

            x = 0

        elif again == "no":

            x = 1

            break

        else:

            print("Incorrect Input please try again")

            again = str(input("would you like to give another try type 'YES' or wanna quit type 'NO'")).lower()

    else:

        print("Please select type the color correctly or choose the color stated above")

        print(colors)

        user = str(input("Please enter your guessed color : ")).lower()

       

q = str(input("Do you want to play again Yes/No : ")).lower()

print(" : Good Bye : ")
