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



