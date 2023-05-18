# 2.2.5 - Polynomial Operations in NumPy

!!!tip "Accompanying Notebook"
    For this lesson, there is an *accompanying notebook* available [here](https://github.com/anhelus/pcs-exercises/blob/master/01_libs/01_numpy/02_polynomials.ipynb).

As we saw in the [previous lesson](04_algebra.md), NumPy offers a wide range of functions for matrix calculations. However, it can also be used for other purposes, including polynomial calculations, through the [`numpy.polynomial`](https://numpy.org/doc/stable/reference/routines.polynomials.html) module. Let's see some of the main uses of this module.

## The `Polynomial` Class

Let's imagine we have two different polynomials, which are not associated with any physical meaning. The two polynomials are expressed by the following equations:

$$
\begin{cases}
p_1: y = 2x + 1 \\
p_2: y = x^2 + 3x + 2
\end{cases}
$$

NumPy allows us to represent a polynomial using objects of the [`Polynomial`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.Polynomial.html#numpy.polynomial.polynomial.Polynomial) class. In particular, an object of this type can be instantiated from the coefficients of the polynomial (but not only that). For example, considering the polynomials mentioned above and their coefficients, we can write:

```py
>>> from numpy.polynomial import Polynomial
>>> p_1_coef = [2, 1]       # coefficient list for p_1
>>> p_2_coef = [1, 3, 2]    # coefficient list for p_2
>>> p_1 = Polynomial(p_1_coef[::-1])
>>> p_2 = Polynomial(p_2_coef[::-1])
```

!!!warning "Order of Coefficients"
    The most important (and counterintuitive) feature of the `Polynomial` class (and all polynomial handling methods in NumPy) is that the coefficients are treated *in ascending order*. In practice, the constant term (the term for $x^0$) is considered first, followed by the coefficient of the first degree, the second degree, and so on. For this reason, in the above code, the coefficient list is reversed.

## Polynomial Addition

To add two polynomials, you can use the [`polyadd()`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyadd.html#numpy.polynomial.polynomial.polyadd) method, which takes two vectors `c1` and `c2` representing the coefficients of the two polynomials to be added. For example, to add two polynomials, you can write:

```py
>>> from numpy.polynomial import polynomial as P
>>> c1 = [1, 2, 3]
>>> c2 = [2, 5, 1]
>>> poly_sum = P.polyadd(c1, c2)
```

The result of this operation will be a numpy array with values `[3, 7, 4]`, equivalent to the polynomial $4x^2 + 7x + 3$.

## Polynomial Subtraction

Subtracting two polynomials is possible using the [`polysub()`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polysub.html#numpy.polynomial.polynomial.polysub) function, which works similarly to `polyadd()`, but the result will be the polynomial resulting from subtracting the coefficients of `c2` from `c1`.

```py
>>> poly_sub

 = P.polysub(c1, c2)
```

## Polynomial Multiplication

The above considerations can be extended to polynomial multiplication using the [`polymul()`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polymul.html) function:

```py
>>> poly_mul = P.polymul(c1, c2)
```

If you need to multiply a polynomial by an independent variable $x$, you can use the [`polymulx()`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polymulx.html) function.

## Polynomial Division

Division between polynomials is a slightly more complex operation than the others, and it requires the use of the [`polydiv()`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polymulx.html) function, which will return two arrays this time: the first represents the coefficients of the quotient polynomial, and the second represents the coefficients of the remainder polynomial. For example:

```py
>>> poly_q, poly_r = P.polydiv(c1, c2)
```

Again, the coefficients are ordered from the lowest degree to the highest degree.

## Polynomial Power

To raise a polynomial to a power, you can use the [`polypow()`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polypow.html) function, which accepts two parameters: a coefficient array `c` as the first argument, and a scalar `pow` as the second argument, representing the power to which the polynomial should be raised. For example:

```py
>>> poly_pow = P.polypow(c1, 2)
array([0., 0., 4., 4., 1.])
```

## Value of a Polynomial

The value $y$ assumed by a polynomial $p$ at a certain value of $x$ can be determined using the [`polyval()`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyval.html) function, which takes an integer (or a list of integers) `x` and a polynomial `p` as arguments. For example, to evaluate the value of $y$ for $x \in [1, 2]$ on the line represented by the polynomial `c1`:

```py
>>> P.polyval([1, 2], c1.coef)
```

!!!warning "Coefficients and Polynomial"
    It is important to note that we are not using an object of the `Polynomial` class, but rather the coefficients of the polynomial, which can be accessed through the `coef` property.

!!!note "Operations with Dimensionality 2 and 3"
    In case you need to evaluate polynomials in two and three dimensions, NumPy provides the functions [`polyval2d()`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyval2d.html) and [`polyval3d()`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyval3d.html).

## Derivative and Integral of Polynomial Functions

We conclude this brief overview with two methods capable of calculating the derivative and integral of a polynomial function.

The [`numpy.polyder()`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyder.html#numpy.polynomial.polynomial.polyder) function allows you to calculate the `m`th derivative (specified as the second argument, defaulting to `1`) of the coefficients of the polynomial `p` (specified as the first argument). For example, to calculate the derivative of `c1`:

```py
>>> P.polyder(c1.coef)
```



The dual method is [`numpy.polyint()`](https://numpy.org/doc/stable/reference/generated/numpy.polynomial.polynomial.polyint.html#numpy.polynomial.polynomial.polyint), which computes the `m`th integral of the coefficients of the polynomial `p`:

```py
>>> P.polyint(c1.coef)
```
