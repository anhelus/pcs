# 1.3.1 - The `argparse` Module

The [`argparse`](https://docs.python.org/3/library/argparse.html) module allows us to pass arguments to a Python script using the command line.

To do this, we need to follow a process articulated in four steps:

1. Create an instance of the [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser) class.
2. Add the arguments that we want to parse.
3. Parse these arguments.
4. Use the passed arguments.

Like many things in Python, describing this series of steps is more complex than implementing it. Therefore, we will use the usual *learn by doing* approach, using a simple example.

Suppose we have a `Person` class defined as follows:

```py linenums="1"
class Person():

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    def __str__(self):
        return f'{self.name} {self.surname}'
```

Now let's write a script to create an object of this class, specifying its parameters through the command line. First, let's import the `argparse` library:

```py
import argparse
```

Next, let's define a method that accepts a generic set of arguments (which we'll call `args`) as a parameter and creates an instance of `Person` from these arguments:

```py linenums="1"
def run(args):
    """ Define the `run` method that will be invoked
    every time the script is executed.
    The method accepts a parameter `args` that represents
    the parsed arguments.
    """
    p = Person(args.name, args.surname)
    print(p)
```

Now we can define the entry point to our script as follows:

```py linenums="1"
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-n',
        '--name',
        help='Name of the person',
        default='Pippo')
    parser.add_argument(
        '-s',
        '--surname',
        help='Surname of the person',
        required=True)
    args = parser.parse_args()
    run(args)
```

In particular:

* on line 2, we create an instance of the `ArgumentParser` type, which we call `parser`.
* on line 3, we add the first argument (the name) to the `parser` using the [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument) method.
* on line 4, we add a *flag* that marks the argument.
* on line 5, we add a *name* to indicate the argument.
* on line 6, we define a help message using the `help` parameter that describes the purpose of the argument.
* on line 7, we assign a default value to the argument related to the person's name.
* on line 8, we create a second argument, which is the surname, and add it to the parser.
* on line 12, we specify that the `surname` argument is required by setting the `required` parameter to `True`.
* on line 13, we parse the passed arguments, saving them in a variable called `args`.
* finally, on line 14, we pass the `args` variable to the previously defined `run()` method.

!!!tip "The `args` variable"
    The `args` variable defines an object of type [`Namespace`](https://docs.python.org/3/library/argparse.html#argparse.Namespace) in which all the arguments passed to the script are saved

, each of which can be invoked using the `args.argument_name` notation.

!!!tip "Using `help`"
    Defining the `help` parameter allows us to use the `python script_name -h` command, which displays the specified help messages during parsing. Therefore, it is advisable to avoid using flags like `-h` to prevent parser collisions and errors.

Save our code in a script called `run.py`. To execute it, we'll use the `-n` and `-s` flags to specify the name and surname, respectively:

```sh
python run.py -n Name -s Surname
```

The output will be:

```sh
Name Surname
```

We can omit the name, but not the surname, as it is a required parameter:

```sh
python run.py -s Surname
Pippo Surname
```

We can also invoke the help by running:

```sh
python run.py -h
```

Finally, let's try using the full notation:

```sh
python run.py --name Name --surname Surname
Name Surname
```

Now let's modify the `Person` class to include age. In this case, let's specify that the age must be an integer; otherwise, an exception will be raised.

```py linenums="1"
class Person():

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if not isinstance(age, int):
            raise ValueError("Please provide an integer for the age.")
        self._age = value
    
    def __str__(self):
        return f'{self.name} {self.surname}'
```

Let's modify the rest of the script to adapt to the new requirements. We'll start with the `run` method:

```py linenums="1" hl_lines="7"
def run(args):
    """ Define the `run` method that will be invoked
    every time the script is executed.
    The method accepts a parameter `args` that represents
    the parsed arguments.
    """
    p = Person(args.name, args.surname, args.age)
    print(p)
```

Then, let's add another argument to the `parser`:

```py linenums="1" hl_lines="13 14 15 16"
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        '-n',
        '--name',
        help='Name of the person',
        default='Pippo')
    parser.add_argument(
        '-s',
        '--surname',
        help='Surname of the person',
        required=True)
    parser.add_argument(
        '-a',
        '--age',
        help='Age of the person')
    args = parser.parse_args()
    run(args)
```

Let's try running the script again:

```sh
python run.py -n Name -s Surname -a 18
```

You will see an error because the arguments passed through `argparse` are normally interpreted as strings.

To resolve this issue, we need to specify the `type` parameter as `int`:

```py linenums="1" hl_lines="5"
parser.add_argument(
    '-a',
    '--age',
    help='Age of the person',
    type=int)
```

If we run the script again, we won't encounter any errors.