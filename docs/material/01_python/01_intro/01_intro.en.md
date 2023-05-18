# 1.1.1 - Introduction to Python

Before we start talking about the Python language, it's important to make sure that the interpreter is installed on our system. To do this, we open a terminal (Shell or Command Prompt, depending on our system) and type:

```sh
python
```

If a screen similar to the one shown in figure 1 appears, Python is already correctly installed on our system.

<figure markdown>
  ![interpreter](./images/python_interpreter.png)
  <figcaption>Figure 1 - Python Interpreter</figcaption>
</figure>

Alternatively, we will need to install it following the procedure indicated on the [official website](https://www.python.org/) and add it to the system path.

## Python and Typing

### Dynamic Typing

Python is an *interpreted* and *dynamically typed* language. In short, this means that the interpreter evaluates the type of each variable at runtime, and that this can change during the execution of the program.

But, in the end, what does this mean for the programmer? Well, very simple.

Let's say we have to define and initialize an integer variable in a *statically typed* language like C++. To do this, we will write something like:

```c++
int var = 0;
```

In Python, we can omit the type, which will be inferred directly from the value assigned to the variable:

```py
var = 0
```

Now let's imagine that our variable needs to become a decimal. In C++, we'll need to do casting:

```c++
float fVar = float(var);
fVar + 1.1;
```

In Python, this won't be necessary, and we can directly perform the desired operations:

```py
var + 1.1			# The result will be 1.1
```

This can apparently simplify life a lot, as there is no longer any need to worry about the type of the variable. However, not everything that glitters is gold: to understand this, it's time to talk about the (Pilate-like) principle of *duck typing*.

#### Duck Typing

Duck typing can be summarized in the following maxim:

!!!quote "Duck Typing"
	*If it walks like a duck and it quacks like a duck, then it must be a duck.*

which in Italian sounds more or less like *Se cammina come un papero, e starnazza come un papero, deve essere un papero* (if it walks like a duck and quacks like a duck, it must be a duck). Let's briefly translate it into "computerese."

Let's instruct our Python interpreter to assign our variable `var` the value of `1`. The interpreter notes that the variable "behaves" like an integer, and therefore "establishes" that it is indeed an integer.

Now let's try to add a value equal to `1.1` to `var`. The result, as expected, will be a decimal number, and therefore the interpreter will "change its mind," since the behaviors assumed by `var` are now assimilable to a variable of type `float`.

The usefulness of duck typing is evident: it allows the developer to "save" numerous casting operations, making the code simpler to write and maintain. However, it must be taken into account when using classes and objects, as the interpreter will try to infer and automatically use a type based on the context in which the variable is used, with the conveniences (and potential disasters) that this entails.

## Built-in Types in Python

Python provides a [series](https://docs.python.org/3/library/stdtypes.html) of *built

# 1.1.2 - Basic Data Types in Python

In Python, there are several built-in data types that allow us to store different types of data. Here is a brief overview:

### Numbers

Python supports integers, floating-point numbers, and complex numbers. Integers and floating-point numbers are widely used in most programming languages, and complex numbers are used less frequently.

```py
# Integers
x = 10
y = -5
z = 0

# Floating-point numbers
a = 3.14
b = -0.27

# Complex numbers
c = 2 + 3j
d = -1j
```

### Strings

Strings are used to store text. In Python, we can create a string by enclosing a sequence of characters in either single quotes or double quotes.

```py
# Single-line string
name = "Alice"
greeting = 'Hello, ' + name + '!'
print(greeting)

# Multi-line string
lyrics = """
And I said, what about Breakfast at Tiffany's?
She said, I think I remember the film
And as I recall, I think, we both kind of liked it
"""
print(lyrics)
```

### Booleans

A Boolean value is a value that can either be `True` or `False`. In Python, Booleans are very important for making decisions based on whether something is `True` or `False`.

```py
# Boolean values
x = True
y = False

# Logical operators
print(x and y)  # False
print(x or y)   # True
print(not x)    # False
```

### Lists

Lists are used to store a collection of items. In Python, lists are mutable, which means we can add, remove, or modify items after the list is created.

```py
# List of integers
numbers = [1, 2, 3, 4, 5]

# List of strings
fruits = ['apple', 'banana', 'orange']

# Mixed list
mixed = [10, 'hello', True, 3.14]

# Adding items
fruits.append('kiwi')
print(fruits)

# Removing items
del mixed[1]
print(mixed)

# Accessing items
print(numbers[2])
print(fruits[-1])
```

### Tuples

Tuples are similar to lists in that they can store a collection of items. However, tuples are immutable, which means we cannot add, remove, or modify items after the tuple is created.

```py
# Tuple of integers
numbers = (1, 2, 3, 4, 5)

# Tuple of strings
fruits = ('apple', 'banana', 'orange')

# Mixed tuple
mixed = (10, 'hello', True, 3.14)

# Accessing items
print(numbers[2])
print(fruits[-1])
```

### Dictionaries

Dictionaries are used to store key-value pairs. In Python, dictionaries are very useful for storing data in a structured format.

```py
# Dictionary of prices
prices = {
    'apple': 1.50,
    'banana': 0.99,
    'orange': 1.25
}

# Accessing values
print(prices['banana'])

# Adding or modifying values
prices['kiwi'] = 2.00
prices['banana'] = 1.25
print(prices)

# Removing values
del prices['orange']
print(prices)
```

These are just some of the basic data types in Python. There are other more advanced data types such as sets, arrays, and classes that we can learn about