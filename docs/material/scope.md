The concept of scope rules how variables and names are looked up in your code. It determines the visibility of a variable within the code. The scope of a name or variable depends on the place in your code where you create that variable. The Python scope concept is generally presented using a rule known as the LEGB rule.

The letters in the acronym LEGB stand for Local, Enclosing, Global, and Built-in scopes. This summarizes not only the Python scope levels but also the sequence of steps that Python follows when resolving names in a program.

In this tutorial, you’ll learn:

What scopes are and how they work in Python
Why it’s important to know about Python scope
What the LEGB rule is and how Python uses it to resolve names
How to modify the standard behavior of Python scope using global and nonlocal
What scope-related tools Python offers and how you can use them
With this knowledge at hand, you can take advantage of Python scopes to write more reliable and maintainable programs. Using Python scope will help you avoid or minimize bugs related to name collision as well as bad use of global names across your programs.

You’ll get the most out of this tutorial if you’re familiar with intermediate Python concepts like classes, functions, inner functions, variables, exceptions, comprehensions, built-in functions, and standard data structures.

Free Bonus: 5 Thoughts On Python Mastery, a free course for Python developers that shows you the roadmap and the mindset you’ll need to take your Python skills to the next level.

Understanding Scope
In programming, the scope of a name defines the area of a program in which you can unambiguously access that name, such as variables, functions, objects, and so on. A name will only be visible to and accessible by the code in its scope. Several programming languages take advantage of scope for avoiding name collisions and unpredictable behaviors. Most commonly, you’ll distinguish two general scopes:

Global scope: The names that you define in this scope are available to all your code.

Local scope: The names that you define in this scope are only available or visible to the code within the scope.

Scope came about because early programming languages (like BASIC) only had global names. With this kind of name, any part of the program could modify any variable at any time, so maintaining and debugging large programs could become a real nightmare. To work with global names, you’d need to keep all the code in mind at the same time to know what the value of a given name is at any time. This was an important side-effect of not having scopes.

Some languages like Python use scope to avoid this kind of problem. When you use a language that implements scope, there’s no way for you to access all the variables in a program at all locations in that program. In this case, your ability to access a given name will depend on where you’ve defined that name.

Note: You’ll be using the term name to refer to the identifiers of variables, constants, functions, classes, or any other object that can be assigned a name.

The names in your programs will have the scope of the block of code in which you define them. When you can access the value of a given name from someplace in your code, you’ll say that the name is in scope. If you can’t access the name, then you’ll say that the name is out of scope.


Remove ads
Names and Scopes in Python
Since Python is a dynamically-typed language, variables in Python come into existence when you first assign them a value. On the other hand, functions and classes are available after you define them using def or class, respectively. Finally, modules exist after you import them. As a summary, you can create Python names through one of the following operations:

Operation	Statement
Assignments	x = value
Import operations	import module or from module import name
Function definitions	def my_func(): ...
Argument definitions in the context of functions	def my_func(arg1, arg2,... argN): ...
Class definitions	class MyClass: ...
All these operations create or, in the case of assignments, update new Python names because all of them assign a name to a variable, constant, function, class, instance, module, or other Python object.

Note: There’s an important difference between assignment operations and reference or access operations. When you reference a name, you’re just retrieving its content or value. When you assign a name, you’re either creating that name or modifying it.

Python uses the location of the name assignment or definition to associate it with a particular scope. In other words, where you assign or define a name in your code determines the scope or visibility of that name.

For example, if you assign a value to a name inside a function, then that name will have a local Python scope. In contrast, if you assign a value to a name outside of all functions—say, at the top level of a module—then that name will have a global Python scope.

Python Scope vs Namespace
In Python, the concept of scope is closely related to the concept of the namespace. As you’ve learned so far, a Python scope determines where in your program a name is visible. Python scopes are implemented as dictionaries that map names to objects. These dictionaries are commonly called namespaces. These are the concrete mechanisms that Python uses to store names. They’re stored in a special attribute called .__dict__.

Names at the top level of a module are stored in the module’s namespace. In other words, they’re stored in the module’s .__dict__ attribute. Take a look at the following code:

>>> import sys
>>> sys.__dict__.keys()
dict_keys(['__name__', '__doc__', '__package__',..., 'argv', 'ps1', 'ps2'])
After you import sys, you can use .keys() to inspect the keys of sys.__dict__. This returns a list with all the names defined at the top level of the module. In this case, you can say that .__dict__ holds the namespace of sys and is a concrete representation of the module scope.

Note: The output of some of the examples in this tutorial has been abbreviated (...) to save space. The output may vary based on your platform, Python version, or even on how long you’ve been using your current Python interactive session.

As a further example, suppose that you need to use the name ps1, which is defined in sys. If you know how .__dict__ and namespaces work in Python, then you can reference ps1 in at least two different ways:

Using the dot notation on the module’s name in the form module.name
Using a subscription operation on .__dict__ in the form module.__dict__['name']
Take a look at the following code:

>>> sys.ps1
'>>> '
>>> sys.__dict__['ps1']
'>>> '
Once you’ve imported sys you can access ps1 using the dot notation on sys. You can also access ps1 using a dictionary key lookup with the key 'ps1'. Both actions return the same result, '>>> '.

Note: ps1 is a string specifying the primary prompt of the Python interpreter. ps1 is only defined if the interpreter is in interactive mode and its initial value is '>>> '.

Whenever you use a name, such as a variable or a function name, Python searches through different scope levels (or namespaces) to determine whether the name exists or not. If the name exists, then you’ll always get the first occurrence of it. Otherwise, you’ll get an error. You’ll cover this search mechanism in the next section.


Remove ads
Using the LEGB Rule for Python Scope
Python resolves names using the so-called LEGB rule, which is named after the Python scope for names. The letters in LEGB stand for Local, Enclosing, Global, and Built-in. Here’s a quick overview of what these terms mean:

Local (or function) scope is the code block or body of any Python function or lambda expression. This Python scope contains the names that you define inside the function. These names will only be visible from the code of the function. It’s created at function call, not at function definition, so you’ll have as many different local scopes as function calls. This is true even if you call the same function multiple times, or recursively. Each call will result in a new local scope being created.

Enclosing (or nonlocal) scope is a special scope that only exists for nested functions. If the local scope is an inner or nested function, then the enclosing scope is the scope of the outer or enclosing function. This scope contains the names that you define in the enclosing function. The names in the enclosing scope are visible from the code of the inner and enclosing functions.

