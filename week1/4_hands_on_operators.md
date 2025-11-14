# Operators

## Overview of operators

| Operator       | Symbol | Example  | Description                     |
| -------------- | ------ | -------- | ------------------------------- |
| Addition       | `+`    | `5 + 3`  | Adds values                     |
| Subtraction    | `-`    | `10 - 2` | Subtracts values                |
| Multiplication | `*`    | `4 * 2`  | Multiplies values               |
| Division       | `/`    | `8 / 3`  | Regular division (float result) |
| Floor Division | `//`   | `8 // 3` | Division that rounds down       |
| Modulus        | `%`    | `10 % 3` | Returns remainder               |
| Exponentiation | `**`   | `2 ** 3` | Raises to power                 |


## 🛠️ Setup Instructions

Open your terminal.
Run the Python interpreter:

`python`

You’ll see something like:
```
Python 3.11.6 (main, Oct 2025)
>>> 
```

The >>> means you’re in the Python interactive shell — ready to test code line by line.

## Tasks
### 👨‍💻 TASK 1: Addition and Subtraction

Try the following in the Python shell:
```
>>> 10 + 5
>>> 10 - 3
>>> 100 - 250
>>> -5 + 10
```

Question:

What happens if you add a negative number?

Can you add a float and an integer, like 3.5 + 2?

### 👨‍💻 TASK 2: Multiplication and Division
```
>>> 8 * 3
>>> 8 / 3
>>> 8 * 0.5
>>> 7 / 2
```

Question:

What type of number does / return? (Try type(7 / 2))

Does Python ever do integer division automatically?

### 👨‍💻 TASK 3: Floor Division (//)
```
>>> 8 // 3
>>> 7 // 2
>>> 10 // 5
>>> -7 // 2
```

Question:

How is // different from /?

Why does -7 // 2 give a different result than you might expect?

### 👨‍💻 TASK 4: Modulus (%)
```
>>> 10 % 3
>>> 12 % 5
>>> 7 % 7
>>> 5 % 10
>>> -7 % 3
```

Question:

What does the modulus operator actually return?

What happens when the first number is smaller or negative?

### 👨‍💻 TASK 5: Exponentiation (**)
```
>>> 2 ** 3
>>> 5 ** 2
>>> 9 ** 0.5
>>> 10 ** -1
```

Can you use ** to find square roots?

#### Advanced:

What’s the difference between 2 ** 3 and 2 ^ 3?
(Hint: try 2 ^ 3 and see what happens.)

What is
```
>>> print(2 ^ 3)
```

`^` is NOT exponentiation.

✅ What it actually does:

`^` is the bitwise XOR operator.

So:

`2 ^ 3`

is calculating:

2 in binary → `010`

3 in binary → `011`

`XOR` → `001` → decimal 1

### 👨‍💻 TASK 6: Combining Operators

Try combining several operations in one line:
```
>>> 10 + 5 * 2
>>> (10 + 5) * 2
>>> 2 ** 3 + 4 * 2
>>> (2 ** 3) + (4 * 2)
```

Question:

What happens when you add parentheses?

What order does Python evaluate operators in? (Look up operator precedence if unsure!)

### 👨‍💻 TASK 7: Interactive Mini Challenge

In your terminal, create two variables:
```
>>> a = 12
>>> b = 5
```

Now try to print the result of each operation:
```
>>> print(a + b)
>>> print(a - b)
>>> print(a * b)
>>> print(a / b)
>>> print(a // b)
>>> print(a % b)
>>> print(a ** b)
```

🧹 Exit the Python Shell

When finished, type:
```
>>> exit()
```
or press Ctrl + D.


