import sys

#another small example
if len(sys.argv)<3:
    #sys.exit with the system's help, it's gonna exit my program then and there on line 6
    sys.exit("too few arguments")
for x in sys.argv:
    print("hello there, my name is", x)


#OUTPUT:
#prints hello there, my name is <file_name>
#prints hello there, my name is first_word.
#prints hello there, my name is second_word.
#etc