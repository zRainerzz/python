def total(galleons,sickles,knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins={"galleons":100,"sickles":50,"knuts":25}
print(total(**coins), "knuts")
""" 
we add coins next to '**' will unpack coins which is a dictionary, that way it will be ordered and use 100 for galleons,50 for sickles and 25 for knuts. 
"""