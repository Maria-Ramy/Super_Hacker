#Reverse the string “rekcah_repus”  without using built-in functions
x="rekcah_repus"
print(x[::-1])

# Syntax: x[start:stop:step]
# This is a slice operation that extracts parts of a string (or list, or other sequences).
# start: The index to start from.
# stop: The index to stop before.
# step: The amount to move forward each time. This can also be negative!

# what does x[::-1] mean?
# start: Not specified → defaults to the end of the string when step is negative.
# stop: Not specified → defaults to the beginning of the string when step is negative.
# step = -1 → It means go backwards through the string.

# You're telling Python:
# "Start from the end of x, go backward one character at a time, and stop when you pass the start."
