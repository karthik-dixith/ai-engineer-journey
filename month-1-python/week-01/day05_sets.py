# Day05 - Sets exercises

# -------------Exercise 1: creating and uniqueness ----------------
print("-------------Exercise1--------------")

nums = {1, 2, 3, 2, 1, 4}

# predict (think about what set construction does to duplicates): {1, 2,3, 2, 1, 4} wrong     right: it is {1,2,3,4}
print(nums)
# predict:4
print(len(nums))


# --------------Exercise 2: the empty-set trap------------------
print("-------------Exercise2--------------")

mystery = {}

# predict - what TYPE is mystery? class dict
print(type(mystery))

# how to actually make an empty set:
real_empty = set()
# predict: class set()wrong   right: <class 'set'>
print(type(real_empty))

# -------------Exercise 3: removing duplicates from a list ---------------
print("-------------Exercise3--------------")

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
unique = set(words)

# predict (order may vary - focus on contents): "apple", "banana", "cherry"
print(unique)
# predict: 3
print(len(unique))


# -------------------Exercise 4: fast membership---------------
print("-------------Exercise4--------------")

allowed = {"admin", "editor", "viewer"}

# predict: True
print("admin" in allowed)
# predict: False
print("guest" in allowed)

# --------------------Exercise 5: add, remove, discard-----------
print("-------------Exercise5--------------")

s = {1, 2, 3}

s.add(4)
s.add(2)

# predict:{1,2,3,4}
print(s)

s.discard(99) # not present simnce 99 does not exist it ignores
# predict:{1, 2, 3}
print(s)

try:
    s.remove(99)  # not present
except Exception as e:
    # predict which error: KEY error
    print(type(e).__name__,"-", e)


# ---------------------Exercise 6: set algebra -----------------------
print("-------------Exercise6--------------")

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# predict each:
print(a | b )  #{1, 2, 3, 4, 5, 6}
print(a & b)   #{3,4}
print(a - b)   #{1,2}
print(b - a)   #{5,6}
print(a ^ b)   #{1,2,5,6}

# ------------------Exercise 7: hashability rule (same as dict keys) -----
print("-------------Exercise7--------------")

s1 = {1, 2, 3}
print(s1)

s2 = {"a", "b", "c"}
print(s2)

s3 = {(1,2), (3,4)}    # tuples of ints
print(s3)

try:
    s4 = {[1,2],[3,4]}   # list inside?
    print(s4)
except Exception as e: # Type error 
    print(type(e).__name__,"-",e)


# ---------------------Exercise 8: a small real use - finding unique tags --------
print("-------------Exercise8--------------")

posts = [
    {"id": 1, "tags": ["python", "ml", "ai"]},
    {"id": 2, "tags": ["python", "web"]},
    {"id": 3, "tags": ["ai", "ml", "llm"]},
]


all_tags = set()
for post in posts:
    for tag in post["tags"]:
        all_tags.add(tag)

# predict the contents (order doesn't matter):{python, ml, ai, web, llm}
print(all_tags)
# predict: 5
print(len(all_tags))
