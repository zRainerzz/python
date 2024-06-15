
while True:
    #try something
    try:
        x=int(input("what's x? "))

    #except something goes wrong
    except ValueError:
        print("error, re-type your x.it should be an integer. i'm  asking you again, ")
    #if nothing goes wrong, else:
    else:
        break
print(f"x is {x}")