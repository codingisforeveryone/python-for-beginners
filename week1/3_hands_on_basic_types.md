# Basic types 

## Overview

| Type      | Example            | Description                        |
| --------- | ------------------ | ---------------------------------- |
| `int`     | `10`               | Whole number                       |
| `float`   | `3.14`             | Decimal number                     |
| `str`     | `"Hello"`          | String (text)                      |
| `bool`    | `True`, `False`    | Boolean value                      |
| `None`    | `None`             | Represents the absence of a value  |

## Exercise

### 🛠️ Setup
Open your terminal and start Python:
```
python
```

You should see:
```
>>>
```

### 👨‍💻 TASK 1: Numbers (int, float)
Integers and Floats
```
>>> a = 10
>>> b = 3.5
>>> a
>>> b
>>> type(a)
>>> type(b)
```

Try:
```
>>> a + b
>>> a / 2
>>> a // 2
>>> a ** 2
```

Question:
What’s the difference between / and //?

### 👨‍💻 TASK 2: Strings (str)

Strings are text — always inside quotes.
```
>>> name = "Alice"
>>> greeting = 'Hello'
>>> name
>>> type(name)
```

Try:
```
>>> full_message = greeting + ", " + name + "!"
>>> full_message
>>> name.upper()
>>> name.lower()
>>> name[0]         # first character
>>> name[-1]        # last character
```

Challenge:
Print the second and third letters of "Python" using slicing.

### 👨‍💻 TASK 3: Booleans (bool)
Booleans are either True or False.
```
>>> is_sunny = True
>>> is_raining = False
>>> print(is_sunny, type(is_sunny))
```

Try some comparisons:
```
>>> 10 > 5
>>> 5 == 5
>>> 3 != 4
>>> 10 < 2
```
Question:
What’s the result of bool(0) and bool("")?


### 👨‍💻 TASK 4: Type Conversion (Casting)

You can convert values between types.
```
>>> x = 10
>>> y = float(x)
>>> print(y, type(y))
```

Try:
```
>>> str_num = "100"
>>> num = int(str_num)
>>> num + 50

>>> float("3.14")
>>> int(3.99)
>>> str(42)
```

Challenge:
What happens if you try int("hello")?

### 👨‍💻 TASK 5: Using type() and isinstance()

Declare variables of different data types
```
>>> a = True          
>>> b = "Hello"       
>>> c = 3.14          
>>> d = 42            
```

Use isinstance() to check whether each variable belongs to a certain type
```
>>> isinstance(a, bool)
>>> isinstance(b, str)
>>> isinstance(c, float)
>>> isinstance(d, int)
>>> isinstance(a, int) 
>>> isinstance(b, bool)
```

Try checking for incorrect types (to see what happens)


### 👨‍💻 TASK 6: Mixed Practice

Predict the type and output of each line, then test it in the terminal:
```
>>> x = 10 + 3.5
>>> type(x)

>>> y = "5" * 3
>>> print(y)
>>> type(y)

>>> z = bool("Python")
>>> print(z)
>>> type(z)
```

### 👨‍💻 TASK 7: None Type (None)

None represents the absence of a value — it’s often used when a variable exists but doesn’t yet hold any data.
```
>>> empty_value = None
>>> print(empty_value)
>>> type(empty_value)
```

Now experiment:
```
>>> a = None
>>> b = 0
>>> c = ""
>>> print(bool(a), bool(b), bool(c))
```

Question:

What do you notice about how None, 0, and "" behave in Boolean context?

Why might you use None instead of 0 or an empty string?


### 🧹 Exit Python
When done, type:
```
>>> exit()
```
or press Ctrl + D.


