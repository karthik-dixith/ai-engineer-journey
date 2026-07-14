#  Day05 Tuples exercises

# -----------Exercise 1: tuples behave like lists for reading----------


point = (3,4,5)

# predict: 3
print(point[0])
# predict:5
print(point[-1])
# predict: 3,4
print(point[0:2])
# predict: 3
print(len(point))

# ---------------Exercise 2: the single-element trap----------
print("--------------Exercise2-----------")

not_a_tuple = (42)
yes_a_tuple = (42,)

# predict: int
print(type(not_a_tuple))
# predict: tuple
print(type(yes_a_tuple))

# --------------------Exercise 3: immutability--------------
print("-----------Exercise3-------------")
t = (1, 2, 3)

# predict what happens when this line runs (don't just guess the output - )
# predict whether it succeds or raises, and if it raises, what error):it raise an error a TypeError
try:
    t[0] = 99
except Exception as e:
    print(type(e).__name__, "-",e)


#---------------------Exercise 4: tuple unpacking ------------
print("-----------Exercise4-------------")

person = ("karthik", 28, "Berlin")
name, age, city = person

# predict: karthik
print(name)
# predict: 28
print(age)
# predict: Berlin
print(city)

#---------------------Exercise 5 : the swap--- ------------
print("-----------Exercise5-------------")

a = 1
b = 2
a,b = b,a

# predict: 2
print(a)
# predict: 1
print(b)

# ----------------Exercise 6: star unpacking-------------
print("-----------Exercise6-------------")

first, *rest = [10, 20, 30, 40, 50]

# predict: 10
print(first)
# predict: [20,30,40,50]
print(rest)
# predict (think carefully about the TYPE here): list
print(type(rest))

# -------------Exercise 7: returning mutiple values-------------
print("-----------Exercise7-------------")

def min_max(numbers):
    return min(numbers), max(numbers)

result = min_max([4, 1, 7, 3, 9, 2])

# predict - what is result, and what is its type? 1,9 Tuple
print(result)
print(type(result))

# now unpack:
lo, hi = min_max([4, 1, 7, 3, 9, 2])
# predict: 1,9
print(lo, hi)