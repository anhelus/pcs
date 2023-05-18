# 2.2.1 Introduction to NumPy

The **NumPy** library, derived from the fusion of *Num*erical and *Py*thon, is one of the most widely used libraries in scientific computing applications in Python.

In practice, NumPy can be considered a *de facto* standard. In fact, the classes and methods provided by the library are extensively used in almost all other Python tools for mathematical, chemical, and physical sciences, as well as engineering.

Let's start our examination with the installation procedure of the library.

## Installing NumPy

!!!note "Installing a Library"
    As usual, remember that the various options for installing a library are described in detail in [Appendix B](../../appendix/03_libraries/lecture.md).

To install NumPy, we will use `pip`, preferably within a virtual environment:

```sh
workon my-virtual-env
(my-virtual-env) pip install numpy
```

## Introduction to NumPy

### The `ndarray`

We have seen earlier that to use a package or module in our Python programs, we need to import it first:

```py
import numpy as np
```

Once NumPy is imported, we can start using the main data structure of the library, which is the *array*, similar to those described in classical mathematical notation.

Specifically, NumPy provides us with `ndarrays`, which are data structures capable of representing $n$-dimensional arrays containing *homogeneous* data.

!!!tip "Note"
    `ndarray` is an abbreviation for *n*-dimensional *array*.

The simplest way to create an array is to use the `array` constructor, passing it a list:

```py
>>> a = np.array([1, 2, 3])
```

### Array vs. Lists

There are several differences between an array and a regular list; the main ones are summarized in the following table.

| Feature       | `ndarray`              | List                        |
| ------------- | ---------------------- | --------------------------- |
| Size          | Fixed                  | Not fixed                   |
| Elements      | Homogeneous (same type) | Heterogeneous (any type)    |
| Scope         | Algebraic operations   | General-purpose             |

In practice:

* an array has a fixed size, unlike a list. Changing its size will require creating a new array and deleting the original one;
* the elements of an array must be of the same type (this limitation does not apply to lists);
* arrays are specifically designed for algebraic operations, while lists are designed for general purposes.

## NumPy and Algebraic Operations

We have mentioned that NumPy arrays are specifically designed for algebraic operations. This is of great relevance to us. To understand it, let's look at a simple example, in which we multiply two row vectors *element-wise*.

To perform the operation just described, we could use a `for` loop or a list comprehension:

```py
# for loop
c = []
for i in range(len(a)):
    c.append(a[i]*b[i])

# list comprehension
c = [a[i] * b[i] for i in range(len(a))]
```

The result of the operation will be *correct* in both cases. However, loops are computationally *expensive*: this means that, especially as the number of elements in the vectors increases, the cost will also increase.

This could be mitigated by using a more efficient language, such as C. However, if we try to extend the calculation to two dimensions, the code becomes:

```py
for i in range(len(a)):
    for j in range(len(b)):
        c.append(a[i][j]*b[i][j])
```

The number of nested loops will increase in proportion to the dimensionality of the arrays involved. This implies that for an $m$-dimensional array, we will have as many nested loops, with all the complexity that comes with it in terms of code complexity.

And this is where NumPy comes to the rescue. In fact, to multiply two arrays *of any dimensionality*, we only need to use the following instruction:

```py
c = a * b
```

Clearly, this syntax is much more concise and simple compared to using nested loops, and it closely resembles the notation used in "real" formulas found in textbooks.

The use of this syntax is based on two fundamental concepts in NumPy:

* *vectorization* of the code, which allows us to write matrix operations without explicitly using loops;
* *broadcasting*, which allows us to use a common syntax regardless of the dimensionality of the arrays involved in the operations.

## Data Types

NumPy provides a range of primitive data types that overlap with the [built-in types](../../01_python/01_intro/01_intro.md#built-in-types-in-python) in Python and have a nearly perfect correspondence with those provided by the C language.

These types are summarized in the [table](https://numpy.org/doc/stable/user/basics.types.html#array-types-and-conversions-between-types) found in the reference.

Two important aspects should be noted:

* the size of each data type depends on the platform (i.e., the operating system and processor) used;
* there is a range of types whose size is *platform-independent*, defined at [this address](https://numpy.org/doc/stable/reference/arrays.scalars.html#sized-aliases). In general, it is advisable to refer to these types.