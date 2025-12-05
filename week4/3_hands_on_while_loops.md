# `while` loops

## Overview

| Feature            | Description                                             |
| ------------------ | ------------------------------------------------------- |
| `while condition:` | Runs the loop as long as the condition is True          |
| `break`            | Exits the loop immediately                              |
| `continue`         | Skips the current iteration and continues with the next |


## Exercise

### 👨‍💻 TASK 1: Basic while Loop

Create a file called while_basic.py:
```
count = 0

while count < 5:
    print("Count is:", count)
    count += 1
```

TASK:

Run it.

Change the condition to < 3 and observe the difference.

### 👨‍💻 TASK 2: Using break
```
Create a file called while_break.py:

count = 0

while True:
    print("Count is:", count)
    count += 1
    if count == 5:
        print("Breaking the loop")
        break
```

TASK:

Run it.

Change the break condition to count == 3 and see what happens.

### 👨‍💻 TASK 3: Using continue

Create a file called while_continue.py:
```
count = 0

while count < 5:
    count += 1
    if count % 2 == 0:
        continue
    print("Odd count:", count)
```

TASK:

Run it and notice how even numbers are skipped.

### 👨‍💻 TASK 4: User Input Loop

Create a file called while_input.py:
```
password = ""

while password != "python123":
    password = input("Enter the password: ")
    if password == "python123":
        print("Access granted!")
    else:
        print("Wrong password, try again.")
```

Challenge:

Modify the loop to limit attempts to 3.

### 👨‍💻 TASK 5: Counter with while
```
num = 1
total = 0

while num <= 10:
    total += num
    num += 1

print("Sum of numbers from 1 to 10:", total)
```

Challenge:

Change the loop to sum numbers from 1 to 50.

### 👨‍💻 TASK 6: Nested while Loops
```
i = 1

while i <= 3:
    j = 1
    while j <= 3:
        print(f"i={i}, j={j}")
        j += 1
    i += 1
```

TASK:

Run it and observe how nested while loops work.

### 👨‍💻 TASK 7: Practical Mini-Project — Guess the Number

Create a file called guess_number.py:
```
import random

secret = random.randint(1, 10)
guess = 0

while guess != secret:
    guess = int(input("Guess the number (1-10): "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Congratulations! You guessed it!")
```

Challenge:

Add a counter for the number of attempts.

Limit the player to 5 attempts and print a “Game Over” message if they fail.



