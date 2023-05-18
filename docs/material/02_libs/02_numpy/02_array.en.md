
# 2.2.2 - Arrays

In the [previous lesson](01_intro.md) we introduced the concept of arrays, which are the "central" data structure in the NumPy ecosystem. In this lesson, we will delve deeper into their main aspects and characteristics.

## Arrays and Lists

At first glance, arrays may appear very similar to traditional lists. However, as we have seen before, there are several notable differences that can be summarized by stating that it is preferable to use an array when performing mathematical operations on homogeneous data.

NumPy arrays are instances of the `ndarray` class, which stands for $n$-dimensional array. With this class, we can represent data structures with an arbitrary number of dimensions, including vectors, matrices, and tensors.

The first step in using an array, as mentioned earlier, is to create it. In this regard, there are several methods, but let's remember the "simplest" one, which involves using the `array()` constructor and passing it a list of elements of the same type:

```py
>>> a = np.array([1, 2, 3, 4, 5, 6])
>>> a
array([1, 2, 3, 4, 5, 6])
```

By passing a list whose elements are themselves lists, we can obtain a multidimensional array as output:

```py
>>> b = np.array([[1, 2, 3], [4, 5, 6]])
>>> b
array([[1, 2, 3],
       [4, 5, 6]])
```

Finally, note that arrays are not necessarily numeric. We can, for example, create an array of strings:

```py
>>> c = np.array(["s1", "s2"])
>>> c
array(['s1', 's2'], dtype='<U2')
```

### Heterogeneous Arrays

We previously mentioned that arrays, unlike lists, must contain homogeneous data. So what would happen if we tried to pass a list of heterogeneous data types to the `array()` method? Let's start by verifying what happens, for example, when using an integer and a float.

```py
>>> d = np.array([1, 1.])
>>> d
array([1., 1.])
```

We immediately notice that an implicit and automatic type conversion has been performed, and all the values passed have been converted to the float format.

It's also interesting to see what happens when we try to pass a list containing a number and a string:

```py
>>> e = np.array([1, "s3"])
>>> e
array(['1', 's3'], dtype='<U11')
```

We can see that, in this case as well, a type conversion has been performed, this time converting the integer to a string.

!!!note "Upcasting"
    The rule to keep in mind is that NumPy (and Python in general) follows the principle of *upcasting*: in other words, when a conversion between different data types is necessary, the type with the highest precision is chosen, minimizing the risk of information loss.

## The number of elements in an array

NumPy arrays have a fixed size and can contain a fixed number of objects of a certain type. To define (or know) this value, we use a property called `shape`, which roughly represents the *shape* of the array. The shape of an array is actually a tuple of non-negative integers, each of which determines the number of elements for each dimension of the array.

Let's create an array that represents a $2 \times 3$ matrix, meaning two rows and three columns:

```py
>>> a = np.array([[1, 2, 3], [4, 5, 6]])
>>> a
array([[1, 2, 3],
       [4, 5, 6]])
```

Let's see what value the `shape` property takes for this array:

```py
>>> a.shape
(2, 3)
```

As expected, our array has a size of two in the first dimension (i.e., the number of rows) and three in the second dimension (i.e., the number of columns).

## Other methods to create an array

In addition to the method seen before, we can create an array by directly using the constructor of the `ndarray` class:

```py
>>> a = np.ndarray([3, 3])       # or a = np.ndarray(shape=(3, 3))
>>> a
array([[0.00000000e+000, 0.00000000e+000, 0.00000000e+000],
       [0.00000000e+000, 0.00000000e+000, 3.02368175e-321],
       [6.69431255e+151, 1.68534231e+246, 6.69431467e+151]])
```

Note that the constructor accepts a list containing the shape of the array, which in this case becomes $3 \times 3$.

!!!note "Note"
    Notice how the numbers with which the array is "filled" are currently random.

In addition to this basic technique, there are several ways to create arrays of a certain type. Let's briefly see them.

### Arrays with zero and unit values

