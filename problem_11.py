
student = {
    "uday": 99,
    "kiran": 65,
    "krishna": 33
}

print("Student Scores:")
for name, score in student.items():
    print(f"{name}: {score}")

topper = max(student, key=student.get)
topper_name= student[topper]

print(f"The highest score is {topper_name}, achieved by {topper}.")