Global (or module) scope is the top-most scope in a Python program, script, or module. This Python scope contains all of the names that you define at the top level of a program or a module. Names in this Python scope are visible from everywhere in your code.

Built-in scope is a special Python scope that’s created or loaded whenever you run a script or open an interactive session. This scope contains names such as keywords, functions, exceptions, and other attributes that are built into Python. Names in this Python scope are also available from everywhere in your code. It’s automatically loaded by Python when you run a program or script.

The LEGB rule is a kind of name lookup procedure, which determines the order in which Python looks up names. For example, if you reference a given name, then Python will look that name up sequentially in the local, enclosing, global, and built-in scope. If the name exists, then you’ll get the first occurrence of it. Otherwise, you’ll get an error.

Note: Notice that the local and enclosing Python scopes are searched only if you use a name inside a function (local scope) or a nested or inner function (local and enclosing scope).

In summary, when you use nested functions, names are resolved by first checking the local scope or the innermost function’s local scope. Then, Python looks at all enclosing scopes of outer functions from the innermost scope to the outermost scope. If no match is found, then Python looks at the global and built-in scopes. If it can’t find the name, then you’ll get an error.

At any given time during execution, you’ll have at most four active Python scopes—local, enclosing, global, and built-in—depending on where you are in the code. On the other hand, you’ll always have at least two active scopes, which are the global and built-in scopes. These two scopes will always be available for you.

Functions: The Local Scope
The local scope or function scope is a Python scope created at function calls. Every time you call a function, you’re also creating a new local scope. On the other hand, you can think of each def statement and lambda expression as a blueprint for new local scopes. These local scopes will come into existence whenever you call the function at hand.

By default, parameters and names that you assign inside a function exist only within the function or local scope associated with the function call. When the function returns, the local scope is destroyed and the names are forgotten. Here’s how this works:

>>> def square(base):
...     result = base ** 2
...     print(f'The square of {base} is: {result}')
...
>>> square(10)
The square of 10 is: 100
>>> result  # Isn't accessible from outside square()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    result
NameError: name 'result' is not defined
>>> base  # Isn't accessible from outside square()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    base
NameError: name 'base' is not defined
>>> square(20)
The square of 20 is: 400
square() is a function that computes the square of a given number, base. When you call the function, Python creates a local scope containing the names base (an argument) and result (a local variable). After the first call to square(), base holds a value of 10 and result holds a value of 100. The second time, the local names will not remember the values that were stored in them the first time the function was called. Notice that base now holds the value 20 and result holds 400.

Note: If you try to access result or base after the function call, then you get a NameError, because these only exist in the local scope created by the call to square(). Whenever you try to access a name that isn’t defined in any Python scope, you’ll get a NameError. The error message will include the name that couldn’t be found.

Since you can’t access local names from statements that are outside the function, different functions can define objects with the same name. Check out this example:

>>> def cube(base):
...     result = base ** 3
...     print(f'The cube of {base} is: {result}')
...
>>> cube(30)
The cube of 30 is: 27000
Notice that you define cube() using the same variable and parameter that you used in square(). However, since cube() can’t see the names inside the local scope of square() and vice versa, both functions work as expected without any name collision.

You can avoid name collisions in your programs by properly using the local Python scope. This also makes functions more self-contained and creates maintainable program units. Additionally, since you can’t change local names from remote places in your code, your programs will be easier to debug, read, and modify.

You can inspect the names and parameters of a function using .__code__, which is an attribute that holds information on the function’s internal code. Take a look at the code below:

>>> square.__code__.co_varnames
('base', 'result')
>>> square.__code__.co_argcount
1
>>> square.__code__.co_consts
(None, 2, 'The square of ', ' is: ')
>>> square.__code__.co_name
'square'
In this code example, you inspect .__code__ on square(). This is a special attribute that holds information about the code of a Python function. In this case, you see that .co_varnames holds a tuple containing the names that you define inside square().


Remove ads
Nested Functions: The Enclosing Scope
Enclosing or nonlocal scope is observed when you nest functions inside other functions. The enclosing scope was added in Python 2.2. It takes the form of the local scope of any enclosing function’s local scopes. Names that you define in the enclosing Python scope are commonly known as nonlocal names. Consider the following code:

>>> def outer_func():
...     # This block is the Local scope of outer_func()
...     var = 100  # A nonlocal var
...     # It's also the enclosing scope of inner_func()
...     def inner_func():
...         # This block is the Local scope of inner_func()
...         print(f"Printing var from inner_func(): {var}")
...
...     inner_func()
...     print(f"Printing var from outer_func(): {var}")
...
>>> outer_func()
Printing var from inner_func(): 100
Printing var from outer_func(): 100
>>> inner_func()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'inner_func' is not defined
When you call outer_func(), you’re also creating a local scope. The local scope of outer_func() is, at the same time, the enclosing scope of inner_func(). From inside inner_func(), this scope is neither the global scope nor the local scope. It’s a special scope that lies in between those two scopes and is known as the enclosing scope.

Note: In a sense, inner_func() is a temporary function that comes to life only during the execution of its enclosing function, outer_func(). Note that inner_func() is only visible to the code in outer_func().

All the names that you create in the enclosing scope are visible from inside inner_func(), except for those created after you call inner_func(). Here’s a new version of outer_fun() that shows this point:

>>> def outer_func():
...     var = 100
...     def inner_func():
...         print(f"Printing var from inner_func(): {var}")
...         print(f"Printing another_var from inner_func(): {another_var}")
...
...     inner_func()
...     another_var = 200  # This is defined after calling inner_func()
...     print(f"Printing var from outer_func(): {var}")
...
>>> outer_func()
Printing var from inner_func(): 100
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    outer_func()
  File "<stdin>", line 7, in outer_func
    inner_func()
  File "<stdin>", line 5, in inner_func
    print(f"Printing another_var from inner_func(): {another_var}")
NameError: free variable 'another_var' referenced before assignment in enclosing
 scope
When you call outer_func() the code runs down to the point in which you call inner_func(). The last statement of inner_func() tries to access another_var. At this point, another_var isn’t defined yet, so Python raises a NameError because it can’t find the name that you’re trying to use.

Last but not least, you can’t modify names in the enclosing scope from inside a nested function unless you declare them as nonlocal in the nested function. You’ll cover how to use nonlocal later in this tutorial.

