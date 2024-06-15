import random

number=random.randint(1,10)
print(number, ' that was the random number, and the next is the coin: ')
coin=random.choice(["heads", "tails"])
print(coin)

cards=["Pawn","King","Queen"]
random.shuffle(cards)
for card in cards:
    print(cards)