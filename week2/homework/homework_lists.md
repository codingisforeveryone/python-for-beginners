# Homework lists

### 👨‍💻 TASK 1: Creating and Viewing Lists

Create the following list:
```
fruits = ["apple", "banana", "cherry", "mango"]
print(fruits)
```

Add a duplicate fruit (e.g. "apple") using append().

Questions:

What happens when a duplicate item is added?

### 👨‍💻 TASK 2: Accessing List Elements

Run:
```
print(fruits[0])
print(fruits[2])
print(fruits[-1])
```

Question:
What happens if you try to access:
```
fruits[10]
```

Explain why.

### 👨‍💻 TASK 3: Modifying List Items

Change "banana" to "blueberry":
```
fruits[1] = "blueberry"
print(fruits)
```

Try:
Change the last item to "pineapple" using a negative index.

### 👨‍💻 TASK 4: Adding and Removing Items

Add items:
```
fruits.append("orange")
fruits.insert(1, "grape")
print(fruits)
```

Remove items:
```
fruits.remove("cherry")
fruits.pop()
print(fruits)
```

Question:
What happens if you call remove() with a value that isn’t in the list?

### 👨‍💻 TASK 5: List Slicing

Run these slices:
```
print(fruits[1:3])
print(fruits[:2])
print(fruits[2:])
print(fruits[-3:-1])
```

Challenge:
Print a slice that contains every item except the first and the last.

### 👨‍💻 TASK 6: Membership Check

Run:
```
print("apple" in fruits)
print("pear" not in fruits)
```

Challenge:
Write a one-line statement that prints "Found it!" only if "banana" is in the list.

### 👨‍💻 TASK 7: Sorting and Reversing

Sort and reverse the fruits list:
```
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
```

Try:
```
nums = [10, 3, 7, 1, 9]
```

Sort it.

Then attempt to sort a list that mixes numbers and strings.

Question:
What happens when you mix numbers and strings and try to sort?

### 👨‍💻 TASK 8: Combining Lists

Combine two lists using +:
```
vegetables = ["carrot", "tomato", "lettuce"]
food = fruits + vegetables
print(food)
```

Try:
Use a for loop to append each vegetable to fruits one by one
(without using +).

### 👨‍💻 TASK 9: Built-in List Functions

Run:
```
numbers = [4, 8, 15, 16, 23, 42]
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sorted(numbers))
```

Challenge:
Calculate the average of the numbers using sum() and len().

⭐ Bonus Task — Nested Lists

Given:
```
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0])
print(matrix[1][2])
```

Question:
How do you print the middle number (5) from the matrix?