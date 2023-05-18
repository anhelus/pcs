# 1.2.3 - Functions

## Function Definition

Python allows you to define a function using the `def` keyword. The general syntax is as follows:

```py
def function_name(parameters):
    # statements
    return return_value
```

It's important to note that:

* It is not necessary to define a type, only a *return value*. If the function doesn't return any value, the `return` statement can be omitted.
* It is not strictly necessary to define the type of each parameter passed.
* Optional parameters with default values can be included.

For example, the following function adds `1` to the input value and returns the new value:

```py
def add_one(i):
    val = i + 1
    return val
```

!!!warning "Input Parameter Types"
    Duck typing means that no checks are performed on the input parameters. However, this doesn't mean that you can't try calling the `add_one()` function with a string parameter, for example; this will result in a (predictable) error.

## Passing Parameters to Functions

Python expects parameters to be passed to a function using a hybrid mode called *call-by-assignment*. In practice, the pass is done *exclusively by value*, but with different effects on mutable and immutable types.

For example, when passing a primitive value (such as an integer), Python behaves as if it were performing a pass by value:

```py
def double(integer):
    integer = integer * 2
    print(f'Value inside the function: {integer}')
```

The result will be:

```py
>>> integer = 1
>>> double(integer)
"Value inside the function: 2"
>>> print(f'Value outside the function: {integer}')
"Value outside the function: 1"
```

This is because the pass is done by value, so the `double()` function acts on a *copy* of the variable passed as an argument, not the original variable. If we use a function that modifies a list instead:

```py
def add_to_list(lst, element):
    lst.append(element)
    print(f'Value inside the function: {lst}')
```

The result will be:

```py
>>> lst = [1, 2]
>>> add_to_list(lst, 3)
"Value inside the function: [1, 2, 3]"
>>> print(f'Value outside the function: {lst}')
"Value outside the function: [1, 2, 3]"
```

In this case, since the list is mutable, the pass is done by *reference*: this means that operations performed inside the `add_to_list()` function will affect the original list.

!!!note "Shallow and Deep Copy"
    By default, Python copies variables using a *shallow copy*: this means that an assignment operation like `a = b` makes `a` point to the same memory address as `b`, and as a result, any modifications to `b` will be reflected in `a`. To avoid this, you can use a *deep copy* using the `deepcopy()` function from the `copy` library.

## The `pass` Statement

Finally, let's briefly discuss the `pass` statement. This statement does nothing; it is useful, for example, when you want to define an empty function (or class) that you plan to implement later:

```py
>>> def empty_function():
...     pass
...
>>> empty_function()
```

!!!note "Note"
    Although it may not be apparent at first, there are several situations where the `pass` statement proves to be extremely useful.