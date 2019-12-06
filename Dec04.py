"""Advent of Code 2019 Day 4"""

import time

start = time.time()

puzzle_input = range(353096,843213)

def password(num):
    """Returns True if meets criteria:
    doubled digits, never decreases"""

    numstr = str(num)
    repeat = False
    for digit in numstr:
        if numstr.count(digit) ==2:
            repeat = True
    if not repeat: return False

    for i,digit in enumerate(numstr):
        if i>0:
            if digit < numstr[i-1]:
                return False
    return True

passwords = 0

for n in puzzle_input:
    if password(n):
        passwords += 1
print("Passwords:",passwords)


print("Time (secs):", round(time.time()-start,1))