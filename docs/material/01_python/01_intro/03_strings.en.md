# 1.1.3 - Strings

In Python, strings can be enclosed in either single or double quotes.

```py
>>> "a string"
'a string'
>>> 'another string'
'another string'
```

In the second statement, we use the escape character (`\`) before the apostrophe. If we omit it, the interpreter would raise a syntax error (`SyntaxError`):

```py
>>> 'another string'
  File "<stdin>", line 1
    'another string
                   ^
SyntaxError: invalid syntax
```

!!!note "Note"
    All characters preceded by the backslash symbol (`\`) will be interpreted as escape characters unless we add the `r` symbol before the start of the string:
    > ```py
      >>> print('C:\new_folder')
      C:
      ew_folder
      >>> print(r'C:\new_folder')
      C:\new_folder
      ```

## Multi-line Strings

!!!note "Strings and Lists"
    Most of the concepts we will see next are also applicable to lists. In fact, to be precise, they are derived from lists, as Python considers a string as a particular type of list.

Strings can span multiple lines. To do this, we can use triple quotes (three consecutive quotation marks) to indicate the beginning and end of the string:

```py linenums="1" hl_lines="1 3"
>>> print("""This is an example\
         of
    a multi-line string\
    """)
This is an example
of
a multi-line string
```

!!!note "Note"
    In the above snippet, we use the `\` character to prevent the interpreter from automatically adding a newline character (`\n`) at the end of each line. As a result, you can see that the newline character is not added in the highlighted lines, but it is present in line 2.

## String Concatenation

Concatenating two strings in Python is straightforward; you can use the `+` operator:

```py linenums="1"
>>> string_a = "First string"
>>> string_b = "Second string"
>>> print(string_a + " - " + string_b)
First string - Second string
```

!!!note "Note"
    If you use the `*` operator, you can concatenate the same string multiple times:
    > ```py
      >>> 3 * 'co.'
      'co.co.co.'
      ```

You can also simply place the two strings next to each other:

```py
>>> "Py" "thon"
'Python'
```

!!!warning "Caution"
    Be careful not to concatenate a *string literal* (a string enclosed in quotes) with a *string variable*. If you try to do so, the interpreter will raise an error:
    > ```py
      >>> py="Py"
      >>> py "thon"
        File "<stdin>", line 1
          py "thon"
              ^
      SyntaxError: invalid syntax
      ```

    The same error would occur if, instead of the variable `py`, you used the result of a concatenation operation:
    > ```py
      >>> ('p' + 'y') 'thon'
        File "<stdin>", line 1
          ('p' + 'y') 'thon'
                      ^
      SyntaxError: invalid syntax
      ```
    In such "hybrid" cases, it is advisable to use the standard concatenation operator, which is `+`.

!!!note "Note"
    There are more efficient ways to concatenate strings, especially when dealing with numerous concatenation operations in large loops. However, the exploration of such methods is beyond the scope of this introduction.

## Indexing Strings

Python defines strings as *arrays

 of characters*, so you can index them. For example:

```py
>>> string = 'Python'
>>> string[0]
'P'
```

Individual characters are also considered as strings, each with a length of one:

```py
>>> letter = 'P'
>>> letter[0]
'P'
```

Python also allows accessing elements using *negative indices*, considering the elements from right to left. In this case, the index of the first element from the right is denoted as `-1`:

```py
>>> string[-1]
'n'
```

## String Slicing

The *slicing* operation allows you to extract a specific part of a string. In general, it takes the following form:

```py
>>> string[i:j:s]
```

where `i` is the starting index, `j` is the ending index, and `s` is the step used. It is important to note that **the element at the starting index will be included, while the element at the ending index will be excluded**.

For example:

```py
>>> string[0:2]
'Py'
>>> string[2:5]
'tho'
```

If you want to consider *all characters up to `j`* (exclusive), you can use the following notation:

```py
>>> string[:j]
```

If you want to consider *all characters starting from `i`* (inclusive), you can use the following notation:

```py
>>> string[i:]
```

For example:

```py
>>> string[1:]
'ython'
>>> string[:5]
'Pytho'
```

In this case as well, negative indices can be used. For example, if you want to take all characters from the third-to-last letter to the end, you can write:

```py
>>> string[-3:]
'hon'
```

And if you want to take all characters up to the third-to-last letter (exclusive):

```py
>>> string[:-3]
'Pyt'
```

!!!tip "Tip"
    You can obtain the entire string using the slicing operation in the following way:
    > ```py
      >>> string[:]
      'Python'
      ```

## String Length

The `len()` function returns the length of a string:

```py
>>> len(string)
6
```

## Immutability of Strings

Strings in Python are *immutable*. As the term implies, this means that they *cannot be modified*. For example, if you try to redefine one or more elements of a string accessed through indexing or slicing, you will encounter an error.

```py
>>> string[0] = 'C'  # Error!
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

!!!tip "Tip"
    However, you can assign the name `string` to a new variable if needed.