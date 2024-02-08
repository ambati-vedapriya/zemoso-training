'''
deque is a double-ended queue that allows fast O(1) appends and pops from both ends.

'''

from collections import deque

# Create a deque
d = deque([1, 2, 3, 4, 5])

# Append to the right (end) of the deque
d.append(6)
print("After append(6):", d)

# Append to the left (beginning) of the deque
d.appendleft(0)
print("After appendleft(0):", d)

# Extend the deque with an iterable from the right
d.extend([7, 8, 9])
print("After extend([7, 8, 9]):", d)

# Extend the deque with an iterable from the left
d.extendleft([-1, 0])
print("After extendleft([-1, 0]):", d)

# Pop from the right
popped_right = d.pop()
print("Popped from the right:", popped_right)

# Pop from the left
popped_left = d.popleft()
print("Popped from the left:", popped_left)

print(d)
# Rotate the deque to the right (positive argument)
d.rotate(2)
print("After rotating 2 steps to the right:", d)

# Rotate the deque to the left (negative argument)
d.rotate(-3)
print("After rotating 3 steps to the left:", d)

# Count occurrences of an element
count_of_3 = d.count(3)
print("Count of 3:", count_of_3)

# Remove the first occurrence of a value
d.remove(4)
print("After removing the first occurrence of 4:", d)

# Reverse the deque
d.reverse()
print("After reversing:", d)

# Clear the deque
d.clear()
print("After clearing the deque:", d)
