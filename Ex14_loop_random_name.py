import random

people = []

for x in range(0, 8):
    person = input("Enter a name: ")
    people.append(person)

index = random.randint(0, 7)

random_person = people[index]

print("The random person is: " + random_person)
