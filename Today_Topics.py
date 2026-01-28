✅ Python
Day - 1
-------------------------

1.
What is Python?  1990 - --2025
almost
35
2.
Features of Python
3.Python is Case Sensitive - ---sql?
4.Python Uses Indentation - ---sql?     java, c, c + + {}
5.Dynamically typed - ----sql?
6.Comments in Python - -----
7.What is sourcecode

Python
Day2
--------------
1.
Print
SYNTAX:
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
print("Hello", "World", sep="-", end="!", file=file, flush=True)
2.
Input
variable_name = input(prompt)
3.
Keywords & Identifiers
●    Keywords
are also called as Reserved Words.
● All the  keywords can be in Lower Case or upper Case.
● We cannot use a keyword as a variable
name, function name or any other

identifier.
●    They are used to define the
syntax and structure of the Python language.In
Python, keywords
are
case - sensitive.
4.Identifiers are the names used to identify a variable, function,


class ,
    module, or other
    objects.

●    They
start
with a letter (A-Z or a-z) or an underscore (_) followed by
zero or more
letters,
underscores, and digits(0 - 9).
●    Python is case - sensitive, so
myVariable and myvariable are two different identifiers.

5.
Identifiers
Rules
for writing identifiers:
Identifiers     can be a combination of letters in lowercase(a toz) or uppercase(A to Z) or digits(0 to 9) or an
underscore(_).

