# Day 11 - Exception handling

# Exercise 1
print("--------Exercise 1--------")

# predict: which letters print, in what order? A then C then D because int of string causes a value error so it jumps to except block then the last print

try:
    print("A")
    x = int("hello")
    print("B")
except ValueError:
    print("C")
print("D")

# Exercise 2
print("---------Exercise 2---------")

# predict: What does each print?

# scores = {"Alice": "88", "Bob": "72"}

# def get_score(name):
#     try:
#         return int(scores[nam])      # note: 'nam', not 'name'
#     except:
#         return "not found"
    
# print(get_score("Alice"))  # predict: not found
# print(get_score("Zoe"))    # predict: not found 

# Bare except: — both returned "not found", exactly as you predicted. But sit with how wrong that is: Alice is right there in the dict, and the program told you she wasn't found. The NameError from your nam typo got swallowed and disguised as a missing key. The program lied with a straight face.

scores = {"Alice": "88", "Bob": "72"}

def get_score(name):
    try:
        return int(scores[name])      # note: 'nam', not 'name'
    except KeyError:
        return "not found"
    
print(get_score("Alice"))  # predict: not found
print(get_score("Zoe"))    # predict: not found 

# except KeyError: — the NameError is no longer a KeyError, so the except doesn't match it, so Python lets it through and crashes. And look at the gift you got:

# NameError: name 'nam' is not defined. Did you mean: 'name'?

# Python points at the exact typo and suggests the fix. That traceback is not the enemy — it's the single most useful thing that could have happened. The bare except: version hid it from you; the specific except KeyError: version handed it back. This is the rule to carry: catch the narrowest exception you actually expect, and let everything else crash loudly. A crash you can see beats a bug you can't.

# Exercise 3
print("---------Exercise 3-----------")

# predict: every line of output, in order: Alice: 88 then skipping bad row: details of the error then skipping bad row: details of the error then Dan: 60
# the loop survives all four rows yes the two bad rows will have different e message 

rows = ["Alice 88", "Bob", "Carol xyz", "Dan 60"]

for line in rows:
    try:
        name, score = line.split()
        print(f"{name}: {int(score)}")
    except ValueError as e:
        print(f"skipping bad row: {e}")


# Exercise 4
print("---------Exercise 4-----------")

# predict: output of check(10, 2), then output of check(10, 0)
# for check(10, 2) result is 5.0 then check completed for (10, 0) cannot divide by zero then check complete will be printed else statement won't be printed as there was exception
def check(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("cannot divide by zero")
    else:
        print(f"result is {result}")
    finally:
        print("check complete")

check(10, 2)
print("---")
check(10, 0)

# Problem

# Task: Write a function parse_scores(rows) that takes a list of strings, each supposed to be "name score". It should return a dictionary mapping each valid name to its integer score, and skip any malformed row without crashing — printing a warning for each one it skips.
# A row can be malformed in the two ways you already saw: wrong number of pieces ("Bob", or "a b c"), or a non-numeric score ("Carol xyz").
# Input to test with:

# rows = ["Alice 88", "Bob", "Carol xyz", "Dan 60", "Eve 91 extra"]

# Expected output shape (exact warning wording is your call, but the structure should match):

# skipping malformed row: 'Bob'
# skipping malformed row: 'Carol xyz'
# skipping malformed row: 'Eve 91 extra'
# {'Alice': 88, 'Dan': 60}

print("\n----------ProblemSolving----------")

rows = ["Alice 88", "Bob", "Carol xyz", "Dan 60", "Eve 91 extra"]

def parse_scores(rows):
    result = {}
    for line in rows:
        try:
            name, score = line.split()
            result[name] = int(score)
        except ValueError as e:
            print(f"{e}: {line}")
    return result        

r = parse_scores(rows) 
print(r)