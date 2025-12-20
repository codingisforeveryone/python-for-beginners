# Python module

A Python module is a file of Python code you can import into other programs to reuse functions, classes, and variables instead of rewriting them.

## Overview

| Concept                  | Explanation                                                               |
| ------------------------ | ------------------------------------------------------------------------- |
| Module                   | A Python file containing functions, classes, or variables                 |
| Import                   | Use `import module_name` or `from module_name import func` to access code |
| `__name__ == "__main__"` | Lets a module be both reusable and executable directly                    |
| Reusability              | Functions can now be used in multiple scripts without rewriting code      |

## Exercise

### 👨‍💻 TASK 1: Create a Module

Create a file called 'mymath.py':
```
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
```


This file is now your module.

Save it in the same folder as your main script.

### 👨‍💻 TASK 2: Create a Script that Uses the Module

Create a file called 'use_mymath.py':
```
import mymath

a = 10
b = 5

print("Add:", mymath.add(a, b))
print("Subtract:", mymath.subtract(a, b))
print("Multiply:", mymath.multiply(a, b))
print("Divide:", mymath.divide(a, b))
```

Run it.

Verify that the functions from mymath.py work correctly.

### 👨‍💻 TASK 3: Import Specific Functions

Create a file called use_specific.py:
```
from mymath import add, multiply

print("Add:", add(2, 3))
print("Multiply:", multiply(4, 5))
```

Run it.

Notice that you only imported the functions you need.


### 👨‍💻 INFO: What is the difference between a python module and a python package?

- A python module is one file.
- A python package is a collection of files structured in subfolders. The subfolders must contain an (empty) `__init__.py` file.

Example:

```
mypackage/
    __init__.py
    math_ops/
        __init__.py
        basic.py
        advanced.py
```
