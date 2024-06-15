def main():
    sz=int(input("the square? "))
    print_square(sz)

def print_square(size):
    #For each row in square.
    for i in range(size):
        #For each column in square.
        for j in range(size):
        
            print('# ',end="")
        print()
    print(f"the total you made is {size}")
    return size
    

main()