Modules: The Global Scope
From the moment you start a Python program, you’re in the global Python scope. Internally, Python turns your program’s main script into a module called __main__ to hold the main program’s execution. The namespace of this module is the main global scope of your program.

Note: In Python, the notions of global scope and global names are tightly associated with module files. For example, if you define a name at the top level of any Python module, then that name is considered global to the module. That’s the reason why this kind of scope is also called module scope.

If you’re working in a Python interactive session, then you’ll notice that '__main__' is also the name of its main module. To check that out, open an interactive session and type in the following:

>>> __name__
'__main__'
Whenever you run a Python program or an interactive session like in the above code, the interpreter executes the code in the module or script that serves as an entry point to your program. This module or script is loaded with the special name, __main__. From this point on, you can say that your main global scope is the scope of __main__.

To inspect the names within your main global scope, you can use dir(). If you call dir() without arguments, then you’ll get the list of names that live in your current global scope. Take a look at this code:

>>> dir()
['__annotations__', '__builtins__',..., '__package__', '__spec__']
>>> var = 100  # Assign var at the top level of __main__
>>> dir()
['__annotations__', '__builtins__',..., '__package__', '__spec__', 'var']
When you call dir() with no arguments, you get the list of names available in your main global Python scope. Note that if you assign a new name (like var here) at the top level of the module (which is __main__ here), then that name will be added to the list returned by dir().

Note: You’ll cover dir() in more detail later on in this tutorial.

There’s only one global Python scope per program execution. This scope remains in existence until the program terminates and all its names are forgotten. Otherwise, the next time you were to run the program, the names would remember their values from the previous run.

You can access or reference the value of any global name from any place in your code. This includes functions and classes. Here’s an example that clarifies these points:

>>> var = 100
>>> def func():
...     return var  # You can access var from inside func()
...
>>> func()
100
>>> var  # Remains unchanged
100
Inside func(), you can freely access or reference the value of var. This has no effect on your global name var, but it shows you that var can be freely accessed from within func(). On the other hand, you can’t assign global names inside functions unless you explicitly declare them as global names using a global statement, which you’ll see later on.

Whenever you assign a value to a name in Python, one of two things can happen:

You create a new name
You update an existing name
The concrete behavior will depend on the Python scope in which you’re assigning the name. If you try to assign a value to a global name inside a function, then you’ll be creating that name in the function’s local scope, shadowing or overriding the global name. This means that you won’t be able to change most variables that have been defined outside the function from within the function.

If you follow this logic, then you’ll realize that the following code won’t work as you might expect:

>>> var = 100  # A global variable
>>> def increment():
...     var = var + 1  # Try to update a global variable
...
>>> increment()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    increment()
  File "<stdin>", line 2, in increment
    var = var + 1
UnboundLocalError: local variable 'var' referenced before assignment
Within increment(), you try to increment the global variable, var. Since var isn’t declared global inside increment(), Python creates a new local variable with the same name, var, inside the function. In the process, Python realizes that you’re trying to use the local var before its first assignment (var + 1), so it raises an UnboundLocalError.

Here’s another example:

>>> var = 100  # A global variable
>>> def func():
...     print(var)  # Reference the global variable, var
...     var = 200   # Define a new local variable using the same name, var
...
>>> func()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    func()
  File "<stdin>", line 2, in func
    print(var)
UnboundLocalError: local variable 'var' referenced before assignment
You likely expect to be able to print the global var and be able to update var later, but again you get an UnboundLocalError. What happens here is that when you run the body of func(), Python decides that var is a local variable because it’s assigned within the function scope. This isn’t a bug, but a design choice. Python assumes that names assigned in the body of a function are local to that function.

Note: Global names can be updated or modified from any place in your global Python scope. Beyond that, the global statement can be used to modify global names from almost any place in your code, as you’ll see in The global Statement.

Modifying global names is generally considered bad programming practice because it can lead to code that is:

Difficult to debug: Almost any statement in the program can change the value of a global name.
Hard to understand: You need to be aware of all the statements that access and modify global names.
Impossible to reuse: The code is dependent on global names that are specific to a concrete program.
Good programming practice recommends using local names rather than global names. Here are some tips:

Write self-contained functions that rely on local names rather than global ones.
Try to use unique objects names, no matter what scope you’re in.
Avoid global name modifications throughout your programs.
Avoid cross-module name modifications.
Use global names as constants that don’t change during your program’s execution.
Up to this point, you’ve covered three Python scopes. Check out the following example for a summary on where they’re located in your code and how Python looks up names through them:

>>> # This area is the global or module scope
>>> number = 100
>>> def outer_func():
...     # This block is the local scope of outer_func()
...     # It's also the enclosing scope of inner_func()
...     def inner_func():
...         # This block is the local scope of inner_func()
...         print(number)
...
...     inner_func()
...
>>> outer_func()
100
When you call outer_func(), you get 100 printed on your screen. But how does Python look up the name number in this case? Following the LEGB rule, you’ll look up number in the following places:

Inside inner_func(): This is the local scope, but number doesn’t exist there.
Inside outer_func(): This is the enclosing scope, but number isn’t defined there either.
In the module scope: This is the global scope, and you find number there, so you can print number to the screen.
If number isn’t defined inside the global scope, then Python continues the search by looking at the built-in scope. This is the last component of the LEGB rule, as you’ll see in the next section.


Remove ads
builtins: The Built-In Scope
The built-in scope is a special Python scope that’s implemented as a standard library module named builtins in Python 3.x. All of Python’s built-in objects live in this module. They’re automatically loaded to the built-in scope when you run the Python interpreter. Python searches builtins last in its LEGB lookup, so you get all the names it defines for free. This means that you can use them without importing any module.

Notice that the names in builtins are always loaded into your global Python scope with the special name __builtins__, as you can see in the following code:

>>> dir()
['__annotations__', '__builtins__',..., '__package__', '__spec__']
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError',..., 'tuple', 'type', 'vars', 'zip']
In the output of the first call to dir(), you can see that __builtins__ is always present in the global Python scope. If you inspect __builtins__ itself using dir(), then you’ll get the whole list of Python built-in names.

The built-in scope brings more than 150 names to your current global Python scope. For example, in Python 3.8 you can get to know the exact number of names as follows:

>>> len(dir(__builtins__))
152
With the call to len(), you get the number of items in the list returned by dir(). This returns 152 names that include exceptions, functions, types, special attributes, and other Python built-in objects.

Even though you can access all of these Python built-in objects for free (without importing anything), you can also explicitly import builtins and access the names using the dot notation. Here’s how this works:

