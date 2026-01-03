# File System

## 1️⃣ What is a File System?

A file system is the way files and directories (folders) are organized and stored on your computer. 

## 2️⃣ Basic Windows File Structure

On Windows, files and folders are organized in a tree-like structure starting from a root directory.

Example of a simple file structure:
C:\
  ├── Users\
  │   └── YourName\
  │       ├── Documents\
  │       ├── Downloads\
  │       └── Desktop\
  ├── Program Files\
  ├── Windows\
  └── ...


## 3️⃣ File Paths

A file path is the location of a file or folder in your file system. It can either be absolute or relative.

### Absolute Path

An absolute path gives the full location starting from the root directory.

Example: C:\Users\YourName\Documents\file.txt

### Relative Path

A relative path tells you the location relative to your current position in the file system.

Example: If you're in C:\Users\YourName\Documents, the relative path to file.txt would simply be file.txt (because it's in the same folder).


## 4️⃣ Working with Files and Folders in Python

### Creating a folder
```
import os
os.mkdir("C:/Users/YourName/Documents/NewFolder")
```
### Creating a file
```
with open("C:/Users/YourName/Documents/NewFolder/hello.txt", "w") as file:
    file.write("Hello, World!")
```

## 5️⃣ Listing Files in a Directory

```
import os

files = os.listdir("C:/Users/YourName/Documents/NewFolder")
print(files)
```

## 6️⃣ Checking if a File or Folder Exists

```
import os

if os.path.exists("C:/Users/YourName/Documents/NewFolder"):
    print("The folder exists.")
else:
    print("The folder does not exist.")
```