We can create an array of arbitrary dimensions where all elements are equal to 1. To do this, we use the `ones()` function:

```py
>>> u = np.ones(shape=(3, 3))
>>> u
array([[1., 1., 1.],
       [1., 1., 1.],
       [1., 1., 1.]])
```

Similarly, we can create arrays of arbitrary dimensions where all elements are equal to zero using the `zeros()` function:

```py
>>> z = np.zeros(shape=(3, 3))
>>> z
array([[0., 0., 0.],
       [0., 0., 0.],
       [0., 0., 0.]])
```

### Empty Arrays

We can create an empty array using the `empty()` function:

```py
>>> e = np.empty(shape=(3, 3))
>>> e
array([[0.00000000e+000, 0.00000000e+000, 0.00000000e+000],
       [0.00000000e+000, 0.00000000e+000, 1.67982320e-321],
       [5.96555652e-302, 1.14188703e-104, 9.91401238e-278]])
```

This function can be useful when we want to preallocate space for an array.

!!!note "Note"
    The observant ones may notice that the array generated by `empty()` is not actually empty but contains random values. In this sense, it produces results equivalent to directly using the `ndarray()` constructor.

### Identity Matrix

We can create an identity matrix using the `eye()` function:

```py
>>> i = np.eye(3)
>>> i
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])
```

!!!warning "Attention"
    In this case, we cannot pass a tuple or list to indicate the dimensions of the array. However, we can specify both the number of rows (using the first parameter) and the number of columns (using the second parameter).

### Diagonal Matrices

The `diag()` function is used both to *create* a diagonal matrix from a vector (which will be the diagonal of the matrix) and to *extract* the diagonal of a matrix. To understand this duality, let's first consider having a row vector with three elements that we want to transform in such a way that it behaves as the diagonal of a matrix.

```py
>>> x = np.array([5, 2, 3])
>>> x
array([5, 2, 3])
```

We can create a diagonal matrix from this vector by passing it as a parameter to the `diag()` function:

```py
>>> d = np.diag(x)
>>> d
array([[5, 0, 0],
       [0, 2, 0],
       [0, 0, 3]])
```

Now let's see how to address the dual problem. Suppose we have an array and we want to extract its diagonal:

```py
>>> x = np.array([[5, 5, 5], [2, 1, 3], [4, 3, 6]])
>>> x
array([[5, 2, 2],
       [2, 1, 3],
       [4, 3, 6]])
```

To do this, we need to use the `diag()` function again:

```py
>>> d = np.diag(x)
>>> d
array([5, 1, 6])
```

!!!tip "Hint"
    The fact that the `diag()` function is used for dual operations can cause confusion. However, just remember that passing a vector returns a matrix, while passing a matrix returns a vector, and that's it.

!!!warning "Attention"
    Obviously, the `diag()` function only accepts one-dimensional (vectors) and two-dimensional (matrices) inputs!

### Triangular Matrices

We conclude this brief overview by showing two methods to extract the triangular matrix, both upper and lower.

Suppose we have the previously defined matrix `x`. To extract the upper triangular matrix, we use the `triu()` function:

```py
>>> tu = np.triu(x)
>>> tu
array([[5, 2, 2],
       [0, 1, 3],
       [0, 0, 6]])
```

To extract the lower triangular matrix, we use the `tril()` function:

```py
>>> tl = np.tril(x)
>>> tl
array([[5, 0, 0],
       [2, 1, 0],
       [4, 3, 6]])
```

!!!tip "Hint"
    In this case, the `tril()` and `triu()` functions can be applied to n-dimensional arrays. Furthermore, the dimensions of the array do not need to have the same size.

## Accessing Array Elements

Just like lists, the most straightforward way to access the value of an element in an array is to use the `[]` operator, specifying the index of the element you want to access. For example, to select the first element of a vector:

```py
>>> a = np.array([1, 2, 3, 4])
>>> a[0]
1
```

In the case of n-dimensional arrays, you need to specify the index for each dimension of the array. For example, for a two-dimensional array, you can select the element in the first row and first column using the following syntax:

