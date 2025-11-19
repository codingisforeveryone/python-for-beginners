# Dictionaries
## Overview

| Operation   | Example                        | Description                  |
| ----------- | ------------------------------ | ---------------------------- |
| Create      | `my_dict = {"a": 1, "b": 2}`   | Define a dictionary          |
| Access      | `my_dict["a"]`                 | Get value by key             |
| Add/Update  | `my_dict["c"] = 3`             | Add or update entry          |
| Remove      | `my_dict.pop("a")`             | Remove by key                |
| Length      | `len(my_dict)`                 | Number of entries            |
| Check Key   | `"a" in my_dict`               | Test for existence           |

## Exercise

### 👨‍💻 TASK 1: Dictionaries (dict)

Dictionaries store key-value pairs.
```
person = {"name": "Mohammad", "age": 20}
print(person)
print(type(person))
print(person["name"])
```

Try:
Add a new key:
```
>>> person["country"] = "Palestine"
>>> print(person)
```

### 👨‍💻 TASK 2: Access Dictionary Values

Access data using keys:
```
>>> print(student["name"])
>>> print(student["age"])
```

Question:
What happens if you try to access a key that doesn’t exist, e.g. student["gpa"]?



### 👨‍💻 TASK 3: Add and Update Entries

Add new key-value pairs or update existing ones.
```
>>> student["gpa"] = 3.8
>>> student["age"] = 21
>>> print(student)
```

Try:
Add a new key "email" and assign a value like "muhammad@example.com".

### 👨‍💻 TASK 4: Remove Entries

Use .pop() and del to remove items.
```
>>> student.pop("major")
>>> print(student)
>>> del student["gpa"]
>>> print(student)
```

Question:
What happens if you try to remove a key that doesn’t exist?


### 👨‍💻 TASK 5: Check for Keys

Use in and not in to test for key existence.
```
>>> print("name" in student)
>>> print("gpa" not in student)
```

Challenge:
Write a one-liner that prints "Email found!" if "email" is in the dictionary.

### 👨‍💻 TASK 6: Dictionary Length

Count how many items are in your dictionary.
```
>>> print(len(student))
```
Now add another key-value pair and check the length again.





## Optional: Advanced Exercise

### Overview
| Nested      | `my_dict["x"]["y"]`            | Access nested value          |
| Loop Keys   | `for k in my_dict:`            | Iterate over keys            |
| Loop Values | `for v in my_dict.values():`   | Iterate over values          |
| Loop Items  | `for k, v in my_dict.items():` | Iterate over key-value pairs |


### 👨‍💻 TASK 7: Loop Through a Dictionary

Loop through keys, values, or both.
```
for key in student:
    print(key)
```
```
for value in student.values():
    print(value)
```
```
for key, value in student.items():
    print(f"{key}: {value}")
```

Try:
Print each key in uppercase followed by its value.

### 👨‍💻 TASK 8: Nested Dictionaries

Dictionaries can hold other dictionaries!
```
>>> classroom = {
...     "student1": {"name": "Alice", "age": 20},
...     "student2": {"name": "Bob", "age": 22}
... }
>>> print(classroom)
>>> print(classroom["student1"]["name"])
```

Try:
Add a third student with their own info.



### 👨‍💻 TASK 9: Practical Challenge — Student Report

Create a dictionary representing a student report:
```
>>> report = {
...     "math": 85,
...     "science": 92,
...     "english": 78
... }
```

Now calculate the average score:
```
>>> average = sum(report.values()) / len(report)
>>> print(f"Average Score: {average}")
```

Challenge:
Add a new subject and recalculate the average.





