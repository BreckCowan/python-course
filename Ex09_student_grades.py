grade1 = float (input("Enter grade of first test: "))
grade2 = float (input("Enter grade of second test: "))
absences = int (input("Enter number of absences: ")) 
total_classes = int (input("Enter total number of classes: "))

avg_grade = (grade1 + grade2) / 2
attendance = (total_classes - absences) / total_classes

print('Average grade', round(avg_grade, 2))
print('Attendance', str(round((attendance * 100), 2))+ '%')

if (avg_grade >= 70 and attendance >= 0.8):
    print("You passed!")
elif(avg_grade < 70 and attendance < 0.8):
    print("You failed due to attendance lower than 80% and an average grade lower than 70!")
elif(attendance >= 0.8):
    print("You failed due to an average grade lower than 70!")
else:
    print("You failed due to attendance lower than 80%!")