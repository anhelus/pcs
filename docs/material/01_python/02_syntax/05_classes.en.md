# 1.2.5 - Object Oriented Programming (OOP) in Python

Python offers extensive support for object-oriented programming (OOP). Before proceeding, however, it is useful to briefly introduce this concept.

## Object-Oriented Programming

*Object-oriented programming* (OOP) is a programming paradigm that allows you to create new user-defined types, which should be understood as complementary to the types defined by the programming language. In this sense, OOP shifts the focus from *functions*, which are central to languages like C and the procedural paradigm, to *data*.

In this sense, it is said that *in OOP everything is an object*.

## Classes

A *class* is a prototype for a particular user-defined data type. For example:

* the `Student` class represents all the properties and actions associated with a student;
* the `Car` class represents all the properties and actions associated with a car;
* the `Engine` class defines the behavior of engines;

and so on.

In general, there can be a class for every type of object in the world, whether real or digital.

It is important not to confuse the class with the *single object*, called an *instance*. For example:

* the student Angelo Cardellicchio is an instance of the `Student` class;
* the Opel Corsa car with license plate AB 123 CD is an instance of the `Car` class;
* the Hyundai Tucson car with license plate CD 321 AB is an instance of the `Car` class;
* the Opel Corsa car with license plate AA 123 CC is another instance of the `Car` class.

## Methods and Attributes

Each class has *methods*, which define the actions that can be performed on each instance of the class, and *attributes*, which are characteristics of the instance.

In particular, each new type, called a *class*, will have appropriate *attributes* and *methods*, each of which is accessible from the outside through appropriate *modifiers*.

For example, the Opel Corsa car with license plate AB 123 CD has a manufacturer (Opel), a model (Corsa), a license plate (AB 123 CD), an engine size, and so on.

!!!note "Further reading"
	We can delve into the concepts underlying OOP in [this appendix](../../appendix/05_oop/lecture.md).

## Classes in Python

To define a class, we will use the `class` keyword:

```py
class ClassName(BaseClass):
	# Class attributes and methods...
```

With the above syntax, we have created a class called `ClassName` that descends from a base class (`BaseClass`).

### The `__init__` Method

Most programming languages use the concept of a *constructor* to create an instance of a class. Python, however, does not use a true constructor, but rather a method for *initializing* the individual attributes of the instance. Hence the name of the method, `__init__`:

```py
class ClassName(BaseClass):

	def __init__(self, *args, **kwargs):
		# ...
		self.arg_1 = arg_1
		# ...
```

!!!tip "Unpacking"
	With the syntax `*args` and `**kwargs`, we want to represent the action of *unpacking* a list and a dictionary, respectively, through which we are passing all the values contained within the sequence.

Particular attention must be paid to the use of the keyword `self`, which allows you to refer to the specific instance of a class (for those familiar with languages like C++, it is conceptually similar to the `this` keyword). For example:

```py
class Person(object):

    def __init__(self, name, surname, age=18):
        self.name = name
        self._surname = surname
        self.__age = age
```

This snippet allows us to highlight four points:

1. the generic `object` class, from which **all** Python classes inherit (although its declaration can be omitted);
2. the functioning of the `self` keyword, which allows associating a specific value to the attributes of the individual instance;
3. the ability to include optional and default parameter values (in this case, `age`, which defaults to `18`);
4. the presence of one or two underscores `_` in front of some attributes.

Let's briefly explore point 4.

### Access Modifiers

Python provides access modifiers for data; specifically, we have the classic `public`, `protected`, and `private`. However, unlike other languages, one or two underscores are used as a suffix to the attribute name to distinguish between the three access modifiers; specifically, a single underscore indicates a protected attribute, while a double underscore indicates a `private` attribute. In our case:

```py
class Person(object):

    def __init__(self, name, surname, age=18):
        self.name = name                # "public" member
        self._surname = surname         # "protected" member
        self.__age = age                # "private" member
```

!!!warning "Attention"
    Despite the access modifier, it is still possible to access protected members from outside the class. In fact:
    > ```py
      >>> p = Person('Jax', 'Teller')
      >>> print(p.name)
      'Jax'
      >>> print(p._surname)
      'Teller'
      ```

    This does not apply to private attributes:

    > ```py
      >>> try:
      >>>     print(p.__age)
      >>> except AttributeError:
      >>>     print('Age is private!')
      Age is private!
      ```

    This syntax can also be used to define protected or private methods.

