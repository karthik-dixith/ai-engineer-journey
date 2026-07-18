# Day 12 Context Managers

# ----------1. Is the file closed after the with block? -----
print("---------1-------------")

with open("demo.txt", "w") as f:
    f.write("line one\n")
# Predict: what does f.closed print? does f still exist out here? True no f doesnt exist becuase the with does the close operation
print("1:", f.closed)

# ----- 2. Exception inside with block ---------
print("----2------")

try:
    with open("demo2.txt", "w") as g:
        g.write("partial")
        raise ValueError("boom")
except ValueError as e:
    print("2a:", e)
# predict: boom and then closed or not, given the block exploded? True it will be closed
print("2b:", g.closed) 

# ----3. what did the file actually get? -----
print("----3------")

with open("demo2.txt") as h:
    # predict: empty string, or "partial"? 3: partial 
    print("3:", repr(h.read()))

# ------4. what does 'as f' actually bind? -----
print("------4-------")

fh = open("demo.txt")
result = fh.__enter__()
# predict: True or False? True 
print("4:", result is fh) # i dont understand what is the second line
fh.close()


# Concept 2: Writing your own

import time

class Timer:
    def __enter__(self):
        print(" enter ran")
        self.start = time.time()
        return "not the timer!"   #deliberately NOT self
    
    def __exit__(self, exc_type, exc_value, tb):
        print(" exit ran, exc_type= ", exc_type)
        return False
    
# -------- 5 -------- what does 'as t' bind?
print("-----5--------")

with Timer() as t:
    print(" in the body")
# predict what is t?  not the timer!
print("5:", t) 


# --------- 6 exit on the exception path ------
print("-----6-------")

try:
    with Timer() as t2:
        raise KeyError("missing")
except KeyError as e:
    print("6:", "caught", e) # 6: caught missing yes exit ran prints , and exc_type = KeyError
# predict: does "exit ran " print? what is exc_type when it does?


# ----------1. after a NORMAL exit, is the file closed? ------

with open ("demo.txt", "w") as f:
    f.write("hello\n")
# predict: True or False? True
print("1:", f.closed)

# --------2. after a CRASH, is the file closed? --------

try:
    with open("demo2.txt", "w") as g:
        g.write("partial")
        raise ValueError("boom")
except ValueError as e:
    print("2a: caught", e)
    # predict: True or False?  2b: True 2a: caught boom
print("2b:", g.closed)


class Greeter:
    def __enter__(self):
        print(" __enter__ ran")
        return "hello from enter"

    def __exit__(self, exc_type, exc_value, tb):
        print(" __exit__ran")

# 3. the two calls, in order -----
print("----3-----")
with Greeter() as g:
    print(" the body ran") #  __enter__ran then __exit__ran then the body ran 
# predict: in what order do the three lines print? 

print("----4------")
with Greeter() as g:
    pass
# predict: what prints? hellofrom enter
print("4:", g)



# From-scratch problem

# Small and concrete. Write a context manager class called Timer that measures how long a block takes.
# Spec:

# __enter__ records the start time and returns self.
# __exit__ computes the elapsed time and prints took 0.123s.
# Use time.time() — it gives you the current time as a float in seconds. Subtract to get a duration.

print("Problem of the day")



import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    def __exit__(self, exc_type, exc_value, tb):
        end = time.time()
        print(f"took {end - self.start:.3f}s")

with Timer():
    total = sum(range(5_000_000))
print("done")


