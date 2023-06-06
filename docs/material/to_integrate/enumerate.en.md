Sure! Here's the improved version of the text translated into English:

## Iterating with for Loops in Python

In Python, a for loop is typically written as a loop over an iterable object. This means that we don't need a counter variable to access the objects in the iterable. However, sometimes we may want to have a variable that changes with each iteration of the loop. Instead of creating and incrementing a variable manually, we can use the `enumerate()` method to get both a counter and a value from the iterable at the same time.

A for loop in Python uses collection-based iteration. In other words, Python assigns the next object in an iterable to the loop variable in each iteration, as shown in this example:

```python
>>> values = ["a", "b", "c"]

>>> for value in values:
...     print(value)
...
a
b
c
```

In this example, `values` is a list with three strings. In Python, lists are a type of iterable object. In the for loop, the loop variable is `value`. In each iteration of the loop, the value is set to the next object in the `values`.

Now, let's print `value` to the screen. The advantage of collection-based iterations is that they help us avoid the common off-by-one error that occurs in other programming languages.

Now, let's imagine that, in addition to the value itself, we want to print the index of the object in the list on the screen in each iteration. One way to approach this task is to create a variable to store the index and update it in each iteration:

```python
>>> index = 0

>>> for value in values:
...     print(index, value)
...     index += 1
...
0 a
1 b
2 c
```

In this example, `index` is an integer that keeps track of where we are in the list. In each iteration of the loop, we print `index` along with `value`. The last step in the loop is to update the value stored in the index by one. However, a common bug occurs when we forget to update the index in each iteration:

```python
>>> index = 0

>>> for value in values:
...     print(index, value)
...
0 a
0 b
0 c
```

In this example, the index remains at 0 in each iteration because there is no code that updates its value at the end of the loop. Especially for long or complicated loops, this type of bug is notoriously difficult to spot.

Another common approach to this problem is to use `range()` combined with `len()` to automatically create an index. This way, we don't have to remember to update the index:

```python
>>> for index in range(len(values)):
...     value = values[index]
...     print(index, value)
...
0 a
1 b
2 c
```

In this example, `len(values)` returns the length of `values`, which is 3. Then, `range()` creates an iterator that goes from the default starting value of 0 until it reaches `len(values) - 1`. In this case, `index` becomes the loop variable. Within the loop, we set the value equal to the object in `values` at the current index. Then, we print the index and the value.

With this example, a common bug that can occur is when we forget to update the value at the beginning of each iteration. This is similar to the previous bug where we forget to update the index. This is one of the reasons why this loop is not considered Pythonic.

It's also worth noting that the above example is somewhat limited because `values` must allow accessing its

 elements using integer indices. Iterables that allow this type of access are called sequences in Python.

!!!note "Technical Detail"
    According to the Python documentation, an iterable is *any* object that can return its members one at a time. Iterables support the iterator protocol, which specifies how the object's members are retrieved when the object is used in an iteration context. Python has two common types of iterators: sequences and generators.