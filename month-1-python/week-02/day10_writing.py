# Day 10 Writing

# Part 1 - basic write
print("----part 1-----")

with open("notes.txt", "w") as f:
    count = f.write("first line")
    print(count)   # predict: first line wrong , right: .write returns the number of characters written not the string so it returns 10 


# part 2 - read it back
print("----part 2-----")

with open("notes.txt") as f:
    print(f.read())    # predict: error because we started of with a write operation wrong , right: it is because we are in write mode so .read() isn't a valid operation once we change it to read mode the ouput will be first line

# part 3 - two writes into the same file
print("----part 3 -----")

with open("notes.txt", "w") as f:
    f.write("apple")
    f.write("banana")
with open("notes.txt") as f:
    print(f.read())    # predict: output will be applebanana

# part 4 - append - "a"
print("----part 4 -----")

with open("log.txt", "w") as f:
    f.write("line one\n")

with open("log.txt", "a") as f:
    f.write("line two\n")

with open("log.txt") as f:
    print(f.read())  # predict line one
                            #  line two

# DAY 10 Problem - save_report

# Write a script that:

# 1. Starts with this data (type it as-is):

# scores = [("Alice", 88), ("Bob", 72), ("Carol", 95), ("Dan", 60)]

# 2. Writes a file report.txt where each line is name: score, one person per line. So the file should read:

# Alice: 88
# Bob: 72
# Carol: 95
# Dan: 60

# 3. Then appends a final summary line to that same file, computed from the data — not hardcoded:

# Average: 78.75

# 4. Finally, opens report.txt in read mode and prints its full contents so you can eyeball the result.

# Solution
print("--------Day 10 solution-------")

scores = [("Alice", 88), ("Bob", 72), ("Carol", 95), ("Dan", 60)]

# first iteration got output but had structural problem

# total = 0
# count = 0
# with open("report.txt", "w") as f:
#     for item in scores:
#         name, score = item
#         with open("report.txt", "a") as f:
#             f.write(f"{name}: {score}\n")
#             total= total+score
#             count = count+1
#             average = total/count
# with open("report.txt", "a") as f:
#     f.write(f"Average: {average}") 

# with open("report.txt") as f:
#     print(f.read())

# second iteration

total = 0
with open("report.txt", "w") as f:
    for name, score in scores:
        f.write(f"{name}: {score}")
        total +=score 

average = total / len(scores)

with open("report.txt", "a") as f:
    f.write(f"Average: {average}")

with open("report.txt") as f:
    print(f.read())

