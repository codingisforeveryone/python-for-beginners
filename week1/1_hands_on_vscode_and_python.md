# Setup VS Code and Python

## 1. Go to the official website

Link: https://code.visualstudio.com/download

## 2. Choose your operating system

Click Download for Windows, macOS, or Linux depending on your OS.

## 3. Install it

### Windows: Download .zip file and unpack. Click Code.exe

### macOS: Open the .zip file and drag Visual Studio Code into the Applications folder.

### Linux: You can install using package managers (example for Ubuntu):
```
sudo apt update
sudo apt install code
```

## 4. Open VSCode and discover
![alt text](images/image-3.png)
## 5. Open terminal
At the top -> Terminal -> New Terminal


## 6. Navigate in the terminal

create folder with the name `my_folder`:
```
mkdir my_folder
```

go into the folder with the name `my_folder`
```
cd my_folder
```

go up in the file system:
```
cd .. 
```
show what's in the current directory:
```
dir
```

## 7. Check if python is already installed
In the terminal type:
```
python --version
```
If you see the version, it is installed, otherwise not.

## 8. Install Python

Link: https://www.python.org/downloads/

Windows: Download installer and follow instructions

MacOS: Download installer and follow instructions

Linux:
```
sudo apt update
sudo apt install python3
```

## 9. Run python in the terminal

```
python
```

You should see:
```
>>>
```

The `>>>` means you’re in the Python interactive shell — ready to test code line by line.