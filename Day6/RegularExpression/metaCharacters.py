import re

# Example 1: A set of characters []
pattern1 = re.compile(r'[a-m]')
result1 = pattern1.findall("Hello World")
print("Example 1:", result1)  # Output: ['e', 'l', 'l', 'l', 'd']

pattern2 = re.compile(r'\d')
result2 = pattern2.findall("There are 42 apples and 123 oranges")
print("Example 2:", result2)  # Output: ['4', '2', '1', '2', '3']

# Example 3: Any character except newline .
pattern3 = re.compile(r'he..o')
result3 = pattern3.findall("hello, heebo, he12o,herty,heo")
print("Example 3:", result3)  # Output: ['hello', 'heebo', 'he12o']

# Example 4: Starts with ^
pattern4 = re.compile(r'^hello')
result4 = pattern4.match("hello, world")
print("Example 4:", result4.group() if result4 else "No match")  # Output: 'hello'

# Example 6: Zero or more occurrences *
pattern6 = re.compile(r'he.*o')
result6 = pattern6.findall("hello, hey there, he123o")
print("Example 6:", result6)  # Output: ['hello', 'hey there', 'he123o']

# Example 7: One or more occurrences +
pattern7 = re.compile(r'he.+o')
result7 = pattern7.findall("hello, heyo, he123o")
print("Example 7:", result7)  # Output: ['hello', 'heyo', 'he123o']

# Example 8: Zero or one occurrences ?
pattern8 = re.compile(r'he.?o')
result8 = pattern8.findall("hello, heo, he123o")
print("Example 8:", result8)  # Output: ['hello', 'heo']


# Example 9: Exactly the specified number of occurrences {}
pattern9 = re.compile(r'he.{2}o')
result9 = pattern9.findall("hello, heyo, he123o")
print("Example 9:", result9)  # Output: ['hello']

# Example 10: Either or |
pattern10 = re.compile(r'falls|stays')
result10 = pattern10.findall("falls or stays")
print("Example 10:", result10)  # Output: ['falls', 'stays']

# Example 11: Capture and group ()
pattern11 = re.compile(r'(\d+)-(\d+)-(\d+)')
result11 = pattern11.match("2022-12-31")
print("Example 11:", result11.groups() if result11 else "No match")  # Output: ('2022', '12', '31')