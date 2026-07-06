
# --------------1------------
print("-------1-------")

a = [1,2,3]
b = a
b.append(4)
# predict: [1,2,3,4] reason: aliasing trap where the label just gets reassigned and points to the same location in the memory
print(a)

x = "hello"
y = x
y += "world"
# predict: "hello world" same reasoning wrong right: strings are immutable so a brand new string will be created y = "helloworld" but x remains unchanged
print(x)

# -----------2------------
print("------2---------")
result = 0 or "" or "found" or 5
# predict: found or returns the truthy operand
print(result)

val = "hi" and 0 and "bye"
# predict: 0 and returns the first falsy operand
print(val)

for i in range(3):
    pass
# predict: 2  the entire loop runs and the last number sustains and leaks out of the loop
print(i)

# ------------3-----------------
print("-------------3------------")

# count = 10
# def f():
#     print(count)
#     count = count + 1

# # predict: what happens when you call f()? here we have function scope so there will be an eror saying count is unboundLocalError
# f()

# ---------------4------------------
print("------------4-------")
nums = [3, 1, 2]
result = nums.sort() 
# predict: it doesnt sort and NOne is printed we have to use sorted(nums)
print(result)
# predict: [3, 1, 2]
print(nums)

s = "banana"
counts = {}
for ch in s:
    counts[ch] = counts.get(ch, 0)+1
# predict: {'b': 1, 'a': 3, 'n':2}
print(counts)

# ---------5----------
print("-----------5------")
nums = [1, 2, 3, 4, 5, 6]
result = {n % 3 for n in nums}
# predict: result is a set so {1,0,2}
print(result)

pairs = [(x,y) for x in range (2) for y in range(2)]
# predict: so there is a tuple inside a list written in comprehension form [(0,0), (0,1), (1,0),(1,1)]
print(pairs)

# -------6-------------
print(" -----------6-------")

text = "abcdefgh"
       #01234567
# predict: "bdf"
print(text[1:6:2])
# predict: "hgfedcba"
print(text[::-1])

# ----------7----------
print("--------7--------")

log = "2024-01-15 | ERROR | disk full"
parts = log.split("|")
# predict: disk full
print(parts[2].strip())


#Problem — Log line analyzer
# You're given a list of raw log lines, each in the format timestamp | LEVEL | message:

logs = [
    "2024-01-15 | ERROR | disk full",
    "2024-01-15 | INFO | started ok",
    "2024-01-16 | ERROR | timeout",
    "2024-01-16 | WARN | low memory",
    "2024-01-17 | ERROR | disk full",
]




