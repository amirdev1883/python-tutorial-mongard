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
