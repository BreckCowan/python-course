f = open("test2.txt", "x")
f.write("\nThis text will be appended to the file.")

f = open("test.txt")
print(f.read())
