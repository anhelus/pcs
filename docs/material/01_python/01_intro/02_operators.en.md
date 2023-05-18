# 1.1.2 - Arithmetic and logical operators

As briefly mentioned in the [previous lesson](01_intro.md), let's now see what the arithmetic and logical operators are, and how they can be used on basic numeric types.

## Arithmetic operators

### Addition, multiplication and subtraction

Let's try to use the interpreter as a simple calculator. To do this, we write directly after the `>>>` symbol the operations we want to perform, and press the `Enter` key. For example:

```py
>>> 2 + 2
4
>>> 3 * 5
15
>>> 10 - 2 * 4
2
```

### Division

Divisions always return a floating-point number. For example:

```py
>>> 16 / 3
5.333333333333333
>>> 2 / 2
1.0
```

!!!note "Evaluating the type of a variable"
	To evaluate the type of a variable `a`, we can use the `type()` function, passing the variable as an argument. For example:
	> ```py
	  >>> a = 10
	  >>> type(a)
	  int
	  >>> b = 3.3
	  >>> type(b)
	  float
	  ```

#### Quotient and remainder of a division

There are two contextual but distinct operations with respect to classical division. In particular, we can use the `//` operator to obtain the quotient of the division. For example, if we try to divide `16` by `3`, we will get a quotient of `5`:

```py
>>> 16 // 3
5
```

The `%` operator, on the other hand, returns the remainder of the division. In the previous case, it will therefore return `1`:

```py
>>> 16 % 3
1
```

!!!note "Modular arithmetic"
	It is obvious that the `%` operator can be used for applications of modular arithmetic.

It is important to emphasize that the `//` and `%` operators return integer values.

### Exponentiation

To raise a number to a power, it is necessary to use the `**` operator, where the left operand is the base, while the right one is the exponent:

```py
>>> 3 ** 2
9
>>> 2 ** 8
256
```

### Summary

We end this section with a brief summary of the different types of arithmetic operator, and their effects on numerical variables.

| Operator | Description | Example | Result |
| --------- | ----------- | ------- | --------- |
| `+` | Addition | `1 + 1` | `2` |
| `-` | Subtraction | `1 - 1` | `0` |
| `*` | Multiplication | `2 * 1` | `2` |
| `**` | Exponentiation | `2 ** 3` | `8` |
| `/` | Division | `2 / 1` | `2` |
| `//` | Quotient | `4 // 3` | `1` |
| `%` | Modulo | `5 % 3` | `2` |

## Logical operators

Logical operators allow implementing the basic operations of [Boolean algebra](https://en.wikipedia.org/wiki/Boolean_algebra).

In this sense, it is appropriate to briefly summarize the principles and operations underlying this type of algebra.

1. In Boolean algebra, variables can only take two possible values: *true*, or $1$, and *false*, or $0$.
2. By combining the values of multiple variables, it is possible to evaluate more or less complex conditions

# 1.1.3 - Comparison operators

Another important category of operators are the comparison operators, which allow us to compare two values and determine whether they are equal, unequal, greater, less, etc. They are frequently used in control structures such as if-else statements and loops.

Here are the comparison operators available in Python:

| Operator | Description |
| --------- | ----------- |
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

These operators compare two operands and return a boolean value (True or False) based on the result of the comparison.

Let's see some examples:

```py
>>> x = 10
>>> y = 5
>>> x == y
False
>>> x != y
True
>>> x > y
True
>>> x < y
False
>>> x >= y
True
>>> x <= y
False
```

Note that the comparison operator `==` (equal to) is different from the assignment operator `=`. The assignment operator is used to assign a value to a variable, while the comparison operator is used to compare two values.

It is also worth mentioning that comparison operators can be chained together using logical operators, as we will see in the next section.