>>> import builtins  # Import builtins as a regular module
>>> dir(builtins)
['ArithmeticError', 'AssertionError',..., 'tuple', 'type', 'vars', 'zip']
>>> builtins.sum([1, 2, 3, 4, 5])
15
>>> builtins.max([1, 5, 8, 7, 3])
8
>>> builtins.sorted([1, 5, 8, 7, 3])
[1, 3, 5, 7, 8]
>>> builtins.pow(10, 2)
100
You can import builtins as you would any other Python module. From this point on, you can access all the names in builtins by using the dotted attribute lookup or fully-qualified names. This can be quite useful if you want to make sure that you won’t have a name collision if any of your global names override any built-in name.

You can override or redefine any built-in name in your global scope. If you do so, then keep in mind that this will affect all your code. Take a look at the following example:

>>> abs(-15)  # Standard use of a built-in function
15
>>> abs = 20  # Redefine a built-in name in the global scope
>>> abs(-15)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable
If you override or re-assign abs, then the original built-in abs() is affected all over your code. Now, suppose that you need to call the original abs() and you forget that you re-assigned the name. In this case, when you call abs() again, you’d get a TypeError because abs now holds a reference to an integer, which is not callable.

Note: Accidentally or inadvertently overriding or redefining built-in names in your global scope can be a source of dangerous and hard-to-find bugs. It’s better to try and avoid this kind of practice.

If you’re experimenting with some code and you accidentally re-assign a built-in name at the interactive prompt, then you can either restart your session or run del name to remove the redefinition from your global Python scope. This way, you’re restoring the original name in the built-in scope. If you revisit the example of abs(), then you can do something like this:

>>> del abs  # Remove the redefined abs from your global scope
>>> abs(-15)  # Restore the original abs()
15
When you delete the custom abs name, you’re removing the name from your global scope. This allows you to access the original abs() in the built-in scope again.

To work around this kind of situation, you can explicitly import builtins and then use fully-qualified names, like in the following code fragment:

>>> import builtins
>>> builtins.abs(-15)
15
Once you explicitly import builtins, you have the module name available in your global Python scope. From this point on, you can use fully-qualified names to unambiguously get the names you need from builtins, just like you did with builtins.abs() in the above example.

As a quick summary, some of the implications of Python scope are shown in the following table:

Action	Global Code	Local Code	Nested Function Code
Access or reference names that live in the global scope	Yes	Yes	Yes
Modify or update names that live in the global scope	Yes	No (unless declared global)	No (unless declared global)
Access or reference names that live in a local scope	No	Yes (its own local scope), No (other local scope)	Yes (its own local scope), No (other local scope)
Override names in the built-in scope	Yes	Yes (during function execution)	Yes (during function execution)
Access or reference names that live in their enclosing scope	N/A	N/A	Yes
Modify or update names that live in their enclosing scope	N/A	N/A	No (unless declared nonlocal)
Additionally, code in different scopes can use the same name for different objects. This way, you can use a local variable named spam and also a global variable with the same name, spam. However, this is considered bad programming practice.


Remove ads
Modifying the Behavior of a Python Scope
So far, you’ve learned how a Python scope works and how they restrict the visibility of variables, functions, classes, and other Python objects to certain portions of your code. You now know that you can access or reference global names from any place in your code, but they can be modified or updated from within the global Python scope.

You also know that you can access local names only from inside the local Python scope they were created in or from inside a nested function, but you can’t access them from the global Python scope or from other local scopes. Additionally, you’ve learned that nonlocal names can be accessed from inside nested functions, but they can’t be modified or updated from there.

Even though Python scopes follow these general rules by default, there are ways to modify this standard behavior. Python provides two keywords that allow you to modify the content of global and nonlocal names. These two keywords are:

global
nonlocal
In the next two sections, you’ll cover how to use these Python keywords to modify the standard behavior of Python scopes.

The global Statement
You already know that when you try to assign a value to a global name inside a function, you create a new local name in the function scope. To modify this behavior, you can use a global statement. With this statement, you can define a list of names that are going to be treated as global names.

The statement consists of the global keyword followed by one or more names separated by commas. You can also use multiple global statements with a name (or a list of names). All the names that you list in a global statement will be mapped to the global or module scope in which you define them.

Here’s an example where you try to update a global variable from within a function:

>>> counter = 0  # A global name
>>> def update_counter():
...     counter = counter + 1  # Fail trying to update counter
...
>>> update_counter()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in update_counter
UnboundLocalError: local variable 'counter' referenced before assignment
When you try to assign counter inside update_counter(), Python assumes that counter is local to update_counter() and raises an UnboundLocalError because you’re trying to access a name that isn’t defined yet.

If you want this code to work the way you expect here, then you can use a global statement as follows:

>>> counter = 0  # A global name
>>> def update_counter():
...     global counter  # Declare counter as global
...     counter = counter + 1  # Successfully update the counter
...
>>> update_counter()
>>> counter
1
>>> update_counter()
>>> counter
2
>>> update_counter()
>>> counter
3
In this new version of update_counter(), you add the statement global counter to the body of the function right before you try to change counter. With this tiny change, you’re mapping the name counter in the function scope to the same name in the global or module scope. From this point on, you can freely modify counter inside update_counter(). All the changes will reflect in the global variable.

With the statement global counter, you’re telling Python to look in the global scope for the name counter. This way, the expression counter = counter + 1 doesn’t create a new name in the function scope, but updates it in the global scope.

Note: The use of global is considered bad practice in general. If you find yourself using global to fix problems like the one above, then stop and think if there is a better way to write your code.

For example, you can try to write a self-contained function that relies on local names rather than on global names as follows:

>>> global_counter = 0  # A global name
>>> def update_counter(counter):
...     return counter + 1  # Rely on a local name
...
>>> global_counter = update_counter(global_counter)
>>> global_counter
1
>>> global_counter = update_counter(global_counter)
>>> global_counter
2
>>> global_counter = update_counter(global_counter)
>>> global_counter
3
This implementation of update_counter() defines counter as a parameter and returns its value augmented by 1 unit every time the function is called. This way, the result of update_counter() depends on the counter you use as an input and not on the changes that other functions (or pieces of code) can perform on the global variable, global_counter.

You can also use a global statement to create lazy global names by declaring them inside a function. Take a look at the following code:

