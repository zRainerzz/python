import sys

#check for errors:
if len(sys.argv)<3:
    #sys.exit with the system's help, it's gonna exit my program then and there on line 6
    sys.exit("too few arguments")

elif len(sys.argv)>3:
    #sys.exit with the system's help, it's gonna exit my program then and there on line 10
    sys.exit("too many arguments")

#printing here:
# comment
#in terminal just type python <filename>.py <name>
print("hello, my name is", sys.argv[2])


#incase you want to show your full name, just type in the terminal: python libraries3sys.py "david smith"
# that way, it will appear, fully. 