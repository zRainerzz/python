def meow(n:int) -> None:
    """it shows that my meow function by design returns none so literally use this arrow notation on python when hinting what the return value"""
    return f"meow\n"*n
number : int =int(input("Number: "))
meows : str=meow(number)
print(meows,end="")