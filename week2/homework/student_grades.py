
# This program processes a list of students, calculates grades,
# filters passing students, prints summaries, and writes results to a file.
# It is intentionally written in one long block for refactoring practice.

students = [
    {"name": "Ali", "scores": [88, 90, 92]},
    {"name": "Sara", "scores": [55, 60, 58]},
    {"name": "John", "scores": [70, 72, 68]},
    {"name": "Maryam", "scores": [95, 98, 100]},
    {"name": "Tim", "scores": [40, 45, 38]},
]

print("Processing student data...\n")

passing_students = []
failing_students = []

# Calculate average grades and separate pass/fail students
for student in students:
    total = 0
    for score in student["scores"]:
        total += score

    average = total / len(student["scores"])
    student["average"] = average

    if average >= 60:
        passing_students.append(student)
    else:
        failing_students.append(student)

# Print all students with their averages
print("All Student Averages:")
print("----------------------")
for student in students:
    print(f"{student['name']} - Average: {student['average']:.2f}")
print()

# Print passing students
print("Passing Students:")
print("-----------------")
for student in passing_students:
    print(f"{student['name']} - {student['average']:.2f}")
print()

# Print failing students
print("Failing Students:")
print("-----------------")
for student in failing_students:
    print(f"{student['name']} - {student['average']:.2f}")
print()

# Write results to file
output = open("student_results.txt", "w")
output.write("Student Results Summary\n")
output.write("=======================\n\n")

output.write("All Students:\n")
for student in students:
    output.write(f"{student['name']} - {student['average']:.2f}\n")

output.write("\nPassing Students:\n")
for student in passing_students:
    output.write(f"{student['name']} - {student['average']:.2f}\n")

output.write("\nFailing Students:\n")
for student in failing_students:
    output.write(f"{student['name']} - {student['average']:.2f}\n")

output.close()

print("Results written to student_results.txt")