# Topics

## Preparation
### Python

https://www.python.org/downloads/windows/ -> Latest Release

### PyCharm

https://www.jetbrains.com/pycharm/download/#section=windows Choose 'Community' Edition (for
the operating system you are working on)

### EduTools
In PyCharm
File -> Setting -> Plugins -> Marketplace -> Edutools -> install

### Python Course
In PyCharm
File -> Learn and Teach -> Browse Courses -> Marketplace -> Introduction to Python

## Intro

- Show Python Interpreter with print("Hello World")
- Show writing a text file in Editor and run it on the command line
- Start PyCharm, write exactly the same file and run it (i) on the command line and (ii) in PyCharm

[hello.py](hello.py)

**Exercise** Course 'Introduction'

## Variables
### Numbers

- int
- float
- complex

### Strings
- 'bla' and "blub"
- Show addition int + string
  - type conversion
- print(f"{bla}")
- String multiplication: String * 2
- Strings are arrays already -> positions (Maybe use this to introduce array concepts?)
- len(string)
- \n, \t

### Boolean

- introduce the concept True/False (1/0)
- introduce equal, and, or

[variables.py](variables.py)

**Exercise** Variables
- Variable Definition
  - Run this without any changes locally.
  - Show error, show how you can jump to code. 
  - Once everything is fixed, -> check
- Undefined Variable
- Variable Types
- Type Conversion

## Debugger

**Exercise** swap the value of two variables, then follow in debugger

[swap_variables.py](swap_variables.py)

## Mathematical operations

- assignment
- math
- show addition of int and String

**Exercises** Variables
- Arithmetic Operators
- Assignments
- Boolean Operators
- Comparison Operators

## List
Don't talk about arrays here, just lists.
Lists can consist of elements belonging to different data types, 
Arrays only consists of elements belonging to the same data type. 
You have to import a module to use arrays.
- slicing
  - Note that the symbol with the index ind1 will be included, while the symbol with the index ind2 – won't.
  - [1:7] 
  - [0:5] == [:5]
- Empty lists are considered False in Python
- in keyword
- Stacks and Queues?
- nested lists = matrices
- ? Tuples: The only significant difference between tuples and lists is that tuples are immutable
- List comprehension?
- sort

[lists.py](lists.py)

**Exercise** Data structures
- Lists introduction
- Lists operations
- List items
- Nested lists
- Join method

## If / else / elif 

Conditional code execution. Indentation is syntax.
Comparisons
- == same value
- The operators 'is' and 'is not' test for object identity: x is y is true if and only if x and y are the same object.
- Comparisons can be chained arbitrarily, and expressions like a < b < c 

[conditions.py](conditions.py)

**Exercise** Condition expressions

## Strings

I put them after lists, as many string operations make only sense if you see Strings as lists of characters

**Exercise** Strings


## Loops
### For

**Exercise** Loops
- For loop
- Loop over a string
- Nested for Loop

**Exercise** run through a list of genes and report in which position there is a specific gene

<!-- 
Use enumerate to get the index with the element as you iterate:
```
  for index, item in enumerate(items):
    print(index, item)
```
-->

### While
### break / continue
### else

Python also allows loop statements to have an else clause. It is executed when the loop terminates through exhaustion
of the iterable (with for) or when the condition becomes False (with while), but not when the loop is terminated by a break statement.

**Exercise** Loops
- while Loop
- break keyword
- Fix infinite Execution
- Else with Loops
- Else with Loops 2
- Continue keyword

**Exercise** rewrite the run through list code with while

**Exercise** Loops
- List Comprehension
- Nested List Comprehension

## Dictionaries

**Exercise** run through two linked lists (genes with name and species) to find the species of a specific gene

- Dictionaries are enclosed in curly braces, e.g., dct = {'key1' : "value1", 'key2' : "value2"}.
- A pair of braces creates an empty dictionary: {}.
- keys() + values() + items(
- if key in dictionary
- "bla" in dictionary

**Exercise** Data structures
- Dictionaries
- Add items from list
- Dictionaries keys() and values()
- Dictionary keys
- In keyword

**Exercise** go back to gene name and species example. Now use a hash. Find the name of the gene id 123

## Read files

- split() lines on \t
- string = string.replace("bla", "blub")
- with open() as bla: for line in bla

**Exercise** File input output

**Exercise** find all up-regulated kinases ("kinase" in element)

## Functions

Show how to change the read file code into a function. With return value.
Then add a word to search for as parameter.
Finally, show default arguments. If no parameter is given, we search for 'excellent'.

- keyword arguments (named parameters)
- scope (no example)
- skip args and kwargs
- skip recursion

**Exercise** Functions
- fibonacci change `print(fib(10))` to `print(fib(22))`
- except Args and kwargs
- except Recursion

**Exercise** write a function which takes a protein function as input and returns a list of genes
which have this function and are up-regulated


**Exercise (Optional)** write a fasta parser

**Exercise (Optional)** extract parser to function

## Modules / Packages

A package is a collection of Python modules: while a module is a single Python file, 
a package is a directory of Python modules containing an additional __init__.py file, 
to distinguish a package from a directory that just happens to contain a bunch of Python scripts.

**Exercise** Modules and Packages
- except Executing modules as scripts

### build your own

**Exercise** Extract up-regulated function finder to module and then to package

**Exercise (Optional)** build your own fasta parser package

### use pre-build modules
Which modules are frequently used?

- https://pypi.org/
- https://pypi.org/project/biopython/
- Show Bio.SeqIO.parse() fasta parser
- Bluetooth
- edge Impulse

**Showcase** bluetooth and ML in my python script

## Classes

- In Python, there is no existence of “Private” instance variables  (Yeah, this is so OO...)
- use robot class to introduce concept
- use protein + domain classes to show
  - a class inside a class
  - encapsulation

**Exercise** Classes and Objects

**Exercise** implement robot class

**Exercise** let the up regulated genes finder return a list of Protein objects
**Exercise (Optional)** let the fasta parser return a list of Protein objects

### Inheritance

Depending on how much time we have, show a Robot with a light on its head

- `class Student(Person)`
- `super()`

## Regex

- import re
- phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') -> r = raw string?
- Pass the string you want to search into the Regex object’s search() method. This returns a Match object.
- Call the Match object’s group() (or groups()) method to return a string of the actual matched text
- re.split() — Regular expression operations

**Exercise** find all up-regulated [P|p]rotein\s+[K|k]inases


## AddOns

### Git / GitHub in PyCharm

### Exception Handling

https://www.geeksforgeeks.org/python-exception-handling/
```
try:
  a = 5 / 0
except: # except ZeroDivisionError: 
  print("Error")
else: # only if try does not cause an exception
  print("We did it!")
finally: # always executed
  print("And finished")
```

### Documentation

optional, depends on time

- https://realpython.com/documenting-python-code/#documenting-your-python-code-base-using-docstrings
- reStructuredText Example
- Stub from PyCharm
- https://www.jetbrains.com/help/pycharm/documenting-source-code.html
- Settings -> Tools -> Python Integrated Tools

**Exercise** write documentation for function

#### Sphinx

- https://www.sphinx-doc.org/en/master/
- Go to Terminal window in PyCharm
- pip install -U sphinx
- Tools Sphinx Quickstart (no 'ö' in name :-)
- .\make html in Terminal

## Exam

Solve Rosalind tests.
