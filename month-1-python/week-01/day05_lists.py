# day5_ Lists exercise

# ------- Exercise 1: basic indexing and slicing ------
print("--------------Exercise 1-------------")
nums = [10, 20, 30, 40, 50]

# predict: 10 will be printed
print(nums[0])
# predict: 50 will be printed points to last element
print(nums[-1])
# predict:20,30,40 
print(nums[1:4])
# predict: 10,20,30
print(nums[:3])
# predict: 30,40,50
print(nums[2:])

#  ------------Exercise 2: mutation and return values ----------

print("--------Exercise 2-----------")
fruits = ["apple", "banana", "cherry"]

# predict: None will be printed
result = fruits.append("date")
print(result)
# predict: apple, banana, cherry, date
print(fruits)

# predict: date
popped = fruits.pop()
print(popped)
# predict: apple,banana, cherry
print(fruits)

# -------Exercise 3: sort vs sorted-------
print("----------Exercise 3-------")
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# predict: 1,1,2,3,4,5,6,9
sorted_copy = sorted(numbers)
print(sorted_copy)
# predict: 3, 1, 4, 1, 5, 9, 2, 6
print(numbers)

#predict: None will be printed
in_place = numbers.sort()
print(in_place)
# predict: 1,1,2,3,4,5,6,9 as .sort would alter the same list 
print(numbers)

# ----------- Exercise 4: the aliasing trap, revisited-------
print("---------------Exercise 4---------------")
a = [1, 2, 3]
b = a
b.append(4)

#predict: 1, 2, 3, 4
print(a)
#predict: 1, 2, 3, 4
print(b)
# predict: True
print(a is b)

#----------Exercise 5: breaking aliasing with a slice copy--------
print("---------------Exercise 5---------------")
x = [1, 2, 3]
y = x[:]
y.append(99)

#predict: 1, 2, 3
print(x)
#predcit: 1,2,3,99
print(y)
#predict: False [:] this create a new list so x i unaffected
print(x is y)
