import re

#re.search(pattern, string, flags=0)
#for more info jump to note.txt
email=input("Whats ur email? ").strip()
if re.search(r"^\w+@[^@]+\.com$", email):
#[^@] means take everything but another @ 
#[abcdefghijklmnopqrstuvwxyz1234567890_] now i'm using everything between the brackets numbers and alphabets or just type [a-zA-Z0-9_] or \w to represent that you want a "word characters."
#^ means start matching at the beginning of the string,   \w means word characters only,   + means one or more,   @ at symbol literally,   [^@] everything but @,   + means 1 or more,   \.com a dot com literally,   $ match at the end   
    print("Valid")
else:
    email=input("Invalid, please re-enter your email. ").strip()