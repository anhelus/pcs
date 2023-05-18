# 2.2.6 - Statistics in NumPy

!!!tip "Accompanying Notebook"
    For this lesson, there is an *accompanying notebook* available at [this address](https://github.com/anhelus/pcs-exercises/blob/master/01_libs/01_numpy/03_statistics.ipynb).

In addition to [polynomials](05_polynomials.md) and [algebraic operations](04_algebra.md), NumPy provides various useful functions for statistical calculations. In this lesson, we will see some of them.

## Minimum and maximum of an array

First, let's look at two useful functions to determine the maximum and minimum values of an array, specifically [`numpy.amax()`](https://numpy.org/doc/stable/reference/generated/numpy.amax.html) and [`numpy.amin()`](https://numpy.org/doc/stable/reference/generated/numpy.amin.html), which allow us to find the maximum along a specific direction of an array.

For example, if we wanted to find the minimum and maximum of a randomly generated vector using the [`default_rng()`](https://numpy.org/doc/stable/reference/random/generator.html) function:

```py
>>> rng = np.random.default_rng(42)
>>> a = rng.integers(low=0, high=10, size=5)
>>> np.amin(a)
>>> np.amax(a)
```

For a matrix, and generally for any $N$-dimensional array, the procedure is similar:

```py
>>> b = rng.integers(low=0, high=10, size=(3, 3))
>>> np.amin(b)
>>> np.amax(b)
```

If we wanted to find the maximum and minimum along the columns of `b`, we would need to specify the `axis` parameter, which would be set to `0`:

```py
>>> np.amin(b, axis=0)
>>> np.amax(b, axis=0)
```

Similarly, to find the minimum and maximum *along the rows*, we would change the value of `axis` to `1`:

```py
>>> np.amin(b, axis=1)
>>> np.amax(b, axis=1)
```

We can also specify a tuple for the value of the `axis` parameter; in this case, the search for the maximum or minimum will be performed along all the axes specified by the tuple. For example, by specifying `(0, 1)`, we will search for the minimum (or maximum) element in the matrix:

```py
>>> np.amin(b, axis=(0, 1))
>>> np.amax(b, axis=(0, 1))
```

!!!note "The `argmax` and `argmin` functions"
    The [`numpy.argmax()`] and [`numpy.argmin()`] functions allow us to find the *index* of the maximum and minimum values, respectively.

## Percentile, Quantile, and Quartiles

The term *percentile* refers to a value that indicates the position of a data point within a distribution, or in other words, the percentage of data points that are below a certain value within the distribution itself.

To calculate the percentile for a given value $p$, we need to follow these steps:

1. Sort the $n$ values of the distribution in ascending order.
2. If $p$ is the percentile, calculate the product $k = n \cdot p \cdot \frac{1}{100}$.
3. If $k$ is an integer, the percentile is the average of the $k$-th and $(k+1)$-th values of the sorted data.
4. If $k$ is not an integer, round $k$ up to the nearest integer, and choose the corresponding value from the sorted data.

Let's consider an example. Suppose we have the following distribution of values:

$$
D = [20, 30, 10, 50, 40, 100, 90, 60, 80, 70]
$$

We want to calculate the $30$th percentile, so $p=30$. Let's follow the steps described above.

1. We sort the data, obtaining the vector $D_{sorted} = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]$.
2. The value of $k$ is $n \cdot p$, where $n=10$ and $p=0.30$, so $k=3$.
3. Since $k$ is an integer, the $30$th percentile is the average of $30$ and $40$, which is $35$.

The concept of *quantile* is related to that of percentile, but it generalizes it in some way. Specifically, when we talk about quantiles, we define a *partition* of the value distribution into a certain number of intervals. It is clear that if we have $100$ intervals, the quantile coincides with the percentile.

A notable partition is the one that divides the value distribution into four parts, called *quartiles*, as follows:

* The first quartile collects all elements below the $25$th percentile (denoted as $Q_1$).
* The second quartile collects elements between the $25$th and $50$th percentiles (denoted as $Q_2$).
* The third quartile contains elements between the $50$th and $75$th percentiles (denoted as $Q_3$).
* The last quartile includes elements beyond $Q_3$.

In other words, if $n$ is the total number of data points in the distribution, then:

$$
\begin{align}
& Q_1 = \frac{n + 1}{4}\\
& Q_2 = \frac{n + 1}{2}\\
& Q_3 = \frac{n + 1}{4} \cdot 3
\end{align}
$$

Quartiles are particularly important when characterizing a *non-parametric* distribution, which cannot be represented in terms of simple statistical parameters such as a normal distribution. In these cases, the distribution can be characterized non-parametrically by the median (the $50$th percentile), the standard deviation, and the *interquartile range*, which is given by $Q3-Q1$.

##### The `numpy.percentile()` and `numpy.quantile()` functions

For example, let's consider an ordered vector of elements from $1$ to $10

$ and calculate the $50$th percentile using the [`numpy.percentile()`](https://numpy.org/doc/stable/reference/generated/numpy.percentile.html) function in NumPy.

```py
>>> a = np.arange(1, 11)
>>> np.percentile(a, 50)
```

There are different ways to calculate the q-percentile, so it is advisable to consult the [reference](https://numpy.org/doc/stable/reference/generated/numpy.percentile.html) and the article [*Sample quantiles in statistical packages by Hyndman, R. J., & Fan, Y*](https://www.tandfonline.com/doi/abs/10.1080/00031305.1996.10473566).

In reality, the `percentile()` function uses the calculation of the median for the $50$th percentile, so it is equivalent to the [`median()`](https://numpy.org/doc/stable/reference/generated/numpy.median.html) function. In this specific case, there may be a deviation from the expected result due to interpolation errors introduced by NumPy:

```py
np.percentile(a, 50)
```

The concept of *quantile* is similar to that of percentile, but in this case, we are not dealing with percentage values, but with normalized values between $0$ and $1$. Therefore, if we use the [`numpy.quantile()`](https://numpy.org/doc/stable/reference/generated/numpy.quantile.html) function as before:

```py
>>> np.quantile(a, .5)
```

Both the `percentile()` and `quantile()` functions have an optional parameter `axis`. For example:

```py
>>> np.percentile(b, 50, axis=0)
>>> np.percentile(b, 50, axis=1)
```

As expected, setting the `axis` parameter to `0` will calculate the percentile for each column, while using `1` will calculate the percentile for each row.

## Arithmetic Mean and Weighted Mean

For calculating the average value of a NumPy array, two methods are available. The first method is the [`numpy.average(a, weights)`](https://numpy.org/doc/stable/reference/generated/numpy.average.html) function, which is used to calculate a weighted average of the elements in `a`, weighted by the elements in `weights` (assuming the dimensions of the two arrays are consistent).

The calculation performed by NumPy with the `average()` function is as follows:

```py
>>> avg = sum(a * weights) / sum(weights)
```

For example, if we want to assign a higher weight to the first and fourth elements of a randomly generated array `a`, we can do the following:

```py
>>> w = np.array([3, 1, 1, 3, 1])
>>> np.average(a, weights=w)
3.2222222222222223
```

The result slightly deviates from the simple arithmetic mean calculated as:

```py
>>> np.average(a)
4.2
```

Keep in mind that the mean is *weighted* by the sum of the weight values!

The [`numpy.mean(a)`](https://numpy.org/doc/stable/reference/generated/numpy.mean.html) function, on the other hand, represents the *arithmetic mean* of the elements in an array and is equivalent to the `average(a)` function without specifying the weights vector. For example:

```py
>>> np.mean(a)
4.2
```

We can also specify the `axis` parameter in this case:

```py
>>> np.mean(b, axis=0)
array([6.33333333, 2.33333333, 6.        ])
>>> np.mean(b, axis=1)
array([4.66666667, 2.33333333, 7.66666667])
```

## Variance and Standard Deviation

The functions [`numpy.std(a)`](https://numpy.org/doc/stable/reference/generated/numpy.std.html) and [`numpy.var(a)`](https://numpy.org/doc/stable/reference/generated/numpy.var.html) are used to calculate the standard deviation and variance of a vector:

```py
>>> np.std(a)
2.4
>>> np.var(a)
5.76
```

Similarly, we can specify the axes along which to perform the desired operation:

```py
>>> np.var(b, axis=0)
array([ 9.55555556, 10.88888889,  0.66666667])
>>> np.var(b, axis=1)
array([11.55555556,  4.22222222,  0.88888889])
```

## Histogram

An histogram provides a graphical representation of the values contained in a vector by grouping them into a certain number of partitions (bins).

For example, a possible representation with two bins for the vector $A = [1, 2, 3, 4]$ would be the vector $[2, 2]$. This is because the two bins divide the range of values taken by $A$ into two parts, with the first bin including the elements $1$ and $2$, and the second bin including the elements $3$ and $4$. Once the bins are calculated, they are "filled" by counting the number of elements in each bin, resulting in the vector $[2, 2]$.

It is possible to specify not only the number of bins but also their limits, which may not coincide with the limits of the vector.

NumPy allows us to obtain the histogram of a vector using the set of functions [`numpy.histogram(a, bins, range)`](https://numpy

.org/doc/stable/reference/generated/numpy.histogram.html), which calculates the (one-dimensional) histogram of the array `a` based on the number of bins (optional) and the range (optional). For example:

```py
>>> h, b = np.histogram(a)
```

In this case, we have used the default value of `bins`, which is 10.

Note that the `histogram()` function returns two values: the first represents the values taken by the histogram (i.e., the number of elements falling into each bin), and the second represents the bin limits.


