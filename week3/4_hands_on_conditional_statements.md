# Conditional statements

## Overview

| Statement                        | Description                                                     |
| -------------------------------- | --------------------------------------------------------------- |
| `if`                             | Executes block if condition is True                             |
| `elif`                           | Checks additional condition if previous `if` or `elif` is False |
| `else`                           | Executes block if all previous conditions are False             |
| `==`, `!=`, `<`, `>`, `<=`, `>=` | Comparison operators                                            |
| `and`, `or`, `not`               | Logical operators to combine conditions                         |
| Nested `if`                      | `if` statements inside another `if` block                       |


## Exercise

Create file `conditional_statements.py`.

### 👨‍💻 TASK 1: Basic if Statement
```
age = 18

if age >= 18:
    print("You are an adult.")
```

Try:
Change age to 15 and see what happens.

### 👨‍💻 TASK 2: if…else Statement
```
age = 15

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

Challenge:
Test with different ages like 0, 18, and 100.

### 👨‍💻 TASK 3: if…elif…else
```
marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")
```

Try:
Change marks to different values and predict the output before running.

### 👨‍💻 TASK 4: Comparison Operators
```
a = 10
b = 20

if a == b:
    print("a is equal to b")
if a != b:
    print("a is not equal to b")
if a < b:
    print("a is less than b")
if a > b:
    print("a is greater than b")
if a <= 10:
    print("a is less than or equal to 10")
```

### 👨‍💻 TASK 5: Logical Operators (and, or, not)
```
temperature = 25
raining = False

if temperature > 20 and not raining:
    print("It’s a nice day!")
    
if temperature > 30 or raining:
    print("Stay indoors.")
```

Challenge:
Experiment with different values for temperature and raining and predict the output.

### 👨‍💻 TASK 6: Nested if Statements
```
marks = 82

if marks >= 50:
    print("You passed!")
    if marks >= 75:
        print("Great job!")
else:
    print("You failed!")
```

Try:
Change marks to 40 and 80 to see the difference.

### 👨‍💻 TASK 7: Practical Example — Number Checker

Create a .py file called number_checker.py:
```
num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")
```
Run it:
```
python number_checker.py
```

Challenge:
Modify it to also check if the number is even or odd.

### 👨‍💻 TASK 8: Practical Example — Simple Login
```
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Access granted")
else:
    print("Access denied")
```

Try:
Change the username/password combinations to see how the program responds.

### 👨‍💻 TASK 9: Practical Example — Leap Year Checker
```
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
```

Challenge:
Test with years like 2000, 1900, 2024, 2023.