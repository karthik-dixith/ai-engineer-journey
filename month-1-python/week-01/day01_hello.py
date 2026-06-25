print("Day 1 : the journey begins.")

x=5
print(type(x))
x= "hello"
print(type (x))

x=5
print(id(x))
x=x+1
print(id(x))

nums=  [1,2,3]
print(id(nums))

nums.append(4)
print(id(nums))

a=5
b = a
b = b + 1
print(a)
print(b)

a = [1, 2, 3]
b = a
b.append(4)
print(a)
print(b)
print(id(a) == id(b))

b=a.copy()
print(id(a) == id(b))