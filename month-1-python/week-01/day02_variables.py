#  Concept 1 — Variables are names bound to objects

# When you write x = 5, you are not creating a box called x and putting 5 inside it. What actually happens:

# Python creates an integer object with the value 5 somewhere in memory.
# Python binds the name x to point at that object.

# So x is a label, not a container. The object lives independently of any name pointing at it. You can confirm this with the built-in id() function, which returns the unique identity (in CPython, the memory address) of an object:


x = 5
print(id(x))  # prints the id of the integer object 5

# Concept 2 — Dynamic typing: types belong to objects, not names

# In a statically typed language (C, Java), you declare a variable's type up front: int x = 5;. The variable itself has a type.
# In Python, the object has a type. The name can be rebound to a different object of a different type at any time:

a = 20
print(type(a)) # prints <class 'int'>

a = "twenty"
print(type(a)) # prints <class 'str'>

a = [10, 5, 5]
print(type(a))  # prints <class 'list'>

#  Concept 3 — Immutable vs mutable objects

# This is the most important distinction in Python, and where most beginner bugs live.
# Immutable objects cannot be changed after creation. If you appear to "modify" one, Python actually creates a new object and rebinds the name. The immutable primitives: int, float, bool, str, tuple, None.

# Mutable objects can be changed in place. The same object is modified; no new object is created. The main mutable types: list, dict, set.

a = 10
print(id(a))

a = a + 1
print(id(a))  # prints a different id, because a new int object was created

b = [1, 2, 3]
print(id(b))

b.append(12)
print(id(b))  # prints the same id, because the list was modified in place

#  Concept 4 — The aliasing trap

# This is the bug everyone hits eventually. When you write b = a, you do not copy the object. You bind a new name to the same object.


a = "hello"
b = a
b = "bye"
print(a)
print(b) # prints "hello" and "bye", because strings are immutable
print(id(a) == id(b))

a = [1, 2, 3]
b = a
b.append(4)
print(id(a) == id(b))  # prints True, because lists are mutable and a and b point to the same list
print(a)
print(b)  # prints [1, 2, 3, 4] for both a and b

#if i want to make a copy of a mutable object, i can use the copy() method

b=a.copy()
b.append(5)
print(a)
print(b)
print(id(a) ==  id(b)) 

#or
b = list(a)
b.append(6)
print(a)
print(b)  # prints [1, 2, 3, 4] for a and [1, 2, 3, 4, 6] for b