def main():
    x=get_int("what's x? ")
    print(f"this x is an integer. {x}")
def get_int(prompt):
    while True:
        #try something
        try:
            x=int(input(prompt))
            #we can just delete else and just type in here return x, but i needed to show you the else in the try except
            #return x

        #except something goes wrong
        except ValueError:
            pass
        #if nothing goes wrong, else:
        else:
            #instead of typing break, we will do return x, return is a stronger command line it returns the value and break from the loop.
            return x

main()