●    An identifier cannot start with a digit.
●    Keywords  cannot be used as identifiers.
●    We cannot  use  special   symbols  like !, @,  # , $, %, etc. in our identifier.
●    An identifier can be of  any  length.

 5.
    Variables and Data
    Types
    ●    A
    variable is a
    container(storage
    area) used
    to
    hold
    data.
    ●    Each
    variable
    should
    be
    given
    a
    unique
    name(identifier).
    ●    Variables
    are
    created
    on
    demand
    whenever
    a
    value is assigned
    to
    them
    using
    the
    equals
    sign
    = which is known as the
    assignment
    operator.
    ●    Value
    of
    the
    variable
    can
    be
    changed
    any
    number
    of
    times
    during
    the
    program
    execution

    Python
    Day3
    -----------------
    ** *Operators
    1.
    Arithmetic
    Operators(+, -, *, /, //, %, ** )
    2.
    Assignment
    Operators( =, +=, -=, *=, /=, //=, %=, **= etc.)
    3.
    Comparison
    Operators( ==, !=, <, >, <=, >= )
    4.
    Logical
    Operators( and, or, not)
    5.
    Membership
    Operators( in, not in )
    6.
    Identity
    Operators( is, is not)

    ** ** Control
    Flow(Decision
    Making)
    if , elif, else statements

    keyword
    condition:
    print()

    if a > 0:
        print("Yes its a positive value")

    Nested if statements
    Ternary
    Conditional
    Expression

    Python
    Day - 4
    -------------------------
    1.
    Definition: Ternary
    Conditional
    Expression

    A
    ternary
    conditional
    expression(also
    known as the
    conditional
    operator)
    is a
    shorthand
    way
    to
    write
    an if - else statement in a
    single
    line.
    It
    allows
    you
    to
    choose
    between
    two
    values
    based
    on
    a
    condition.

    Syntax:
    value_if_true if condition else value_if_false

    2.
    Striing
    function
    -------------------

    Python
    Day - 5
    -------------------------
    Loops
    concepts in python
    For
    loop:
    SYNTAX:
    for variable in sequence:
    # code block

    Defination:
    A
    for loop is used to iterate over a sequence
    (like a list, tuple, string, or range).
    It executes a block of code once
    for each item in the sequence.

    While:
    SYNTAX:
    while condition:
    # code block

    Defination:
    A
    while loop repeats a block of code as long as a condition is True.

    Continue:
    SYNTAX:
    for / while loop:
        if condition:
            continue
    Defination:
    🔸 continue
    statement

    Definition:
    Used to skip the current iteration and continue with the next one.

    break:
    SYNTAX:
    for / while loop:
        if condition:
            break

    Definition:
    Used
    to
    exit
    a
    loop
    immediately, even if the
    condition
    is still
    true or sequence
    not finished.

    Python
    Day - 6
    -------------------------
    String
    slicing: Python_Class - ---P - 0, y - 1
    SYNTAX:
    string[start: end:step]
    start → starting
    index(inclusive)
    end → ending
    index(exclusive)
    step → interval(optional)

    List:
    Defination:
    A list in Python is an ordered collection of items. It can store different data
    types(int, float, string, etc.) and is mutable(can be changed).

    Common List Methods
    -------------------
    1.append()
    2.insert()
    syntax: list_name.insert(index, item)
    3.remove()
    syntax: list_name.remove(item)
    4.pop()
    syntax: list_name.pop(index)
    5.sort() By defult: ASC
    6.reverse()
    syntax:
    7.count()
    8.extend()

    formating
    string

    List
    comprehension
    SYNTAX:
    [expression for item in iterable]
    [expression for item in iterable if condition]
    [expression_if_true if condition else expression_if_false for item in iterable]

    Tuple
    ✔ Basic tuple
    ✔ Tuple without parentheses
    ✔ Single - item tuple(important)


    1.Tuple methods
        1. count()
        2.index()
    2.Nested Tuple
    3.Tuple unpacking
    4.Tuple operations
        1.Concatenation   = +
        2.Repetition   = *
        3.Membership  in
    5.Accessing Tuples elements



Set:
1.Definition

A set is an unordered, mutable, collection of unique elements.
A list is an rdered, mutable, collection of  elements.
A tuple is an rdered, nonmutable, collection of  elements.


Syntax:
s1={1,2,3,4,4}
s2=()  empty set

2.Set Methods:
    2.1 Add
    2.2 Update
    2.3 Remove
    2.4 Discard
    2.5 Pop
    2.6 Clear
    2.7 Copy

3.Set Operations
    🔶 1. Union (| or .union())
    🔶 2. Intersection (& or .intersection())
    🔶 3. Difference (- or .difference())
    🔶 4. Symmetric Difference (^ or .symmetric_difference())


4.Dict:
🟦 What is a Dictionary in Python?

A dictionary is a mutable, unordered collection of key–value pairs.

📌 Key points:

1.Keys must be unique
2.Keys must be immutable (string, number, tuple…)
3.Values can be anything (list, dict, set, etc.)
4.Items are stored as {key: value}

1.1 Accessing Values  d[Keyname] or d.get(KeyValue)
1.2 Adding / Updating  d[NewKey]=Value or d.update({"NewKey": 30})
1.3 Removing Items   # pop(),popitem() del d[] and clear
1.4 How we can iterate Dict

Python - Day9
--------------
✅ Definition

A function is a block of reusable code.
You define a function using the def keyword.


1. Defining and Calling Functions (def)
2. Arguments and Return Values
3. Default Arguments
4. Keyword Arguments
5. *args (Variable-Length Positional Arguments)
6. **kwargs (Variable-Length Keyword Arguments)
7. Using *args and **kwargs Together


Error Handling
------------------------------
1. Error Handling (Exception Handling)
Error handling in Python allows you to respond to errors (also called exceptions) gracefully without crashing the program.
When Python encounters an error during program execution, it “throws” an exception. You can “handle” these
exceptions using try, except, finally, and else.

2. Try–Except Blocks
try:
    # Code that may cause an error
except ExceptionType:
    # Code that runs if the error occurs


3. Multiple Exception Handling

Syntax 1: Multiple except blocks
try:
    # risky code
except ValueError:
    # handle ValueError
except TypeError:
    # handle TypeError

Syntax 2: Multiple exceptions in one block
try:
    # risky code
except (ValueError, TypeError):
    # handle both

4. Finally Block
The finally block runs whether or not an exception occurs, often used
for cleanup (closing files, releasing resources, etc.)

Syntax:
try:
    # risky code
except SomeError:
    # handle error
finally:
    # code that always runs

5. Common Exceptions
(a) ValueError:Occurs when a function receives an argument of correct type but invalid value.
(b) TypeError: Occurs when an operation is applied to an object of inappropriate type.
(c) ZeroDivisionError: Occurs when dividing a number by zero.
(d) IndexError : Occurs when accessing an invalid list index.
(e) KeyError : Occurs when accessing a non-existing dictionary key.
(f) FileNotFoundError : Occurs when attempting to open a non-existent file.



Python - Day10
--------------

✅ 1. Modules and Packages
✅ 2. Importing Modules
    A) Using import module   : SYNTAX:import module_name
    B) Using from … import    : SYNTAX: from module_name import function_name
