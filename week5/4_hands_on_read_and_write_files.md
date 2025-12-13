# Read and write files

## Overview

| Operation             | Mode   | Description                            |
| --------------------- | ------ | -------------------------------------- |
| `open(filename, "r")` | Read   | Open file for reading                  |
| `open(filename, "w")` | Write  | Create or overwrite file               |
| `open(filename, "a")` | Append | Add content to existing file           |
| `file.read()`         | -      | Read entire file content               |
| `file.readlines()`    | -      | Read file line by line into a list     |
| `file.write()`        | -      | Write text to a file                   |
| `with` statement      | -      | Automatically handles closing the file |

## Exercise

### 👨‍💻 TASK 1: Writing to a File

Create a file called write_file.py:
```
# write_file.py
# Write some text to a file

file = open("example.txt", "w")
file.write("Hello, this is the first line.\n")
file.write("This is the second line.\n")
file.close()

print("Data written to example.txt")
```

TASK:

Run it.

Open example.txt in a text editor and check the content.

### 👨‍💻 TASK 2: Reading from a File

Create a file called read_file.py:
```
# read_file.py
# Read the content of a file

file = open("example.txt", "r")
content = file.read()
file.close()

print("File content:")
print(content)
```

TASK:

Run it after write_file.py to see the content.

### 👨‍💻 TASK 3: Reading Line by Line

Create a file called read_lines.py:
```
# read_lines.py
# Read a file line by line

with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())
```

TASK:

Run it. Notice that .strip() removes the newline character \n.

### 👨‍💻 TASK 4: Appending to a File

Create a file called append_file.py:
```
# append_file.py
# Append new content to a file

with open("example.txt", "a") as file:
    file.write("This line is appended.\n")

print("New line added to example.txt")
```

TASK:

Run it multiple times.

Open example.txt and see how content is added without overwriting.

### 👨‍💻 TASK 5: Writing and Reading with with Statement

Create a file called write_read_with.py:
```
# write_read_with.py
# Write and read using 'with' statement

with open("data.txt", "w") as f:
    f.write("Python is fun!\n")
    f.write("File handling is important.\n")

with open("data.txt", "r") as f:
    content = f.read()
    print(content)
```

TASK:

Run it.

Compare it to the previous example.txt.

### 👨‍💻 TASK 6: Practical Mini-Project — To-Do List

Create a file called todo.py:
```
# todo.py
# Simple to-do list program

while True:
    action = input("Enter 'add', 'show', or 'quit': ").lower()
    
    if action == "add":
        task = input("Enter a task: ")
        with open("tasks.txt", "a") as f:
            f.write(task + "\n")
    elif action == "show":
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
        print("Your tasks:")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t.strip()}")
    elif action == "quit":
        print("Goodbye!")
        break
    else:
        print("Invalid action. Try again.")
```

TASK:

Run it.

Add tasks, show tasks, and quit.

Check tasks.txt to see how data is saved.