>>> def create_lazy_name():
...     global lazy  # Create a global name, lazy
...     lazy = 100
...     return lazy
...
>>> create_lazy_name()
100
>>> lazy  # The name is now available in the global scope
100
>>> dir()
['__annotations__', '__builtins__',..., 'create_lazy_name', 'lazy']
When you call create_lazy_name(), you’re also creating a global variable called lazy. Notice that after calling the function, the name lazy is available in the global Python scope. If you inspect the global namespace using dir(), then you’ll see that lazy appears last in the list.

Note: Even though you can use a global statement to create lazy global names, this can be a dangerous practice that can lead to buggy code. So, it’s best to avoid things like this in your code.

For example, suppose you’re trying to get access to one of those lazy names and, for some reason, your code hasn’t called the function that creates that name yet. In this case, you’ll get a NameError and your program will crash.

Finally, it’s worth noting that you can use global from inside any function or nested function and the names listed will always be mapped to names in the global Python scope.

Also notice that, even though using a global statement at the top level of a module is legal, it doesn’t make much sense because any name assigned in the global scope is already a global name by definition. Take a look at the following code:

>>> name = 100
>>> dir()
['__annotations__', '__builtins__',..., '__spec__', 'name']
>>> global name
>>> dir()
['__annotations__', '__builtins__',..., '__spec__', 'name']
The use of a global statement like global name doesn’t change anything in your current global scope, as you can see in the output of dir(). The variable name is a global variable whether you use global or not.


Remove ads
The nonlocal Statement
Similarly to global names, nonlocal names can be accessed from inner functions, but not assigned or updated. If you want to modify them, then you need to use a nonlocal statement. With a nonlocal statement, you can define a list of names that are going to be treated as nonlocal.

The nonlocal statement consists of the nonlocal keyword followed by one or more names separated by commas. These names will refer to the same names in the enclosing Python scope. The following example shows how you can use nonlocal to modify a variable defined in the enclosing or nonlocal scope:

>>> def func():
...     var = 100  # A nonlocal variable
...     def nested():
...         nonlocal var  # Declare var as nonlocal
...         var += 100
...
...     nested()
...     print(var)
...
>>> func()
200
With the statement nonlocal var, you tell Python that you’ll be modifying var inside nested(). Then, you increment var using an augmented assignment operation. This change is reflected in the nonlocal name var, which now has a value of 200.

Unlike global, you can’t use nonlocal outside of a nested or enclosed function. To be more precise, you can’t use a nonlocal statement in either the global scope or in a local scope. Here’s an example:

>>> nonlocal my_var  # Try to use nonlocal in the global scope
  File "<stdin>", line 1
SyntaxError: nonlocal declaration not allowed at module level
>>> def func():
...     nonlocal var  # Try to use nonlocal in a local scope
...     print(var)
...
  File "<stdin>", line 2
SyntaxError: no binding for nonlocal 'var' found
Here, you first try to use a nonlocal statement in the global Python scope. Since nonlocal only works inside an inner or nested function, you get a SyntaxError telling you that you can’t use nonlocal in a module scope. Notice that nonlocal doesn’t work inside a local scope either.

Note: For more detailed information on the nonlocal statement, check out PEP 3104 — Access to Names in Outer Scopes.

In contrast to global, you can’t use nonlocal to create lazy nonlocal names. Names must already exist in the enclosing Python scope if you want to use them as nonlocal names. This means that you can’t create nonlocal names by declaring them in a nonlocal statement in a nested function. Take a look at the following code example:

>>> def func():
...     def nested():
...         nonlocal lazy_var  # Try to create a nonlocal lazy name
...
  File "<stdin>", line 3
SyntaxError: no binding for nonlocal 'lazy_var' found
In this example, when you try to define a nonlocal name using nonlocal lazy_var, Python immediately raises a SyntaxError because lazy_var doesn’t exist in the enclosing scope of nested().

Using Enclosing Scopes as Closures
Closures are a special use case of the enclosing Python scope. When you handle a nested function as data, the statements that make up that function are packaged together with the environment in which they execute. The resulting object is known as a closure. In other words, a closure is an inner or nested function that carries information about its enclosing scope, even though this scope has completed its execution.

Note: You can also call this kind of function a factory, a factory function, or—to be more precise—a closure factory to specify that the function builds and returns closures (an inner function), rather than classes or instances.

Closures provide a way to retain state information between function calls. This can be useful when you want to write code based on the concept of lazy or delayed evaluation. Take a look at the following code for an example of how closures work and how you can take advantage of them in Python:

>>> def power_factory(exp):
...     def power(base):
...         return base ** exp
...     return power
...
>>> square = power_factory(2)
>>> square(10)
100
>>> cube = power_factory(3)
>>> cube(10)
1000
>>> cube(5)
125
>>> square(15)
225
Your closure factory function power_factory() takes an argument called exp. You can use this function to build closures that run different power operations. This works because each call to power_factory() gets its own set of state information. In other words, it gets its value for exp.

Note: Variables like exp are called free variables. They are variables that are used in a code block but not defined there. Free variables are the mechanism that closures use to retain state information between calls.

In the above example, the inner function power() is first assigned to square. In this case, the function remembers that exp equals 2. In the second example, you call power_factory() using 3 as an argument. This way, cube holds a function object, which remembers that exp is 3. Notice that you can freely reuse square and cube because they don’t forget their respective state information.

For a final example on how to use closures, suppose that you need to calculate the mean of some sample data. You collect the data through a stream of successive measurements of the parameter you’re analyzing. In this case, you can use a closure factory to generate a closure that remembers the previous measurements in the sample. Take a look at the following code:

>>> def mean():
...     sample = []
...     def _mean(number):
...         sample.append(number)
...         return sum(sample) / len(sample)
...     return _mean
...
>>> current_mean = mean()
>>> current_mean(10)
10.0
>>> current_mean(15)
12.5
>>> current_mean(12)
12.333333333333334
>>> current_mean(11)
12.0
>>> current_mean(13)
12.2
The closure that you create in the above code remembers the state information of sample between calls of current_mean. This way, you can solve the problem in an elegant and Pythonic way.

Note: If you’d to learn more about scopes and closures, then check out the Exploring Scopes and Closures in Python video course.

Notice that if your data stream gets too large, then this function can become a problem in terms of memory usage. That’s because with each call to current_mean, sample will hold a bigger and bigger list of values. Take a look at the following code for an alternative implementation using nonlocal:

