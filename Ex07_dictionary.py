person = { 'name': 'John', 'age': 28 , 'gender': 'M', 'address': '101 Sherwood Dr', 'phone': "2105555551"}

key = input("What information do you want to know about the person? ").lower()

result = person.get(key, "That information is not available")

print(result)
