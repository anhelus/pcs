# 2.1 - Jupyter Lab

!!!tip "Accompanying Notebook"
    For this lesson, there is an accompanying *notebook* available at [this link](https://github.com/anhelus/pcs-exercises/blob/master/01_libs/00_jupyter_sample.ipynb).

Until now, we have been running Python scripts directly from the command line. However, it is evident that this approach is limited, especially in data science applications.

To overcome these limitations, the SciPy framework introduces [Jupyter Lab](https://jupyter.org/), which is one of the most widely used tools by data analysts nowadays: the *notebook*.

## Anatomy of a Notebook

A notebook is, in simple terms, an *interactive environment* that allows us to *write* and *test* our code. In particular, we can write one or more instructions and execute them separately from each other using the concept of *cells*, which are individual "blocks" of code.

!!!tip "Tip"
    Jupyter notebooks also allow us to include comments, descriptions, and equations using two well-known markup languages: [Markdown](https://daringfireball.net/projects/markdown/) and [LaTeX](https://www.latex-project.org/).

Now let's see how to create and use our first notebook.

## Installation and Launching Jupyter Lab

!!!note "Installing a Library"
    Remember that the various options for installing a library are described in detail in [Appendix B](../../appendix/03_libraries/lecture.md).

To install Jupyter Lab, we'll use `pip`, preferably within a virtual environment:

```sh
workon my-virtual-env
(my-virtual-env) pip install jupyterlab
```

Unlike other libraries, Jupyter doesn't need to be imported explicitly. Instead, you can launch the interactive environment using the following command in the terminal:

```sh
jupyter lab
```

!!!note "Importing iPython"
    In theory, it is possible to import iPython and use the methods and classes provided like any other library. However, in practice, it is more common to use the interactive environment offered by Jupyter notebooks.

## The First Notebook

At this point, you will see a screen similar to the one shown in Figure 1.

<figure markdown>
  ![intro](./images/intro.png){ width="450" }
  <figcaption>Figure 1 - The introductory screen of Jupyter Lab</figcaption>
</figure>

Let's create our first notebook by clicking on the *Python 3* button in the *Notebook* menu. Once the notebook is created, we can start interacting with the environment. Before proceeding, let's define the name of our notebook from the left menu.

Let's try doing something simple: create a function that adds two numeric variables and returns the result, and then call it with two different values.

First, write the code for the function in the first cell:

```py
def sum(a, b):
    result = a + b
    return result
```

To execute the code in the cell, press the `Play` button or use the keyboard shortcut `Shift+Enter`. Once the first cell is executed, Jupyter will automatically create a new cell. In the new cell, we can write the instructions to call the `sum()` function with different values.

```py
sum(5, 7)
```

Execute the cell, and you will see the value returned by the function displayed below the cell.

## Other Useful Operations

Jupyter allows us to perform several useful operations, including:

* deleting an entire cell,
* inserting a cell above or below the currently selected cell,
* stopping the kernel,
* restarting

 the kernel.

Let's focus for a moment on the last two operations. It may happen that you need to interrupt the current flow of execution of the instructions or restart the notebook. Since Jupyter is based on the concept of a *kernel*, which is responsible for executing the notebook, we say that we can *interrupt* or *stop* the kernel or *restart* it.

Interrupting the kernel only stops the execution of the current cell. It does not result in any data loss, and you can continue running the code in the notebook at any time, either from the beginning of that cell or from within another cell. Restarting the kernel, on the other hand, completely "freezes" the execution, deleting all variables stored in memory. It is a true "reset" that should be used when, for example, you need to reorganize the code or when you have made too many modifications that lead to inconsistent results.

## Colab

More and more often, scientific computing and data science code requires extensive computational resources that may not be available on our personal computers. To overcome this problem and allow anyone to experiment with the libraries we will see in this course, there is a tool called [Colab](https://colab.research.google.com/) provided by Google that allows us to run Jupyter notebooks for free.

Of course, the free version has some limitations, but they are more than sufficient for our purposes.