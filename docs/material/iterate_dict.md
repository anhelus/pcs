# Cosa sono i dizionari?

I *dizionari* sono una delle pietre miliari di Python. Numerosi aspetti del linguaggio sono centrati sui dizionari: moduli, classi, oggetti, globals() e locals()

Getting Started With Python Dictionaries
Dictionaries are a cornerstone of Python. Many aspects of the language are built around dictionaries. Modules, classes, objects, globals(), and locals() are all examples of how dictionaries are deeply wired into Python’s implementation.

Here’s how the Python official documentation defines a dictionary:

An associative array, where arbitrary keys are mapped to values. The keys can be any object with __hash__() and __eq__() methods. (Source)

There are a couple of points to notice in this definition:

Dictionaries map keys to values and store them in an array or collection. The key-value pairs are commonly known as items.
Dictionary keys must be of a hashable type, which means that they must have a hash value that never changes during the key’s lifetime.
Unlike sequences, which are iterables that support element access using integer indices, dictionaries are indexed by keys. This means that you can access the values stored in a dictionary using the associated key rather than an integer index.

The keys in a dictionary are much like a set, which is a collection of hashable and unique objects. Because the keys need to be hashable, you can’t use mutable objects as dictionary keys.

On the other hand, dictionary values can be of any Python type, whether they’re hashable or not. There are literally no restrictions for values. You can use anything as a value in a Python dictionary.

Note: The concepts and topics that you’ll learn about in this section and throughout this tutorial refer to the CPython implementation of Python. Other implementations, such as PyPy, IronPython, and Jython, could exhibit different dictionary behaviors and features that are beyond the scope of this tutorial.

Before Python 3.6, dictionaries were unordered data structures. This means that the order of items typically wouldn’t match the insertion order:

>>> # Python 3.5
>>> likes = {"color": "blue", "fruit": "apple", "pet": "dog"}

>>> likes
{'color': 'blue', 'pet': 'dog', 'fruit': 'apple'}
Note how the order of items in the resulting dictionary doesn’t match the order in which you originally inserted the items.

In Python 3.6 and greater, the keys and values of a dictionary retain the same order in which you insert them into the underlying dictionary. From 3.6 onward, dictionaries are compact ordered data structures:

>>> # Python 3.6
>>> likes = {"color": "blue", "fruit": "apple", "pet": "dog"}

