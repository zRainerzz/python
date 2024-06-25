names=[]
with open('names.txt') as file:
    for line in sorted(file):
        names.append(line.rstrip())
    #readline is a method and its purpose in life is to read all the lines from the file and return it to me as a list.
    #strip off of the end of the line the actual new line itself so that print is handling the printing of everything.

    #the file will automatically closed as soon as the calling command close.
    #w refers to write/overwrite in the file.
    #a refers to append/add to the file.
    #r refers to read-only the file.
    for name in sorted(names, reverse=True):
        print(f"Hello, {name}")