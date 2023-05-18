# 1.2.6 - Scripts, Modules, and Packages

When using Python, the temptation is to interact directly with the interpreter, launching it from the terminal and executing the necessary instructions each time. However, this approach, although immediate, has several disadvantages, such as:

* We won't have access to the syntax highlighting offered by a regular IDE.
* We won't be able to retrieve the code once the interpreter is closed.
* We won't be able to easily modify or verify the code's functionality.

It is evident that using the interpreter directly is not an optimal way to develop Python code. Therefore, it is necessary to define actual *scripts* using our preferred IDE. These scripts will be saved as files with the `.py` extension, each containing a series of instructions required for the execution of our program.

## The First Script

Let's create our first Python script. To do this, open our preferred IDE, such as Visual Studio Code, and create a file named `main.py`. Inside this file, we will write the following code:

```py
# main.py
def hello_world():
    print('Hello, world')

hello_world()
```

Now open a terminal, navigate to the folder where we saved this script, and execute it using the following command:

```sh
cd path_to_script_folder
python main.py
```

The two previous instructions:

* Change the directory (`cd` command) to the folder where the script is located.
* Tell the Python interpreter to run the `main.py` script.

If everything goes well, we should see the output `Hello, world` on the screen:

```sh
Hello, world
```

## Modules

When the size of our code base (the amount of code we write for our program) starts to become particularly "bulky," it is advisable to adopt a *modular* approach by separating different parts of the code into separate files, each containing functions related to different tasks. Let's consider an example.

Imagine we want to write a program that defines functions to calculate the area of various geometric shapes. Let's modify our `main.py` file as follows:

```py
# main.py
def calculate_square_area(side):
    return side * side


def calculate_rectangle_area(length, width):
    return length * width


def calculate_triangle_area(base, height):
    return (base * height) / 2


square_area = calculate_square_area(4)
rectangle_area = calculate_rectangle_area(2, 3)
triangle_area = calculate_triangle_area(2, 3)
```

Now, let's say we want to add a trigonometric calculation function:

```py
# main.py
import math

def calculate_tangent(angle):
    return math.sin(angle) / math.cos(angle)


tangent_pi = calculate_tangent(math.pi)
```

Our `main.py` file now includes both geometric and trigonometric functions.

What would happen if we wanted to integrate integral calculation functions or other types of functions? In such cases, the codebase would increase in size, and there would be a "mix" of functions related to different areas (although similar to each other). A good idea would be to *separate* different parts of the program, grouping geometric functions in a file called `geometry.py`, trigonometric functions in a file called `trigonometry.py`, and so on.

These files, which primarily contain functions (but not limited to), are called *modules*.

!!!note "Note"
    The line between scripts and modules is very thin, and in practice, it is easy to confuse and use them interchangeably. However, it is important to note that, ideally, scripts should only contain code that will be *executed*, while modules should contain.


### I moduli `geometria` e `trigonometria`

Now let's create the `geometria.py` file, where we will "move" the previously defined functions for geometric calculations.

```py
# geometria.py
def calculate_square_area(side):
    return side * side


def calculate_rectangle_area(base, height):
    return base * height


def calculate_triangle_area(base, height):
    return (base * height) / 2
```

Similarly, in the `trigonometria.py` file, we will define the function for calculating the tangent.

```py
# trigonometria.py
import math

def calculate_tangent(angle):
    return math.sin(angle) / math.cos(angle)
```

Now let's rewrite the `main.py` file:

```py linenums="1"
# main.py
import geometria
import trigonometria

if __name__ == "__main__":
    print(geometria.calculate_square_area(4))
    print(trigonometria.calculate_tangent(math.pi))
```

We can notice two things:

1. Firstly, we are calling the `calculate_square_area()` and `calculate_tangent()` functions defined in the `geometria` and `trigonometria` modules, respectively. These modules are imported into our script using the `import` directive.
2. On line 5, the "strange" syntax is used to declare what is known as the `main` entry point, which is the starting point of our program's code. The `main` entry point is typically present in all programming languages, sometimes in slightly different forms than shown here. However, in the case of particularly simple scripts, the `main` entry point can be omitted as the interpreter will be able to execute it autonomously.

Let's try running the script by executing the command `python main.py` in the terminal. If everything went well, we should see the values of the area of a square and the tangent of π on the screen.

## Using Imports

Regarding the `geometria` module, we have only used the `calculate_square_area()` function, "neglecting" the other two functions still present in the module. In such cases, we can use a modified version of the `import` directive, which takes the following form:

```py
from module import function_or_class
```

which, in our specific case, becomes:

```py
from geometria import calculate_square_area
```

This way, we can import only what we need, which is particularly useful for improving the efficiency of our code; the reason will become clear shortly.

### Aliases

The `import` directive also allows us to define aliases, which are particularly useful when using complex package names. For example:

```py
import trigonometria as tr

print(tr.calculate_tangent(math.pi))
```

## The `dir()` Function

The `dir()` function returns a list of all names (both functions and classes) defined in a module. For example:

```py
>>> dir(geometria)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'calculate_square_area', 'calculate_rectangle_area', 'calculate_triangle_area']
```

It's interesting to note that, in addition to the functions, classes, and variables we defined, the `geometria` module automatically defines *other* variables, which are imported using `import`:

```py
import geometria

if __name__ == "__main__":
    print(geometria.__file__)
    print(geometria.calculate_square_area(4))
```

We can access the `__file__` variable of

 the `geometria` module, which indicates its relative path within the file system. Obviously, this variable is rarely useful, but it adds additional overhead to the code, highlighting the importance of using the `from` directive appropriately.

## Standard Library Modules

Python has several modules that belong to the standard library, which are automatically available once the interpreter is installed. Some of the most commonly used ones are:

* `sys`: the module integrated into the interpreter, providing various utilities necessary for its functioning.
* `os`: the module delegated to interacting with the operating system on which the interpreter runs.
* `time`: the module used for all time-related utility functions, such as timing the execution of a function.
* `datetime`: the module used for date and time functionalities.
* `copy`: the module used for managing, among other things, deep copying of an object.

For a comprehensive list, please refer to the [Python Library Reference](https://docs.python.org/3/library/).

## Packages

We conclude by mentioning *packages*, which are collections that group together coherent modules, making it easier to access them later. In practice, packages are nothing more than folders containing multiple modules (i.e., files with the `.py` extension), along with a file called `__init__.py`, which allows the interpreter to recognize that folder as a package and, occasionally, contains package initialization instructions.

To access a module contained within a package, we can use the `import` directive, modifying it as follows:

```py
import package_name.module_name
# or...
from package_name.module_name import function_name
```