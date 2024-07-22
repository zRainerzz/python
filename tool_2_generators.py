def main():
    n=int(input("What's n? how many sheep you want to generate?"))
    for s in sheep(n):
        print(s)

def sheep(n):
    flock=[]
    for i in range (n):
        flock.append("🐑" * i)
        return flock

if __name__ == "__main__":
    main()

"""
imagine if you can print 1m sheeps without forcing the capability of the processor?
yeah, instead of forcing the processor to print 1m sheeps at once, you can make a generator that will
generate sheeps seperately, little by little until it reaches 1m, without the processor knowing that it is generating that
"""