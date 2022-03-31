my_age = 37

user_age = int(input("How old are you? "))

if(my_age > user_age):
    print("You are younger than me!")
elif(my_age < user_age):
    print("You are older than me!")
elif(my_age == user_age):
    print("We are the same age!")