# Homework - pandas

### 👨‍💻 TASK 1: define dataframe and save as csv-file

TASK: Install pandas:
```
pip install pandas
```

Create use_pandas.py:
```
import pandas as pd

data = {
    "Name": ["Alice", "Ali", "Aisha"],
    "Age": [25, 30, 35],
    "City": ["Berlin", "Jerusalem", "London"]
}

df = pd.DataFrame(data)
print(df)
print("\nAverage Age:", df["Age"].mean())

# save csv (comma separated values) file
df.to_csv("people.csv", index=False)
```

TASK:

Run it.

Add more rows or columns to practice data manipulation.



