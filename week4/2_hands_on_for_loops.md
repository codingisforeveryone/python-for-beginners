# `for` loops

## Exercise

### 👨‍💻 TASK 1: Basic List Iteration

Create a file called for_loop_list.py:
```
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

TASK:

Run it.

Add more fruits to the list and see how the loop adapts.

### 👨‍💻 TASK 2: Iterating Over a String

Create a file called for_loop_string.py:
```
word = "Python"

for letter in word:
    print(letter)
```

TASK:

Run it.

Modify the string and observe how the loop prints each character.

### 👨‍💻 TASK 3: Using range()

Create a file called for_loop_range.py:
```
# Print numbers from 0 to 4
for i in range(5):
    print(i)

# Print numbers from 1 to 5
for i in range(1, 6):
    print(i)

# Print even numbers from 2 to 10
for i in range(2, 11, 2):
    print(i)
```

Challenge:

Change the step to 3 and see which numbers are printed.

### 👨‍💻 TASK 4: Sum of Numbers
```
total = 0

for i in range(1, 6):
    total += i

print("Sum of numbers from 1 to 5:", total)
```

TASK:

Modify the range to sum numbers from 1 to 100.

### 👨‍💻 TASK 5: Using break and continue
```
for i in range(1, 10):
    if i == 5:
        print("Breaking at 5")
        break
    if i % 2 == 0:
        print(f"{i} is even, skipping")
        continue
    print(f"{i} is odd")
```

TASK:

Predict the output before running.

Modify the numbers and conditions to see how break and continue work.

### 👨‍💻 TASK 6: Nested Loops
```
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i = {i}, j = {j}")
```

Challenge:

Use nested loops to print a 3x3 multiplication table.

### 👨‍💻 TASK 7: Loop with else
```
for i in range(3):
    print(i)
else:
    print("Loop completed without break")
```

Challenge:

Add a break inside the loop and see what happens to the else block.

✅ Bonus Mini-Project: List Filtering
```
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print("Even numbers:", even_numbers)
```

TASK:

Modify the code to create a list of numbers divisible by 3.