!!!tip "Tip"
    The syntax shown in the previous snippet is related to *exception handling*.

### Methods

The syntax for defining a class method is similar to that used for defining a function.

```py
def method(self, *args, **kwargs):
    pass
```

However, there is a fundamental difference: the first attribute of a method belonging to a class is *always* a reference to the instance through the `self` keyword. This reference does not need to be specified when the method is called from outside:

```py
# ...
p = Person()            # p is an instance of Person
p.method(parameter)     # calling the method from the instance
# ...
```

In the above code, we used the dot operator `.` to access `method()` defined inside the `Person` class.

Now let's explore some specific types of methods that can be obtained using certain decorators (see Appendix B).

#### Class Methods

The `@classmethod` decorator allows us to define the so-called *class methods*:

```py
@classmethod
def build_person(cls, name: str, surname: str, age: int):
    return cls(name, surname, age)
```

Unlike standard methods, class methods have a reference to the class (`cls`) rather than the instance (`self`). This means they are methods that apply to the entire class, not to a single instance. A typical example of using a class method is shown in the previous snippet, where we create a `Person` class object from a string.

!!!tip "Fun Fact"


    The previous method is, in fact, an implementation of the Builder design pattern.

To call a class method, you need to refer to the name of the class itself, not to a single instance:

```py
>>> person = Person.build_person('Bobby Munson', 58)
>>> print("{} {}".format(person.name, person._surname))
Bobby Munson
```

#### Static Methods

Using the `@staticmethod` decorator, we can define a *static method*. In Python, the behavior of such a method can be summarized as a function defined within the class, which can be called on instances of the same class. For example:

```py
@staticmethod
def is_valid_name(name):
    if len(name) < 2:
        return False
    else:
        return True
```

This method can be freely called using the dot operator `.` on a single instance:

```py
>>> print(Person.is_valid_name('Li'))
True
```

Another possibility is to call it on the class itself:

```py
>>> print(Person.is_valid_name('X'))
False
```

#### Abstract Methods

We can define *abstract methods* (see Appendix C) using the `@abstractmethod` decorator. To do this, our class must inherit from the `ABC` class (which stands for *Abstract Base Class*) in the `abc` package:

```py
from abc import ABC, abstractmethod

class BaseClass(ABC):

    # ...

    @abstractmethod
    def method_to_override(self):
        pass
```

Methods marked with the `@abstractmethod` decorator must be implemented in the derived classes (in other words, we need to override them):

```py
class DerivedClass(BaseClass):

    # ...

    def method_to_override(self):
        # ...
```

### Properties

In many programming languages, traditional *accessor* (getter) and *mutator* (setter) methods are used to access instance attributes of a class. Python doesn't prohibit this: for example, we can write a `get_name(self)` method to access a person's name and a `set_name(self, name)` method to set this property.

However, it's possible to use a more concise syntax (and ultimately more *Pythonic*) using the `@property` decorator, which represents a four-parameter function:

```py
property(fget=None, fset=None, fdel=None, doc=None)
```

In particular:

* `fget` is the function used to retrieve the attribute's value;
* `fset` is the function used to set the attribute's value;
* `fdel` is the function to delete the attribute;
* `doc` is the function to document and describe the attribute.

Thanks to `property`, we can follow the OOP best practices, making the class attributes private and accessing them through appropriate methods.

```py
class Person():

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 2:
            raise ValueError("The name must be at least two characters long.")
        else:
            self.__name = value

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        if len(value) < 2:
            raise ValueError("The surname must be at least two characters long.")
        else:
            self.__surname = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value

):
        if value < 0:
            raise ValueError("Age cannot be negative.")
        else:
            self.__age = value
```

Some notes:

* We have rewritten the `Person` class to turn all attributes into properties.
* For each property, we have specified a getter that returns the value of the property.
* In addition to the getter, we have specified a setter that includes a form of validation for the value passed as input.

Let's see how to use our new class:

```py
>>> draco = Person('Draco', 'Malfoy', 12)
>>> print(draco.name)
'Draco'
>>> print(draco.age)
12
>>> hermione = Person('', 'Granger', 18)
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<stdin>", line 3, in __init__
    File "<stdin>", line 14, in name
ValueError: The name must be at least two characters long.
```

Note that from the perspective of the script calling the class, there are no differences. However, the validation logic allows us to avoid errors and inconsistent situations, and we can also use properties to access the class's private attributes.