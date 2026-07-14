# AI Engineer Journey - Learning Log

## Day 1 (2026-06-23)

- Set up Git , python, and VS Code; cloned the repo.
- Learned: What Git, GitHub, a repo , a commit and a push are.
- Tripped me up: " wrong terminal path, so cleared that"

## Day 2 (2026-06-24)

- learned: python's reference model : names -> objects, immutable vs mutable, aliasing trap
- tripped me up: " do not use triple quotes for multi line comment"

## Day 3 (2026-06-25)

- learned: control flow if elif else for while range continue break, repr function, truthiness sweep
- tripped me up: i thought any change made to a variable inside a loop is local and doesn't affect the variable outside which is wrong

## Day 4 (2026-06-27)

- learned: functions with return, positional vs keyword arguments, function scope the LEGB rule , type hints
- tripped me up: even if wrong position the value gets updated , global and local confusion, type hints prediction be more carefull

Key lesson: Python decides local scope at compile time — assignment anywhere in a function makes the name local everywhere, including reads before the assignment (UnboundLocalError).

## Day 5 (2026-06-29)

- learned: lists, tuples, dicts, sets. Indexing/slicing, mutation methods returning None, the sort/sorted split, tuple immutability and unpacking, dict reading patterns (bracket vs .get with defaults), the count-or-initialize idiom counts[ch] = counts.get(ch, 0) + 1, set membership and algebra, hashability rule for dict keys and set members.

- trippes me up: dicts cannot hold duplicate keys (overwrite preserves postion); set dusplicates are eleiminated at construction; get()never raises for missing keys; confusion between .remove and .discard

## Day 6 (2026-07-03)

-learned : Comprehensions: list/dict/set comprehension; filter (trailing if) vs conditional transform (leading ternary); comprehension scope (variable does NOT leak, unlike for-loops); flatten vs list-of-lists.

- Tripped me up: leaked loop var holds final value not the entire sequence; set comp collects the output expr (n%3 → {0,1,2}); dict-comp colliding keys are last-write-wins.

## Day 7 (2026-07-04)

- learned: Strings — immutable sequence, indexing/slicing (start:stop:step, negative step), case/whitespace/search methods, split & join.

- tripped me up - parse by splitting on structural separators and indexing pieces — never count characters. Also: methods return new strings (opposite of .sort()); separator.join(list) not list.join(separator).

## Day 8 (2026-07-06)

- learned : reviewed all the concepts learnt this week
- tripped me up : .get(key) concept , strings are immutable lesson learnt , truthy and falsy concept
- solved a problem which covers all the concepts split-parse, .get counting, sorted vs .sort(), or-fallback

## Day 9 (2026-07-10)

- learned: File reading: with/open, .read() and the read cursor (second read returns ''), .readlines() vs iterating the file object, trailing \n on every line and stripping it. Coding problem: parse scores.txt, print each student, compute average.
- tripped me up: predicted second f.read() would re-return full contents (got '' / len 0) — cursor stays at end, doesn't rewind; predicted len of full string as 17 (actual 20, each \n counts as one char).

## Day 10 (2026-07-13)

- learned: File writing: open modes "w" (truncate) and "a" (append), .write() writes exact chars + returns count, print vs write newline difference.
- tripped me up: when in write mode .read() isn't a valid operation,wrote scores to report.txt in "w", appended derived average in "a". Caught a shadowed double-open (nested with reusing f) that worked on Windows by luck.

## Day 11 (2026-07-14)

- learned: Exceptions: try/except control flow (exception abandons rest of try), catch the narrowest type not bare except (bare swallows your own typos), 'as e' for the message, else runs only on success + finally runs always.
- tripped me up : while solvind the problem of the day got stuck on adding new values to existing dictionary which caused a bug and created new dictionary everytime the loop ran so fixed it and learned
