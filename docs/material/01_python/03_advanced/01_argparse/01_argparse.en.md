# 1.3.1 - The `argparse` Module

The [`argparse`](https://docs.python.org/3/library/argparse.html) module is a cool Python tool that lets us pass arguments to a Python script using the command line. It's pretty handy when you want to customize the behavior of your script without modifying the code.

To get started with `argparse`, just follow these four simple steps:

1. Create an instance of the [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser) class. This will be our command-line argument parser.
2. Add the arguments that we want to parse. These are the options and values we expect the user to provide.
3. Parse the arguments. This step takes the user's input from the command line and extracts the values accordingly.
4. Finally, use the passed arguments in your script to do whatever you need to do.

But don't worry if it sounds a bit confusing at first. The best way to learn is by doing, so let's dive into a simple example to make things crystal clear.

Imagine we have a class called `Person` that represents a person's name and surname. It looks something like this:

```python
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    def __str__(self):
        return f'{self.name} {self.surname}'
```

Now, let's write a script that creates an object of the `Person` class by specifying the name and surname through the command line. First things first, we need to import the `argparse` library, like this:

```python
import argparse
```

Next, we'll define a method that takes a bunch of arguments (we'll call them `args`) and uses them to create an instance of the `Person` class. This is where `argparse` comes into play. We'll handle the parsing of command-line arguments inside this method.

Sure! Here's an improved version of the text:

Now, let's define the `run` method. This method will be invoked every time the script is executed, and it takes a parameter called `args`, which represents the parsed arguments.

Inside the `run` method, we'll create an instance of the `Person` class using the values from the parsed arguments. We'll use `args.name` as the name and `args.surname` as the surname. Then, we'll simply print out the person's name and surname.

Here's the code for the `run` method:

```python
def run(args):
    """
    The `run` method gets executed whenever the script is run.
    It accepts a parameter called `args`, which contains the parsed arguments.
    """
    p = Person(args.name, args.surname)
    print(p)
```

Now, let's define the entry point for our script. This is the part that gets executed when we run the script directly. We'll use an `if __name__ == '__main__'` block to ensure that this code is only executed when the script is run directly, and not when it's imported as a module.

Inside the block, we'll create an instance of the `ArgumentParser` class and assign it to a variable called `parser`. This will be our command-line argument parser.

We'll then add two arguments to the parser. The first argument is for the person's name, and we'll use the [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument) method to add it. We'll specify a flag (`-n` or `--name`) to mark the argument, a name for the argument, and a help message that describes its purpose. We'll also set a default value of `'Pippo'` for the name argument.

The second argument is for the person's surname, and we'll add it in a similar way. However, this time we'll mark it as required by setting the `required` parameter to `True`.

Finally, we'll parse the passed arguments using the `parse_args()` method and save the result in a variable called `args`. We'll then pass this `args` variable to the `run()` method we defined earlier.

Here's the updated code for the entry point of our script:

```python
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-n',
        '--name',
        help='Name of the person',
        default='Foo')
    parser.add_argument(
        '-s',
        '--surname',
        help='Surname of the person',
        required=True)
    args = parser.parse_args()
    run(args)
```

With this code, we've set up our script to accept command-line arguments for the person's name and surname, and we'll create a `Person` object using those values.

The `args` variable is an object of type [`Namespace`](https://docs.python.org/3/library/argparse.html#argparse.Namespace) that holds all the arguments passed to the script. Each argument can be accessed using the `args.argument_name` notation.

To ensure a smooth parsing experience, it's recommended to avoid using flags like `-h` that may cause collisions or errors. Instead, we can define the `help` parameter for each argument. This allows us to use the `python script_name -h` command, which displays the specified help messages during parsing.

Let's save our code in a script called `run.py`. To execute it, we'll use the `-n` and `-s` flags to specify the name and surname, respectively:

```sh
python run.py -n Name -s Surname
```

The output will be:

```sh
Name Surname
```

We can omit the name, but the surname is a required parameter:

```sh
python run.py -s Surname
Pippo Surname
```

We can also invoke the help by running:

```sh
python run.py -h
```

Now, let's try using the full notation:

```sh
python run.py --name Name --surname Surname
Name Surname
```

Now, let's make a modification to the `Person` class. We'll include an `age` attribute and specify that it must be an integer; otherwise, an exception will be raised.

```python
class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError("Please provide an integer for the age.")
        self._age = value
    
    def __str__(self):
        return f'{self.name} {self.surname}'
```

Let's modify the rest of the script to accommodate the new requirements. First, we'll update the `run` method:

```python
def run(args):
    """
    The `run` method gets executed whenever the script is run.
    It accepts a parameter called `args`, which contains the parsed arguments.
    """
    p = Person(args.name, args.surname, args.age)
    print(p)
```

Next, we'll add another argument to the `parser`:

```python
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
        help='Age of the person',
        type=int)
    args = parser.parse_args()
    run(args)
```

If we try running the script again:

```sh
python run.py -n Name -s Surname -a 18
```

We'll encounter an error because arguments passed through `argparse` are normally interpreted as strings. To resolve this, we need to specify the `type` parameter as `int`:

```python
parser.add_argument(
    '-a',
    '--age',
    help='Age of the person',
    type=int)
```

After making this modification, running the script again will work without any errors.
