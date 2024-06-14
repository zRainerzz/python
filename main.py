fname =input("-what's your name? ").strip().title()


#split user's name into first and last names
first, last=fname.split(' ')
print(f"hello, {last}")