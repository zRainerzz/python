def meow(n:int) -> None:
    """
    it shows that my meow function by design returns none so literally use this arrow notation on python when hinting what the return value
    
    :param n: Number of times to meow
    :type n: int
    :raise TypeError: if n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """
    return f"meow\n"*n
number : int =int(input("Number: "))
meows : str=meow(number)
print(meows,end="")