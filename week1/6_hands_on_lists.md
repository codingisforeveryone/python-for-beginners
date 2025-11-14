# Lists
## Overview of list operations

| Operation | Example                   | Description       |
| --------- | ------------------------- | ----------------- |
| Create    | `my_list = [1, 2, 3]`     | Make a new list   |
| Access    | `my_list[0]`              | Get first element |
| Modify    | `my_list[1] = 99`         | Change an element |
| Add       | `my_list.append(4)`       | Add to the end    |
| Insert    | `my_list.insert(1, "hi")` | Add at position   |
| Remove    | `my_list.remove("hi")`    | Remove by value   |
| Pop       | `my_list.pop()`           | Remove last       |
| Slice     | `my_list[1:3]`            | Get a portion     |
| Sort      | `my_list.sort()`          | Sort in place     |
| Length    | `len(my_list)`            | Count items       |

## Exercise

### 👨‍💻 TASK 1: Create and View a List

Let’s start by creating a simple list of fruits.
```
>>> fruits = ["apple", "banana", "cherry", "mango"]
>>> print(fruits)
```

Try:

What happens if you add a duplicate item, like another "apple"?

What happens if the list is empty ([])?

### 👨‍💻 TASK 2: Access List Elements

![alt text](image-5.png)

Lists are ordered, and you can access items by their index number.
```
>>> print(fruits[0])      # First item
>>> print(fruits[2])      # Third item
>>> print(fruits[-1])     # Last item
```

Question:
What happens if you try to access an index that doesn’t exist, e.g. fruits[10]?

### 👨‍💻 TASK 3: Modify List Items

Lists are mutable, meaning you can change their contents.
```
>>> fruits[1] = "blueberry"
>>> print(fruits)
```

Try:
Change the last fruit to "pineapple" using a negative index.

### 👨‍💻 TASK 4: Add and Remove Items

Use list methods to grow or shrink your list.
```
>>> fruits.append("orange")      # Adds to the end
>>> fruits.insert(1, "grape")    # Adds at position 1
>>> print(fruits)
```

Now remove some:
```
>>> fruits.remove("cherry")      # Removes by value
>>> fruits.pop()                 # Removes last item
>>> print(fruits)
```

Question:
What happens if you call remove() with a value not in the list?

### 👨‍💻 TASK 5: Slicing Lists

Slicing lets you access parts of a list.
```
>>> print(fruits[1:3])
>>> print(fruits[:2])
>>> print(fruits[2:])
>>> print(fruits[-3:-1])
```

Challenge:
Print every item except the first and last.

### 👨‍💻 TASK 6: Check for Membership

You can check if an item is in a list with in.
```
>>> print("apple" in fruits)
>>> print("pear" not in fruits)
```

Challenge:
Write a one-line statement that prints "Found it!" if "banana" is in the list.

### 👨‍💻 TASK 7: Sorting and Reversing

Lists can be sorted alphabetically or numerically.
```
>>> fruits.sort()
>>> print(fruits)
>>> fruits.reverse()
>>> print(fruits)
```

Try:

Sort a list of numbers: nums = [10, 3, 7, 1, 9]

What happens if you mix numbers and strings?

### 👨‍💻 TASK 8: Combining Lists

You can join lists in different ways.
```
>>> vegetables = ["carrot", "tomato", "lettuce"]
>>> food = fruits + vegetables
>>> print(food)
```

Try:
Use a loop to add each vegetable to fruits instead of +.

### 👨‍💻 TASK 9: List Functions

Python provides many built-in functions for lists.
```
>>> numbers = [4, 8, 15, 16, 23, 42]
>>> print(len(numbers))
>>> print(max(numbers))
>>> print(min(numbers))
>>> print(sum(numbers))
>>> print(sorted(numbers))
```

Challenge:
Find the average of the numbers in the list using sum() and len().

### 👨‍💻 BONUS TASK: Nested Lists

Lists can contain other lists!
```
>>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> print(matrix[0])
>>> print(matrix[1][2])
```

Question:
How would you print the middle number (5)?

🧹 Exit Python

When you’re done:
```
>>> exit()
```

or press Ctrl + D.