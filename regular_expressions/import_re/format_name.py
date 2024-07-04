import re

name=input("What's your name? ").strip()
matches=re.search(r"^(.+), (.+)$", name)

#now you have the ability to capture what is between the two parentheses, in a variable called matches.
if matches:
    #if  matches not false then
    last, first=matches.groups()
    name=f'{first} {last}'
print(f"hello, {name}")