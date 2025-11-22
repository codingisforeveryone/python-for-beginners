# 📚 HOMEWORK: Python Functions Practice


## Task 1 — Write Your Own Greeting Function

Create a file named homework_functions.py using your terminal or VS Code.


Write a function:
```
def say_hello():
    print("Your custom greeting message here!")
```
✔️ Requirements:

Change the message to something unique

Call the function twice

## Task 2 — Function with Parameters

Create a function that takes two parameters: first_name and last_name.

Example:
```
def greet_full_name(first_name, last_name):
    # your code
```
✔️ Requirements:

Print a greeting including both names

Call it with 3 different names

## Task 3 — Function With Return Values

Create three functions:
```
def subtract(a, b): ...
def multiply(a, b): ...
def divide(a, b): ...
```
✔️ Requirements:

Each function must return its result

Store results in variables and print them

Add error handling for divide-by-zero
Example:
```
if b == 0:
    return "Cannot divide by zero"
```
## Task 4 — Function With Default Arguments

Create:
```
def introduce(name="Anonymous", age=0):
    print(f"My name is {name} and I am {age} years old.")
```
✔️ Requirements:

Test the function with:

Only a name

Only age (hint: use keyword arguments)

No arguments

Both name and age

## Task 5 — Multiple Return Values

Write a function that returns:

The sum of two numbers

The difference

The product

The average

Example:
```
def stats(a, b):
    # your code
```
✔️ Requirements:

Capture results:
```
s, d, p, avg = stats(12, 4)
```

Print all four returned values

## Task 6 — Function With List Input

Create a function:
```
def get_max(numbers):
    # return the largest number
```
✔️ Requirements:

Test it with at least 3 lists

No using Python’s built-in max()

Bonus: Write a function get_min(numbers) without using min().

## Task 7 — Mini Project: Student Grade Calculator

Create a file named grades.py.

Inside, write functions:
```
def average_grade(grades_list): ...
def highest_grade(grades_list): ...
def lowest_grade(grades_list): ...
```
✔️ Requirements:

A list of at least 5 grades

Print:

The average

Highest grade

Lowest grade

Bonus Challenge:
Write a function grade_letter(score) that returns:
```
Score	Grade
90–100	A
80–89	B
70–79	C
60–69	D
< 60	F
```
## Task 8 — Organize Code Into Modules

Create two files:

math_ops.py and main.py

Contains functions:
- add
- subtract
- multiply
- divide
- power


Import all functions:
```
from math_ops import add, subtract, multiply, divide, power
```
✔️ Requirements:

Call each function at least once

Print the results

Bonus:
Add a square_root function using exponent 0.5.

## Optional: Task 9 — Refactoring
Copy the file student_grades.py and rename it to student_grades_refactored.py

Refactor (i.e restructure) the file [`student_grades.py`](student_grades.py) into subfunctions, for example
- student_scores()
- calculate_grades()
- print_results()
- write_results_to_file()

and call this subfunctions, so that the file does the same as before.

Compare the output (print and written file) of both files and assure it is the same.

Question: How could you automate that check that the refactored file does the same? 