```py
>>> b = np.array([[1, 2], [3, 4]])
>>> b[0][0]
1
```

## Boolean Masks

We can access a subset of elements in an array using a "mask," which is another array of the same dimensions as the original array, containing boolean values only. By doing so, we extract only the elements whose corresponding position in the mask has a value of `True`. For example, we can select all elements belonging to the first column of the array `b`:

```py
>>> mask = np.array([[True, False], [True, False]])
>>> b[mask]
array([1, 3])
```

Similarly, we can choose all elements that satisfy a certain logical/mathematical condition:

```py
>>> mask = (b > 2)
>>> mask
array([[False, False],
       [ True,  True]])
>>> b[mask]
array([3, 4])
```

It's interesting to note that the previous notation can be further simplified using logical relations:

```py
>>> b[b > 2]
array([3, 4])
```

If desired, we can adapt the previous form to use arbitrarily complex expressions:

```py
>>> b[b % 2 == 0]
array([2, 4])
>>> b[(b > 1) & (b < 4)]
array([2, 3])
```

## Array Slicing

Just like lists, arrays also support slicing operations:

```py
>>> a = np.array([1, 2, 3, 4])
>>> a[0:2]
array([1, 2])
```

For multidimensional arrays, slicing is done along the nth dimension of the array. This concept is easy to understand when visualizing an n-dimensional array as an array of arrays:

```py
>>> b
array([[1, 2],
       [3, 4]])
>>> b[0:1]              # Slicing is done along the second dimension
array([[1, 2]])
```

## The `nonzero()` Function

We can use the `nonzero()` function to select the elements and indices of an array whose value is not zero. For example:

```py
>>> x = np.array([[3, 0, 0], [0, 4, 0], [5, 6, 0]])
>>> x
array([[3, 0, 0],
       [0, 4, 0],
       [5, 6, 0]])
>>> np.nonzero(x)
(array([0, 1, 2, 2], dtype=int64), array([0, 1, 0, 1], dtype=int64))
```

The `nonzero()` function returns a tuple with the row and column indices of the non-zero elements. In particular, the resulting tuple will have a number of elements equal to each dimension of the input array `x`, and the $i$-th array will indicate the indices relative to the $i$-th dimension. In this case, the first array represents the indices related to the first dimension of the non-zero values (in this case, the row indices), while the second array represents the indices related to the second dimension (column indices). Therefore, we have the following non-zero elements:

| Row Index | Column Index | Value |
| --------- | ------------ | ----- |
| 0         | 0            | 3     |
| 1         | 1            | 4     |
| 2         | 0            | 5     |
| 2         | 1            | 6     |

!!!tip "Obtaining a list of tuples"
    We can obtain a list of tuples representing the pairs of indices for the non-zero elements by using the `zip` function:
    > ```py
      >>> s = np.nonzero(tarry)
      >>> s
      (array([0, 1, 2, 2], dtype=int64), array([0, 1, 0, 1], dtype=int64))
      >>> coords = list(zip(s[0], s[1]))
      >>> coords
      [(0, 0), (1, 1), (2, 0), (2, 1)]
      ```

## Fancy Indexing

We conclude this lesson by discussing a very interesting technique called *fancy indexing*, which involves using an array of indices to access multiple elements simultaneously. For example:

```py
>>> rand = np.random.RandomState(42)
>>> x = rand.randint(100, size=10)
>>> indexes = np.array([[1, 4],[5, 2]])
>>> x
array([51, 92, 14, 71, 60, 20, 82, 86, 74, 74])
>>> x[indexes]
array([[92, 60],
       [20, 14]])
```

In the above code, we are:

1. using the `randint()` function to generate an array of random integers between 0 and 100;
2. creating a two-dimensional array `indexes`;
3. using fancy indexing to return an array with the dimensions of `indexes` and the elements of `x` taken from the positions indicated by `indexes`.

The power of fancy indexing lies in the fact that we can not only easily access multiple elements of an array in a single operation, but we can also rearrange these elements as desired!
