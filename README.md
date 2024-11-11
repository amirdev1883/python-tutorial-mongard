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
# 🔍 Determining the Variable Type
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

# ❌ Deleting Variables in Python
In Python, you can delete variables using the del statement. After deleting a variable, you can no longer use it; attempting to do so will result in an error:

```python
>>> n = 300
>>> del n
>>> n
```
NameError: name 'n' is not defined
As you can see, using a deleted variable triggers a NameError, indicating the variable no longer exists. Typically, programmers don’t need to delete variables manually since Python’s interpreter can automatically identify and remove unused variables to save memory.

# 🔗 Multiple Variable Assignment in Python
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

# 📜 Variable Naming Rules in Python

When naming variables in Python, you must follow specific rules to ensure compatibility with the Python interpreter. Not following these rules will lead to a **SyntaxError**:

- A variable name must start with an English letter or an underscore (`_`) and cannot start with a number or any other character.
- A variable name can only include English letters, numbers, and underscores (`_`).
- Variable names are **case-sensitive**, meaning `Name` and `name` are considered different.
- **Reserved keywords** in Python cannot be used as variable names.
- Variable names **cannot contain spaces**.

Below are some examples of invalid variable names:

```python
1name
n@me
n me
```
# 💡 Choosing Meaningful Variable Names
When creating a variable, try to pick a name that is descriptive of its purpose. For instance, if you’re storing the number of college graduates, you could choose one of the following:

```python
>>> numberofcollegegraduates = 2500
>>> NUMBEROFCOLLEGEGRADUATES = 2500
>>> numberOfCollegeGraduates = 2500
>>> NumberOfCollegeGraduates = 2500
>>> number_of_college_graduates = 2500
```
In the examples above, the purpose of each variable is clear. However, some of these naming styles are less readable due to inconsistent use of uppercase and lowercase letters.

Most programmers find the first two examples (where letters are joined together) harder to read, especially the one written in all caps. The three most commonly used methods for multi-word variable names are:

Camel Case: Subsequent words start with uppercase letters to highlight word boundaries. Example: numberOfCollegeGraduates
Pascal Case: Similar to Camel Case, but the first word also starts with an uppercase letter. Example: NumberOfCollegeGraduates
Snake Case: Words are separated by underscores. Example: number_of_college_graduates
Python’s style guide, known as PEP 8, includes naming conventions that suggest standards for naming different types of objects. According to PEP 8:

Snake Case should be used for function and variable names.
Pascal Case should be used for class names.
# 🧠 How Python Manages Variables
When you create a variable in Python, what exactly happens? How does Python handle variables? This is an important question, as Python's approach differs from many other programming languages.

Python is a highly object-oriented language. In Python, everything, including variables, functions, classes, etc., is an object.

Consider this code:

```python
>>> print(300)
300
```
When you run this code, Python performs the following steps:

Creates an integer object.
Assigns it the value 300.
Displays it in the output.
You can confirm that an integer object is created by using the built-in type() function:

```python
>>> type(300)
<class 'int'>
```
In Python, when you create a variable, you’re essentially selecting a symbolic name for an object. The object is stored in memory, and you can access it using the variable name.

For example:

```python
>>> n = 300
```
This assignment creates an integer object with the value 300 and assigns the variable n to reference that object.

# 🔀 Variable Assignment
The code below confirms that n points to an integer object:

```python
>>> print(n)
300
>>> type(n)
<class 'int'>
```
Now, consider the following line:

```python
>>> m = n
```
What happens here? Python doesn’t create a new object. It simply creates a new symbolic name, m, that points to the same object referenced by n.

Adding a New Reference to a Variable in Python
Now, if you do the following:

```python
>>> m = 400
```
Python creates a new integer object with the value 400, and m becomes a reference to this new object.

Changing the Second Reference of a Variable in Python
Finally, suppose you execute the following command:

```python
>>> n = "foo"
```
Python creates a string object with the value "foo" and assigns n to reference this object.

Removing a Variable Reference in Python
There is now no reference to the integer object 300. This object becomes "orphaned," and there is no way to access it. Throughout an object's lifetime, as long as there’s a reference to it, it will remain active. However, once the number of references to an object reaches zero, the object will be removed for memory optimization. This process is known as garbage collection.

# 🔍 Identity of Variables in Python

In Python, each variable or object created is assigned a unique identifier. This ensures that no two objects share the same identifier.

The **`id`** function in Python returns the unique identifier (an integer) for a variable. Using `id`, you can check if two variables point to the same object:

```python
>>> n = 300
>>> m = n
>>> id(n)
60127840
>>> id(m)
60127840


>>> m = 400
>>> id(m)
60127872
```
After assigning m = n, both variables m and n refer to the same object, as confirmed by the fact that id(m) and id(n) return the same value. However, when m is reassigned to 400, m and n then point to different objects with distinct identities.

# 🔒 Constants in Python
Constants refer to variables whose values should not change during runtime. In many programming languages, constants are enforced by the interpreter, meaning their values cannot be modified once assigned. However, Python does not natively support constants.

The common practice in Python to indicate a constant is to use uppercase letters for variable names. For example, instead of host, you can write HOST. This is merely a convention, and you can change constant values if needed.

Typically, constants are stored in a separate module and imported when necessary. For instance, consider a file named settings.py as shown below:

```python
# settings.py
HOST = 'smtp.gmail.com'
PASSWORD = 'secure_pass'
```
Additionally, Python’s interpreter includes several built-in constants, which you can find in the Built-in Constants section.

# 📚 Conclusion
This guide covered the basics of Python variables, including references, identity, and naming conventions. You now have a good understanding of some Python data types and know how to create variables that reference objects of these types.
