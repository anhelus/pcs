# Exercise 1.1

**Prompt**: *Let's create a string that has the value **PCS** using the integrated interpreter.*

**Solution**

Open the Python interpreter by typing `python` from the command line. Then, enter the following statement and press `Enter`:

```py
>>> s = 'PCS'
PCS
```

# Exercise 1.2

**Prompt**: *Evaluate the length of the string created in the previous exercise and verify that it is equal to 3.*

**Solution**

Firstly, we can use the [`len()`](https://docs.python.org/3/library/functions.html#len) function, which, as we have seen in the lesson, accepts a *sequence* (i.e., an iterable object) and returns an integer representing the length of the iterable.

Since the string is a sequence, we can invoke the `len()` function and pass `s` as an argument:

```py
>>> len(s)
3
```

By calling the `len(s)` function, we notice that the returned value is the expected one, which is `3`.

We can also assign the returned value to a variable `l`:

```py
>>> l = len(s)
```

At this point, we can verify that `l` is equal to `3` using the equality operator:

```py
>>> l == 3
True
```

# Exercise 1.3

**Prompt**: *Verify that the number `x` is between `0` and `10`.*

**Solution**

First, let's assign an arbitrary value to `x`:

```py
>>> x = 1
```

Now, we can check if `x` is between `0` and `10` using the `and` boolean operator:

```py
>>> x < 10 and x > 0
True
```

# Exercise 1.4

**Prompt**: Create a list from the string defined in the previous exercises.

**Solution**

One possibility is to use the class constructor [`list()`](https://docs.python.org/3/library/functions.html#func-list), which accepts a sequence and returns a list based on it. We can write:

```py
>>> l_1 = list(s)
```

If we try to display `l_1`, we will get the following result:

```py
>>> l_1
['p', 'c', 's']
```

Another way is to use the `[]` operator, which will create a list with a single element, namely the string `s`. In practice:

```py
>>> l_2 = [s]
>>> l_2
['pcs']
```