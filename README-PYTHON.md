# 🐍 Python Basics Guide

This guide covers the fundamentals of Python: variables, control structures, classes, logging, and how to run your code.

---

## 🔸 1. Variables

### ✅ Defining Variables
```python
x = 10             # Integer
name = "Alice"     # String
pi = 3.14          # Float
is_active = True   # Boolean
```

---

## 🔸 2. Conditional Statements

### ✅ If / Else
```python
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
```

---

## 🔸 3. Loops

### ✅ For Loop
```python
for i in range(5):
    print(i)
```

### ✅ While Loop
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

---

## 🔸 4. Functions

### ✅ Defining and Calling
```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

---

## 🔸 5. Classes and Objects

### ✅ Creating a Class
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"My name is {self.name}, I am {self.age} years old.")

# Create an object
p = Person("Alice", 30)
p.greet()
```

---

## 🔸 6. Logging (Instead of print)

### ✅ Using the Logging Module
```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

logging.debug("This is a debug message")
logging.info("App started")
logging.warning("This is a warning")
logging.error("Something went wrong")
logging.critical("Critical failure")
```

You can also log to a file:
```python
logging.basicConfig(filename='app.log', level=logging.INFO)
```

---

## 🔸 7. How to Run a Python Program (Windows CMD)

1. Save your code in a file with `.py` extension (e.g., `program.py`)
2. Open **Command Prompt** (`cmd`)
3. Navigate to the folder containing your file using `cd`:
   ```cmd
   cd path\to\your\folder
   ```
4. Run the program using:
   ```cmd
   python program.py
   ```
   or if `python` doesn't work, try:
   ```cmd
   py program.py
   ```

---

## ✅ Quick Tips

- Use `#` for comments
- Indentation is crucial (4 spaces is the standard)
- Use meaningful variable and function names

---

📚 **Next Topics to Explore**: Lists, Dictionaries, Exception Handling, Modules, File I/O
