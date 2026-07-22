class Watcher:
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        print("cleaning up") # predict: will be printed second 
        return True
    
with Watcher():
    print("start")   # predict: start will be printed first 
    raise ValueError("boom")
    print("end")   # predict: 

print("survived")  # predict:  this will also be printed

class Watcher:
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        print("cleaning up") # predict: will be printed second 
        return False   
    
with Watcher():
    print("start")   # predict: start will be printed first 
    # raise ValueError("boom")
    print("end")   # predict:  it will not be printedbecuase the block is interrupted 

print("survived")  # predict:  this deos not print

# Contrast the two runs directly, because this is the entire point of the pair:

# return True → exception suppressed → execution continues after the with → survived printed.
# return False → exception propagates → program crashes → survived never reached.

# The one thing that stayed constant across both runs: cleaning up printed every time. That's the guarantee. __exit__ runs whether or not there's an exception, and whether or not it suppresses it. Cleanup always happens. What return True/False decides is only what happens to the exception afterward — silence it, or let it keep flying.

# So the mental model for __exit__'s return value:

# truthy  → "I handled it, move on"      → exception dies, program lives
# falsy   → "not my problem"             → exception propagates, program may die

print("-----------------\n")

# clarification of order of execution

class Watcher:
    def __init__(self):
        print("1: constructing")
    def __enter__(self):
        print("2: entering")
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        print("4: exiting")
        return False
    
with Watcher():
    print("3: inside the block")


# Second half
print("\nsecond half concept - contextmanager ")

from contextlib import contextmanager

@contextmanager
def watcher():
    print("entering")
    yield
    print("exiting")

with watcher():
    print("inside the block")

# output

# entering
# inside the block
# exiting

# to give the block a value

from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.time()
    yield start
    elapsed = time.time() - start
    print(f"elapsed: {elapsed:.4f}s")

with timer() as t:
    print("start time was", t)
    total = sum(range(1_000_000))

# so here yield start is the variable t

# what if there is an exception in the block how to handle it so the lines below yield run

from contextlib import contextmanager

@contextmanager
def watcher():
    print("entering")
    try:
        yield
    finally:
        print("exiting")  # runs even if the block raised
    
with watcher():
    print("start")
    # raise ValueError("boom")


# problem of the day
print("-------------problem of the day--------")

# Write a context manager called tag using @contextmanager that wraps output in an HTML-style tag. Spec:

# It takes one argument, the tag name (a string like "p" or "div").
# On enter, it prints the opening tag: <p>.
# On exit, it prints the closing tag: </p> — and this must print even if the block raises.
# It doesn't need to yield any value (no as needed).

# Usage:
# with tag("p"):
#     print("Hello world")

# Expected output:
# <p>
# Hello world
# </p>

# Then prove your finally works: add a version where the block raises an exception partway through, and confirm the closing tag still prints before the exception propagates.

print("---------Solution------------")

from contextlib import contextmanager

@contextmanager
def tag(value):
    print(f"<{value}>")
    try:
        yield
    finally:
        print(f"</{value}>")

with tag("p"):
    print("Hello world")

from contextlib import contextmanager

@contextmanager
def tag(value):
    print(f"<{value}>")
    try:
        yield
    finally:
        print("exiting")
        print(f"</{value}>")

with tag("p"):
    print("Hello world")
    # raise ValueError ("boom")
