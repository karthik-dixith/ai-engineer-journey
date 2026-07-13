# reading a file


with open('notes.txt') as f:
    content = f.read()

print(content)

print("--------------")

with open('notes.txt') as f:
    first = f.read()
    second = f.read()


# predict: apple banana cherry
print(first)
# predict: there is nothing to read so it wont print anything
print(second)
# predict: 0
print(len(second))

with open('notes.txt') as f:
    a = f.read()
    b = f.read()

# predict: 20
print(len(a))
# predict: 0
print(len(b))
# predict: False
print(a == b)

print("--------------")

with open('notes.txt') as f:
    lines = f.readlines()

print(lines)

print("--------------")

with open('notes.txt') as f:
    lines = f.readlines()

# predict: 3
print(len(lines))
# predict: apple\n
print(lines[0])
# predict: apple the \n will be removed
print(lines[0].strip())
# predict: 6
print(len(lines[0]))

# coding problem

# Create a text file called scores.txt in your week-02 folder with exactly these lines:
# Alice 85
# Bob 72
# Charlie 91
# Dana 68

# Write a program in day-09.py that:

# 1. Opens scores.txt and reads it.
# 2. For each line, prints the student's name and their score on one clean line, formatted like this: Alice scored 85
# 3. After listing everyone, prints the average score of all four students, like: Average: 79.0
total = 0
count = 0
with open('scores.txt') as f:
    for line in f:
        parts = line.split(" ")
        print(f"{parts[0]} scored {parts[1].strip()}")
        score = int(parts[1])
        # print(type(score))
        total = total + score
        count = count + 1 
        
average = total/count
print(f"Average: {average}")
