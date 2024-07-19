class Vault:
    def __init__(self,galleons=0,sickles=0,knuts=0):
        self.galleons=galleons
        self.sickles=sickles
        self.knuts=knuts
    def __str__(self):
        return f"Galleons: {self.galleons} | Sickles: {self.sickles} | Knuts: {self.knuts}"
    #that's an essential special method to define to myself how i want a Vault to be printed.
    def __add__(self,other):
    #to combine two vaults as example.
        galleons=self.galleons + other.galleons
        sickles=self.sickles + other.sickles
        knuts=self.knuts + other.knuts
        return Vault(galleons,sickles,knuts)
potter=Vault(100,50,25)
print("potter's vault: ",potter)
weasley=Vault(25,50,100)
print("weasly's vault: ",weasley)
total= potter +weasley
print (f"the total is: {total}")