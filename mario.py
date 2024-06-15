def game():
    x=int(input("gimme the height."))
    print_column(x)
    s=int(input("gimme the rows."))
    print_row(s)



def print_column(height):
    for _ in range(height):
        print("#\n",end="")

def print_row(width):
    print("?"*width)



game()