>>> likes
{'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
Keeping the items in order is a pretty useful feature. However, if you work with code that supports older Python versions, then you must not rely on this feature, because it can generate buggy behaviors. With newer versions, it’s completely safe to rely on the feature.

Another important feature of dictionaries is that they’re mutable data types. This means that you can add, delete, and update their items in place as needed. It’s worth noting that this mutability also means that you can’t use a dictionary as a key in another dictionary.


Remove ads
Understanding How to Iterate Through a Dictionary in Python
As a Python developer, you’ll often be in situations where you need to iterate through an existing dictionary while you perform some actions on its key-value pairs. So, it’s important for you to learn about the different options for dictionary iteration in Python.

When it comes to iterating through a dictionary in Python, the language provides some great tools and techniques to help you out. You’ll learn about several of these tools and techniques in this tutorial. To start off, you’ll learn the basics of iterating over dictionaries and their keys, values, and items using for loops.

Traversing a Dictionary Directly
Python’s dictionaries have some special methods that Python uses internally to perform some operations. These methods use the naming convention of adding a double underscore at the beginning of and at the end of the method’s name.

You can use the built-in dir() function to get a list of methods and attributes that any Python object provides. If you run dir() with an empty dictionary as an argument, then you’ll get all the methods and attributes of the dict class:

>>> dir({})
['__class__', '__contains__', '__delattr__', ... , '__iter__', ...]
A closer look at the previous output reveals the '__iter__' entry, which is a method that Python automatically calls when you require an iterator for a container data type. This method should return a new iterator object, which allows you to iterate through all the items in the underlying container type.

For Python dictionaries, .__iter__() allows direct iteration over the keys by default. This means that if you use a dictionary directly in a for loop, Python will automatically call .__iter__() on that dictionary, and you’ll get an iterator that goes over its keys:

>>> likes = {"color": "blue", "fruit": "apple", "pet": "dog"}

>>> for key in likes:
...     print(key)
...
color
fruit
pet
Python is smart enough to know that likes is a dictionary and that it implements .__iter__(). In this example, Python calls .__iter__() automatically, and this allows you to iterate over the keys of likes without further effort on your side.

This is the primary way to iterate through a dictionary in Python. You just need to put the dictionary directly into a for loop, and you’re done!

If you use this approach along with the [key] operator, then you can access the values of your dictionary while you loop through the keys:

>>> for key in likes:
...     print(key, "->", likes[key])
...
color -> blue
fruit -> apple
pet -> dog
In this example, you use key and likes[key] at the same time to access your target dictionary’s keys and the values, respectively. This technique enables you to perform different operations on both the keys and the values of likes.

Even though iterating through a dictionary directly is pretty straightforward in Python, you’ll often find that dictionaries provide more convenient and explicit tools to achieve the same result. That’s the case with the .items() method, which defines a quick way to iterate over the items or key-value pairs of a dictionary.

Looping Over Dictionary Items: The .items() Method
When you’re working with dictionaries, iterating over both the keys and values at the same time may be a common requirement. The .items() method allows you to do exactly that. The method returns a view object containing the dictionary’s items as key-value tuples:

>>> likes = {"color": "blue", "fruit": "apple", "pet": "dog"}

>>> likes.items()
dict_items([('color', 'blue'), ('fruit', 'apple'), ('pet', 'dog')])
Dictionary view objects provide a dynamic view of the dictionary’s items. Here, dynamic means that when the dictionary changes, the views reflect those changes.

Views are iterable, so you can iterate through the items of a dictionary using the view object that results from calling .items(), as you can see in the example below:

>>> for item in likes.items():
...     print(item)
...
('color', 'blue')
('fruit', 'apple')
('pet', 'dog')
In this example, .items() returns a view object that yields key-value pairs one at a time and allows you to iterate through them.

If you take a closer look at the individual items that .items() yields, then you’ll note that they’re tuple objects:

>>> for item in likes.items():
...     print(item)
...     print(type(item))
...
('color', 'blue')
<class 'tuple'>
('fruit', 'apple')
<class 'tuple'>
('pet', 'dog')
<class 'tuple'>
In this updated loop, you use the built-in type() function to check the data type of every item that .items() yields. As you can confirm in the loop’s output, all the items are tuples. Once you know this, you can use tuple unpacking to iterate through the keys and values in parallel.

To achieve parallel iteration through keys and values, you just need to unpack the elements of every item into two different variables, one for the key and another for the value:

>>> for key, value in likes.items():
...     print(key, "->", value)
...
color -> blue
fruit -> apple
pet -> dog
The key and value variables in the header of your for loop do the unpacking. Every time the loop runs, key gets a reference to the current key, and value gets a reference to the value. This way, you have more control over the dictionary content. Therefore, you’ll be able to process the keys and values separately in a readable and Pythonic manner.


Remove ads
Iterating Through Dictionary Keys: The .keys() Method
Python dictionaries offer a second way for you to iterate through their keys. Apart from using the target dictionary directly in a loop, you can also use the .keys() method. This method returns a view object containing only the dictionary keys:

>>> likes = {"color": "blue", "fruit": "apple", "pet": "dog"}

>>> likes.keys()
dict_keys(['color', 'fruit', 'pet'])
The .keys() method returns an object that provides a dynamic view of the keys in likes. You can use this view object to iterate through the dictionary keys. To do this, call .keys() in the header of a for loop:

>>> for key in likes.keys():
...     print(key)
...
color
fruit
pet
When you call .keys() on likes, you get a view of keys. Python knows that view objects are iterable, so it starts looping.

You might wonder why you’d use .keys() instead of just iterating over the dictionary directly. The quick answer is that using .keys() explicitly allows you to better communicate the intention of iterating over the keys only.

Walking Through Dictionary Values: The .values() Method
Another common need that you’ll face when iterating through dictionaries is to loop over the values only. The way to do that is to use the .values() method, which returns a view with the values in the underlying dictionary:

>>> likes = {"color": "blue", "fruit": "apple", "pet": "dog"}

>>> likes.values()
dict_values(['blue', 'apple', 'dog'])
In this code, .values() returns a view object that yields values from likes. As with other view objects, the result of .values() is also iterable, so you can use it in a loop:

>>> for value in likes.values():
...     print(value)
...
blue
apple
dog
Using .values(), you only have access to the values of your target dictionary, likes. Note that this iteration tool doesn’t give you access to the key associated with each value. So, you should use this technique if you only need to access the values in the target dictionary.

Changing Dictionary Values During Iteration
Sometimes you’ll need to change the values in a dictionary while you iterate through them in Python. In the following example, you update the price of a bunch of products in a dictionary:

>>> fruits = {"apple": 0.40, "orange": 0.35, "banana": 0.25}

>>> for fruit, price in fruits.items():
...     fruits[fruit] = round(price * 0.9, 2)
...

>>> fruits
{'apple': 0.36, 'orange': 0.32, 'banana': 0.23}
In this example, you use the expression fruits[fruit] = round(price * 0.9, 2) to modify the values of fruits and apply a 10 percent discount.

A subtle detail to note in the above example is that to update the values, you use the original dictionary instead of just updating the current price directly with something like price = round(price * 0.9, 2). Why do you need fruits[fruit] if you have direct access to price? Is it possible to update price directly?

The real problem is that reassigning fruit or price doesn’t reflect in the original dictionary. What really happens is that you’ll lose the reference to the dictionary component without changing anything in the dictionary.

Safely Removing Items From a Dictionary During Iteration
Because Python dictionaries are mutable, you can remove existing key-value pairs from them as needed. In the following example, you remove an item selectively, according to its specific value. Note that to safely shrink a dictionary while iterating through it, you need to use a copy:

>>> fruits = {"apple": 0.40, "orange": 0.35, "banana": 0.25}

>>> for fruit in fruits.copy():
...     if fruits[fruit] >= 0.30:
...         del fruits[fruit]
...

>>> fruits
{'banana': 0.25}
In this example, you use .copy() to create a shallow copy of your target dictionary, fruits. Then you loop over the copy while removing items from the original dictionary. In the example, you use the del statement to remove dictionary items. However, you can also use .pop() with the target key as an argument.

If you don’t use a copy of your target dictionary while trying to remove items in a loop, then you get an error:

>>> fruits = {"apple": 0.40, "orange": 0.35, "banana": 0.25}

>>> for fruit in fruits:
...     if fruits[fruit] >= 0.30:
...         del fruits[fruit]
...
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    for fruit in fruits:
RuntimeError: dictionary changed size during iteration
When you try to remove an item from a dictionary during iteration, Python raises a RuntimeError. Because the original dictionary has changed its size, it’s ambigous how to continue the iteration. So, to avoid this issue, always use a copy of your dictionary in the iteration.


Remove ads
Iterating Through Dictionaries: for Loop Examples
So far, you’ve learned the basic ways to iterate through a dictionary in Python. You now know how to iterate over dictionary keys, values, and items using different tools and techniques. It’s time to move on and write some examples of what you can do with the content of a dictionary while you iterate through it in a for loop.

Note: In the section on comprehension examples, you’ll learn that you can also use comprehensions to solve the same problems in a more concise way.

To kick things off, you’ll start with an example of how to filter dictionary items by value using a for loop.

Filtering Items by Their Value
Sometimes, you’ll be in situations where you have a dictionary and want to create a new one that only contains the data that satisfies a given condition. You can do this with a conditional statement while you traverse the dictionary. Consider the following toy example:

>>> numbers = {"one": 1, "two": 2, "three": 3, "four": 4}

>>> small_numbers = {}

>>> for key, value in numbers.items():
...     if value <= 2:
...         small_numbers[key] = value
...

>>> small_numbers
{'one': 1, 'two': 2}
In this example, you filter the items with a value less than 2 and add them to your small_numbers dictionary. This new dictionary only contains the items that satisfy the condition value <= 2, which is your filtering condition.

There’s another technique that you can use to filter items from a dictionary. Key view objects are like Python sets. So, they support set operations, such as union, intersection, and difference. You can take advantage of this set-like behavior to filter certain keys from a dictionary.

For example, in the code below, you use a set difference to filter out the citrus from your fruits dictionary:

>>> fruits = {"apple": 0.40, "orange": 0.35, "banana": 0.25}

>>> fruits.keys() - {"orange"}
{'apple', 'banana'}
When you run fruits.keys() - {"orange"}, you’re really running a set difference operation. You can use this trick to create a new dictionary without citrus fruits:

>>> non_citrus = {}

>>> for key in fruits.keys() - {"orange"}:
...     non_citrus[key] = fruits[key]
...

>>> non_citrus
{'apple': 0.4, 'banana': 0.25}
In this example, you build a new dictionary out of the set of keys that you get from computing the difference between your dictionary’s keys and a set of unwanted keys.

The fact that key view objects behave like sets is a little-known feature that can be useful in some situations. So, keep it in your tool kit.

Running Calculations With Keys and Values
Running calculations with a dictionary’s values while you iterate through the dictionary itself is another common task. Suppose you’ve stored the data for your company’s sales in a dictionary, and now you want to know the year’s total income.

To solve this problem, you can use an accumulator variable with an initial value of zero. Then, you can accumulate every value in your dictionary in that variable:

>>> incomes = {"apple": 5600.00, "orange": 3500.00, "banana": 5000.00}
>>> total_income = 0.00

>>> for income in incomes.values():
...     total_income += income
...

>>> total_income
14100.0
Here, you iterate through the values in your incomes dictionary and sequentially accumulate them in total_income. The augmented assignment total_income += income does the magic, and at the end of the loop, you get the total income for the year.

As with many tasks in Python, you’ll have a better way to do the same computation, as in the example below. You can use the built-in sum() function:

>>> sum(incomes.values())
14100.0
In this example, you pass the values in your incomes dictionary directly as an argument to sum(). The function implicitly iterates over the values and computes their sum in the process.

Even though the sum() solution is concise, fast, and readable, the loop solution is more generic and allows you to perform computations other than just summing up the values.


Remove ads
Swapping Keys and Values Through Iteration
Suppose you have a dictionary and need to turn keys into values and values into keys. In this situation, you can use a for loop to iterate through the original dictionary while you build the new one with swapped keys and values:

>>> numbers = {"one": 1, "two": 2, "three": 3, "four": 4}
>>> swapped = {}

>>> for key, value in numbers.items():
...     swapped[value] = key
...

>>> swapped
{1: 'one', 2: 'two', 3: 'three', 4: 'four'}
The expression swapped[value] = key does the hard work for you by swapping the keys and values in a new dictionary. Note that for this code to work, the data stored in the values of your original dictionary must be of a hashable data type. Otherwise, you’ll get an error.

Again, Python has other tools that allow you to write the previous example in a more concise way. This time, you can use the built-in zip() function along with the dict() constructor:

>>> dict(zip(numbers.values(), numbers.keys()))
{1: 'one', 2: 'two', 3: 'three', 4: 'four'}
In this example, you use zip() to generate tuples of value-key pairs. To do that zip() implicitly iterates over the values and keys of your numbers dictionary. Then you use the resulting tuples as arguments to dict() and build the desired dictionary.

Iterating Through Dictionaries: Comprehension Examples
A dictionary comprehension is a compact way to process and transform data in order to produce a new dictionary as a result. In contrast to list comprehensions, dictionary comprehensions need a key that maps to a value. You can first provide two expressions separated by a colon (:). After this, you’ll provide a for clause, and you can also include an optional if clause.

To illustrate how dictionary comprehensions work, suppose that you have two lists of data, and you need to create a new dictionary from them. In this case, you can use the built-in zip() to loop over the elements of both lists in parallel:

>>> categories = ["color", "fruit", "pet"]
>>> objects = ["blue", "apple", "dog"]

>>> likes = {key: value for key, value in zip(categories, objects)}
>>> likes
{'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
In this example, zip() receives two iterables, categories and objects, as arguments and makes an iterator that aggregates elements from each iterable. The tuple objects that zip() generates are then unpacked into key and value, which you finally use to create the new desired dictionary.

Note: The above example demonstrates how dictionary comprehensions work in Python. Still, a better way to write the example would be the following:

>>> categories = ["color", "fruit", "pet"]
>>> objects = ["blue", "apple", "dog"]

>>> dict(zip(categories, objects))
{'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
The zip() function generates the key-value pairs from the original lists, while the dict() constructor creates the new dictionary for you. Isn’t that cool?

Dictionary comprehensions open up a wide spectrum of new possibilities and provide you with a great tool to iterate through and transform dictionaries in Python.

Filtering Items by Their Value: Revisited
To filter items in a dictionary with a comprehension, you just need to add an if clause that defines your filtering condition. Earlier, you worked with the condition value <= 2. You can get the same result with a dictionary comprehension:

>>> numbers = {"one": 1, "two": 2, "three": 3, "four": 4}

>>> {key: value for key, value in numbers.items() if value <= 2}
{'one': 1, 'two': 2}
Now your resulting dictionary contains only the items that satisfy your condition. Compared to the previous section’s solution, this one is more concise and efficient.

Swapping Keys and Values Through Iteration: Revisited
You can also approach the problem of swapping keys and values using a dictionary comprehension. With this tool, you can write a more concise, Pythonic solution that’s also more efficient. Here’s how:

>>> numbers = {"one": 1, "two": 2, "three": 3, "four": 4}

>>> {value: key for key, value in numbers.items()}
{1: 'one', 2: 'two', 3: 'three', 4: 'four'}
With this comprehension, you create a new dictionary where the keys have taken the place of the values and vice versa. This new approach gives you the ability to write more readable, succinct, and efficient code.

Again, the condition for this code to work is the same one you saw before: the values must be hashable objects. Otherwise, you won’t be able to use them as keys for your new dictionary.


Remove ads
Traversing a Dictionary in Sorted and Reverse Order
Sometimes, you may need to iterate through a dictionary in sorted order. You can do this by using the built-in sorted() function. When you call this function with an iterable as an argument, you get a list of items in sorted order.

Note: To dive deeper into sorting Python dictionaries, check out Sorting a Python Dictionary: Values, Keys, and More.

Iterating over a dictionary in reverse order can also be a common requirement in code. In this case, you can use the built-in reversed() function, which takes an iterable as an argument and yields its items in reverse order.

In the following sections, you’ll learn how to use these tools to iterate through a Python dictionary in sorted and reverse order, respectively.

Iterating Over Sorted Keys
If you need to iterate through the keys of a dictionary in sorted order, then you can pass your dictionary as an argument to sorted(). You’ll get a list containing the keys in sorted order. This list will allow you to traverse your dictionary sorted by keys:

>>> incomes = {"apple": 5600.00, "orange": 3500.00, "banana": 5000.00}

>>> for fruit in sorted(incomes):
...     print(fruit, "->", incomes[fruit])
...
apple -> 5600.0
banana -> 5000.0
orange -> 3500.0
In this example, you sort the keys by calling sorted() with your dictionary as an argument. Note that you could’ve also used sorted(incomes.keys()) to get the same result. In both cases, you’ll get a list containing the keys of your dictionary in sorted order.

Note that the sorting order will depend on the data type of your keys and the internal rules that Python uses to sort that specific data type. In this example, Python sorts the keys using its internal rules for sorting strings. These rules are based on the characters’ Unicode code points. A further explanation of these internal rules is out of this tutorial’s scope.

Looping Through Sorted Values
You may also need to iterate through a Python dictionary with its items sorted by values. To do this, you can use sorted() too. This time, you’ll need to use a second argument called key when you call sorted(). This keyword-only argument specifies a one-argument function to extract a comparison key from the items that you’re processing.

To iterate through dictionary items sorted by value, you can write a function that returns the value of each item and then use this function as the key argument to sorted(). In the example below, you do this with a short lambda function:

>>> incomes = {"apple": 5600.00, "orange": 3500.00, "banana": 5000.00}

>>> for fruit, income in sorted(incomes.items(), key=lambda item: item[1]):
...     print(fruit, "->", income)
...
orange -> 3500.0
banana -> 5000.0
apple -> 5600.0
In this example, you define a lambda function and use it to sort the items of incomes by value with sorted(). The lambda function tells sorted() to sort incomes.items() by the second element of each item, item[1], which is the income value.

You may also want to iterate through the values of a dictionary in sorted order without considering the keys. In that case, you can use .values() to provide the augment for sorted(). Here’s a quick example:

>>> for income in sorted(incomes.values()):
...     print(income)
...
3500.0
5000.0
5600.0
Calling sorted() with incomes.values() as an argument returns the values of your dictionary in sorted order. Remember that the keys won’t be accessible if you use .values(). That’s okay. Sometimes, you don’t need the keys, just the values, and this is a quick way to access them.

Sorting a Dictionary With a Comprehension
What if you need to sort an existing dictionary and build a sorted one? As you already know, since Python 3.6, dictionaries remember the insertion order of their items. This feature allows you to sort the items of a dictionary using sorted() while you build a new dictionary with a comprehension:

>>> incomes = {"apple": 5600.00, "orange": 3500.00, "banana": 5000.00}

>>> {fruit: incomes[fruit] for fruit in sorted(incomes)}
{'apple': 5600.0, 'banana': 5000.0, 'orange': 3500.0}

>>> {
...      fruit: income
...      for fruit, income in
...      sorted(incomes.items(), key=lambda item: item[1])
... }
{'orange': 3500.0, 'banana': 5000.0, 'apple': 5600.0}
These comprehensions allow you to create new dictionaries with their items sorted by key and value, respectively. In both cases, the comprehension iterates over the original dictionary in sorted order and builds a new dictionary.


Remove ads
Iterating Through a Dictionary in Reverse-Sorted Order
If you need to traverse your dictionaries in reverse-sorted order, then you can use the reverse argument to sorted(). This argument takes a Boolean value. If you use True, then the items are sorted in reverse order:

>>> incomes = {"apple": 5600.00, "orange": 3500.00, "banana": 5000.00}

>>> for fruit in sorted(incomes, reverse=True):
...     print(fruit, "->", incomes[fruit])
...
orange -> 3500.0
banana -> 5000.0
apple -> 5600.0
In this example, you iterate over the keys of incomes in reverse-sorted order by using the reverse argument to sorted() in the header of your for loop. This example sorts the keys. Why don’t you try writing an example that sorts the values in reverse order?

Traversing a Dictionary in Reverse Order
Another possibility that Python offers when it comes to iterating through dictionaries is to use the built-in reversed() function. This function takes an iterable as an argument and returns an iterator that yields items in reverse order.

Using reversed(), you can traverse your dictionaries in reverse order:

>>> numbers = {"one": 1, "two": 2, "three": 3, "four": 4}

>>> for key, value in reversed(numbers.items()):
...     print(key, "->", value)
...
four -> 4
three -> 3
two -> 2
one -> 1
In this example, the call to reversed() yields items from numbers in reverse order. This enables you to iterate through your dictionary from right to left, which can be useful in some situations.

Iterating Over a Dictionary Destructively With .popitem()
Sometimes you need to iterate through a dictionary and delete its items after use. To accomplish this task, you can use the .popitem() method, which removes and returns key-value pairs from a dictionary in last-in, first-out (LIFO) order. When the target dictionary is empty, then .popitem() raises a KeyError exception.

If you need to destructively iterate through a dictionary in Python, then .popitem() can do the trick for you:

>>> likes = {"color": "blue", "fruit": "apple", "pet": "dog"}

>>> while True:
...     try:
...         print(f"Dictionary length: {len(likes)}")
...         item = likes.popitem()
...         # Do something with the item here...
...         print(f"Item {item} removed")
...     except KeyError:
...         print("Your dictionary is now empty.")
...         break
...
Dictionary length: 3
Item ('pet', 'dog') removed
Dictionary length: 2
Item ('fruit', 'apple') removed
Dictionary length: 1
Item ('color', 'blue') removed
Dictionary length: 0
Your dictionary is now empty.
Here, you used a while loop instead of a for loop. The reason for this is that it’s not safe to iterate through a dictionary with a for loop when you need to remove items from the dictionary at hand. You continue this until the dictionary becomes empty, and .popitem() raises the KeyError exception.

Instead of relying on exception handling, you can condition your while loop on the dictionary having elements left:

>>> likes = {"color": "blue", "fruit": "apple", "pet": "dog"}
⏎
>>> while likes:
...     print(f"Dictionary length: {len(likes)}")
...     item = likes.popitem()
...     # Do something with the item here ...
...     print(f"Item {item} removed")
...
Dictionary length: 3
Item ('pet', 'dog') removed
Dictionary length: 2
Item ('fruit', 'apple') removed
Dictionary length: 1
Item ('color', 'blue') removed
The variable item keeps a reference to the current item so that you can perform actions with it in every iteration. The loop breaks out when the dictionary becomes empty, and likes becomes falsy. The difference between these two examples can be summed up as LBYL vs EAFP or, more explicitly, look before you leap or easier to ask forgiveness than permission.

Using Built-in Functions to Implicitly Iterate Through Dictionaries
Python provides some built-in functions that are useful when you’re working with collections like dictionaries. These functions are a sort of iteration tool because they implement an internal loop. Because of their internal loop, you can use these functions to iterate through a dictionary implicitly.

In the following sections, you’ll explore two of these functions: map() and filter(). With map(), you can apply a given transformation to all the items in a dictionary and build a new one. With filter(), you can extract the desired items into a new dictionary.


Remove ads
Applying a Transformation to a Dictionary’s Items: map()
Python’s map() function takes a function object and an iterable as arguments. It returns an iterator that results from applying the input function to every item in the input iterable. You can use map() to iterate through dictionaries in Python by taking advantage of the function’s implicit loop.

Say you want to apply a price discount to all the products in your fruits dictionary. In this case, you can define a function that manages the discount and then use that function as the first argument to map(). Then you can use .items() to provide the iterable object:

>>> fruits = {"apple": 0.40, "orange": 0.35, "banana": 0.25}

>>> def apply_discount(product, discount=0.05):
...     return product[0], round(product[1] * (1 - discount), 2)
...

>>> dict(map(apply_discount, fruits.items()))
{'apple': 0.38, 'orange': 0.33, 'banana': 0.24}

>>> dict(map(lambda item: apply_discount(item, 0.1), fruits.items()))
{'apple': 0.34, 'orange': 0.3, 'banana': 0.22}

>>> dict(map(lambda item: apply_discount(item, 0.15), fruits.items()))
{'apple': 0.32, 'orange': 0.28, 'banana': 0.2}
In this code snippet, you define a function named apply_discount(), which applies a discount to the price of a given product. Then it returns a tuple containing the product and its new price.

The first call to map() iterates through the items of the dictionary, fruits.items(), and applies the default 5 percent discount to each fruit. In this case, you use the dict() constructor to generate a new dictionary from the data that map() returns.

In the second and third calls to map(), you wrap apply_discount() in a lambda function so that you can provide a different discount value to apply_discount(). This is a common technique that you can use when a tool like map() requires a function with a given number of arguments and your target function doesn’t match that number.

Filtering Items in a Dictionary: filter()
The built-in filter() function is another tool that you can use to implicitly iterate through a dictionary and filter its items according to a given condition. This tool also takes a function object and an iterable as arguments. It returns an iterator from those elements of the input iterable for which the function returns True.

Say that you want to extract the products with a price lower than 0.40 from your fruits dictionary. To do this, you can define a function to determine if the price satisfies that condition and pass the function as the first argument to filter(). Again, the second argument can be fruits.items(). Here’s the code to achieve this:

>>> fruits = {"apple": 0.40, "orange": 0.35, "banana": 0.25}

>>> def has_low_price(item, price=0.4):
...     return item[1] < price
...

>>> dict(filter(has_low_price, fruits.items()))
{'orange': 0.35, 'banana': 0.25}
You iterate through the items of fruits with filter(). The has_low_price() function compares the item’s price with a target price and returns True if the item’s price is less than the target. Otherwise, it returns False. As a result, you get only the items whose price is lower than the target.

To provide a different target price, you can use a lambda function as you did in the previous section. Go ahead and give it a try.

Traversing Multiple Dictionaries as One
The collections and itertools modules from the Python standard library provide a couple of useful tools that allow you to iterate through multiple dictionaries in one go.

In collections, you’ll find the ChainMap class, which allows you to create a dictionary-like object by combining multiple existing dictionaries. With ChainMap, you can iterate through several dictionaries as if they were a single one.

In itertools, you’ll find a function called chain() that allows you to iterate over multiple Python dictionaries one at a time.

In the following sections, you’ll learn how to use these two tools for iterating over multiple dictionaries in a single loop. You’ll also learn how both tools differ from each other.

Iterating Through Multiple Dictionaries With ChainMap
The collections module from the standard library provides a specialized container type called ChainMap. It’s a dictionary-like class that you can use to create a single, updateable view out of multiple existing dictionaries. The resulting object will logically appear and behave as a single dictionary.

ChainMap doesn’t merge the input dictionaries together. Instead, it keeps them in an internal list. The input dictionaries can have duplicate keys. However, only the first instance of a duplicated key will be accessible in lookup and update operations.

Now, suppose you have two dictionaries containing different categories of products and their prices. You need to iterate through them together as one dictionary. To achieve this, you can create a ChainMap object and initialize it with your dictionaries:

>>> from collections import ChainMap

>>> fruits = {"apple": 0.40, "orange": 0.35}
>>> vegetables = {"pepper": 0.20, "onion": 0.55}

>>> catalog = ChainMap(fruits, vegetables)
>>> catalog
ChainMap({'apple': 0.4, 'orange': 0.35}, {'pepper': 0.2, 'onion': 0.55})

>>> for product, price in catalog.items():
...     print(product, "->", price)
...
pepper -> 0.2
onion -> 0.55
apple -> 0.4
orange -> 0.35
After importing ChainMap from collections, you need to create a ChainMap object with the dictionaries that you want to chain. Then you can freely iterate through the resulting object as you would do with a regular dictionary.

ChainMap objects have the same interface as regular dictionaries, so you can use .keys(), values(), and .items() to iterate through their different components.

When using ChainMap to iterate over multiple dictionaries in one go, you must keep in mind that if you have duplicate keys, then you’ll only be able to access the first instance of them. Consider the following example:

>>> from collections import ChainMap

>>> for_adoption = {"dogs": 10, "cats": 7, "pythons": 3}
>>> vet_treatment = {"dogs": 4, "cats": 3, "turtles": 1}
>>> pets = ChainMap(for_adoption, vet_treatment)

>>> for pet, count in pets.items():
...     print(pet, "->", count)
...
...
dogs -> 10
cats -> 7
turtles -> 1
pythons -> 3
In this example, the loop only went through the first instances of "dogs" and "cats". Therefore, you don’t get data from the duplicate instances of these keys.


Remove ads
Iterating Through a Chain of Dictionaries With chain()
The itertools module provides the chain() function, which can take multiple iterable objects as arguments and make an iterator that yields elements from all of them. To do its job, chain() starts yielding items from the first iterable until exhaustion, then the function yields items from the next iterable, and so on until all the input iterable objects are exhausted.

This behavior allows you to iterate through multiple dictionaries in a chain that goes through all the keys, even if there are repeated ones:

>>> from itertools import chain

>>> for_adoption = {"dogs": 10, "cats": 7, "pythons": 3}
>>> vet_treatment = {"dogs": 4, "cats": 3, "turtles": 1}
>>> pets = chain(for_adoption.items(), vet_treatment.items())

>>> for pet, count in pets:
...     print(pet, "->", count)
...
...
dogs -> 10
cats -> 7
pythons -> 3
dogs -> 4
cats -> 3
turtles -> 1
In the above code, chain() returns an iterator that yields items from for_adoption and vet_treatment. Note that unlike ChainMap, the chain() function gives you access to all the keys from your input dictionaries, even the duplicated ones.

Looping Over Merged Dictionaries: The Unpacking Operator (**)
Python 3.5 introduced an unpacking generalization that allows you to use the new dictionary unpacking operator (**) to merge multiple dictionaries into one. This feature allows you to iterate through multiple dictionaries in one go:

>>> fruits = {"apple": 0.40, "orange": 0.35}
>>> vegetables = {"pepper": 0.20, "onion": 0.55}

>>> for product, price in {**fruits, **vegetables}.items():
...     print(product, "->", price)
...
apple -> 0.4
orange -> 0.35
pepper -> 0.2
onion -> 0.55
The dictionary unpacking operator (**) is an awesome feature in Python. It allows you to merge multiple dictionaries into a new one, as you did in the example above. Once you’ve merged the dictionaries, you can iterate through the new dictionary as usual.

It’s important to note that if the dictionaries that you’re merging have repeated or duplicate keys, then the values of the rightmost dictionary will prevail:

>>> for_adoption = {"dogs": 10, "cats": 7, "pythons": 3}
>>> vet_treatment = {"dogs": 4, "cats": 3, "turtles": 1}

>>> for pet, count in {**for_adoption, **vet_treatment}.items():
...     print(pet, "->", count)
...
dogs -> 4
cats -> 3
pythons -> 3
turtles -> 1
In this example, instead of having access to the first instances of the duplicate keys, "dogs" and "cats", you get the second instances. This behavior makes sense because the first unpacking operator creates those keys, and the second unpacking updates their values, overriding them.

