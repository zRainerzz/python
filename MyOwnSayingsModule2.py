import sys
from MyOwnSayingsModule import salutation
from MyOwnSayingsModule import farewell

if len(sys.argv)==2:
    salutation(sys.argv[1])
elif len(sys.argv)==3:
    farewell(sys.argv[2])
else:
    print("invalid input, text is too long, there's a case where you maybe have typed only python <filename>.py .")
    sys.exit()