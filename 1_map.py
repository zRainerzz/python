"""
map is a python comes with function called map
whose purpose in life is to allow me to map that is apply some function to every element of some sequensce(like a list).
"""

def main():
    yell("This", "is" ,"CS50")

def yell(*words):
    uppercased = [map(str.upper,words)]
    print(*uppercased)
if __name__== "__main__":
    main()