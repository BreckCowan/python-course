def say_hello(person1, person2="The Director"):
    print("Hello " + person1 + ", how are you doing? " + person2 + " is waiting for you")

def fahr2celsius(fahr):
    celsius = (5 * (fahr - 32)) / 9
    return celsius

print("Celsius: ", round (fahr2celsius(100), 2) )
print("Kelvin: ", round (fahr2celsius(100) + 273.5 , 2) )

say_hello("Jane")

