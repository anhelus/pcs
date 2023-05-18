# 1.2.4 - Data Structures

In this lesson, we will delve into some techniques for manipulating [lists](../01_intro/04_lists.md) and other fundamental data structures.

## List Comprehension

One of the most commonly used techniques for creating a list from another sequence is called *list comprehension*, which replaces the syntax defined by traditional loops with more *Pythonic* constructs.

In its basic form, a list comprehension has the following syntax:

```py
output_list = [f(element) for element in input_list]
```

In other words, it generates an output list (`output_list`) by applying the function `f()` to each `element` of the original list (`input_list`).

For example, given a list of integers, we can create a list where the $i$-th element is twice the value of the $i$-th element in the input list.

```py
>>> input_list = [1, 2, 3]
>>> output_list = [x * 2 for x in input_list]
[2, 4, 6]
```

### Extended Form with if-else

List comprehensions can also include conditional statements. Here's an example of the extended form:

```py
output_list_if = [f(element) for element in input_list if condition]
```

In this case, the function `f()` will be called only on the elements that satisfy the given `condition`. For example, we can use a list comprehension to return all the even values in a list:

```py
>>> output_even = [x for x in input_list if x % 2 == 0]
[2]
```

If we want to include an `else` clause:

```py
output_list_if_else = [f(element) if condition else g(element) for element in input_list]
```

The function `f()` will be invoked on the elements that satisfy the `condition`, while the function `g()` will be invoked on the elements that don't satisfy it. For instance, we can return all the even elements and double the odd elements simultaneously:

```py
>>> complex_output = [x if x % 2 == 0 else x * 2 for x in input_list]
[2, 2, 6]
```

## Tuples

*Tuples* allow you to represent a collection of heterogeneous values separated by commas. For example:

```py
tuple = ('hello', 'world', 12)
```

Similar to lists, one of the values in a tuple can also be another tuple. For example:

```py
tuple = ('hello', 'world', (1, 2))
```

However, unlike a list, tuples are *immutable*. This doesn't mean they can't contain mutable objects within them. Let's look at the following example:

```py
tuple = ('hello', 'world', [1, 2, 3])
```

The tuple contains two strings (immutable) and a list (mutable). Let's try to modify the list:

```py
tuple[2] = [2, 2, 3]
```

It will result in an error similar to this:

```sh
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

As expected, we encountered an assignment error due to the immutability of the tuple. However, let's now try to modify the list *directly*:

```py
tuple[2][0] = 2 		# The tuple will be ('hello', 'world', [2, 2, 3])
```

This operation is permissible,

 and the result is as expected.

!!!tip "Tuples and Lists"
	An observant reader will notice that tuples and lists are similar in terms of syntax but differ mainly in mutability. From this, it follows that tuples are extremely effective when we only need to access the elements contained within, while lists should be used when it's also necessary to modify the elements as needed.

## Sets

Sets are also similar to lists in terms of syntax but offer a significant difference: *they cannot contain duplicate elements*.

!!!note "Note"
	We can draw a clear analogy with the mathematical concept of a set.

The syntax for creating a set is as follows:

```py
set = {1, "string", 2}
```

A set can contain heterogeneous data, but it cannot include lists or dictionaries. This is because sets (as well as dictionaries themselves) are [hash tables](https://en.wikipedia.org/wiki/Hash_table) and utilize the concept of *hashing* to represent data compactly and efficiently. The inability to represent lists and dictionaries in this way automatically excludes them from being included within a set.

Another consideration is that sets are *unordered*, which makes it impossible to access (and *modify*) an element of the set using its index, as was the case with lists and tuples.

!!!tip "Tip"
	Sets can be used to isolate unique elements present in a list. To do this, simply convert the list to a set:
	> ```py
	  l = [1, 2, 2, 3]		# The list is [1, 2, 2, 3]
  	  s = set(l)			# The set is [1, 2, 3]
	  ```

## Dictionaries

The fourth and final type of data container is the *dictionary*, also known as an *associative array* or *hash map* in other programming languages.

The basic element of a dictionary is a *key-value pair*, where a certain value (of any type) is associated with a specific key (of immutable type).

Dictionaries share several characteristics with sets, such as the inability to use lists as keys and the prevention of duplicate keys. Additionally, key-value pairs are accessed based on the key itself, not the order of the pairs.

!!!note "Note"
	One difference between sets and dictionaries is that dictionaries are *ordered* starting from Python 3.7.

To create a dictionary, we can use a similar syntax to that used for sets. For example, to create an empty dictionary:

```py
>>> dictionary = {}
```

We can then add key-value pairs to the dictionary as follows:

```py
>>> dictionary['k'] = 'v'
>>> dictionary[1] = 'n'
{'k': 'v', 1: 'n'}
```

To access the value associated with a specific key:

```py
>>> dictionary[1]
'n'
```

### Keys and Values

We can retrieve the list of all keys present in a dictionary using the `keys()` method, which returns an object of type `dict_keys`, which can be converted to a list:

```py
>>> keys = dictionary.keys()
dict_keys(['k', 1])
>>> list(keys)
['k', 1]
```

Similarly, we can access all the values in the dictionary using the `values()` method, which returns an object of type `dict_values`, which can also be converted to a list:

```py
>>> values = dictionary.values()
dict_values(['v', 'n'])
>>> list(values)
['v', 'n']
```

We can also access all key-value pairs using the `items()` method, which returns an object of type `dict_items`, which can

 be converted into a list of tuples:

```py
>>> pairs = dictionary.items()
dict_items([('k', 'v'), (1, 'n')])
>>> list(pairs)
[('k', 'v'), (1, 'n')]
```

### Creating a Non-Empty Dictionary

There are several ways to create a non-empty dictionary.

#### Using the `{}` operator

The simplest and most common way is to declare the initial key-value pairs within the `{}` operator:

```py
>>> dictionary = {'k1': 1, 'k2': 2}
>>> dictionary
{'k1': 1, 'k2': 2}
```

#### Using the `dict()` constructor

Another way is to use the `dict()` constructor:

```py
>>> dictionary = dict(k1=1, k2=2)
```

#### Using the `zip` function

We can also use the `zip` function to create a dictionary from two lists:

```py
>>> keys = ['k1', 'k2']
>>> values = [1, 2]
>>> dictionary = dict(zip(keys, values))
```

#### Dict Comprehension

A way to obtain a dictionary from another iterable object is through *dict comprehension*, which has the following form:

```py
>>> output = {key: value for value in iterable}
```

For example, we can create a dictionary where the keys are the numbers from 1 to 9, and the corresponding values are their squares:

```py
>>> squares = {str(i): i ** 2 for i in range(1, 10)}
```
