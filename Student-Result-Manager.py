print("===== STUDENT RESULT MANAGER =====")

name = input("Enter student name: ")

maths = float(input("Enter Maths marks: "))
physics = float(input("Enter Physics marks: "))
chemistry = float(input("Enter Chemistry marks: "))
english = float(input("Enter English marks: "))
python = float(input("Enter Python marks: "))

total = maths + physics + chemistry + english + python
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n===== RESULT =====")
print("Student Name:", name)
print("Total Marks:", total, "/ 500")
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)

if percentage >= 50:
    print("Result: PASS")
else:
    print("Result: FAIL")