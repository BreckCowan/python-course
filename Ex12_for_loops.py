blog_posts = ["test1", "test2", "test3"]

for post in blog_posts:
    if post == "test2":
        continue
    else:
        print(post)

print("-----------------------------------")

myString = "This in my string"

for char in myString:
    print(char)

print("-----------------------------------")

for x in range(0, 10):
    print(x)

print("-----------------------------------")

person = {'name': 'John', 'age': '27', 'city': 'New York', 'country': 'USA', 'favorite_language': 'Python'}

for key in person:
    print(key, ':', person[key])

print("-----------------------------------")

blog_posts = {"Python": ["test1", "Java", "test2", "C#", "test3"], "JavaScript": ["test1", "test2", "test3"], "C#": ["test1", "test2", "test3"], "Ruby": ["test1", "test2", "test3"]}

for category in blog_posts:
    print("Posts about", category)
    for post in blog_posts[category]:
        print(post)
