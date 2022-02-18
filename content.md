# Topics

## Preparation
### Mail
Dear Students,\
the starting day of our course is getting closer. As pointed out in WueStudy the topic will not be 'Linux and Perl'.
Rather, we will learn programming in Python (OK, first steps of ;-). As we have only five days, I would hate it
if we loose precious time for installing the needed resources. Thus, I want everyone of you to have the
following installed and running on the computer you are gonne work with:

- **Python** Please install the latest release from here https://www.python.org/downloads/windows/
- **PyCharm** (The IDE we will be using) https://www.jetbrains.com/pycharm/download/#section=windows Choose 'Community' Edition (for
the operating system you are working on)
- **EduTools** In Pycharm: File -> Setting -> Plugins -> Marketplace -> EduTools -> install
- **Introduction to Python** In PyCharm:  File -> Learn and Teach -> Browse Courses -> Marketplace -> Introduction to Python

In case you encounter any problems, Google it and find a solution. Arguably the most important skill I want to teach
you in this course is to find solutions for you programming problems by yourself. There are tons of YouTube
videos explaining every detail of the installation process. And, as you will see in the course, StackOverflow
is always there to help!

OK, and if you got completely stuck ;-) ask for help in the course forum. 

Looking forward to our Python journey,\
Joerg Schultz

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

**Exercise** Course 'Introduction'

## Variables
### Numbers

- int
- float
- complex

### Strings
- 'bla' and "blub"
- print(f"{bla}")
- String multiplication: String * 2
- Strings are arrays already -> positions (Maybe use this to introduce array concepts?)
- len(string)
- \n, \t

### Boolean

## Debugger

**Exercise** swap the value of two variables, then follow in debugger

## Mathematical operations

- assignment
- math
- show addition of int and String

## If / else / elif 

Comparisons
- == same value
- The operators 'is' and 'is not' test for object identity: x is y is true if and only if x and y are the same object.
- Comparisons can be chained arbitrarily, and expressions like a < b < c 

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
- nested lists
- ? Tuples: The only significant difference between tuples and lists is that tuples are immutable
- List comprehension?
- sort

## Loops
### For

**Exercise** run through a list of genes and report in which position there is a specific gene

Use enumerate to get the index with the element as you iterate:
```
  for index, item in enumerate(items):
    print(index, item)
```

### While

**Exercise** rewrite the run through list code with while

### break / continue
### else

Python also allows loop statements to have an else clause. It is executed when the loop terminates through exhaustion
of the iterable (with for) or when the condition becomes False (with while), but not when the loop is terminated by a break statement.

## Dictionaries

**Exercise** run through two linked lists (genes with name and species) to find the species of a specific gene

- Dictionaries are enclosed in curly braces, e.g., dct = {'key1' : "value1", 'key2' : "value2"}.
- A pair of braces creates an empty dictionary: {}.
- keys() + values() + items(
- if key in dictionary
- "bla" in dictionary

**Exercise** go back to gene name and species example. Now use a hash. Find the name of the gene id 123

## Read files

- split() lines on \t
- string = string.replace("bla", "blub")
- with open() as bla: for line in bla

**Exercise** find all up-regulated kinases ("kinase" in element)

## Regex

- import re
- phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') -> r = raw string?
- Pass the string you want to search into the Regex object’s search() method. This returns a Match object.
- Call the Match object’s group() (or groups()) method to return a string of the actual matched text
- re.split() — Regular expression operations

**Exercise** find all upregulated [P|p]rotein\s+[K|k]inases

## Functions

**Exercise** write a fasta parser

- keyword arguments (named parameters)
- scope (no example)
- skip args and kwargs
- skip recursion

**Exercise** extract parser to function

## Documentation

optional, depends on time

- https://realpython.com/documenting-python-code/#documenting-your-python-code-base-using-docstrings
- reStructuredText Example
- Stub from PyCharm
- https://www.jetbrains.com/help/pycharm/documenting-source-code.html
- Settings -> Tools -> Python Integrated Tools

**Exercise** write documentation for function

### Sphinx

- https://www.sphinx-doc.org/en/master/
- Go to Terminal window in PyCharm
- pip install -U sphinx
- Tools Sphinx Quickstart (no 'ö' in name :-)
- .\make html in Terminal

## Classes

- In Python, there is no existence of “Private” instance variables  (Yeah, this is so OO...)
- use robot class to introduce concept
- use protein + domain classed to show
  - a class inside a class
  - encapsulation

**Exercise** implement robot class

**Exercise** let the fasta parser return a list of Protein objects

### Inheritance

skip, too much

## Modules / Packages

A package is a collection of Python modules: while a module is a single Python file, 
a package is a directory of Python modules containing an additional __init__.py file, 
to distinguish a package from a directory that just happens to contain a bunch of Python scripts.

### build your own

**Exercise** build your own fasta parser package

Which modules are frequently used?

- https://pypi.org/
- https://pypi.org/project/biopython/
- Show Bio.SeqIO.parse() fasta parser
- Bluetooth
- edge Impulse

**Showcase** bluetooth and ML in my python script

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

## Exam

Solve Rosalind tests.