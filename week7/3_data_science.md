# Simple Data Science Example Project

## 📁 Dataset:

[study_data.csv](study_data.csv)

## 🧠 Questions We’ll Answer

- Does more studying really improve scores?
- Is sleep important?
- Does attendance matter?
- Which factor is most related to performance?

📦 Libraries
```
pip install pandas matplotlib seaborn
```
🧑‍💻 Python Code (Real Data Science Style)
```
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
```
##  Load data
```
df = pd.read_csv("study_data.csv")
```
##  1️⃣ Inspect the data
```
print(df.info())
print(df.describe())
```

## 2️⃣ Check for missing values
```
print("\nMissing values:\n", df.isnull().sum())
```

## 3️⃣ Correlation analysis
```
corr = df[["StudyHours", "SleepHours", "Attendance", "ExamScore"]].corr()
print("\nCorrelation Matrix:\n", corr)
```
## 4️⃣ Heatmap visualization
```
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Between Study Habits and Exam Score")
plt.show()
```
## 5️⃣ Relationship plots
```
sns.scatterplot(x="StudyHours", y="ExamScore", data=df)
plt.title("Study Hours vs Exam Score")
plt.show()

sns.scatterplot(x="SleepHours", y="ExamScore", data=df)
plt.title("Sleep Hours vs Exam Score")
plt.show()

sns.scatterplot(x="Attendance", y="ExamScore", data=df)
plt.title("Attendance vs Exam Score")
plt.show()
```

## 🧠 Insight, Not Just Code

“Study hours have the strongest relationship with exam scores”

“Sleep helps, but less than study time”

“Attendance matters a lot”

This is real data science thinking.

