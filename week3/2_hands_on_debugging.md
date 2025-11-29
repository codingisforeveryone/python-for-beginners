# Debugging

### 👨‍💻 Task 1: Debugging a TypeError

Goal: Use the debugger to inspect variable types.
```
age = "25"
next_year = age + 1   # Bug: string + int
print(next_year)
```

Instructions:

Add `breakpoint()` before the problematic line.

Inspect the type: type(age).

Fix the error.

To stop debugging type `q`.

To continue and jump to next breakpoint() type `c`.


### 👨‍💻 Task 2: Fixing a Function That Returns the Wrong Value

Goal: Step into functions with breakpoint().
```
def multiply(a, b):
    result = a + b   # Bug: should be a * b
    return result

x = multiply(3, 4)
print("Result:", x)
```

Instructions:

Add `breakpoint()` inside the function.

Examine values of a, b, and result.

Correct the logic.

To stop debugging type `q`.

To continue and jump to next breakpoint() type `c`.