>>> def mean():
...     total = 0
...     length = 0
...     def _mean(number):
...         nonlocal total, length
...         total += number
...         length += 1
...         return total / length
...     return _mean
...
>>> current_mean = mean()
>>> current_mean(10)
10.0
>>> current_mean(15)
12.5
>>> current_mean(12)
12.333333333333334
>>> current_mean(11)
12.0
>>> current_mean(13)
12.2
Even though this solution is more verbose, you don’t have an endlessly growing list anymore. You now have a single value for total and length. This implementation is a lot more efficient in terms of memory consumption than the previous solution.

Finally, you can find some examples of using closures in the Python standard library. For example, functools provides a function named partial() that makes use of the closure technique to create new function objects that can be called using predefined arguments. Here’s an example:

>>> from functools import partial
>>> def power(exp, base):
...     return base ** exp
...
>>> square = partial(power, 2)
>>> square(10)
100
You use partial to build a function object that remembers the state information, where exp=2. Then, you call this object to perform the power operation and get the final result.


Remove ads
Bringing Names to Scope With import
When you write a Python program, you typically organize the code into several modules. For your program to work, you’ll need to bring the names in those separate modules to your __main__ module. To do that, you need to import the modules or the names explicitly. This is the only way you can use those names in your main global Python scope.

Take a look at the following code for an example of what happens when you import some standard modules and names:

>>> dir()
['__annotations__', '__builtins__',..., '__spec__']
>>> import sys
>>> dir()
['__annotations__', '__builtins__',..., '__spec__', 'sys']
>>> import os
>>> dir()
['__annotations__', '__builtins__',..., '__spec__', 'os', 'sys']
>>> from functools import partial
>>> dir()
['__annotations__', '__builtins__',..., '__spec__', 'os', 'partial', 'sys']
You first import sys and os from the Python standard library. By calling dir() with no arguments, you can see that these modules are now available for you as names in your current global scope. This way, you can use dot notation to get access to the names that are defined in sys and os.

Note: If you want to dive deeper into how imports work in Python, then check out Absolute vs Relative Imports in Python.

In the latest import operation, you use the form from <module> import <name>. This way, you can use the imported name directly in your code. In other words, you don’t need to explicitly use the dot notation.

Discovering Unusual Python Scopes
You’ll find some Python structures where name resolution seems not to fit into the LEGB rule for Python scopes. These structures include:

Comprehensions
Exception blocks
Classes and instances
In the next few sections, you’ll cover how Python scope works on these three structures. With this knowledge, you’ll be able to avoid subtle errors related to the use of names in these kinds of Python structures.

Comprehension Variables Scope
The first structure you’ll cover is the comprehension. A comprehension is a compact way to process all or part of the elements in a collection or sequence. You can use comprehensions to create lists, dictionaries, and sets.

Comprehensions consist of a pair of brackets ([]) or curly braces ({}) containing an expression, followed by one or more for clauses and then zero or one if clause per for clause.

The for clause in a comprehension works similarly to a traditional for loop. The loop variable in a comprehension is local to the structure. Check out the following code:

>>> [item for item in range(5)]
[0, 1, 2, 3, 4]
>>> item  # Try to access the comprehension variable
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    item
NameError: name 'item' is not defined
Once you run the list comprehension, the variable item is forgotten and you can’t access its value anymore. It’s unlikely that you need to use this variable outside of the comprehension, but regardless, Python makes sure that its value is no longer available once the comprehension finishes.

Note that this only applies to comprehensions. When it comes to regular for loops, the loop variable holds the last value processed by the loop:

>>> for item in range(5):
...     print(item)
...
0
1
2
3
4
>>> item  # Access the loop variable
4
You can freely access the loop variable item once the loop has finished. Here, the loop variable holds the last value processed by the loop, which is 4 in this example.


Remove ads
Exception Variables Scope
Another atypical case of Python scope that you’ll encounter is the case of the exception variable. The exception variable is a variable that holds a reference to the exception raised by a try statement. In Python 3.x, such variables are local to the except block and are forgotten when the block ends. Check out the following code:

>>> lst = [1, 2, 3]
>>> try:
...     lst[4]
... except IndexError as err:
...     # The variable err is local to this block
...     # Here you can do anything with err
...     print(err)
...
list index out of range
>>> err # Is out of scope
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    err
NameError: name 'err' is not defined
err holds a reference to the exception raised by the try clause. You can use err only inside the code block of the except clause. This way, you can say that the Python scope for the exception variable is local to the except code block. Also note that if you try to access err from outside the except block, then you’ll get a NameError. That’s because once the except block finishes, the name doesn’t exist anymore.

To work around this behavior, you can define an auxiliary variable out of the try statement and then assign the exception to that variable inside the except block. Check out the following example:

>>> lst = [1, 2, 3]
>>> ex = None
>>> try:
...     lst[4]
... except IndexError as err:
...     ex = err
...     print(err)
...
list index out of range
>>> err  # Is out of scope
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'err' is not defined
>>> ex  # Holds a reference to the exception
list index out of range
You use ex as an auxiliary variable to hold a reference to the exception raised by the try clause. This can be useful when you need to do something with the exception object once the code block has finished. Note that if no exception is raised, then ex remains None.

Class and Instance Attributes Scope
When you define a class, you’re creating a new local Python scope. The names assigned at the top level of the class live in this local scope. The names that you assigned inside a class statement don’t clash with names elsewhere. You can say that these names follow the LEGB rule, where the class block represents the L level.

Unlike functions, the class local scope isn’t created at call time, but at execution time. Each class object has its own .__dict__ attribute that holds the class scope or namespace where all the class attributes live. Check out this code:

>>> class A:
...     attr = 100
...
>>> A.__dict__.keys()
dict_keys(['__module__', 'attr', '__dict__', '__weakref__', '__doc__'])
When you inspect the keys of .__dict__ you’ll see that attr is in the list along with other special names. This dictionary represents the class local scope. The names in this scope are visible to all instances of the class and to the class itself.

To get access to a class attribute from outside the class, you need to use the dot notation as follows:

>>> class A:
...     attr = 100
...     print(attr)  # Access class attributes directly
...
100
>>> A.attr  # Access a class attribute from outside the class
100
>>> attr  # Isn't defined outside A
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    attr
NameError: name 'attr' is not defined
Inside the local scope of A, you can access the class attributes directly, just like you did in the statement print(attr). To access any class attribute once the code block of the class is executed, you’ll need to use the dot notation or attribute reference, as you did with A.attr. Otherwise, you’ll get a NameError, because the attribute attr is local to the class block.

