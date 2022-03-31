months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec")
birthday = input("Type your birthday in the format DD-MM-YYYY: ")

index = int(birthday[:2]) - 1
bd_month = months[index]

print("Your were born in", bd_month)
