def main():
    n=int(input("what's n? "))
    if n<0 :
        number=get_number(n)
    meow(3)

def get_number(n):
    while True:
        n=int(input("what's n? "))
        if n>0:
            break
    return n


def meow(n):
    for _ in range (n):
        print("meow")
main()