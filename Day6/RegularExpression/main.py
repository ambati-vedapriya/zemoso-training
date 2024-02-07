import re

pattern = "re"
text = '''
RegEx Module
Python has a built-in package called re, which can be used to work with Regular Expressions.
Import the re module:
RegEx in Python
When you have imported the re module, you can start using regular expressions:
'''
match = re.search(pattern, text)
print(match)

# Search the string to see if it starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

# Method 1: re.match() -> Returns a Match object if there is a match anywhere in the string
pattern = re.compile(r'\d+')
match_result = pattern.match('123abc')
print("Method 1 (match()):", match_result.group() if match_result else "No match")

# Method 2: re.search()
search_result = re.search(r'\d+', 'abc1231def')
print("Method 2 (search()):", search_result.group() if search_result else "No match")

# Method 3: re.findall() -> Returns a list containing all matches
findall_result = re.findall(r'\d+', 'There are 42 apples and 123 oranges and 123 bananas')
print("Method 3 (findall()):", findall_result)

# Method 4: re.finditer()
# re.finditer() function returns an iterator yielding match objects for each match found in the string.
finditer_result = re.finditer(r'\d+', 'There are 42 apples and 123 oranges')
print("Method 4 (finditer()):")
for match in finditer_result:
    print(match.group())

# Method 5: re.split() -> Returns a list where the string has been split at each match
split_result = re.split(r'\s+', 'This is a sentence with multiple words')
print("Method 5 (split()):", split_result)

# Method 6: re.sub() -> Replaces one or many matches with a string
sub_result = re.sub(r'\d+', 'X', 'There are 42 apples and 123 oranges')
print("Method 6 (sub()):", sub_result)


# Creating a pattern to match email addresses
email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

# Example usage
text = "Contact us at info@example.com or support@company.com"
matches = email_pattern.findall(text)

for match in matches:
    print("Found:", match)
