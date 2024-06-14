fname =input("-what's your first name? ")
print("-hello ",  fname)

#ask user about their name.remove space and capitalize the first letter from the first word
lnames =input("-what's your last name? ").capitalize().strip()
s=fname+" "+lnames

fname=fname.strip()
print(f"Okay, {fname} {lnames}")

#captalize every first letter from each word
s=s.title()

print("your name is: ",s)