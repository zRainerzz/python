import sys


if len(sys.argv)<3:
    print("too few arguments")

elif len(sys.argv)>3:
    print("too many")

else:
    # comment
    #in terminal just type python <filename>.py <name>
    print("hello, my name is", sys.argv[2])