✅ 3. Using Built-in Modules
✅ 4. Creating Your Own Module
✅ 5. Installing External Packages Using pip
SYNTAX: pip install package_name
Examples:
pip install pandas
pip install pytest



✅ Python File Handling Explained
| Mode   | Meaning                         |
| ------ | ------------------------------- |
| `"r"`  | Read (file must exist)          |
| `"w"`  | Write (creates/overwrites file) |
| `"a"`  | Append (adds to end)            |
| `"b"`  | Binary mode (images, videos)    |
| `"r+"` | Read + Write                    |


Python - Day11
-------------------
✅ 1. Introduction to Object-Oriented Programming (OOP)
Object-Oriented Programming (OOP) is a programming paradigm where you structure your code using objects—these objects
represent real-world things and contain:

Data (variables) → called attributes

Functions (methods) → behaviors the object can perform

🔥 Why OOP?
-----------------
* Makes code modular and reusable
* Helps organize large programs
* Encourages code reusability via inheritance
* Models real-world entities

✅ 2. Classes and Objects
✅ 3. __init__() Method (Constructor)
✅ 4.Inheritance in Python (Complete Guide)
⭐ 1. Single Inheritance  : A child class inherits from one parent class.


Python - Day12
--------------
OOP Concepts Continue
✅ 3. __init__() Method (Constructor)
️✅ 4. Encapsulation
        4.1 Public   : public attributes → can be accessed anywhere
        4.2 Protect : Single_ :  protected attributes _var → should be accessed within class/subclass
        4.3 Privite : Double __     private attributes __var → not accessible directly outside the class

✅ 5.Polymorphism
One name, many forms — the same function/method behaves differently for different objects.

 5.1 the number/type of arguments (overloading)
 5.2 the class in which it is implemented (overriding)

    **Polymorphism has 2 types:

    1.Compile-time Polymorphism → Method Overloading
    2.Runtime Polymorphism → Method Overriding

✅  6. Abstraction
Showing only the necessary details and hiding complex internal implementation.
✔ Why?
To reduce complexity.
✔ How in Python?
Using abstract classes and abstract methods (abc module).



Python - Day12
--------------------------------------
🔹 1. Lambda Functions
    Syntax: lambda arguments: expression
    Examples:
        1.✔ Example 1: Add 10 to a number
        2.✔ Example 2: Multiply two numbers
        3.✔ Example 3: Sorting with lambda

🔹 2. map()
    Syntax: map(function, iterable)
    Examples:
    1.✔ Example 1: Square each number
    2.✔ Example 2: Convert strings to integers
    3.✔ Example 3: Add items of two lists

🔹 3. filter()
    Syntax: filter(function, iterable)
    Examples:
    1.✔ Example 1: Keep even numbers
    2.✔ Example 2: Keep strings with length > 3
    3.✔ Example 3: Keep positive numbers

🟦 4. reduce()?
    Import:
        from functools import reduce
    Syntax: reduce(function, iterable[, initializer])
    Examples:
    🟩 1. Example: Sum of List
    🟩 2. Example: Product of List
    🟦 3.Using Initializer (Optional Third Argument)

✅ ETL Transformation Rules
    1.1️⃣ Expression Transformation     # Exampple source : frist Name, Last Name   Target: EmpName(First+Last)
    2.2️⃣ Sort Transformation           # Sorter have two sort 1.asc and 2. desc #  Based empid or stduentid
    3.3️⃣ Lookup Transformation         # Source emp and dept(dloc) :   emp who are working Bangalore location Target table()
    4.4️⃣ Aggregate Transformation      # sum,count,avg,max,min  : Data filter
    5.5️⃣ Filter Transformation        # Based condition we can filter HYD : Amirpet voter list   : Row Count change
    6.9️⃣ Router Transformation        #    Networking roueter : IP addres 1,2,3,4,5  Loc or  deptment  or etc....
    7.1️⃣1 Rank Transformation        #  winwods   Top N records, Botton n records
    8.1️⃣3 Data Masking Transformation  #    any bank Net banking Login it will display , Account number, Credit Carrds
    9.1️⃣4 Pivot Transformation        #



# When you are student  appling for BE UI Application


Pivote Syntax:
SELECT *
FROM (select column names table_name)
PIVOT (
    aggregate_function(column_to_aggregate)
    FOR column_to_turn_into_columns IN (value1, value2, value3...)
);

sum(sal) deptatment wise
-----------------








