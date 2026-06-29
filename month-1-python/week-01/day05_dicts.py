#  day05 Dcitionaries exercise

# --------------------Exercise1: creating and reading------------
print("-------------Exercise1-------------")

person = {"name":"Karthik", "age": 28, "city": "Berlin"}

# predict: Karthik
print(person["name"])
# predict: 28
print(person["age"])
#predict: 3
print(len(person))

# --------------------Exercise 2: missing keys - bracket vs .get()---------

print("-------------Exercise2-------------")

# predict whether each succeds or raises; 

try:
    print(person["country"])
except Exception as e:
    print(type(e).__name__, "-", e)  

# predict: key error as the key does not exist
print(person.get("country"))
# predict: Germany
print(person.get("country", "Germany"))
# predict: Karthik
print(person.get("name", "Anonymus"))


# --------------------Exercise 3 : writing - insert vs overwrite ---------
print("-------------Exercise3-------------")

person["age"] = 29
person["country"] = "Germany"

# predict the full dict now:"name":"Karthik", "age": 28, "city": "Berlin", "age":29, "country": "Germany"
print(person)

# ---------------Exercise 4 : membership check keys, not values----------
print("-------------Exercise4-------------")

# predict: True
print("name" in person)
# predict:  False
print("Karthik" in person)
# predict: True
print("Karthik" in person.values())

# --------------Exercise 5 : iterating -----------------
print("-------------Exercise 5 --------------")

prices = {"apple": 1.20, "banana": 0.50, "cherry": 3.00}

# predict what gets printed (3 lines): apple banana cherry like in three different lines
for key in prices:
    print(key)

# predict what gets printed (3 lines): 1.20 0.50 3.00 like in three different lines
for value in prices.values(): 
    print(value)

# predict what gets printed (3 lines): apple costs 1.20 banana 0.50  cherry 3.00 like in three different lines
for fruit, price in prices.items():
    print(f"{fruit} costs {price}")

# -------------------Exercise 6: the return-value pattern again -----------
print("-------------Exercise 6 --------------")

inventory = {"apples": 10, "banana": 5}

# predict: None
result = inventory.update({"apples":12, "cherries": 8})
print(result)
# predict the full dict: {"apples": 12, "banana":5, "cherries": 8}
print(inventory)

# ---------------Exercise 7: hashable keys - the crucial constraint-------
print("-------------Exercise 7 --------------")

# predict whether each line succeds or raises (and which error) 

d1 = {1: "one", 2: "two"}        # int keys - fine? succeeds
print(d1)

d2 = {"a": 1, "b":2}             # str keys - fine? succeds
print(d2)

d3 = {(1, 2): "point"}           # tuple key — fine? succeeds
print(d3)

try:
    d4 = {[1, 2]: "point"}       # list key — ??? type error list cannot be a key
    print(d4)
except Exception as e:
    print(type(e).__name__, "-", e)


# --------------------Exercise 8: a small real-world use --------------
# count the occurrences of each character in a string
print("-------------Exercise 8 --------------")

text = "mississippi"
counts = {}
for ch in text:
    counts[ch] = counts.get(ch, 0) + 1

# predict the final dict: {'m': 1, 'i': 4, 's': 4, 'p': 2}
print(counts)


