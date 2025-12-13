# Libraries (packages)
## Overview of libraries in this exercise

| Step | Library          | Purpose                        |
| ---- | ---------------- | ------------------------------ |
| 1    | requests         | Access web APIs                |
| 2    | numpy            | Numerical computations         |
| 3    | matplotlib       | Data visualization             |
| 4    | pandas           | Data manipulation and analysis |

## Tasks
### 👨‍💻 TASK 1: Installing a Library

TASK: Install the requests library using pip.
```
pip install requests
pip install beautifulsoup4
```


Check installation:
```
pip freeze
```

### 👨‍💻 TASK 2: Using the requests and beautifulsoup Library

Create a file called use_requests.py:
```
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0"}
url = "https://github.com/codingisforeveryone/python-for-beginners/tree/main"

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

title = soup.title.text
print("Page title:", title)
```

TASK:

Run it.

Observe the status code and headers from GitHub’s API.

### 👨‍💻 TASK 3: Installing and Using numpy

TASK: Install numpy:
```
pip install numpy
```

Create a file called use_numpy.py:
```
import numpy as np

# Create an array
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)
print("Mean:", np.mean(arr))
print("Sum:", np.sum(arr))
```

TASK:

Run it.

Modify the array and calculate different statistics.

### 👨‍💻 TASK 4: Installing and Using matplotlib

TASK: Install matplotlib:
```
pip install matplotlib
```

Create a file called use_matplotlib.py:
```
# use_matplotlib.py
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
```

TASK:

Run it.

Modify x and y to see how the plot changes.

### 👨‍💻 TASK 6: Bonus — Using pandas

TASK: Install pandas:
```
pip install pandas
```

Create use_pandas.py:
```
# use_pandas.py
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)
print(df)
print("\nAverage Age:", df["Age"].mean())
```

TASK:

Run it.

Add more rows or columns to practice data manipulation.