On the other hand, if you try to access an attribute that isn’t defined inside a class, then you’ll get an AttributeError. Check out the following example:

>>> A.undefined  # Try to access an undefined class attribute
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    A.undefined
AttributeError: type object 'A' has no attribute 'undefined'
In this example, you try to access the attribute undefined. Since this attribute doesn’t exist in A, you get an AttributeError telling you that A doesn’t have an attribute named undefined.

You can also access any class attribute using an instance of the class as follows:

>>> obj = A()
>>> obj.attr
100
Once you have the instance you can access the class attributes using the dot notation, as you did here with obj.attr. Class attributes are specific to the class object, but you can access them from any instances of the class. It’s worth noting that class attributes are common to all instances of a class. If you modify a class attribute, then the changes will be visible in all instances of the class.

Note: Think of the dot notation as if you were telling Python, “Look for the attribute called attr in obj. If you find it, then give it back to me.”

Whenever you call a class, you’re creating a new instance of that class. Instances have their own .__dict__ attribute that holds the names in the instance local scope or namespace. These names are commonly called instance attributes and are local and specific to each instance. This means that if you modify an instance attribute, then the changes will be visible only to that specific instance.

To create, update, or access any instance attribute from inside the class, you need to use self along with the dot notation. Here, self is a special attribute that represents the current instance. On the other hand, to update or access any instance attribute from outside the class, you need to create an instance and then use the dot notation. Here’s how this works:

>>> class A:
...     def __init__(self, var):
...         self.var = var  # Create a new instance attribute
...         self.var *= 2  # Update the instance attribute
...
>>> obj = A(100)
>>> obj.__dict__
{'var': 200}
>>> obj.var
200
The class A takes an argument called var, which is automatically doubled inside .__init__() using the assignment operation self.var *= 2. Note that when you inspect .__dict__ on obj, you get a dictionary containing all instance attributes. In this case, the dictionary contains only the name var, whose value is now 200.

Note: For a more on how classes work in Python, check out Introduction to Object-Oriented Programming in Python.

Even though you can create instance attributes within any method in a class, it’s good practice to create and initialize them inside .__init__(). Take a look at this new version of A:

>>> class A:
...     def __init__(self, var):
...         self.var = var
...
...     def duplicate_var(self):
...         return self.var * 2
...
>>> obj = A(100)
>>> obj.var
100
>>> obj.duplicate_var()
200
>>> A.var
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    A.var
AttributeError: type object 'A' has no attribute 'var'
Here, you modify A to add a new method called duplicate_var(). Then, you create an instance of A by passing in 100 to the class initializer. After that, you can now call duplicate_var() on obj to duplicate the value stored in self.var. Finally, if you try to access var using the class object instead of an instance, then you’ll get an AttributeError because instance attributes can’t be accessed using class objects.

In general, when you’re writing object-oriented code in Python and you try to access an attribute, your program takes the following steps:

Check the instance local scope or namespace first.
If the attribute is not found there, then check the class local scope or namespace.
If the name doesn’t exist in the class namespace either, then you’ll get an AttributeError.
This is the underlying mechanism by which Python resolves names in classes and instances.

Although classes define a class local scope or namespace, they don’t create an enclosing scope for methods. Therefore, when you’re implementing a class, references to attributes and methods must be done using the dot notation:

>>> class A:
...     var = 100
...     def print_var(self):
...         print(var)  # Try to access a class attribute directly
...
>>> A().print_var()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    A().print_var()
  File "<stdin>", line 4, in print_var
    print(var)
NameError: name 'var' is not defined
Since classes don’t create an enclosing scope for methods, you can’t access var directly from within print_var() like you try to do here. To get access to class attributes from inside any method, you need to use the dot notation. To fix the problem in this example, change the statement print(var) inside print_var() to print(A.var) and see what happens.

You can override a class attribute with an instance attribute, which will modify the general behavior of your class. However, you can access both attributes unambiguously using the dot notation like in the following example:

>>> class A:
...     var = 100
...     def __init__(self):
...         self.var = 200
...
...     def access_attr(self):
...         # Use dot notation to access class and instance attributes
...         print(f'The instance attribute is: {self.var}')
...         print(f'The class attribute is: {A.var}')
...
>>> obj = A()
>>> obj.access_attr()
The instance attribute is: 200
The class attribute is: 100
>>> A.var  # Access class attributes
100
>>> A().var # Access instance attributes
200
>>> A.__dict__.keys()
dict_keys(['__module__', 'var', '__init__',..., '__getattribute__'])
>>> A().__dict__.keys()
dict_keys(['var'])
The above class has an instance attribute and a class attribute with the same name var. You can use the following code to access each of them:

Instance: Use self.var to access this attribute.
Class: Use A.var to access this attribute.
Since both cases use the dot notation, there are no name collision problems.

Note: In general, good OOP practices recommend not to shadow class attributes with instance attributes that have different responsibilities or perform different actions. Doing so can lead to subtle and hard-to-find bugs.

Finally, notice that the class .__dict__ and the instance .__dict__ are totally different and independent dictionaries. That’s why class attributes are available immediately after you run or import the module in which the class was defined. In contrast, instance attributes come to life only after an object or instance is created.


Remove ads
Using Scope Related Built-In Functions
There are many built-in functions that are closely related to the concept of Python scope and namespaces. In previous sections, you’ve used dir() to get information on the names that exist in a given scope. Besides dir(), there are some other built-in functions that can help you out when you’re trying to get information about a Python scope or namespace. In this section, you’ll cover how to work with:

globals()
locals()
dir()
vars()
Since all these are built-in functions, they’re available for free in the built-in scope. This means that you can use them at any time without importing anything. Most of these functions are intended to be used in an interactive session to get information on different Python objects. However, you can find some interesting use cases for them in your code as well.

globals()
In Python, globals() is a built-in function that returns a reference to the current global scope or namespace dictionary. This dictionary always stores the names of the current module. This means that if you call globals() in a given module, then you’ll get a dictionary containing all the names that you’ve defined in that module, right before the call to globals(). Here’s an example:

>>> globals()
{'__name__': '__main__',..., '__builtins__': <module 'builtins' (built-in)>}
>>> my_var = 100
>>> globals()
{'__name__': '__main__',..., 'my_var': 100}
The first call to globals() returns a dictionary containing the names in your __main__ module or program. Note that when you assign a new name at the top level of the module, like in my_var = 100, the name is added to the dictionary returned by globals().

