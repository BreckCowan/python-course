data_valid = False

while data_valid == False:
    grade1 = float (input("Enter grade of first test: "))
    if grade1 < 0 or grade1 > 100:
        print("Grade should be between 0 and 100!")
        continue
    else:
        data_valid = True

data_valid = False

while data_valid == False:
    grade2 = float(input("Enter grade of second test: "))
    if grade2 < 0 or grade2 > 100:
        print("Grade should be between 0 and 100!")
        continue
    else:
        data_valid = True
        
data_valid = False

while data_valid == False:
    total_classes = int(input("Enter total number of classes: "))
    if total_classes <= 0:
        print("Number of classes should be greater than 0!")
        continue
    else:
        data_valid = True

data_valid = False

while data_valid == False:
    absences = int(input("Enter number of absences: "))
    if absences < 0 or absences > total_classes:
        print("Absences should be between 0 and total number of classes!")
        continue
    else:
        data_valid = True

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