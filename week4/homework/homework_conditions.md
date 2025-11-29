# 📚 HOMEWORK: Conditional Statements

## Task 1: Basic if Statement

Starter Code:
```
temperature = 30

if temperature > 25:
    print("It's a hot day!")
```

Tasks:

Change temperature to 20 — what will happen?

Change it to 25 — will the message print or not? Explain why.

Add another print statement outside the if and explain the difference.

## Task 2: if…else Statement

Starter Code:
```
password = "abc123"

if password == "admin123":
    print("Access granted.")
else:
    print("Access denied.")
```

Tasks:

Test with "admin123" — what is printed?

Test with "abc123" — why is access denied?

Modify the code so that:

"admin123" prints Access granted

any other password prints Try again

Add a comment explaining how the else part works.

## Task 3: if…elif…else

Starter Code:
```
speed = 75

if speed > 120:
    print("Too fast! Fine issued.")
elif speed > 80:
    print("Slow down!")
elif speed > 50:
    print("Normal speed.")
else:
    print("Too slow!")
```

Tasks:

Predict the output for speeds: 130, 100, 60, and 20.

Run the code to check your predictions.

Add another condition:

If speed = 120, print "Borderline speed".

## Task 4: Comparison Operators

Starter Code:
```
x = 12
y = 12
z = 20
```

Tasks:
Write code using comparison operators to print:

"x and y are equal"

"z is greater than x"

"x is less than or equal to y"

"z is not equal to y"

A condition that prints only if all three values are equal.

## Task 5: Logical Operators (and, or, not)

Starter Code:
```
battery = 40
charging = False
```

Tasks:

Write an if statement that prints "Battery low" if battery < 20 and not charging.

Write an if that prints "Charging recommended" if battery < 50 or charging is True.

Predict the output for combinations:

battery = 10, charging = False

battery = 10, charging = True

battery = 70, charging = False

Change the values and test your predictions.

## Task 6: Nested if Statements

Starter Code:
```
height = 150

if height >= 120:
    print("You can enter the ride!")
    if height >= 160:
        print("You can sit in the front row!")
else:
    print("Sorry, you're too short.")
```

Tasks:

Predict the output for heights: 110, 135, 165.

Explain why only some heights print both messages.

Add another nested condition:

If height ≥ 180, print "You are tall enough for the extreme seat!"