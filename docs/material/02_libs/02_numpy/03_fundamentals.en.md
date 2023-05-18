# 2.2.3 - Basic Operations on Arrays

After introducing arrays in the [previous lesson](./02_array.md), let's continue our discussion on arrays by exploring a series of fundamental operations that can be performed on them.

## Basic Algebraic Operations

Let's start with basic algebraic operations. For example, we can add two arrays element-wise using the `+` operator:

```py
>>> a = np.array([1, 2])
>>> b = np.array([3, 4])
>>> a + b
array([4, 6])
```

Similarly, we can perform element-wise subtraction, multiplication, and division using the mathematical operators `-`, `*`, and `/`:

```py
>>> a - b
array([-2, -2])
>>> a * b
array([3, 8])
>>> a / b
array([0.33333333, 0.5])
>>> b / a
array([3., 2.])
```

## The `numpy.sum()` function

The [`numpy.sum()`](https://numpy.org/doc/stable/reference/generated/numpy.sum.html#numpy.sum) function allows us to sum all elements of an array. For example, to sum all elements of a vector:

```py
>>> a = np.array([1, 2, 3, 4])
>>> a.sum()
10
```

In the case of a multidimensional array, we can specify the `axis` parameter, which indicates the axis along which the elements are summed. The value passed can be an integer, in which case the sum is performed along the $i$-th dimension, or a tuple of integers, in which case the sum is performed on each of the specified dimensions. Let's see some examples.

Suppose we have a two-dimensional array of size $2 \times 3$ (i.e., two rows and three columns).

```py
>>> b = np.array([[1, 2, 3], [4, 5, 6]])
>>> b
array([[1, 2, 3],
       [4, 5, 6]])
```

Let's determine which dimension corresponds to rows and which dimension corresponds to columns. We can use the `shape` attribute for that.

```py
>>> b.shape
(2, 3)
```

In the `shape` tuple, we can see that the first element corresponds to the number of rows, and the second element corresponds to the number of columns. Let's sum the array along the rows by setting `axis=0`:

```py
>>> b.sum(axis=0)
array([5, 7, 9])
```

Similarly, we can sum along the columns by setting `axis=1`:

```py
>>> b.sum(axis=1)
array([6, 15])
```

Let's see what happens in higher dimensions. Let's create a three-dimensional array:

```py
>>> c = np.random.rand(2, 3, 4)
>>> c
array([[[0.92287179, 0.46394039, 0.87332474, 0.74359334],
        [0.52656447, 0.6055654 , 0.74493945, 0.9349442 ],
        [0.90911935, 0.01961204, 0.66304527, 0.3025307 ]],

       [[0.86562763, 0.37544415, 0.4984404 , 0.74486371],
        [0.10910642, 0.24617353, 0.6237486 , 0.26432378],
        [0.37713232, 0.08804626, 0.21283048, 0.41133527]]])
>>> c.shape
(2, 3, 4)
```

Now let's sum all elements along the rows and columns:

```py
>>> c.sum(axis=(0, 1))
array([3.71042197, 1.79878176, 3.61632893, 3.401591  ])
```

We have seen the versatility of the `sum()` function and its ability to operate on arrays of any dimension.

!!!tip "The `axis` parameter"
    We will encounter the `axis` parameter in every application involving NumPy and related libraries.

## The `dot()` function

The `dot()` function allows us to perform matrix multiplication *row by column*. Specifically, the function is called on the matrix *on the left* in the multiplication, while the passed parameter is the matrix *on the right*.

For example, we can multiply a row vector by a column vector, resulting in a scalar:

```py
>>> a = np.array([[1, 2]])
>>> b = np.array([[3], [4]])
>>> a.dot(b)
array([11])
```

Conversely, multiplying a column vector by a row vector will result in a matrix:

```py
>>> b.dot(a)
array([[3, 6],
       [4, 8]])
```

## The `numpy.sort()` function

The [`numpy.sort()`](https://numpy.org/doc/stable/reference/generated/numpy.sort.html) function allows us to sort the elements of an array. For example:

```py
>>> arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
>>> np.sort(arr)
array([1, 2, 3, 4, 5, 6, 7, 8])
```

The sorting is done in *ascending* order (from the smallest to the largest element). In the case of an $n$-dimensional array, we can also specify the axis along which the sorting occurs by specifying the `axis` parameter. For example:

```py
>>> mat = np.array([[2, 3, 1], [4, 2, 6], [7, 5, 1]])
>>> mat
array([[2, 3, 1],
       [4, 2, 6],
       [7, 5, 1]])
```

To sort along the rows:

```py
>>> np.sort(mat, axis=0)
array([[2, 2, 1],
       [4, 3, 1],
       [7, 5, 6]])
```

While to sort along the columns:

```py
>>> np.sort(mat, axis=1)
array([[1, 2, 3],
       [2, 4, 6],
       [1, 5, 7]])
```

We can also specify different sorting algorithms using the `kind` argument, which allows us to choose between quicksort, mergesort, and heapsort.

!!!note "Inplace sorting"
    Keen observers will notice that the `sort()` function can be called directly on the `mat` object (`mat.sort()`) or by using NumPy (`np.sort()`). In the former case, the matrix is modified *inplace*, while in the latter case, it is not modified, and a copy is returned.

!!!note "Other sorting functions"
    There are also other functions for sorting an array, such as [`argsort()`](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort), [`lexsort()`](https://numpy.org/doc/stable/reference/generated/numpy.lexsort.html#numpy.lexsort), [`searchsorted()`](https://numpy.org/doc/stable/reference/generated/numpy.searchsorted.html#numpy.searchsorted), and [`partition()`](https://numpy.org/doc/stable/reference/generated/numpy.partition.html#numpy.partition).

## The `dot()` function

The `dot()` function allows us to perform matrix multiplication *row by column*. Specifically, the function is called on the matrix *on the left* in the multiplication, while the passed parameter is the matrix *on the right*.

For example, we can multiply a row vector by a column vector, resulting in a scalar:

```py
>>> a = np.array([[1, 2]])
>>> b = np.array([[3], [4]])
>>> a.dot(b)
array([11])
```

Conversely, multiplying a column vector by a row vector will result in a matrix:

```py
>>> b.dot(a)
array([[3, 6],
       [4, 8]])
```

## The `numpy.sort()` function

The [`numpy.sort()`](https://numpy.org/doc/stable/reference/generated/numpy.sort.html) function allows us to sort the elements of an array. For example:

```py
>>> arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
>>> np.sort(arr)
array([1, 2, 3, 4, 5, 6, 7, 8])
```

The sorting is done in *ascending* order (from the smallest to the largest element). In the case of an $n$-dimensional array, we can also specify the axis along which the sorting occurs by specifying the `axis` parameter. For example:

```py
>>> mat = np.array([[2, 3, 1], [4, 2, 6], [7, 5, 1]])
>>> mat
array([[2, 3, 1],
       [4, 2, 6],
       [7, 5, 1]])
```

To sort along the rows:

```py
>>> np.sort(mat, axis=0)
array([[2, 2, 1],
       [4, 3, 1],
       [7, 5, 6]])
```

While to sort along the columns:

```py
>>> np.sort(mat, axis=1)
array([[1, 2, 3],
       [2, 4, 6],
       [1, 5, 7]])
```

We can also specify different sorting algorithms using the `kind` argument, which allows us to choose between quicksort, mergesort, and heapsort.

!!!note "Inplace sorting"
    Keen observers will notice that the `sort()` function can be called directly on the `mat` object (`mat.sort()`) or by using NumPy (`np.sort()`). In the former case, the matrix is modified *inplace*, while in the latter case, it is not modified, and a copy is returned.

!!!note "Other sorting functions"
    There are also other functions for sorting an array, such as [`argsort()`](https://numpy.org/doc/stable/reference/generated/numpy.argsort.html#numpy.argsort), [`lexsort()`](https://numpy.org/doc/stable/reference/generated/numpy.lexsort.html#numpy.lexsort), [`searchsorted()`](https://numpy.org/doc/stable/reference/generated/numpy.searchsorted.html#numpy.searchsorted), and [`partition()`](https://numpy.org/doc/stable/reference/generated/numpy.partition.html#numpy.partition).

#### Multidimensional Arrays and `delete()`

The `delete()` function can also be used on multidimensional arrays. In this case, it is necessary to specify the axis along which to operate.

For example, if we want to remove the first row from the following array, we need to set the `axis` parameter to `0`:

```py
>>> mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
>>> np.delete(mat, 0, 0)
array([[4, 5, 6],
       [7, 8, 9]])
```

On the other hand, if we want to remove the first column, we need to pass the value `1`:

```py
>>> np.delete(mat, 0, 1)
array([[2, 3],
       [5, 6],
       [8, 9]])
```

If we do not specify a value for the `axis` parameter, we get this result:

```py
>>> np.delete(mat, 0)
array([2, 3, 4, 5, 6, 7, 8, 9])
```

In other words, by not specifying a value for `axis`, we remove the first element of the "flattened" array.

!!!tip "Other Element Removal Techniques"
    There are other ways to remove elements from an array. For example, you could use the `slice(start, stop, step)` function, which creates a `slice` object on the indices ranging from `start` to `stop` with a step of `step`. This can be used for purposes similar to the previous methods; for example:
    > ```py
      >>> np.delete(a, slice(0, 2, 1))
      array([3, 4])
      ```

    Another way is to use a boolean mask:
    > ```py
      >>> mask = np.array([[True, False, True], [False, False, True], [False, True, True]])
      >>> mtrx[mask]
      array([1, 3, 6, 8, 9])
      ```

### The `numpy.insert()` Function

The [`numpy.insert()`](https://numpy.org/doc/stable/reference/generated/numpy.insert.html) function allows us to insert an element into an array. The parameters accepted by the function are:

* `arr`: the array on which we want to perform the insertion operation;
* `obj`: the indices at which to insert the new values;
* `values`: the values to insert at the indices specified by `obj`;
* `axis`: the axis along which we want to operate.

For example, to insert a new row into the previous matrix, we need to specify the row index (`3`), the elements of the row to insert (`[10, 11, 12]`), and the axis (`0`):

```py
>>> np.insert(mat, 3, [10, 11, 12], 0)
array([[ 1,  2,  3],
       [ 4,  5,  6],
       [ 7,  8,  9],
       [10, 11, 12]])
```

By changing the axis to `1`, the insertion is performed on the columns:

```py
>>> np.insert(mat, 3, [10, 11, 12], 1)
array([[ 1,  2,  3, 10],
       [ 4,  5,  6, 11],
       [ 7,

  8,  9, 12]])
```

By not specifying any axis, the specified element is inserted into the flattened matrix:

```py
>>> np.insert(mat, 9, 10)
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
```

### The `numpy.append()` Function

The [`numpy.append()`](https://numpy.org/doc/stable/reference/generated/numpy.append.html) function allows us to append the specified values to the end of an array. The parameters accepted by the function are:

* `arr`: the array on which we want to perform the append operation;
* `values`: the values to append to the array;
* `axis`: the axis along which we want to operate.

By not specifying the axis, the concatenation is performed on the flattened matrix:

```py
>>> np.append(mat, [[10, 11, 12]])
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12])
```

If we specify the value `0` for the `axis` parameter, the concatenation is performed along the rows:

```py
>>> np.append(mat, [[10, 11, 12]], axis=0)
array([[ 1,  2,  3],
       [ 4,  5,  6],
       [ 7,  8,  9],
       [10, 11, 12]])
```

If we specify the value `1` for the `axis` parameter, the concatenation is performed along the columns:

```py
>>> np.append(mat, [[10], [11], [12]], axis=1)
array([[ 1,  2,  3, 10],
       [ 4,  5,  6, 11],
       [ 7,  8,  9, 12]])
```

!!!warning "Attention"
    In the last instruction, we used a *column* vector, while in the penultimate one, we used a *row* vector.

## Array Dimensions and Shape

There are several properties of an array that describe its dimensions and shape.

Referring back to our matrix `mat`, we can determine the number of axes using the `ndarray.ndim` attribute:

```py
>>> mat.ndim
2
```

The number of elements is defined by the `ndarray.size` attribute:

```py
>>> mat.size
9
```

The `ndarray.shape` attribute, which we briefly saw earlier, returns a tuple of integers indicating the number of elements along each axis of the array:

```py
>>> mat.shape
(3, 3)
```

## Modifying the Dimensions of an Array

We can modify the dimensions of an array using the [`numpy.reshape()`](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html) function. The parameters passed to the function are:

* `arr`: the array to modify the dimensions of;
* `new_shape`: the new dimensions of the array.

If we wanted to change the dimensions of a $4 \times 4$ matrix to $2 \times 8$, we could use the `reshape()` function as follows:

```py
>>> mat = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
>>> np.reshape(mat, (2, 8))
array([[ 1,  2,  3,  4,  5,  6,  7,  8],
       [ 9, 10, 11, 12, 13, 14, 15, 16]])
```

!!!tip "Tip"
    An alternative syntax is as follows:
    > ```py
      >>> mat.reshape((2, 8))
      array([[ 1,  2,  3,  4,  5,  6,  7,  8],
             [ 9, 10, 11, 12, 13, 14, 15, 16]])
      ```
      
    This means that the `reshape()` function is available both as a NumPy library function and as a method on `ndarray` objects.

!!!warning "Attention"
    The new dimensions of the array must be consistent with those of the original array!

## Flattening an Array

We have already seen the *flattening* of an array, which is automatically performed in certain situations (such as when calling `delete()` or `insert()` without specifying the `axis` parameter). However, we can use the [`numpy.flatten()`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flatten.html) function to manually perform this operation:

```py
>>> mat.flatten()
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16])
```

Another way to flatten an array is to use the [`numpy.ravel()`](https://numpy.org/doc/stable/reference/generated/numpy.ravel.html) function.

The `ravel()` and `flatten()` functions may appear to be similar. However, there is a fundamental difference: `flatten()` will *always* return a copy of the original array, while `ravel()`, if possible, will return a *view*, which is a variable that points to the same memory address as the original object.
