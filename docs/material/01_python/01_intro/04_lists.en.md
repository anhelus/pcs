# 1.1.4 - Lists

We have already mentioned that a string is nothing but a special case of a *list*. The natural question that arises is: *what is a list*?

Lists are one of the four *built-in* data structures that Python offers for storing sequences of data. From a purely "conceptual" point of view, we can consider them similar to arrays found in other programming languages, albeit with some significant differences.

We can create a list in the following way:

```py
>>> lista = [1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
```

## Concatenation, Indexing, and Slicing on Lists

Just like with strings, we can perform indexing, slicing, and concatenation operations on lists:

```py
>>> lista[0]
1
>>> lista[2:]
[3, 4, 5]
>>> lista_two = [6, 7]
>>> lista + lista_two
[1, 2, 3, 4, 5, 6, 7]
>>> lista + [6]
[1, 2, 3, 4, 5, 6]
```

Let's look at some examples. Consider the following list:

```py
>>> l = [1, 2, 3, 4, 5, 6]
```

Let's take the elements at even indices (i.e., 0, 2, and 4):

```py
>>> l[0::2]
[1, 3, 5]
```

Let's take all elements starting from the third-to-last and with even indices:

```py
>>> l[(-3 + 1)::2]
[5]
```

!!!note "Note"
	In the previous example, a small "trick" was used to account for the fact that indexing starts from 0 and not 1.

Let's start from the third-to-last element and go backward towards the origin:

```py
>>> l[-3::-1]
[4, 3, 2, 1]
```

Let's start from the last element and go up to the third-to-last from the origin:

```py
>>> l[:3:-1]
[6, 5]
```

Let's take the last three elements in reverse order:

```py
>>> l[len(l)-1:len(l)-4:-1]
[6, 5, 4]
```

Let's take elements at even indices in reverse order:

```py
>>> l[::-2]
[6, 4, 2]
```

## Mutability of a List

Unlike strings, lists are *mutable* objects. Therefore, we can modify their contents:

```py
>>> lista[0] = 99
>>> lista
[99, 2, 3, 4, 5]
```

## List Operations

We can also remove elements from a list using the `[]` operator combined with the slicing operation:

```py
>>> lista[4:] = []
>>> lista
[99, 2, 3, 4]
```

!!!note "Note"
	The observant ones may have noticed that the `[]` operator simply indicates an empty list.

!!!tip "Tip"
	We can remove all elements from a list using slicing and the `[]` operator:
	> ```py
	  >>> lista[:] = []
	  >>> lista
	  []
	  ```

A list can contain heterogeneous elements. It is even allowed to contain *iterables*, including other lists:

```py
>>> lista.append([1, 2, 3])
>>> lista
[99, 2, 3, 4, [1, 2, 3]]
```

In the above example, we used the `append()` function to insert an element at the end of the list. It is interesting to note that the inserted element is itself a list and "coexists" peacefully with the other numerical elements.

Let's further extend the list by changing the first element to a string:

```py
>>> lista[0] = string
>>> lista
['Python', 2, 3, 4, [1, 2, 3]]
```