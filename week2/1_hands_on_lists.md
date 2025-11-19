# Lists
## Overview of list operations

| Operation | Example                   | Description       |
| --------- | ------------------------- | ----------------- |
| Create    | `my_list = [1, 2, 3]`     | Make a new list   |
| Access    | `my_list[0]`              | Get first element (index start at 0) |
| Modify    | `my_list[1] = 99`         | Change second element |
| Add       | `my_list.append(4)`       | Add to the end    |
| Insert    | `my_list.insert(1, "hi")` | Add at position   |
| Remove    | `my_list.remove("hi")`    | Remove by value   |
| Pop       | `my_list.pop()`           | Remove last       |
| Slice     | `my_list[0:3]`            | Get element with index 0 to 2 (start is included, end is excluded)|
| Sort      | `my_list.sort()`          | Sort in place     |
| Length    | `len(my_list)`            | Count items       |

## Exercise

Create a file `list_exercise.py`

### 👨‍💻 TASK 1: Create and View a List

Let’s start by creating a simple list of fruits.
```
print("Task 1")

fruits = ["apple", "banana", "cherry", "mango"]
print(fruits)
```

Run the file by typing in the terminal:
```
python list_exercise.py
```
Make sure that you are in the right folder!

### 👨‍💻 TASK 2: Access List Elements

![alt text](images/image-5.png)

Lists are ordered, and you can access items by their index number.
```
print("Task 2")

print(fruits[0])      # First item
print(fruits[2])      # Third item
print(fruits[-1])     # Last item
```

Question:
What happens if you try to access an index that doesn’t exist, e.g. fruits[10]?

### 👨‍💻 TASK 3: Modify List Items

Lists are mutable, meaning you can change their contents.
```
print("Task 3")

fruits[1] = "blueberry"
print(fruits)
```

Try:
Change the last fruit to "pineapple" using a negative index.

### 👨‍💻 TASK 4: Add and Remove Items

Use list methods to grow or shrink your list.
```
print("Task 4")

fruits.append("orange")      # Adds to the end
print("with orange", fruits)
fruits.insert(1, "grape")    # Adds at position 1
print("with grape ", fruits)
```

Now remove some:
```
fruits.remove("cherry")      # Removes by value
print("cherry removed ", fruits)
fruits.pop()                 # Removes last item
print("last item removed", fruits)
```

Question:
What happens if you call remove() with a value not in the list?

### 👨‍💻 TASK 5: Slicing Lists

Slicing lets you access parts of a list.
```
print("Task 5")

print(fruits[1:3])
print(fruits[:2])
print(fruits[2:])
print(fruits[-3:-1])
```

Challenge:
Print every item except the first and last.

### 👨‍💻 TASK 6: Check for Membership

You can check if an item is in a list with in.
```
print("Task 6")

print("apple" in fruits)
print("pear" not in fruits)
```

### 👨‍💻 TASK 7: Sorting and Reversing

Lists can be sorted alphabetically or numerically.
```
print("Task 7")

fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
```

Try:

Sort a list of numbers: nums = [10, 3, 7, 1, 9]

### 👨‍💻 TASK 8: Combining Lists

You can join lists in different ways.
```
print("Task 8")

vegetables = ["carrot", "tomato", "lettuce"]
food = fruits + vegetables
print(food)
```


### 👨‍💻 TASK 9: List Functions

Python provides many built-in functions for lists.
```
print("Task 9")

numbers = [4, 8, 15, 16, 23, 42]
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sorted(numbers))
```

Challenge:
Find the average of the numbers in the list using sum() and len().

### 👨‍💻 BONUS TASK: Nested Lists

Lists can contain other lists!
```
print("Bonus Task")

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0])
print(matrix[1][2])
```

Question:
How would you print the middle number (5)?
