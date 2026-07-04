# day 06  Comprehensions

# ------ 1. Basic mapping --------
squares = [n*n for n in range(6)]
# PREDICT: squares == [0, 1, 4, 9, 16, 25] range always -1 
print("1:", squares)

# -----2. Filtering (trailing if) ------
evens = [n for n in range(10) if n % 2 == 0]
# PREDICT: evens == [0, 2, 4, 6, 8,]
print("2:", evens)

# --------3. Filter + transform together --------
even_squares = [n*n for n in range(10) if n % 2 == 0]
# PREDICT: even_squares == [0, 4, 16, 36, 64]
print("3:", even_squares)

# ---------4. Conditional transform (leading ternary, keeps all) -----------
labels = ["even" if n % 2 == 0 else "odd" for n in range(5)]
# PREDICT: labels == [even, odd, even, odd, even]
print("4:", labels)

# --------5. Scope: does a FOR-LOOP variab;e survive the loop? ------
for i in range(3):
    pass
# PREDICT: what does print(i) show? print("5:", 0,1, 2) wrong it completes the loop and last surviving value would be 2 that would leak out so it is ("5:", 2)
print("5:", i)

# --------6. Scope: does a COMPERHENSION variable survive? ---------
comp = [j for j in range(3)]
# PREDICT: does j exist out here? what happens on print(j)?  Name error because the j value does not leak out
try:
    print("6:", j)
except NameError as e:
    print("6: NameError ->", e)

# ---------7. Dict comprehension --------
sq_map = {n: n*n for n in range(4)}
# PREDICT: sq_map == {7:, 0:0, 1:1, 2:4, 3:9}
print("7:", sq_map)

# --------8. Dict comprehension with colliding keys ----

collide = {n % 3: n for n in range(7)}
# PREDICT: collide == ? (which value wins for each key?)  n=0 → key 0, val 0 → {0:0}
# n=1 → key 1, val 1 → {0:0, 1:1}
# n=2 → key 2, val 2 → {0:0, 1:1, 2:2}
# n=3 → key 0 again → {0:3, 1:1, 2:2}
# n=4 → key 1 again → {0:3, 1:4, 2:2}
# n=5 → key 2 again → {0:3, 1:4, 2:5}
# n=6 → key 0 again → {0:6, 1:4, 2:5}
# so ("8:", {0:6, 1:4, 2:5})
print("8:", collide)

# ---------9. Set comprehension (dedup) --------
mods = {n % 3 for n in range(10)}
# PREDICT: mods == {9: 0, 1, 2}
print("9:", mods)

# ----------10. Nested comprehension: flatten a matrix ------
matrix = [[1,2,3],[4,5,6]]
flat = [x for row in matrix for x in row]
# PREDICT: flat == ? [10: 1, 2, 3, 4, 5, 6]
print("10:", flat)

# ---------11. Nested: build a list of lists --------
grid = [[r*c for c in range(3)] for r in range (3)]
# PREDICT: grid == ? 11: [[0, 0, 0],[0, 1, 2],[0, 2, 4] 
print("11:", grid)


# self programming

# Start with this list:
words = ["apple", "kiwi", "banana", "fig", "cherry", "plum"]

# # Task 1. Using a comprehension, build a list called long_upper that contains the uppercase form of every word with more than 4 letters. (Two things happening here: a filter and a transform — decide which goes where.)

long_upper = [word.upper() for word in words if len(word)>4 ]
print(long_upper)


# task 2 
# Task 2. Using a comprehension, build a dict called lengths that maps each word to its length.

lengths = { word: len(word) for word in words}
print(lengths)

# Optional task
#  build a set called unique_lengths holding the distinct word-lengths across the list, using a set comprehension.

unique_lengths = {len(word) for word in words}
print(unique_lengths)

