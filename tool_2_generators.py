def main():
    n=int(input("What's n? how many sheep you want to generate?"))
    for i in range(n):
        print(sheep(i))

def sheep(n):
    flock=[]
    for i in range (n):
        flock.append("🐑" * i)
        return flock

if __name__ == "__main__":
    main()