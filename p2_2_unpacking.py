def total(galleons,sickles,knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins=[100,50,25]
print(total(*coins), "knuts")
""" 
we add coins next to '*' will unpack coins, that way it will be ordered and use 100 for galleons,50 for sickles and 25 for knuts. 
"""