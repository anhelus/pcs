# 1.2.2 - Structured Programming

Like all C-derived languages, Python also supports the main constructs of structured programming. Let's briefly go over them.

## Conditional Statement

Let's start with the conditional statement, which, like in any programming language, is expressed using the `if` and `else` keywords.

The basic syntax is as follows:

```py
if condition:
    statements
else:
    other_statements
```

In practice, if the `condition` is true, the `statements` will be executed. Alternatively, if the `condition` is false, the `other_statements` will be executed. For example:

```py
if a < 5:
    print('a is less than 5')
else:
    print('a is greater than or equal to 5')
```

To use the `else if` notation, we need to use the `elif` keyword. For example:

```py
if a < 5:
    print('a is less than 5')
elif a == 5:
    print('a is equal to 5')
else:
    print('a is greater than 5')
```

!!!note "Switch/Case in Python"
    Until version 3.10, Python did not provide an implementation for the `switch/case` construct. However, starting from version 3.10, the so-called *pattern matching* has been implemented using the `match/case` syntax:
    > ```py
      match command:
          case "case 1":
              statements()
          case "other case":
              print("Unknown command")
      ```
    We will explore this construct in the [appropriate lesson]().

## Loops

### `for` Loop

The `for` loop iterates over a *sequence*, such as a list or a string, and has the following syntax:

```py
for element in sequence:
    statements()
```

For example, in the following code block, we iterate over a sequence and print the numbers from 0 to 5 (excluding 5) iteratively:

```py
vals = [0, 1, 2, 3, 4]
for i in vals:
    print(i)
```

The output will be:

```bash
0
1
2
3
4
```

Compared to "classic" languages, the `for` loop in Python only operates on *iterables*, so in some cases, it may require a code redesign. However, this feature of Python also results in simpler code. For example, iterating over a string is straightforward:

```py
string = "Python"
for char in string:
    print(char)
```

In both cases, the output will be:

```bash
P
y
t
h
o
n
```

!!!warning "No free lunches!"
    As the *no free lunches theorem* reminds us, **there are no free lunches**! In fact, the syntactic simplicity offered by Python comes at a cost. A Python script, no matter how optimized, will almost never offer performance comparable to optimized C or C++ code, unless you use specific (and advanced) techniques.

### `while` Loop

Unlike the `for` loop, the `while` loop operates similarly to its counterparts in other programming languages. The generic syntax is:

```py
while condition:
    statements()
```

For example:

```py
import random
i = True
while i:
    if random.randint(-5, 5) > 0:
        print("Continuing!")
    else:
        print("Exiting!")
        i = False
```

The code in the above block generates a random integer value in the range $

[-5, 5]$ using the `randint` function. If the generated value is greater than 0, the loop continues; otherwise, it exits.

The output could be, for example:

```bash
Continuing!
Continuing!
Exiting!
```

!!!note "Boolean Values in Python"
    Keen observers may notice that boolean values in Python are written as `True` and `False`. This is not a typo: the first letter is capitalized.

## The `range()` Function

Let's revisit the `for` loop we saw earlier:

```py
vals = [0, 1, 2, 3, 4]
for i in vals:
    print(i)
```

Although the code is already concise, manually writing the sequence to iterate over can become quite complex. Python comes to our rescue with the `range(i, j, s)` function, which generates a sequence with all the numbers between `i` (inclusive) and `j` (exclusive) with a step of `s`. For example, to generate numbers from 0 to 4, we can write:

```pycon
>>> r = range(0, 5, 1)
>>> print(list(r))
[0, 1, 2, 3, 4]
```

!!!note "Note"
    Notice that we need to convert `r` to a list (`list(r)`) to print its values.

If omitted, `i` and `s` assume default values of 0 and 1, respectively:

```py
>>> r = range(5)
>>> print(list(r))
[0, 1, 2, 3, 4]
```

You can also specify a *decremental sequence* by setting `i > j` and `s < 0`:

```py
>>> r = range(5, 1, -1)
>>> print(list(r))
[5, 4, 3, 2]
```

## `break` and `continue` Statements

The `break` and `continue` statements allow you to *exit the loop* or *skip to the next iteration*, respectively. For example:

```py
while True:
    if randint(-5, 5) > 0:
        print("Continuing!")
        continue
    else:
        print("Exiting!")
        break
print("Exited!")
```

The preceding statements will *exit* the loop when a negative number is randomly generated and continue iterating when a positive number is randomly generated.