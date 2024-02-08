Regular expression : It is an expression which is used to extract some information.

- re is a module. It provides so much predefined functions.
- It is a collection of pre-defined functions.
- To process the input text.

- match() : To test te input string starts with specified pattern or not.

- search() : To test the specified pattern is present or not in the given input.

- findall() : To find duplicates for specified pattern.

- split() : How to split the input string.

- sub() : Used to replace the substring with the given pattern.

- compile() : Used to create pattern object and can be re-used.

<----Regex Pattern syntax---->

[abc] - a, b or c
[^abc] - any character expect a, b, c
[a-z] - a to z
[A-Z] - A to Z
[a-zA-Z] - a to z, A to Z
[0-9] - 0 to 9

Quantifiers :

[ ]? - occurs 0 or 1 time
[ ]+ - occurs 1 or more times
[ ]\* - occurs 0 or more times
[ ]{n} - occurs n times
[ ]{n,} - occurs n or more times
[ ]{y,z} - occurs atleast y time, but less than z times

Meta characters :

\d - [0-9]
\D - [^0-9]
\w - [a-zA-Z_0-9]
\W - [^\w]

NOTE : \ tells comp to treat following character as search character for '+', '.'

Raw strings :

- when you prefix a string with the letter r or R that string becomes a raw string.

- Unlike a regular string,a raw string treats the backslashes (\\) as literal character so raw string often appear in Regex objects.


$ - Matches the end
{} -Exactly the specified number of occurrences
() -Enclose a group of Regex