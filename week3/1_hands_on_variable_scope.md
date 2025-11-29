# Variable scope

## Exercise

### 👨‍💻 TASK 1: Local Scope

Create a file called local_scope.py:
```
def greet():
    message = "Hello from inside the function!"
    print(message)

greet()

# Uncomment the next line to see what happens
# print(message)
```

TASK:

Run it.

Uncomment print(message) outside the function.

Observe the error and understand why message is local to the function.


### 👨‍💻 TASK 2: Global Scope

Create a file called global_scope.py:
```
message = "Hello from the global scope!"

def greet():
    print(message)

greet()
print(message)
```

TASK:

Run it.

Observe that the function can access the global variable.


### 👨‍💻 TASK 3: Local vs Global
```
x = 10  # global variable

def test_scope():
    x = 5  # local variable
    print("Inside function:", x)

test_scope()
print("Outside function:", x)
```


Challenge:

Run it and explain why the x inside the function does not change the global x.
