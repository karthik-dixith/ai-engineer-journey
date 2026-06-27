# Exercise 1a: basic function with return

def square(x):
    return x*x

# Prediction: what does this print? 25
# print(square(5)) -> 25
print(square(5))

# Exercise 1b: function with no return statement
def shout(text):
    print(text.upper())

# Prediction: what gets printed by each of these two lines?
# print(shout("hello")) -> first line prints:HELLO
#                       -> second line prints: None because the parameter goes inside the function but there is no return statement so None will be returned

result = shout("hello")
print(result)


# Exercise 1c: early return 
def absolute(n):
    if n < 0:
        return -n
    return n

# Prediction: what do these print?
# print(absolute(-7))  -> 7
# print(absolute(7))  -> 7
# print(absolute(0))  -> 0

print(absolute(-7))  
print(absolute(7))  
print(absolute(0)) 

# 3. Positional vs keyword arguments

# When you call a function, you can pass arguments in two ways:
# pythondef describe(name, age, city):
#     return f"{name} is {age} years old and lives in {city}."

# # Positional: order matters
# print(describe("Karthik", 30, "Berlin"))

# # Keyword: order doesn't matter, name does
# print(describe(age=30, city="Berlin", name="Karthik"))

# # Mixed: positional MUST come before keyword
# print(describe("Karthik", city="Berlin", age=30))

# Why care? Two reasons:

# Readability. requests.get(url, timeout=5, allow_redirects=False) reads much better than requests.get(url, 5, False). The keyword tells you what each value means.

# Robustness. If a library adds a new parameter in the middle of an existing function signature, code that used keyword args keeps working. Code that relied on positional order breaks.

print("--------------Positional vs keyword arguments---------------")

# Exercise 2 

# Exercise 2a: predict each call
def order(item, quantity=1, gift_wrap=False):
    return f"{quantity}x {item}, gift wrap: {gift_wrap}"

# Prediction: What does each print?
# print(order("book")) -> 1x book, gift wrap: False because book is in positon
# print(order("book", 3)) -> 3x book, gift wrap: False because both are in position
# print(order("book", gift_wrap=True))-> 1x book, gift_wrap: True
# print(order("book", quantity=2, gift_wrap=True)) -> 2x book, gift_wrap=True
# print(order(quantity=5, item="pen")) -> 5x pen, gift_wrap: False

print(order("book"))
print(order("book", 3))
print(order("book", gift_wrap=True))
print(order("book", quantity=2, gift_wrap=True))
print(order(quantity=5, item="pen"))


# Exercise 2b: this one is a trap. Prect carefully before running
def order_bad(item, gift_wrap=False, quantity=1):
    return f"{quantity}x {item}, gift wrap: {gift_wrap}"

# Prediction: I want to order 5 books, no gift wrap.
# I write: order_bad("book", 5)
# What does this actually print, and is it what I wanted?
# Prediction:  1x book, gift-wrap: 5 as 5 is in wrong postion its gets overrided
print(order_bad("book",5))

# This is one reason scikit-learn's API looks like KNeighborsClassifier(n_neighbors=5, weights="distance") rather than KNeighborsClassifier(5, "distance"). There are too many parameters for positional calls to be readable, so the library is designed expecting keyword usage.

print("-------------Function scope — the LEGB rule----------------")

# Remember Day 3's lesson: Python has no block scope. A variable defined inside an if or for block is visible outside it.
# But functions are different. A function creates its own scope. Variables defined inside a function don't leak out. Variables outside the function are visible inside it (read-only, by default).

def make_message():
    word = "hello"
    return word.upper()

print(make_message())
# print(word)  # NameError!

# word exists only inside the function. Once the function returns, word is gone.
# The full rule has a name: LEGB. When Python sees a name (a variable reference), it looks for it in this order:

# Local — inside the current function
# Enclosing — inside any function that wraps this function (we'll see this with closures later)
# Global — at the top level of the module/file
# Built-in — names like print, len, range that are always available

# Exercise 3 

# Exercise 3a
x = 10

def show():
    print(x)  # reading the global x

show() # 10 will be printed
print(x) # 10 will be printed

# Exercise 3b: local variable doesn't leak

def make_y():
    y = 99
    print(y)

make_y()
# prediction: what happens on the next line? Name error because y exists inside the function
# print(y)  
# Uncomment to test: 
# print(y)

# Exercise 3c: this is the interesting one
counter = 0

# this cause error

# def increment():
#     counter = counter + 1 # what happens here? counter becomes 1 because global variable call
#     print(counter)


# Predicition : what happens when we call increment()? 
# Three options to consider:
#   (a) it prints 1, and the global counter becomes 1
#   (b) it prints 1, but the global counter stays 0
#   (c) it raises an error
# Your prediction: b the global remains unaffected

# increment()
# print(counter)  # what does this print after the call? 1 will be printed as per LEGB rule

# the right way or correction is

counter = 0

def increment(c):
    return c+1

counter = increment(counter)
print(counter) # output will be 1

print("-----------Type hints------------")

# Up to now, you've been writing functions like this:
#def square(x):
#     return x * x
# Nothing tells anyone — you, your editor, your future collaborators — what x is supposed to be, or what comes back. The function works on 5, on 2.5, on "hi" (try square("hi") and see what happens). Sometimes that flexibility is a feature; mostly it's a liability.
# Type hints let you annotate what you expect:
# pythondef square(x: int) -> int:
#     return x * x
# Two things just happened:

# x: int says "I expect x to be an int."
# -> int says "this function returns an int."

# The basic types

# pythondef add(x: int, y: int) -> int:
#     return x + y

# def greet(name: str) -> str:
#     return f"Hello, {name}"

# def is_adult(age: int) -> bool:
#     return age >= 18

# def average(numbers: list) -> float:
#     return sum(numbers) / len(numbers)

# def no_return() -> None:
#     print("I return nothing useful")

# One thing to know about defaults with hints
# The syntax for a parameter with both a hint and a default:

# def greet(name: str, greeting: str = "Hello") -> str:
#     return f"{greeting}, {name}!"

# Hint comes after the name, default comes after the hint. Read it left-to-right: "name, which is a str", "greeting, which is a str, defaulting to 'Hello'".

# Exercise 4

# Exercise 4a: add type hints to these functions
# Rewrite each one with appropriate hints for parameters and return value

# def double(x):
#     return x * 2

# Rewriting
def double(x: int) -> int:
    return x *2

# def full_name(first, last):
#     return f"{first} {last}"

# Rewriting
# def full_name(first: str,last: str) -> str:
#     return f"{first} {last}"

# # def is_even(n):
# #     return n%2 == 0

# # Rewriting
# def is_even(n: int) -> float # my prediction float: false it is bool because comaprison operator
#     return n%2 == 0

# # def log_message(msg):
# #     print(f"[LOG {msg}]")

# # Rewriting
# def log_message(msg: str) -> str # my prediction str: wrong it is None as it has no return statement
#     print(f"[LOG{msg}]")


# Exercise 4b: predict what happens here
def add(x: int, y: int) -> int:
    return x + y

# Prediction: what does this print? Or does it error?
# print(add(3, 4))           -> ??? 7
# print(add("hello", "world")) -> ??? my predcition: error but it does string concatenation so output is : helloworld
# print(add(3, "world"))     -> ??? error

print(add(3,4))
print(add("hello","world"))
# print(add(3, "world"))    # uncomment last, predict separately







