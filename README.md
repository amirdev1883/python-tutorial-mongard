# 🐍 What is Python?

Welcome to the **Free Python Course from Scratch**! Python is a versatile computer programming language often used for **building websites and software**, **automation**, and **data analysis**. Python is a **general-purpose language**, meaning it can be used to create a wide variety of programs. Due to its simplicity and versatility, Python has become one of the most widely used programming languages today.

Python was created by **Guido van Rossum** and was first released on **February 20, 1991**. The name "Python" was inspired by a comedy television show called *Monty Python* that aired on the **BBC**. One of the amazing features of Python is that it was initially developed by one person! Although Guido didn't develop all components of Python himself, Python's rapid expansion worldwide results from the continuous efforts of thousands of programmers, testers, users, and enthusiasts. The **Python Software Foundation (PSF)**, a non-profit membership organization, is responsible for Python's development, enhancement, and promotion.

Before diving into the **free Python course videos**, let’s get familiar with Python's pros and cons:

## ✅ Advantages of Python
- **Readable and simple**: Python is designed to be similar to the **English language**, making it easy to read and write.
- **Efficient language**: Python’s simplicity allows developers to focus on problem-solving without spending too much time on syntax or behavior understanding. **Less code, more work**.
- **Interpreted language**: Python executes code **line by line**, which helps detect errors quickly.
- **Extensive standard library**: Python has a vast standard library, so you can find almost all the functions you need for your work without relying on external libraries.

## ❌ Disadvantages of Python
- **Slow execution**: Python’s line-by-line execution can slow down programs. Its **dynamic nature** also contributes to its slower speed due to additional runtime tasks. Therefore, Python isn’t ideal for projects where speed is a priority.
- **Memory usage**: Python’s simplicity comes at the cost of higher memory consumption. If memory management is crucial in your project, Python may not be the best choice.
- **Dynamic typing**: In Python, the data type of a variable can change at any time, which might lead to runtime errors. Programmers must perform thorough testing in Python.

## 🕒 How Long Does It Take to Learn Python?
Learning the basics of Python can take anywhere from **a few weeks to several months**, depending on your goals and dedication. Since Python has numerous applications, you could spend **years mastering Python from A to Z**. Knowing what you want to do and whether you plan to use Python professionally can help determine how long your journey will take. Your first step is right here with this **introductory Python course**!

Among programming languages, Python is one of the easiest to learn. Its readability and structural elements are designed to be **easily understood**, making it relatively easy to learn. However, this simplicity mainly applies to beginner levels. Python has many complexities that can take years to master, but don’t worry — with this free course, you’re in good hands!

## 🧑‍🏫 Who is this Basic Python Course For?
This Python course is **perfect for beginners with no prior knowledge of programming** or Python and requires no prerequisites. It covers everything you need to start learning Python. The course begins with a brief introduction to Python and IDEs, then dives into Python fundamentals. Starting with **variables** — the simplest concept — we progress to advanced topics like **object-oriented programming** and **inheritance**. After completing this course, you’ll be ready to tackle more complex Python topics.

# 🐍 Creating Variables in Python

Python is a **dynamically typed** language, meaning you don’t need to specify the type of a variable when creating it. There’s no need to define a variable's type before using it — the **Python interpreter** determines the type automatically. A variable is created the moment you assign a value to it for the first time.

## ➡️ Creating a New Variable

To create a new variable, you use the **equals sign** (`=`). Take a look at the example below:

```python
>>> n = 300
```
In the example above, we stored the numeric value 300 in a variable named n. Now, you can use this variable in your program:

```python
>>> print(n)
300
```
🔍 Determining the Variable Type
When assigning a value to a variable, Python automatically determines the variable type. For example, in the code above, the Python interpreter knows that n holds a number. To check the variable type, you can use the type function:

```python
>>> n = 300
>>> type(n)
<class 'int'>
```
If you store a string in a variable, the Python interpreter will determine the variable type as str:

```python
>>> m = 'amir'
>>> type(m)
<class 'str'>
```

# 🔄 Changing Variable Values in Python

Unlike **statically typed** languages where a variable’s type is fixed, in Python, you can change a variable's type. For example, if a variable holds a number, you can change it to other types like a **string** or **dictionary**.

Consider the following code:

```python
>>> n = 300
>>> n = 'amir'
>>> n
'amir'
```
As shown above, the variable n initially held a number, but we were able to change it to a string.

❌ Deleting Variables in Python
In Python, you can delete variables using the del statement. After deleting a variable, you can no longer use it; attempting to do so will result in an error:

```python
>>> n = 300
>>> del n
>>> n
```
NameError: name 'n' is not defined
As you can see, using a deleted variable triggers a NameError, indicating the variable no longer exists. Typically, programmers don’t need to delete variables manually since Python’s interpreter can automatically identify and remove unused variables to save memory.

🔗 Multiple Variable Assignment in Python
Python provides special techniques to create multiple variables simultaneously. For instance, you can create multiple variables on a single line using commas:

```python
>>> a, b = 100, 200
>>> a
100
>>> b
200
```
You can even create more than two variables with different data types:

```python
>>> a, b, c = 0.1, 100, 'string'
```
If there’s only one variable on the left side, a tuple is created:

```python
>>> a = 100, 200
>>> a
(100, 200)
>>> type(a)
<class 'tuple'>
```
If the number of variables and values doesn’t match, a ValueError will occur. However, by using the asterisk (*) operator, you can store the extra values as a list in a variable:

```python
>>> a, b = 100, 200, 300
ValueError: too many values to unpack (expected 2)

>>> a, b, c = 100, 200
ValueError: not enough values to unpack (expected 3, got 2)

>>> a, *b = 100, 200, 300
>>> a
100
>>> type(a)
<class 'int'>

>>> b
[200, 300]
>>> type(b)
<class 'list'>

>>> *a, b = 100, 200, 300
>>> a
[100, 200]
>>> type(a)
<class 'list'>

>>> b
300
>>> type(b)
<class 'int'>
```
Another trick for creating multiple variables with the same value is to use the equals sign (=) consecutively:

```python
>>> a = b = 100
>>> a
100
>>> b
100
```
