# Concept 1: Conditionals and truthiness

x = 10

# prediction: big will be printed
if x > 5:
    print("big")
elif x > 0:
    print("small positive")
else:
    print("zero or negative")

# Truthiness sweep

# repr() is a built-in function that returns the "official" string representation of an object — ideally, one you could paste back into Python to recreate the object.
# Compare it to str(), which returns the "informal" or "display" representation, meant for humans reading output.
# pythons = "hello"

# print(str(s))    # hello
# print(repr(s))   # 'hello'

# Where {v!r} fits in
# Inside an f-string, {v} interpolates v using str(). {v!r} interpolates using repr(). That's the only difference. The !r is a conversion flag — !s for str (the default), !r for repr.
# So f"{v!r} is truthy" is shorthand for f"{repr(v)} is truthy". Both work; the !r form is more idiomatic.
# In your truthiness sweep, !r is doing real work: it lets you visually distinguish "" (empty string, falsy) from None (also falsy but a different reason) from 0 (falsy but a number). Without it, the empty string entry would just print as a blank.

values = [0, 1, "", "hello", [], [0], None, False, True, "False"]

for v in values:
    # prediction: which of these are truthy 0 is falsy , 1 is truthy,'' is falsy, [] is falsy , None is falsy, False is falsy, 'hello' is truthy , [0] is truthy , true is truthy , 'False' is truthy

    if v:
        print(f"{v!r} is truthy")
    else:
        print(f"{v!r} is falsy")


#Short-circuit behavior - predict each one 
# things to remember

# and returns the first falsy operand, or the last operand if all are truthy
# or returns the first truthy operand, or the last operand if all are falsy
# not always returns a strict True or False
# prediction: default will be printed
print(0 or "default")
#prediciton: hello will be printed
print("hello" or "world")
# prediction: 0 will be printed 
print(0 and "ignored")
# prediction: first will be printed
print("first" and "second")

# Concept 2: for loops and range 

# You've already used for informally. Now the formal version.
# A for loop in Python is fundamentally different from a for loop in C, Java, or JavaScript. Those languages have C-style for (i = 0; i < 10; i++) — initialize a counter, check a condition, increment. Python doesn't have that. Python's for is what other languages call foreach: it iterates over a collection's items, one at a time.

# That's the entire syntax. The collection can be a list, a string, a tuple, a dictionary, a set, a file, a range, or anything that implements the iterator protocol (a detail we'll cover later — for now, "things you can loop over").

# range

# If you want to loop a specific number of times — the C-style use case — you use range().
# range(n) produces the integers from 0 up to but not including n:
# pythonfor i in range(5):
#     print(i)
# Prints 0, 1, 2, 3, 4. Five values, starting at zero, stopping before 5.
# Three forms of range:

# range(stop) — 0 to stop - 1
# range(start, stop) — start to stop - 1
# range(start, stop, step) — start to stop - 1, stepping by step

# pythonrange(5)         # 0, 1, 2, 3, 4
# range(2, 7)      # 2, 3, 4, 5, 6
# range(0, 10, 2)  # 0, 2, 4, 6, 8
# range(10, 0, -1) # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
# The "stop is exclusive" rule is universal in Python. It catches everyone at first. The benefit: range(len(my_list)) gives you exactly the valid indices into my_list, because indices go from 0 to len - 1. The "off by one" question answers itself once you internalize this.


# enumerate
# Common need: you're looping over items but you also want the index.
# The naive approach:

fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(i, fruits[i])

# Works, but unidiomatic. Python provides enumerate:

for i, fruit in enumerate(fruits):
    print(i, fruit)

# enumerate(fruits) yields pairs: (0, "apple"), (1, "banana"), (2, "cherry"). The i, fruit on the left is tuple unpacking — Python takes each pair and binds the first element to i, the second to fruit. Same mechanism as a, b = 1, 2.

# break and continue

# Two loop-control statements:

# break exits the loop entirely. The remaining iterations don't happen.
# continue skips to the next iteration. The rest of the current body is not executed.

for i in range(10):
    if i == 5:
        break       # exits the loop at i=5
    print(i)        # prints 0, 1, 2, 3, 4

for i in range(10):
    if i % 2 == 0:
        continue    # skip even numbers
    print(i)        # prints 1, 3, 5, 7, 9

# Exercise 2

# Concept 2: for loops and range

# Basic iteration over a list

fruits = ["apple", "banana", "cherry"]

# prediction: prints apple , banana, cherry
for fruit in fruits:
    print(fruit)

# Iterating a string
# prediciton: prints D, a, y, 3
for char in "Day3":
    print(char)

# range basics
# prediciton:prints 0, 1, 2, 3
for i in range(4):
    print(i)

# range with start and stop
# prediction: 2, 3, 4, 5
for i in range(2,6):
    print(i)

# range with step 
# prediction: 0, 3, 6, 9
for i in range(0, 10, 3):
    print(i)


# range counting down
# prediction: prints 5, 4, 3, 2, 1
for i in range(5, 0, -1):
    print(i)

# enumerate
# prediction: prints 0:apple 1: banana 2: cherry
for i, fruit in enumerate(fruits):
    print(f"{i}:{fruit}")

# break
# prediction : what's the last number printed? 2
for i in range(10):
    if i ==3:
        break
    print(i)

# continue
# predicition: which numbers are printed? 1 3 5
for i in range(6):
    if i % 2 ==0:
        continue
    print(i)

# combining: sum the numbers 1 through 10
total = 0
for i in range(1,11):
    total = total + i
# predicition 55
print(f"sum 1 to 10: {total}")


# Concept 3 While loops

# Exercise 3 

# Basic counter
count = 0
# prediction: what does this print? 0 1 2 

while count < 3:
    print(count)
    count = count + 1

# prediction: what is count after the loop? still 0
print(f"after loop, count is {count}")

# Halving until below 1
n = 100 
# prediction: how many lines print? 7 lines
while n >= 1:
    print(n)
    n = n / 2

# prediction: what is n now? 100
print(f"n is now {n}")

# While with break - find first mutiple of 7 above 50
i = 50
while True:
    i = i + 1
    if i % 7 == 0:
        break
# prediction: 56
print(f"first multiple of 7 above 50: {i}")

# while with continue - print odd numbers below 10
# (yes, you could do this with a for loop; doing it with while for practice)
j = 0
while j < 10:
    j = j + 1
    if j % 2 == 0:
        continue
    # prediction: which numbers print? 1 3 5 7 9 
    print(j)