An interesting example of how you can use globals() in your code would be to dynamically dispatch functions that live in the global scope. Suppose you want to dynamically dispatch platform-dependent functions. To do this, you can use globals() as follows:

# Filename: dispatch.py

from sys import platform

def linux_print():
    print('Printing from Linux...')

def win32_print():
    print('Printing from Windows...')

def darwin_print():
    print('Printing from macOS...')

printer = globals()[platform + '_print']

printer()
If you run this script in your command line, then you’ll get an output that will depend on your current platform.

Another example of how to use globals() would be to inspect the list of special names in the global scope. Take a look at the following list comprehension:

>>> [name for name in globals() if name.startswith('__')]
['__name__', '__doc__', '__package__',..., '__annotations__', '__builtins__']
This list comprehension will return a list with all the special names that are defined in your current global Python scope. Note that you can use the globals() dictionary just like you would use any regular dictionary. For example, you can iterate through it through it using these traditional methods:

.keys()
.values()
.items()
You can also perform regular subscription operations over globals() by using square brackets like in globals()['name']. For example, you can modify the content of globals() even though this isn’t recommended. Take a look at this example:

>>> globals()['__doc__'] = """Docstring for __main__."""
>>> __doc__
'Docstring for __main__.'
Here, you change the key __doc__ to include a docstring for __main__ so that from now on, the main module’s docstring will have the value 'Docstring for __main__.'.

locals()
Another function related to Python scope and namespaces is locals(). This function updates and returns a dictionary that holds a copy of the current state of the local Python scope or namespace. When you call locals() in a function block, you get all the names assigned in the local or function scope up to the point where you call locals(). Here’s an example:

>>> def func(arg):
...     var = 100
...     print(locals())
...     another = 200
...
>>> func(300)
{'var': 100, 'arg': 300}
Whenever you call locals() inside func(), the resulting dictionary contains the name var mapped to the value 100 and arg mapped to 300. Since locals() only grabs the names assigned before you call it, another is not in the dictionary.

If you call locals() in the global Python scope, then you’ll get the same dictionary that you would get if you were to call globals():

>>> locals()
{'__name__': '__main__',..., '__builtins__': <module 'builtins' (built-in)>}
>>> locals() is globals()
True
When you call locals() in the global Python scope, you get a dictionary that’s identical to the dictionary returned by the call to globals().

Note that you shouldn’t modify the content of locals() because changes may have no effect on the values of local and free names. Check out the following example:

>>> def func():
...     var = 100
...     locals()['var'] = 200
...     print(var)
...
>>> func()
100
When you try to modify the content of var using locals(), the change doesn’t reflect in the value of var. So, you can say that locals() is only useful for read operations since updates to the locals dictionary are ignored by Python.


Remove ads
vars()
vars() is a Python built-in function that returns the .__dict__ attribute of a module, class, instance, or any other object which has a dictionary attribute. Remember that .__dict__ is a special dictionary that Python uses to implement namespaces. Take a look at the following examples:

>>> import sys
>>> vars(sys) # With a module object
{'__name__': 'sys',..., 'ps1': '>>> ', 'ps2': '... '}
>>> vars(sys) is sys.__dict__
True
>>> class MyClass:
...     def __init__(self, var):
...         self.var = var
...
>>> obj = MyClass(100)
>>> vars(obj)  # With a user-defined object
{'var': 100}
>>> vars(MyClass)  # With a class
mappingproxy({'__module__': '__main__',..., '__doc__': None})
When you call vars() using sys as an argument, you get the .__dict__ of sys. You can also call vars() using different types of Python objects, as long as they have this dictionary attribute.

Without any argument, vars() acts like locals() and returns a dictionary with all the names in the local Python scope:

>>> vars()
{'__name__': '__main__',..., '__builtins__': <module 'builtins' (built-in)>}
>>> vars() is locals()
True
Here, you call vars() at the top level of an interactive session. With no argument, this call returns a dictionary containing all the names in the global Python scope. Note that, at this level, vars() and locals() return the same dictionary.

If you call vars() with an object that doesn’t have a .__dict__, then you’ll get a TypeError, like in the following example:

>>> vars(10)  # Call vars() with objects that don't have a .__dict__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: vars() argument must have __dict__ attribute
If you call vars() with an integer object, then you’ll get a TypeError because this type of Python object doesn’t have a .__dict__.

dir()
You can use dir() without arguments to get the list of names in the current Python scope. If you call dir() with an argument, then the function attempts to return a list of valid attributes for that object:

>>> dir()  # With no arguments
['__annotations__', '__builtins__',..., '__package__', '__spec__']
>>> dir(zip)  # With a function object
['__class__', '__delattr__',..., '__str__', '__subclasshook__']
>>> import sys
>>> dir(sys)  # With a module object
['__displayhook__', '__doc__',..., 'version_info', 'warnoptions']
>>> var = 100
>>> dir(var)  # With an integer variable
['__abs__', '__add__',..., 'imag', 'numerator', 'real', 'to_bytes']
If you call dir() with no arguments, then you get a list containing the names that live in the global scope. You can also use dir() to inspect the list of names or attributes of different objects. This includes functions, modules, variables, and so on.

Even though the official documentation says that dir() is intended for interactive use, you can use the function to provide a comprehensive list of attributes of a given object. Note that you can also call dir() from inside a function. In this case, you’ll get the list of names defined in the function scope:

>>> def func():
...     var = 100
...     print(dir())
...     another = 200  # Is defined after calling dir()
...
>>> func()
['var']
In this example, you use dir() inside func(). When you call the function, you get a list containing the names that you define in the local scope. It’s worth noting that in this case, dir() only shows the names you declared before the function call.

Conclusion
The scope of a variable or name defines its visibility throughout your code. In Python, scope is implemented as either a Local, Enclosing, Global, or Built-in scope. When you use a variable or name, Python searches these scopes sequentially to resolve it. If the name isn’t found, then you’ll get an error. This is the general mechanism that Python uses for name resolution and is known as the LEGB rule.

You’re now able to:

Take advantage of Python scope to avoid or minimize bugs related to name collision
Make good use of global and local names across your programs to improve code maintainability
Use a coherent strategy to access, modify, or update names across all your Python code
Additionally, you’ve covered some scope-related tools and techniques that Python offers and how you can use them to gather information about the names that live in a given scope or to modify the standard behavior of Python scope. Of course, there’s more to this topic that’s outside the scope of this tutorial, so get out there and continue to tackle name resolution in Python!

