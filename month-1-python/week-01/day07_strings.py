# Day07  Strings

# -----------------Exercise 1 --------------------
print("---------Exercise 1----------")

lang = "Python"
#       012345

print(lang[0])   # predict: P
print(lang[-1])  # predict: n
print(lang[1:4]) # predict: yth
print(lang[:3])  # predict: Pyt
print(lang[3:])  # predict:hon
print(lang[::-1])  # predict: nohtyP
print(lang[::2])  # predict: Pto

shout = lang.upper()
print(shout)   # Predict: PYTHON
print(lang)   #Predict: Python

# lang[0] = "J"   # predict: what happens here? string object error  J cannot be assigned


# -------------------- Exercise 2----------------------
print("-------------Exercise 2 ---------------")

text = "  Data Science  "

print(text.strip())         # predict: "Data Science"
print(text.upper())         # predict: "  DATA SCIENCE  "
print(text.lower().strip()) # predict: "data science"
print(text)                 # predict: "  Data Science  "

filename = "report_final.pdf"

print(filename.endswith(".pdf"))  # predict: True
print(filename.startswith("draft")) # predict: False
print("final" in filename)          # predict: True
print(filename.find("."))           # predict: 12
print(filename.find("x"))           # predict: -


# ------------------------- Exercise 3 -----------------------
print("--------------Exercise 3-----------------")

log_line = "2026-07-04 ERROR disk full"

parts = log_line.split()
print(parts)                       # predict: ['2026-07-04', 'ERROR', 'disk', 'full']
print(len(parts))                  # predict: 4
print(parts[1])                    # predict: ERROR

path = "month-1/week-01/day7.py"
print(path.split("/"))             # predict: ['month-1', 'week-01', 'day7.py']

pieces = ["ai", "engineer", "journey"]
print("_".join(pieces))          # predict: ai_engineer_journey
print(" ".join(pieces))          # predict: ai engineer journey
print("".join(pieces))           # predict: aiengineerjourney

# the round trip: split then re-join with a different  separator
csv = "a,b,c,d"
print("|".join(csv.split(",")))          # predict:   'a|b|c|d'


# Coding Exercise

# Problem — Parse a log line.
# You're given this string (type it into your file exactly):

log = "2026-07-04T09:15:42 | WARNING | disk usage at 87%"

# Write code that extracts and prints each of the following. Figure out which methods and slices to combine — this deliberately uses split, strip, indexing, and a case method together, because real parsing always chains them.

# 1. The date only — 2026-07-04 (not the time). Hint: the date and time are joined by a T.
# 2. The severity level in lowercase — warning. Note the spaces around the | separators; you'll need to deal with them.
# 3. The number 87 as it appears in the message — pull out the 87% piece and then strip the % off, leaving 87% → 87.
# 4.  A count of how many words are in the message portion (disk usage at 87% → 4).

# Expected output shape (your values should match):

# Date: 2026-07-04
# Severity: warning
# Usage: 87
# Word count: 4
# There's more than one valid way to slice this apart — any approach that produces the right output is correct. Watch the stray whitespace around the | characters; that's the trap this problem is built around. Write it, run it, report back with your code and output.

# 1
date = log[:10]
print("Date:",date)


#2 
s = log.split("|")[1].strip().lower()
print("Severity:", s)

# 3
usage = log.split("|")[2]
s = usage.split(" ")
print(s[-1].strip("%"))

# 4
word = log.split("|")[2].strip().split()
print("Word count:",len(word))
