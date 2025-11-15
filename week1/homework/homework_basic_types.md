# Homework basic types

### 🛠️ Setup
Open your terminal and start Python:
```
python
```

You should see:
```
>>>
```

### 👨‍💻 TASK 1: My Info Card

Create a small “info card” using variables.

Create the following variables:
- name → your name (string)
- age → your age (integer)
- height → your height in meters (float)
- is_student → whether you are a student (boolean)

Print each variable and its type, e.g.:
```
print("Name:", name, "| Type:", type(name))
```
Note: here you are using the print() statement with `,` separting the the output.

Print a short sentence using your variables, for example:
```
print(f"My name is {name}, I am {age} years old, and my height is {height} meters.")
```
Note: here you are using an `f`-string:
- before your string you write `f` -> like this `f""`
- then you can insert variables between the text -> link this:
```
>>> age = 15
>>> f"I am {age} years old" 
```
### 👨‍💻 TASK 2: Simple Math Practice

Use integer and float operations.

Create two variables:
```
>>> a = 15
>>> b = 4
```
Print the results of:
```
>>> a + b
>>> a / b
>>> a // b
>>> a ** b
```
Write a short comment in your code explaining the difference between / and //.

### 👨‍💻 TASK 3: Working with Strings

Create a variable:
```
word = "Python"
```

Do the following:

- Print the word in uppercase and lowercase.
- Print the first and last letters.
- Print the middle three letters using slicing.
- Combine two strings, e.g.:
```
>>> greeting = "Hello"
>>> message = greeting + " " + word + "!"
>>> print(message)
```

### 👨‍💻 TASK 4: Boolean Logic

Create these variables:
```
>>> is_sunny = True
>>> is_raining = False
```
Use comparison operators to print the results of:
```
>>> 10 > 5
>>> 3 == 4
>>> bool(0)
>>> bool("")
```
Predict what each line will print before you run it.


### 👨‍💻 TASK 5: Type Conversion

Try the following:
```
>>> str_num = "100"
>>> num = int(str_num)    # this convert the string `str_num` to an `int`
>>> num + 50
```

Convert 3.99 to an integer and explain what happens.

### 👨‍💻 TASK 6: Mixed Practice Challenge

Without running the code, predict what will be printed and what the type of each variable will be. Then test it.
```
>>> x = 10 + 3.5
>>> type(x)

>>> y = "5" * 3
>>> y
>>> type(y)

>>> z = bool("Python")
>>> z
>>> type(z)
```

### 👨‍💻 TASK 7: Data Types

What is the difference between an integer (int) and a float (float)?

Which data type would you use to represent:

- a person’s name
- their age
- their height in meters
- whether they are a student
- What does the value None represent in Python?

### 👨‍💻 TASK 8: Numbers and Operators

- What’s the difference between the / and // operators? Give an example.
- What does the ** operator do in Python?
- If a = 10 and b = 3, what are the results of:
```
a / b
a // b
a ** b
```
### 👨‍💻 TASK 9: Strings

- What’s the difference between single quotes ' ' and double quotes " " in strings?
- What does name[0] return if name = "Alice"?
- What is string concatenation? Give an example.
- What happens if you try to multiply a string, e.g. "Hi" * 3?

### 👨‍💻 TASK 10: Booleans and Logic

What are the two possible values of a boolean variable?

What is the result of:
```
>>> 10 > 5
>>> 5 == 5
>>> 3 != 4
>>> 10 < 2
```
What is the result of bool(0) and bool(""), and why?


### 👨‍💻 TASK 11: Type Conversion

- What happens when you run float(3)?
- What happens if you try to run int("hello")? Why?
- How do you convert a number to a string in Python?

### 👨‍💻 TASK 12: Type Checking

- What is the purpose of the type() function?
- What is the difference between type(x) and isinstance(x, int)?

### 👨‍💻 TASK 13: Reflection (Open-ended)

- What was the most surprising thing you discovered when testing Python data types?
- In your own words, why is it important to understand data types before writing more complex Python programs?



