# Topics
## PyCharm

Please install before course

### EduTools
File -> Setting -> Plugins -> Marketplace -> Edutools -> install

### Python Course
File -> Learn and Teach -> Browse Courses -> Marketplace -> Introduction to Python

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

## Mathematical operations

- assignment
- math
- show addition of int and String
Switch the value of two variables

Comparisons
- == same value
- The operators 'is' and 'is not' test for object identity: x is y is true if and only if x and y are the same object.
- Comparisons can be chained arbitrarily, and expressions like a < b < c 
## Debugger

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

Use enumerate to get the index with the element as you iterate:
```
  for index, item in enumerate(items):
    print(index, item)
```

### While

### break / continue
### else

Python also allows loop statements to have an else clause. It is executed when the loop terminates through exhaustion
of the iterable (with for) or when the condition becomes False (with while), but not when the loop is terminated by a break statement.

## If / else / elif 

-> Run through two synced lists (gene id and gene name)

## Dictionaries (aka Hashes :D )

- Dictionaries are enclosed in curly braces, e.g., dct = {'key1' : "value1", 'key2' : "value2"}.
- A pair of braces creates an empty dictionary: {}.
- keys() + values() + items()
- "bla" in dictionary

-> go back to gene id and name example. Now use a hash. Find the name of the gene id 123

## Read files

## Regex

## Functions

- keyword arguments (named parameters)
- scope (no example)
- skip args and kwargs
- skip recursion

## Documentation

- https://realpython.com/documenting-python-code/#documenting-your-python-code-base-using-docstrings
- reStructuredText Example
- Stub from PyCharm
- https://www.jetbrains.com/help/pycharm/documenting-source-code.html
- Settings -> Tools -> Python Integrated Tools

## Classes

### Inheritance?

## Modules

Which modules are frequently used? Can one of the Python afficionados show some?

## Git / GitHub in PyCharm

## Exam

Solve Rosalind tests.