#try something
try:
    x=int(input("what's x? "))

#except something goes wrong
except ValueError:
    print('error, re-type your x. you just typed: it should be an integer. ') 
#if nothing goes wrong, else:
else:
    print(f"this is {x}")
