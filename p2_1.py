import sys
"""
type python3 p2_1.py -n 3
"""
if len(sys.argv)==1:
    print("meow")
elif len(sys.argv)==3 and sys.argv[1]== "-n":
    n =int(sys.argv[2])
    for _ in range(n):
        print("meows")
else:
    print("usage: p2_1.py")