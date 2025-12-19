# Classes

### What is a `class`?
A `class` combines data and functions. A `class` can be used when an object of that class is created. 


### 👨‍💻 TASK 1: Create a Bank Account Class

Create a file called `bank_account.py`:
```
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner     
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
    
    def info(self):
        print(f"owner: {self.owner}, balance: {self.balance}")
```

### 👨‍💻 TASK 2: Create Objects and Test Methods

Create a file `test_account.py` 

```
# create object account_muhammad from class BankAccount
account_muhammad = BankAccount("Muhammad", 1000)

# create object account_aisha from class BankAccount
account_aisha = BankAccount("Aisha", 500)

account_muhammad.info()
account_aisha.info()

account_muhammad.withdraw(100)


account_aisha.deposit(100)
account_aisha.info()

account_aisha.withdraw(300)
account_aisha.info()
```

Run in terminal:
```
python test_account.py
```

Observe how each account works independently.


✅ Key Concepts Covered

| Concept    | Explanation                                       |
| ---------- | ------------------------------------------------- |
| `class`    | `BankAccount` A blueprint/design for creating bank account objects        |
| Objects     | account_muhammad, account_aisha – specific accounts created from the `class` `BankAccount`  |
| Attributes  | `owner`, `balance` – data stored in each object                  |
| Methods     | `deposit()`, `withdraw()`, `info()` – changes attributes or shows info             |
| `self`     | `self` is used when a attribute or method is accessed within the `class`  |
| `__init__()` | the `__init__()` function is called constructor, it is called when an object is created (constructed)                     |


# Class Inheritance

Inheritance: 

- child `class` inherits from parent `class`
- Reuse code from a parent class
- Add specific attributes/methods to child classes
- Parent class is also called superclass


### TASK 3: Inheritance - Create child class and extend functionality of parent class

Create a file `student_account.py`:

```
from bank_account import BankAccount 

class StudentAccount(BankAccount):

    def __init__(self, owner, balance, minimum_balance):
        super().__init__(self, owner, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print("Sorry, you can't withdraw money.")
        else:
            super().withdraw(amount)
```


### TASK 4: Create object of StudentAccount

Create object and test

```
account_tariq = StudentAccount("Tariq", 5, 0)
account_tariq.info()

account_tariq.withdraw(10)

account_tariq.deposit(50)
account_tariq.withdraw(10)

account_tariq.info()
```