
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

# Write a program that does all four of these:

print("------------Problem to solve--------------")

# 1. Count how many times each level appears. Build a dict like {'ERROR': 3, 'INFO': 1, 'WARN': 1} using the .get(key, 0) + 1 idiom — loop the lines, split each on the pipe, pull out the level piece, strip it, count it.

# 2. Collect just the messages into a list, in order, into a variable called messages. So ['disk full', 'started ok', 'timeout', 'low memory', 'disk full'].

# 3. Sort that messages list two different ways and prove you understand the difference:

# Make alpha = sorted(messages) and print both alpha and messages right after — show that messages is untouched.
# Then call messages.sort() and print messages — show it's now mutated in place.
# Predict what each of those three prints shows before running.

# 4. Pick a display level using short-circuit or. Given a variable chosen = "" (empty, so falsy), write level = chosen or "ERROR" and print level. Predict what comes out and why.

count = {}
messages = []
for line in logs:
    parts = line.split("|")
    level = parts[1].strip()
    count[level] = count.get(level,0)+1
    message = parts[2].strip()
    messages.append(message)
    
    


print(count)
print(messages)
alpha =sorted(messages) # predict : it returns the sorted output but doesn't affect the messages
print(alpha)
print(messages)   
sort_mssg=messages.sort()  # predict:  it returns None as the sorting would be done to the messages 
print(sort_mssg)
chosen = ""
level = chosen or "ERROR"
# predict: it prints ERROR
print(level)






        


