import re

#re.search(pattern, string, flags=0)
#for more info jump to note.txt
email=input("Whats ur email? ").strip()
if re.search(r"^[a-zA-Z0-9_]+@[^@]+\.com$", email):
#[^@] means take everything but another @ 
#[abcdefghijklmnopqrstuvwxyz1234567890_] now i'm using everything between the brackets numbers and alphabets or just type [a-zA-Z0-9_]
    print("Valid")
else:
    email=input("Invalid, please re-enter your email. ").strip()