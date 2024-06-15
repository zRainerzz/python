#try something
try:
    x=int(input("what's x? "))
    print(f"this is {x}")  
#except something goes wrong
except ValueError:
    print('error, re-type your x. you just typed: it should be an integer. ') 
    x=int(input("uhm, excuse me...what's your x again? "))
    print(f"this is {x}") 
