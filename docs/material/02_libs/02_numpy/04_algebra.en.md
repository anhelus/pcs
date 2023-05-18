# 2.2.4 - Algebraic Operations in NumPy

!!!tip "Accompanying Notebook"
    For this lesson, there is an *accompanying notebook* available at [this link](https://github.com/anhelus/pcs-exercises/blob/master/01_libs/01_numpy/01_algebra.ipynb).

After covering the [fundamental operations](03_fundamentals.md) in NumPy, let's delve into linear algebra operations, some of which are integrated into the [`linalg`](https://numpy.org/doc/stable/reference/routines.linalg.html) package.

The examples we will see in the following sections all involve the use of this package, so it is necessary to import it before proceeding with the lesson.

```py
from numpy import linalg
```

## Matrix Transpose

In reality, the first operation we will describe does *not* require the use of the `linalg` module, and it is the operation that allows us to take the transpose of a matrix.

Recall that the transpose $A^T$ of a matrix $A$ is defined as the matrix in which the element with index $(i, j)$ is the element with indices $(j, i)$ of the original matrix. In practice:

$$
(A^T)_{ij} = A_{ji} \forall A \in \mathbb{R}^{m,n}, 1 \leq i \leq m, 1 \leq j \leq n
$$

To accomplish this, we simply use the [`numpy.transpose()`](https://numpy.org/doc/stable/reference/generated/numpy.transpose.html) function.

```py
>>> x = np.array([[1, 2, 3], [4, 5, 6]])
>>> np.transpose(x)
array([[1, 4],
       [2, 5],
       [3, 6]])
```

## Matrix Inverse

The calculation of the matrix inverse, on the other hand, requires the use of the [`linalg.inv()`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.inv.html) function, which takes the matrix to be inverted as a parameter.

Recall that the inverse matrix $A_{inv}$ of an invertible matrix $A$ is the matrix for which the following relationship holds:

$$
A_{inv}A=AA_{inv}=I
$$

In other words, the matrix product between $A$ and its inverse is commutative and equal to the identity matrix of the same rank.

For example:

```py
>>> mat = np.array([[5, 0, 0], [0, 2, 0], [0, 0, 4]])
>>> linalg.inv(mat)
array([[0.2 , 0.  , 0.  ],
       [0.  , 0.5 , 0.  ],
       [0.  , 0.  , 0.25]])
```

Obviously, *the matrix `mat` must be invertible*, that is, it must be square and have maximum rank. If we were to pass a rectangular matrix, an error of type `LinAlgError` would be raised:

```py
>>> mat = np.array([[1, 2, 3], [4, 5, 6]])
>>> linalg.inv(mat)
Traceback (most recent call last):
```

## Vector and Matrix Products

### The `dot()` function

In the [previous lesson](03_fundamentals.md#basic-algebraic-operations), we saw an example of using the `dot(a, b)` function to calculate the matrix product between arrays `a` and `b`. This function follows all the rules of matrix calculations, as summarized in the following table.

| Dimensionality of `a` | Dimensionality of `b` | Result |
| ---------------- | ----- | --------- |
| One-dimensional (vector) | One-dimensional (vector) | Dot product |
| Two-dimensional (matrix) | Two-dimensional (matrix) | Matrix product |
| Scalar | $n$-dimensional | Dot product with $n$-dimensional array |
| $n$-dimensional | Scalar | Dot product with $n$-dimensional array |

Note that:

* when multiplying two vectors, the result is the dot product;
* when multiplying two matrices, the result is the matrix product, and it is recommended to use the [`matmul()`](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html) function instead;
* when multiplying a scalar and a matrix, it is recommended to use the [`multiply()`](https://numpy.org/doc/stable/reference/generated/numpy.multiply.html) function or alternatively, the `*` operator.

In the [lesson notebook](https://github.com/anhelus/pcs-exercises/blob/master/01_libs/01_numpy_algebra.ipynb), we will see some examples of matrix products.

!!!note "Multiplication of Multidimensional Arrays"
    When both arrays to be multiplied are $n$-dimensional, additional rules apply, which can be found at [this link](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot).

### Inner Product

Recall that for two arbitrary one-dimensional vectors $a = [a_{1}, \ldots, a_{j}]$ and $b = [b_{1}, \ldots, b_{j}]$, both with $j$ elements, the *dot product* or *inner product* is given by:

$$
p = \sum_{i=1}^j a_{i} \cdot b_{i}
$$

To calculate the dot product between vectors `a` and `b`, we can use the [`numpy.inner(a, b)`](https://numpy.org/doc/stable/reference/generated/numpy.inner.html) function:

```py
>>> a = np.array([1, 2, 3])
>>> b = np.array([4, 5, 6])
>>> np.inner(a, b)
32
```

#### The Functions `inner()` and `dot()`

An attentive reader may have noticed that, in practice, for monodimensional vectors, the `inner()` and `dot()` functions return the same result:

```py
np.inner(a, b)      # Output: 32
a.dot(b)            # Output: 32, same as b.dot()
```

The difference between the two functions becomes apparent when using arrays with dimensions greater than 1:

```py
>>> a = np.array([[1, 2], [3, 4]])
>>> b = np.array([[5, 6], [7, 8]])
>>> np.inner(a, b)   # Result with inner()
array([[17, 23],
       [39, 53]])
>>> a.dot(b)   # Result with dot()
array([[19, 22],
       [43, 50]])
```

In practice, referring back to the documentation:

* Regarding the `dot()` function, it is equivalent to `matmul()` and represents a matrix multiplication. In the case of monodimensional vectors, it is equivalent to the dot product. For $n$ dimensions, it is the sum of the products between the last dimension of the first vector and the dimensions ranging from 2 to $n$ of the second vector.
* Regarding the `inner()` function, it represents the dot product for monodimensional vectors. In the case of $n$ dimensions, it represents the sum of the products along the last dimension.

In other words:

```py
a.dot(b) == sum(a[i, :] * b[:, j])
np.inner(a, b) == sum(a[i, :] * b[j, :])
```

Referring to the previous example:

$$
\text{dot} = \left(\begin{array}{cc}
1 & 2\\
3 & 4
\end{array}\right)
\left(\begin{array}{cc}
5 & 6\\
7 & 8
\end{array}\right) = \\
= \left(\begin{array}{cc}
1 \cdot 5 + 2 \cdot 7 & 1 \cdot 6 + 2 \cdot 8   \\
3 \cdot 5 + 4 \cdot 7 & 3 \cdot 6 + 4 \cdot 8
\end{array}\right)
= \left(\begin{array}{cc}
19 & 22\\
43 & 50
\end{array}\right)
$$

$$
\text{inner} = \left(\begin{array}{cc}
1 & 2\\
3 & 4
\end{array}\right)
\left(\begin{array}{cc}
5 & 6\\
7 & 8
\end{array}\right) = \\
= \left(\begin{array}{cc}
1 \cdot 5 + 2 \cdot 6 & 1 \cdot 7 + 2 \cdot 8   \\
3 \cdot 5 + 4 \cdot 6 & 3 \cdot 7 + 4 \cdot 8
\end{array}\right)
= \left(\begin{array}{cc}
17 & 23\\
39 & 53
\end{array}\right)
$$

### Outer Product

The *outer product* between two vectors $a = [a_1, a_2, \ldots, a_j]$ and $b = [b_1, b_2, \ldots, b_j]$ is defined as the matrix $P$ where:

$$
P = \left[
	\begin{array}{ccc}


		a_1 \cdot b_1 & \ldots & a_1 \cdot b_n \\
		\vdots        & \ddots & \vdots        \\
		a_n \cdot b_1 & \ldots & a_n \cdot b_n
	\end{array}
\right]
$$

To calculate it, NumPy provides the function [`numpy.outer(a, b)`](https://numpy.org/doc/stable/reference/generated/numpy.outer.html).

For example:

```py
a = np.array([1, 2])
b = np.array([3, 4])

np.outer(a, b)
```

#### The `matmul()` Function

When we talked about the `dot()` function, we saw how it is possible to use it to perform matrix multiplication between matrices `mat_1` and `mat_2`. However, there is another possibility, which is also the *recommended* one, which is to use the [`numpy.matmul()`](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html) function:

```py
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
np.matmul(a, b)
```

The `matmul()` function has a fundamental difference compared to the `dot()` function, as it does not accept scalars as input (although it is possible to pass vectors and $n$-dimensional arrays). There is actually another important difference that concerns $n$-dimensional operations, but we will not discuss it here.

!!!note "The `@` Operator"
    The `@` operator is delegated to direct multiplication of two-dimensional arrays and is used "under the hood" by the `matmul()` function.

## Matrix Power

The [`np.linalg.matrix_power(a, n)`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_power.html) function allows us to raise matrix `a` to the power of `n`. For example:

```py
np.linalg.matrix_power(a, 5)
```

## Eigenvalues and Eigenvectors

To calculate the eigenvalues and eigenvectors of a matrix, NumPy provides the [`np.linalg.eig()`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eig.html) function, which returns the eigenvalues and right eigenvectors of a square matrix:

```py
(v, w) = np.linalg.eig(a)
v
w
```

There are also other functions for calculating eigenvalues and eigenvectors. In particular:

* [`np.linalg.eigh()`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigh.html) calculates the eigenvalues and eigenvectors of a real or complex symmetric matrix;
* [`np.linalg.eigvals()`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigvals.html#) calculates the eigenvalues of a square matrix;
* [`np.linalg.eigvalsh()`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigvalsh.html#) calculates the eigenvalues of a real or complex symmetric matrix.

## Norm, Rank, Determinant, and Trace

The [`np.linalg.norm(a)`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html) function allows us to calculate the norm of a matrix. Optionally, we can specify three parameters:

* `ord`, which represents the order of the norm to calculate (by default, the Frobenius norm is calculated);
* `axis`, which indicates the axis (or axes, in the case of a multidimensional array) to operate on;
* `keepdims`, used to optionally return the axis along which the norm is calculated.

To calculate the Frobenius norm of matrix `mat`, we can use this syntax:

```py
np.linalg.norm(a)
```

To calculate the determinant, rank, and trace of a matrix, we can use the functions [`np.linalg.det()`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.det.html), [`np.linalg.matrix_rank()`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_rank.html), and [`np.trace()`](https://numpy.org/doc/stable/reference/generated/numpy.trace.html). For example:

```py
np.linalg.det(a)
np.linalg.matrix_rank(a

)
np.trace(a)
```

The `trace()` function can also be used to calculate the sum of the upper/lower diagonals by specifying the `offset` parameter. For example:

```py
np.trace(mtrx, offset=1)
np.trace(mtrx, offset=-1)
```

## Solving Linear Systems of Equations

We conclude this (necessarily) brief overview of linear algebra operations with the function [`np.linalg.solve(a, b)`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html), which allows us to solve a system of linear equations where matrix `a` is the coefficient matrix, and vector `b` is the vector of known terms. For example:

```py
b = np.array([3, 2, 3])
np.linalg.solve(mat, b)
```

Of course, the matrix `a` must be square, and the vector `b` must have exactly `n` elements, where `n` is the order of `a`!

!!!note "Operations on Tensors"
    NumPy provides the N-dimensional tensor version of some functions. In particular, we mention the tensor product function [`np.tensordot()`](https://numpy.org/doc/stable/reference/generated/numpy.tensordot.html#numpy.tensordot) and the function for solving tensor equations [`np.linalg.tensorsolve()`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.tensorsolve.html).

## Reference

As mentioned several times, this overview has been necessarily brief and limited. For a more complete overview, the recommendation is always to refer to the [excellent NumPy documentation](https://numpy.org/doc/stable/reference/routines.linalg.html).
