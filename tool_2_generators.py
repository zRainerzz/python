def main():
    n=int(input("What's n? how many sheep you want to generate? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range (n):
        yield "🐑" * i
        #now we are able to return 1 value at a time.

if __name__ == "__main__":
    main()

"""
imagine if you can print 1m sheeps without forcing the capability of the processor?
yeah, instead of forcing the processor to print 1m sheeps at once, you can make a generator that will
generate sheeps seperately, little by little until it reaches 1m, without the processor knowing that it is generating that massive amount of data.
instead of you printing 1 sheep and run the program 1m times, it will automatically run itself 1m times.

to conclude, you won't have to return the whole flock at once.
this is the end of my messed up course, hope everyone liked it, generating supposed to be the last lesson :)
THANK YOU PYTHON!
"""