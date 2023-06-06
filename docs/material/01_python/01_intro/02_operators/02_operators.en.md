# 1.1.2 - Arithmetic and logical operators

As mentioned briefly in the [previous lesson](../01_intro/lecture.en.md), let's now explore the arithmetic and logical operators and how they can be applied to basic numeric types.

## Arithmetic operators

### Addition, multiplication, and subtraction

We can use the Python interpreter as a simple calculator. To do this, we enter the desired operations directly after the `>>>` symbol and press the `Enter` key. For example:

```py
>>> 2 + 2
4
>>> 3 * 5
15
>>> 10 - 2 * 4
2
```

In the above examples, we see how the addition (`+`), multiplication (`*`), and subtraction (`-`) operators work with numeric values. The interpreter evaluates the expressions and returns the corresponding results.

### Division

When performing division, the result is always a floating-point number. For example:

```py
>>> 16 / 3
5.333333333333333
>>> 2 / 2
1.0
```

!!!note "Evaluating the type of a variable"
	To determine the type of a variable `a`, we can use the `type()` function by passing the variable as an argument. For example:
	> ```py
	  >>> a = 10
	  >>> type(a)
	  <class 'int'>
	  >>> b = 3.3
	  >>> type(b)
	  <class 'float'>
	  ```

#### Quotient and remainder of division

There are two related but distinct operations when it comes to division. We can use the `//` operator to obtain the quotient of the division. For example, dividing `16` by `3` gives us a quotient of `5`:

```py
>>> 16 // 3
5
```

On the other hand, the `%` operator returns the remainder of the division. In the previous example, it would yield `1`:

```py
>>> 16 % 3
1
```

!!!note "Modular arithmetic"
	The `%` operator can also be used for modular arithmetic applications.

It's important to note that the `//` and `%` operators return integer values.

### Exponentiation

To raise a number to a power, we use the `**` operator, where the left operand is the base and the right operand is the exponent:

```py
>>> 3 ** 2
9
>>> 2 ** 8
256
```

### Summary

Let's conclude this section with a concise summary of the different arithmetic operators and their effects on numerical variables.

| Operator | Description | Example | Result |
| --------- | ----------- | ------- | --------- |
| `+` | Addition | `1 + 1` | `2` |
| `-` | Subtraction | `1 - 1` | `0` |
| `*` | Multiplication | `2 * 1` | `2` |
| `**` | Exponentiation | `2 ** 3` | `8` |
| `/` | Division | `2 / 1` | `2.0` |
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