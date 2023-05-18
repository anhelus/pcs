# 1.2.1 - Basic Syntax

Let's explore some of the fundamental concepts that characterize the syntax of the Python language.

## Comments

Python supports two types of comments. The first, and simplest, is the single-line comment, which is preceded by the `#` (hash) character:

```py
>>> # This is a comment!
```

The other type of comment is a multiline comment, and it is defined in the same way as a [multiline string](../01_intro/03_strings.md):

```py
""" This is an example
of a multiline comment!
"""
```

!!!note "Single and Double Quotes"
	Similar to strings, you can use either single or double quotes interchangeably (but consistently!) for comments.

## Use of Parentheses

The use of parentheses in Python differs from what is done in many C-like languages. In particular, let's see how round parentheses, square brackets, and curly braces are used (and what they are used for).

### Round Parentheses

Round parentheses are used in three cases:

* for function calls;
* for creating a tuple;
* to express precedence in a mathematical operation.

In other cases, they are optional and can be omitted.

Let's see a brief example of expressing precedence in a mathematical operation:

```py
>>> a = 2
>>> b = 3
>>> c = 4
>>> r_1 = a + b * c
14
>>> r_2 = (a + b) * c
20
```

In the upcoming lessons, we will see how to use round parentheses [in tuples](02_structured.md) and [function calls](03_functions.md).

### Square Brackets

Square brackets are used for creating and accessing elements of a data structure.

```py
# Create a list
my_list = [1, 2, 3]
# Access the second element of the list
my_list[1]			# The accessed value is 2
```

We will discuss this more extensively in the [next lesson](02_structured.md).

### Curly Braces

Curly braces are used to create sets and dictionaries.

```py
my_dict = {'a': 1, 'b': 2}
my_set = {1, 2, 3}
```

Again, we will discuss this more extensively in the [next lesson](02_structured.md).

## End of an Instruction

Unlike C-like languages that require a `;` (semicolon) to terminate a single instruction, Python considers a newline `\n` as the termination character of an instruction. In other words, the interpreter associates the end of an instruction with the newline character.

## Code Blocks

To delimit a code block in Python, the colon `:` character and *indentation* are used. In particular, all the code that follows a colon `:` and is indented at the same level belongs to the same block. For example:

```py
>>> a = 1				# Code not in a block
>>> if a < 10:			# Start of the outer if block
>>> 	b = 5
>>> 	print('outer block')
>>> 	if b > 1:		# Start of the nested if block
>>> 		print('inner block')
```

!!!note "Indentation and Curly Braces"
	Keen observers may have noticed that indentations play a role similar to curly braces in C-like languages.